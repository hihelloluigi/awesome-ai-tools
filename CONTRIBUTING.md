# Contributing Guide

Thanks for considering a contribution! This repo follows the spirit of the [awesome](https://awesome.re) lists and uses a **CSV-first** workflow.

## TL;DR

- ✅ **Edit only `data/tools.csv`** in your PR.  
- 🚫 Do **not** edit `README.md` or `data/tools.json` — they’re generated **after** your PR is merged.  
- ✅ Keep entries concise, objective, and in the right category & alphabetical order.  
- ✅ Use the PR template checklist.

---

## How to add a tool

1. **Search first** to avoid duplicates.
2. **Edit** `data/tools.csv` and add a new row with these columns:

   | name | url | category | description | pricing | oss |
   |---|---|---|---|---|---|
   | Tool Name | https:\/\/example.com | Agents | Short, factual description | Free tier + Pro | yes/no |

   - **name:** Official name (respect stylized casing; avoid ALL CAPS unless brand)
   - **url:** Prefer official website; repo URL if it’s open-source
   - **category:** Use an existing category; propose new ones only if truly needed
   - **description:** Max ~12 words, objective (no hype/marketing language)
   - **pricing:** Optional (e.g., Free, Free tier, Paid, OSS)
   - **oss:** `yes` if open-source, otherwise `no` (or leave empty)

3. **Commit** your CSV change and open a **Pull Request**.

> **Note:** The README list and `data/tools.json` are generated automatically after merge to `main`.

---

## Format the README (What CI generates)

Each entry appears as a single bullet:

- Tool Name — Short description · Pricing: Free tier + Pro · Open Source

CI builds categories and alphabetical order from the CSV.

---

## Quality Checklist

- [ ] Link works and isn’t behind a login.
- [ ] No tracking parameters in URLs (strip `utm_*`, etc.).
- [ ] Description is concise and objective (no superlatives or hype).
- [ ] Correct category; **alphabetical order** by tool name within the category.
- [ ] `oss` is `yes` only if clearly open-source (with a public repo/license).

---

## PR Process

1. Open your PR with the CSV change and fill out the PR template.
2. **CI (Validate on PR)**:
   - Runs the generators without committing (to ensure your row parses).
   - Fails if you changed `README.md` or `data/tools.json` (you shouldn’t).
3. **Maintainer review**:
   - Checks format, link validity, category, and description quality.
4. **After merge to `main`**:
   - CI regenerates `README.md` and `data/tools.json` from the CSV and commits them.

---

## Local (optional)

You can preview changes locally (not required):

```bash
python scripts/generate_readme.py
python scripts/generate_json.py
```

If you don’t have Python 3 available, you can skip this; CI will validate on the PR for you.

---

## Categories

Keep categories broad and useful. Propose new ones sparingly and only when many tools clearly don’t fit existing sections.

---

° Code of Conduct

Be respectful and constructive. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
