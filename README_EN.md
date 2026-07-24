[🇪🇸 Versión en español](README.md)

# 🎯 MMOSkill-embeds

**Content management and delivery system** for MMO skill information.
Converts plain English text → structured Spanish → Discord embeds.

## Pipeline

```
data/*.txt (EN source)
    ↓  Translation with controlled vocabulary
data/es_*.py (SkillText in Spanish)
    ↓  Embed builders
embeds/*.py (discord.Embed)
    ↓  Bot commands
!skshot, !skmagic, !skblade, !skmartial, !skhalberd
```

## Features

- **5 skill branches** complete: Shot, Magic, Blade, Martial, Halberd
- **EN→ES translation pipeline** with custom dictionaries and excluded words
- **Modular architecture** — each branch is just 4 files following the same pattern
- **Auto index system** with clickable Discord links, multi-server
- **Custom emojis** with plain text fallback
- **Aliases** for quick skill access
- **WIP:** Katana, Dual

## Commands

| Command | Branches |
|---------|----------|
| `!skshot` | Shot (25 skills) |
| `!skmagic` | Magic (24 skills) |
| `!skblade` | Blade (24 skills) |
| `!skmartial` | Martial (23 skills) |
| `!skhalberd` | Halberd (24 skills) |

Each command supports: `<skill>`, `<skill> save`, `<tier>`, `all`, `list`, `index`, `nuke`, `scan`.

## Project Structure

```
MMOSkill-embeds/
├── bot.py                 # Entry point + !clean
├── branches/              # Command registration (1 per branch)
│   ├── _base.py           # Generic BranchHandlers
│   ├── shot.py
│   ├── magic.py
│   ├── sblade.py
│   ├── martial.py
│   └── halberd.py
├── embeds/                # Embed builders
├── data/                  # Translations (es_*.py) + EN sources
├── storage/               # JSON persistence per branch
├── imgs/                  # Assets per branch
├── sort_lists.py          # Sorts translation lists
├── .env.example
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/<user>/MMOSkill-embeds.git
cd MMOSkill-embeds
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, add your `DISCORD_TOKEN`, and run:

```bash
python bot.py
```

## License

[MIT](LICENSE)