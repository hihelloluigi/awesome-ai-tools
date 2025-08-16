#!/usr/bin/env python3
# Generate README sections from data/tools.csv.
# Usage:
#   python scripts/generate_readme.py

import csv, re, sys, os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_CSV = os.path.join(REPO_ROOT, "data", "tools.csv")
README_MD = os.path.join(REPO_ROOT, "README.md")

def load_rows(path):
    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def make_tool_line(row):
    name = (row.get("name") or "").strip()
    url = (row.get("url") or "").strip() or "#"
    if not name:
        return ""
    line = f"- [{name}]({url})"
    extras = []

    desc = (row.get("description") or "").strip()
    if desc:
        extras.append(desc)

    pricing = (row.get("pricing") or "").strip()
    if pricing:
        extras.append(f"**Pricing:** {pricing}")

    oss = (row.get("oss") or "").strip().lower()
    if oss in ("yes", "true", "open source", "oss", "y", "open-source"):
        extras.append("**Open Source**")

    if extras:
        line += " — " + " · ".join(extras)
    return line

def build_sections(rows):
    # Group by category
    categories = {}
    for r in rows:
        cat = (r.get("category") or "Uncategorized").strip() or "Uncategorized"
        categories.setdefault(cat, []).append(r)

    # Build TOC and sections (alphabetical by category and by tool name)
    toc = []
    sections = []
    for cat in sorted(categories.keys(), key=lambda s: s.lower()):
        anchor = re.sub(r"[^a-z0-9]+", "-", cat.lower()).strip("-")
        toc.append(f"- [{cat}](#{anchor})")
        tools = sorted(categories[cat], key=lambda r: (r.get("name") or "").lower())
        lines = "\n".join([x for x in (make_tool_line(r) for r in tools) if x])
        sections.append(f"### {cat}\n\n{lines}\n")
    return "\n".join(toc), "\n".join(sections)

def replace_block(readme_text, toc_text, sections_text):
    """
    Replace everything between:
      '## Contents' ... '## The List' ... up to the next '\\n---\\n'
    with newly generated TOC + sections.
    """
    pattern = r"(## Contents[\s\S]*?## The List\n\n)[\s\S]*?(?=\n---\n)"
    replacement = "## Contents\n\n" + toc_text + "\n\n## The List\n\n" + sections_text + "\n"
    new_text, n = re.subn(pattern, replacement, readme_text)
    if n == 0:
        # If markers are not found, append to the end as a fallback
        new_text = readme_text.rstrip() + "\n\n" + replacement
    return new_text

def main():
    if not os.path.exists(DATA_CSV):
        print(f"ERROR: CSV not found at {DATA_CSV}", file=sys.stderr)
        sys.exit(1)
    if not os.path.exists(README_MD):
        print(f"ERROR: README not found at {README_MD}", file=sys.stderr)
        sys.exit(1)

    rows = load_rows(DATA_CSV)
    toc, sections = build_sections(rows)

    with open(README_MD, "r", encoding="utf-8") as f:
        readme = f.read()

    updated = replace_block(readme, toc, sections)

    with open(README_MD, "w", encoding="utf-8") as f:
        f.write(updated)

    print("README regenerated from data/tools.csv.")

if __name__ == "__main__":
    main()