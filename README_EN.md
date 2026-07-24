[🇪🇸 Versión en español](README.md)

# 🎯 MMOSkill-embeds

> **Content localization and publishing pipeline** for MMO skills.
>
> Converts plain English text into a structured domain model, using AI-assisted translation and game-specific rules, then automatically generates Discord embeds.

## Why this project exists

Maintaining MMO skill documentation in Discord is repetitive and error-prone:

- copying information from the game
- translating manually
- keeping terminology consistent
- creating embeds one by one
- maintaining indexes

This project automates that workflow by separating processing from presentation.

## Architecture

```text
Plain text (EN)
        │
        ▼
AI-assisted translation
        │
        ▼
Localization rules
(dictionaries, exclusions, terminology)
        │
        ▼
Domain model
SkillText
        │
        ▼
Presentation builders
        │
        ▼
Discord embeds
```

## Features

- 🌐 English → Spanish localization pipeline
- 🤖 AI-assisted translation workflow
- 📚 Custom dictionaries
- 🚫 Technical term exclusions
- 🧩 Domain model (`SkillText`) decoupled from Discord
- 🏗 Modular, decoupled architecture
- 🔗 Automatic indexes with clickable navigation
- 🌍 Multi-server compatible
- 😀 Custom emoji support with text fallback
- ⚡ Alias system for quick access
- 🔄 Easy to extend with new skill branches

## Domain model

Every skill is converted into a structured model before any output is generated:

```python
@dataclass(frozen=True)
class SkillText:
    title: str        # Skill name
    description: str  # In-game description
    details: str      # Stats, formulas, effects, bonuses
```

This intermediate representation keeps processing independent from presentation and allows reuse across different output formats.

## Implemented branches

| Branch | Skills | Command |
|--------|-------:|---------|
| Shot | 25 | `!skshot` |
| Magic | 24 | `!skmagic` |
| Blade | 24 | `!skblade` |
| Martial | 23 | `!skmartial` |
| Halberd | 24 | `!skhalberd` |

**Over 120 documented skills.**

## Commands

Every branch supports the same subcommands:

```
<skill>        Show a skill
<skill> save   Show and register in the index
<tier>         Show a full tier (t1-t5)
all            Show all skills
list           List available skills
index          Show or update the index
scan           Scan channel and register already-sent skills
nuke           Delete bot messages and reset the index
```

## Project structure

```text
MMOSkill-embeds/
│
├── bot.py
│
├── branches/
│   ├── _base.py          # Generic BranchHandlers
│   ├── shot.py
│   ├── magic.py
│   ├── sblade.py
│   ├── martial.py
│   └── halberd.py
│
├── embeds/               # Embed builders
│
├── data/                 # Translations (es_*.py) + EN sources
│
├── storage/              # JSON persistence per branch
│
├── imgs/                 # Assets per branch
│
├── sort_lists.py         # Sorts translation lists
│
├── .env.example
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/a-vil/MMOSkill-embeds.git
cd MMOSkill-embeds
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, add your `DISCORD_TOKEN`:

```env
DISCORD_TOKEN=your_token_here
```

Run:

```bash
python bot.py
```

> 💡 Includes `sort_lists.py` to keep translation dictionaries sorted.

## Roadmap

### Branches
- [x] Shot
- [x] Magic
- [x] Blade
- [x] Martial
- [x] Halberd
- [ ] Katana
- [ ] Dual Sword

### Project
- [ ] Unit tests
- [ ] CI/CD
- [ ] Docker
- [ ] CLI

### Exporters
- [ ] JSON
- [ ] Markdown
- [ ] HTML

---

## License

[MIT](LICENSE)