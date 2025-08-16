#!/usr/bin/env python3
# Generate data/tools.json from data/tools.csv.
# Usage:
#   python scripts/generate_json.py

import csv, json, os, sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(REPO_ROOT, "data", "tools.csv")
JSON_PATH = os.path.join(REPO_ROOT, "data", "tools.json")

def main():
    if not os.path.exists(CSV_PATH):
        print(f"ERROR: CSV not found at {CSV_PATH}", file=sys.stderr)
        sys.exit(1)
    rows = []
    with open(CSV_PATH, newline='', encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter=';'):
            # Normalize minimal fields
            rows.append({
                "name": (row.get("name") or "").strip(),
                "url": (row.get("url") or "").strip(),
                "category": (row.get("category") or "Uncategorized").strip(),
                "description": (row.get("description") or "").strip(),
                "pricing": (row.get("pricing") or "").strip(),
                "oss": (row.get("oss") or "").strip(),
            })
    os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
    with open(JSON_PATH, "w", encoding="utf-8") as out:
        json.dump(rows, out, indent=2, ensure_ascii=False)
    print(f"Wrote {JSON_PATH} with {len(rows)} items.")

if __name__ == "__main__":
    main()