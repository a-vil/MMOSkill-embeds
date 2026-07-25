[🇪🇸 Versión en español](README.md)

# 🎯 MMOSkill-embeds

> **Content localization and publishing pipeline for MMO skills.**
>
> MMOSkill-embeds automates the transformation of plain text into structured, localized content, automatically generating Discord embeds through a modular pipeline.

## What it does

This project solves a repetitive workflow:

- translating skills
- keeping terminology consistent
- preserving game vocabulary
- generating embeds
- maintaining indexes

The entire flow is automated through a processing pipeline.

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

## Architecture

```text
Source text
      │
      ▼
Localization pipeline
      │
      ▼
SkillText
      │
      ▼
Embed Builder
      │
      ▼
Discord
```

For internal design details see:

> 📖 **ARCHITECTURE.md**

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

## Installation

```bash
git clone https://github.com/a-vil/MMOSkill-embeds
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

## Contributing

Contributions are welcome.

Before making significant changes, review:

- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [AGENTS.md](./AGENTS.md)

## License

[PolyForm Noncommercial 1.0.0](LICENSE)