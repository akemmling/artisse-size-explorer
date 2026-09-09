#!/usr/bin/env python3
"""Pull anonymous visitor statistics from GoatCounter and write stats/community.json.

Runs in GitHub Actions (see .github/workflows/community-stats.yml). Needs the
environment variable GOATCOUNTER_TOKEN: an API token with the "Read statistics"
permission, created at https://akemmling.goatcounter.com/user/api.

Counts are unique visitors as GoatCounter defines them (cookieless, per day).
"""
import json, os, sys, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone, timedelta

SITE = os.environ.get("GOATCOUNTER_SITE", "https://akemmling.goatcounter.com")
TOKEN = os.environ.get("GOATCOUNTER_TOKEN")
START = os.environ.get("STATS_START", "2026-06-01")
OUT = os.environ.get("STATS_OUT", "stats/community.json")

if not TOKEN:
    sys.exit("GOATCOUNTER_TOKEN is not set")

now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
end = now.strftime("%Y-%m-%dT%H:00:00Z")

def get(path, **params):
    url = f"{SITE}/api/v0/{path}?" + urllib.parse.urlencode(params, doseq=True)
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "artisse-size-explorer community-stats",
    })
    # GoatCounter occasionally answers a valid request with 404 {"error":"not found"};
    # a retry a little later succeeds, so retry on 404/429/5xx and on network errors.
    delay = 10
    for attempt in range(1, 7):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:300]
            msg = f"GoatCounter API {e.code} for {path}: {body}"
            if e.code not in (404, 429) and e.code < 500:
                sys.exit(msg)
        except (urllib.error.URLError, TimeoutError) as e:
            msg = f"GoatCounter API network error for {path}: {e}"
        print(f"attempt {attempt}: {msg}; retrying in {delay}s", file=sys.stderr)
        time.sleep(delay)
        delay = min(delay * 2, 120)
    sys.exit(f"giving up on {path} after 6 attempts")

# Sanity check: who is this token? (prints permissions and site access, never the token itself)
me = get("me")
tok = me.get("token") or {}
print("token:", json.dumps({k: v for k, v in tok.items() if k not in ("token",)}, default=str)[:400])

# Daily visitor totals (growth curve)
tot = get("stats/total", start=START, end=end)
daily = [{"day": s["day"][:10], "visitors": int(s.get("daily") or 0)} for s in tot.get("stats", [])]
daily.sort(key=lambda d: d["day"])
# trim leading zero days so "since" is the first real visit
while daily and daily[0]["visitors"] == 0:
    daily.pop(0)
total = int(tot.get("total") or sum(d["visitors"] for d in daily))

# Visitors by country (paginate; API caps limit at 100)
countries, offset = [], 0
while True:
    page = get("stats/locations", start=START, end=end, limit=100, offset=offset)
    for s in page.get("stats", []):
        code = (s.get("id") or "").upper()
        name = s.get("name") or code
        if not code or code in ("", "(unknown)"):
            name = "Unknown"
            code = ""
        countries.append({"code": code, "name": name, "visitors": int(s.get("count") or 0)})
    if not page.get("more"):
        break
    offset += 100
countries = [c for c in countries if c["visitors"] > 0]
countries.sort(key=lambda c: -c["visitors"])

out = {
    "generated": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "since": daily[0]["day"] if daily else START,
    "total_visitors": total,
    "countries": countries,
    "daily": daily,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    f.write("\n")
print(f"wrote {OUT}: {total} visitors, {len(countries)} countries, {len(daily)} days")
