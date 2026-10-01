#!/usr/bin/env python3
"""Self-hosted GitHub stats card (one SVG) built from public data. No third-party image service.

    python github_stats.py --user ishaan-sandhwar --out docs/github-stats.svg [--theme slate]

Data sources
  * contribution calendar : https://github.com/users/<user>/contributions   (public, no token)
  * followers, repo count : the public profile page
  * repositories/languages: REST API when GITHUB_TOKEN is set (robust, used inside GitHub Actions),
                            otherwise the public "repositories" tab pages (works anywhere, can break if GitHub
                            changes its markup)

Only the Python standard library is used, so the script runs in a bare GitHub Actions job.
"""
import argparse
import collections
import datetime
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request

UA = {"User-Agent": "readme-github-stats/1.0"}
FONT = '"Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif'
PALETTES = {  # bg, accent1, accent2
    "slate": ("#0d1117", "#161b22", "#60a5fa", "#c084fc"),
    "ocean": ("#0b1220", "#14213d", "#38bdf8", "#34d399"),
    "violet": ("#120b22", "#231650", "#a78bfa", "#f472b6"),
    "ember": ("#1a0f0a", "#3a1c10", "#fb923c", "#facc15"),
    "forest": ("#08140f", "#0f2e22", "#34d399", "#a3e635"),
}
LANG_COLORS = ["#60a5fa", "#f59e0b", "#34d399", "#f472b6", "#a78bfa", "#fb923c", "#38bdf8", "#94a3b8"]


def get(url, token=None):
    headers = dict(UA)
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=40).read().decode("utf-8", "replace")


# ───────────────────────── data ─────────────────────────
def contribution_calendar(user):
    page = get(f"https://github.com/users/{user}/contributions")
    cells = re.findall(r'<td[^>]*class="ContributionCalendar-day"[^>]*>', page)
    tips = dict(re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]*)</tool-tip>', page))
    days = {}
    for c in cells:
        d = re.search(r'data-date="([\d-]+)"', c)
        i = re.search(r'\bid="([^"]+)"', c)
        lv = re.search(r'data-level="(\d)"', c)
        if not d:
            continue
        m = re.match(r"(\d+) contribution", tips.get(i.group(1), "") if i else "")
        days[d.group(1)] = (int(m.group(1)) if m else 0, int(lv.group(1)) if lv else 0)
    if not days:
        raise RuntimeError("contribution calendar could not be parsed")
    return days


def streaks(days):
    ordered = sorted(days)
    longest = run = 0
    prev = None
    for d in ordered:
        if days[d][0] > 0:
            ok = prev is not None and (datetime.date.fromisoformat(d) - datetime.date.fromisoformat(prev)).days == 1
            run = run + 1 if ok else 1
            longest = max(longest, run)
            prev = d
        else:
            run = 0
    i = len(ordered) - 1
    if days[ordered[i]][0] == 0:   # today may not have a contribution yet
        i -= 1
    current = 0
    while i >= 0 and days[ordered[i]][0] > 0:
        current += 1
        i -= 1
    return longest, current


def profile_and_repos(user, token):
    langs, repos, followers = collections.Counter(), 0, None
    if token:
        prof = json.loads(get(f"https://api.github.com/users/{user}", token))
        followers, repos = prof["followers"], prof["public_repos"]
        page = 1
        while True:
            batch = json.loads(get(f"https://api.github.com/users/{user}/repos?per_page=100&page={page}", token))
            for r in batch:
                if not r["fork"] and r.get("language"):
                    langs[r["language"]] += 1
            if len(batch) < 100:
                break
            page += 1
        return followers, repos, langs
    prof = get(f"https://github.com/{user}")
    m = re.search(r'<span class="text-bold color-fg-default">([\d.]+k?)</span>\s*followers', prof)
    followers = m.group(1) if m else "?"
    m = re.search(r'Repositories\s*<span[^>]*title="(\d+)"', prof)
    repos = int(m.group(1)) if m else 0
    page = 1
    while page <= 10:
        h = get(f"https://github.com/{user}?tab=repositories&page={page}")
        items = [b for b in re.findall(r'<li[^>]*itemprop="owns"[^>]*>(.*?)</li>', h, re.S) if "name codeRepository" in b]
        if not items:
            break
        for b in items:
            lang = re.search(r'itemprop="programmingLanguage">([^<]+)<', b)
            if lang and "Forked from" not in b:
                langs[lang.group(1)] += 1
        page += 1
    return followers, repos, langs


# ───────────────────────── svg ─────────────────────────
def render(user, days, followers, repos, langs, theme):
    bg0, bg1, a1, a2 = PALETTES[theme]
    W, H = 1280, 372
    total = sum(v[0] for v in days.values())
    active = sum(1 for v in days.values() if v[0] > 0)
    longest, current = streaks(days)
    today = datetime.date.today().isoformat()
    esc = html.escape
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
         f'aria-label="GitHub snapshot for {esc(user)}: {total} contributions in the last year, {active} active days, longest streak {longest} days, '
         f'{repos} public repositories">',
         f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>'
         f'<linearGradient id="ac" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{a1}"/><stop offset="1" stop-color="{a2}"/></linearGradient></defs>',
         f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>',
         f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="17" fill="none" stroke="#ffffff" stroke-opacity="0.09"/>',
         f'<text x="36" y="46" font-family=\'{FONT}\' font-size="22" font-weight="700" fill="#ffffff">GitHub snapshot</text>',
         f'<text x="{W - 36}" y="46" text-anchor="end" font-family=\'{FONT}\' font-size="13" fill="#8b98ab">public data for @{esc(user)} · updated {today}</text>',
         f'<rect x="36" y="56" width="120" height="3" rx="1.5" fill="url(#ac)"/>']
    tiles = [(f"{total:,}", "contributions, last year"), (str(active), "active days"), (f"{longest} days", "longest streak"),
             (f"{current} days", "current streak"), (str(repos), "public repositories"), (str(followers), "followers")]
    tw, th, gx, gy = 160, 84, 12, 12
    for i, (val, label) in enumerate(tiles):
        x, y = 36 + (i % 3) * (tw + gx), 80 + (i // 3) * (th + gy)
        s.append(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="12" fill="#ffffff" fill-opacity="0.05" stroke="#ffffff" stroke-opacity="0.10"/>')
        s.append(f'<text x="{x + tw / 2}" y="{y + 38}" text-anchor="middle" font-family=\'{FONT}\' font-size="28" font-weight="800" fill="#ffffff">{esc(val)}</text>')
        s.append(f'<text x="{x + tw / 2}" y="{y + 62}" text-anchor="middle" font-family=\'{FONT}\' font-size="12.5" fill="#a8b3c4">{esc(label)}</text>')
    # heatmap (weeks as columns, Sunday first)
    ordered = sorted(days)
    first = datetime.date.fromisoformat(ordered[0])
    offset = (first.weekday() + 1) % 7
    hx, hy, cell, gap = 584, 100, 10, 2.6
    pitch = cell + gap
    s.append(f'<text x="{hx}" y="82" font-family=\'{FONT}\' font-size="12.5" fill="#8b98ab">Contributions over the last year</text>')
    last_month = None
    for k, d in enumerate(ordered):
        n = k + offset
        col, row = n // 7, n % 7
        date = datetime.date.fromisoformat(d)
        cnt, lv = days[d]
        x, y = hx + col * pitch, hy + row * pitch
        if lv == 0:
            s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell}" height="{cell}" rx="2.2" fill="#ffffff" fill-opacity="0.07"/>')
        else:
            colr, op = (a1, 0.30 + 0.17 * lv) if lv < 4 else (a2, 1)
            s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell}" height="{cell}" rx="2.2" fill="{colr}" fill-opacity="{op:.2f}"/>')
        if date.day <= 7 and row == 0 and date.month != last_month and col < 52:
            s.append(f'<text x="{x:.1f}" y="{hy - 6}" font-family=\'{FONT}\' font-size="10.5" fill="#8b98ab">{date.strftime("%b")}</text>')
            last_month = date.month
    ly = hy + 7 * pitch + 14
    s.append(f'<text x="{hx}" y="{ly + 9}" font-family=\'{FONT}\' font-size="11" fill="#8b98ab">Less</text>')
    for j, lv in enumerate((0, 1, 2, 3, 4)):
        colr, op = (a1, 0.30 + 0.17 * lv) if 0 < lv < 4 else ((a2, 1) if lv == 4 else ("#ffffff", 0.07))
        s.append(f'<rect x="{hx + 32 + j * 14}" y="{ly}" width="10" height="10" rx="2.2" fill="{colr}" fill-opacity="{op:.2f}"/>')
    s.append(f'<text x="{hx + 32 + 5 * 14 + 4}" y="{ly + 9}" font-family=\'{FONT}\' font-size="11" fill="#8b98ab">More</text>')
    # language bar: primary language of each own repository
    by = 296
    s.append(f'<text x="36" y="{by - 12}" font-family=\'{FONT}\' font-size="12.5" fill="#8b98ab">Languages · primary language of each original repository</text>')
    tot = sum(langs.values()) or 1
    x = 36
    barw = W - 72
    items = langs.most_common(6)
    for i, (name, n) in enumerate(items):
        w = barw * n / tot
        s.append(f'<rect x="{x:.1f}" y="{by}" width="{max(w - 2, 2):.1f}" height="14" rx="3" fill="{LANG_COLORS[i % len(LANG_COLORS)]}"/>')
        x += w
    x = 36
    for i, (name, n) in enumerate(items):
        s.append(f'<circle cx="{x + 5}" cy="{by + 36}" r="5" fill="{LANG_COLORS[i % len(LANG_COLORS)]}"/>')
        label = f"{name} {n}"
        s.append(f'<text x="{x + 16}" y="{by + 40}" font-family=\'{FONT}\' font-size="13.5" fill="#d5deea">{esc(label)}</text>')
        x += len(label) * 7.8 + 40
    s.append("</svg>")
    return "\n".join(s)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--user", required=True)
    ap.add_argument("--out", default="docs/github-stats.svg")
    ap.add_argument("--theme", default="slate", choices=sorted(PALETTES))
    a = ap.parse_args()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    days = contribution_calendar(a.user)
    followers, repos, langs = profile_and_repos(a.user, token)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(render(a.user, days, followers, repos, langs, a.theme))
    total = sum(v[0] for v in days.values())
    print(f"wrote {a.out}: {total} contributions, {repos} repos, {followers} followers, languages {dict(langs)}")


if __name__ == "__main__":
    try:
        main()
    except (urllib.error.URLError, RuntimeError) as exc:
        sys.exit(f"github_stats failed: {exc}")
