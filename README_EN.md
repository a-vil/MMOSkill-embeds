[🇪🇸 Versión en español](README.md)

# 🎯 MMOSkill-embeds

AI-assisted localization toolkit for documenting MMO skills on Discord.
Transforms English text into a structured data model (SkillText) in Spanish through a structured workflow, and integrates it into a bot that publishes the results as embeds.
Source text (EN) → data/*.txt → translate-en-es → SkillText → embed-integration → Bot → Discord

## Features

- 🌐 EN → ES localization via the translate-en-es skill with style guide
- 📚 Custom dictionaries for forced term mappings
- 🚫 Exclusions to preserve game vocabulary in English
- 🧩 Domain model (SkillText) — structured data per skill
- 🔧 Bot integration via the embed-integration skill
- 🏗 Modular structure: each skill branch is independent
- 🔗 Automatic indexes on Discord with clickable navigation
- 😀 Custom emoji support with text fallback
- ⚡ Aliases for quick access to any skill
- 🌍 Multi-server compatible
- 🔄 Easy to extend with new skill branches

## Workflow

1. Source text — Write the skills in English inside a text file under data/.
2. AI-assisted localization — Use the translate-en-es skill to transform the text into Spanish:
- Applies custom dictionaries and excluded terms
- Preserves game vocabulary and skill names in English
- Keeps {placeholder} variables intact
- Follows style rules for natural, non-literal output
- The result is data/es_*.py with SkillText: title, description, and details per skill
3. AI-assisted integration — Use the embed-integration skill to connect that SkillText into the bot:
- Generates embed builders, storage, and command registration
- _base.py handles repetitive logic; you only configure
4. Execution — The bot listens for commands (!skshot, !skmagic, etc.) and replies with embeds from the integrated data.

## Architecture

```text
Source text (EN)
      │
      ▼
data/*.txt
      │
      ▼
translate-en-es  (AI skill)
      │
      ▼
SkillText  (title, description, details in Spanish)
      │
      ▼
embed-integration  (AI skill)
      │
      ▼
Bot  (commands !skshot, !skmagic, ...)
      │
      ▼
Discord Embeds
```

For internal design details see:

> 📖 **[ARCHITECTURE.md](./ARCHITECTURE.md)**

## Implemented branches

The source text included in this repository corresponds to **Toram Online**, the game used to develop and test the project. These branches serve as a reference and functional base for adapting to other MMOs.

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

- [x] Pipeline as conversational flow (assisted by AI agent)
- [ ] Pipeline as standalone CLI (without dependency on the agent)
- [ ] Unit tests
- [ ] CI/CD
- [ ] Docker

## Credits

The source text in English and the images used in the embeds come from the Discord server **[Phantom's Library](https://discord.gg/fnhkyz5B4E)**. This repository only contains the transformation and structuring of that content; the original data is not my own work.

## License

[PolyForm Noncommercial 1.0.0](LICENSE)
