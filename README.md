[🇺🇸 English version](README_EN.md)

# 🎯 MMOSkill-embeds

**Sistema de gestión y delivery de contenido** para habilidades de un MMO.
Convierte texto plano en inglés → español estructurado → embeds de Discord.

## Flujo de trabajo

```
data/*.txt (EN fuente)
    ↓  Traducción con vocabulario controlado
data/es_*.py (SkillText en español)
    ↓  Builders de embeds
embeds/*.py (discord.Embed)
    ↓  Comandos del bot
!skshot, !skmagic, !skblade, !skmartial, !skhalberd
```

## Características

- **5 ramas de habilidades** completas: Shot, Magic, Blade, Martial, Halberd
- **Pipeline de traducción EN→ES** con diccionarios personalizados y palabras excluidas
- **Arquitectura modular** — cada rama son solo 4 archivos siguiendo el mismo patrón
- **Sistema de índice** automático con links clickeables, multi-servidor
- **Emojis custom** con fallback a texto plano
- **Alias** para acceso rápido a skills
- **WIP:** Katana, Dual

## Comandos

| Comando | Ramas |
|---------|-------|
| `!skshot` | Shot (25 skills) |
| `!skmagic` | Magic (24 skills) |
| `!skblade` | Blade (24 skills) |
| `!skmartial` | Martial (23 skills) |
| `!skhalberd` | Halberd (24 skills) |

Cada comando soporta: `<skill>`, `<skill> save`, `<tier>`, `all`, `list`, `index`, `nuke`, `scan`.

## Estructura

```
MMOSkill-embeds/
├── bot.py                 # Entry point + !clean
├── branches/              # Registro de comandos (1 por rama)
│   ├── _base.py           # BranchHandlers genérico
│   ├── shot.py
│   ├── magic.py
│   ├── sblade.py
│   ├── martial.py
│   └── halberd.py
├── embeds/                # Builders de embeds
├── data/                  # Traducciones (es_*.py) + fuentes EN
├── storage/               # Persistencia JSON por rama
├── imgs/                  # Assets por rama
├── sort_lists.py          # Ordena listas de traducción
├── .env.example
└── requirements.txt
```

## Instalación

```bash
git clone https://github.com/<user>/MMOSkill-embeds.git
cd MMOSkill-embeds
pip install -r requirements.txt
```

Copia `.env.example` a `.env`, agrega tu `DISCORD_TOKEN`, y ejecuta:

```bash
python bot.py
```

## Licencia

[MIT](LICENSE)