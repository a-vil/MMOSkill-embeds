# AGENTS.md

Bot de Discord para embeds de habilidades de MMO en 5 ramas: Shot, Magic, Blade, Martial, Halberd.
Comandos: `!skshot`, `!skmagic`, `!skblade`, `!skhalberd`, `!skmartial`, `!skkatana`.
Cada uno con subcomandos.

## Comandos

| Acción | Comando |
|--------|---------|
| Ejecutar bot | `python bot.py` |
| Instalar dependencias | `pip install -r requirements.txt` |

- Requiere `DISCORD_TOKEN` en `.env` (copiar `.env.example`).
- `python-dotenv` carga `.env` automáticamente.
- `message_content` intent habilitado — el bot lee mensajes con prefijo `!`.

## Estructura del Proyecto

- `bot.py` — entry point, configuración del bot, comando `!clean`
- `branches/*.py` — registro de comandos (1 archivo por rama, usa `BranchHandlers` genérico)
- `embeds/*.py` — builders de embeds (skill keys, tiers, aliases, imágenes, emojis)
- `data/es_*.py` — traducciones `SkillText` por rama
- `data/*.txt` / `data/*.md` — archivos fuente en inglés
- `storage/*.py` — persistencia JSON por rama
- `imgs/` — assets de imágenes por rama
- `.env` — contiene `DISCORD_TOKEN` y variables de emojis personalizados
- `sort_lists.py` — ordena `words_custom.txt` y `words_excluded.txt`

## Convenciones

- Usa `discord.Embed` con `discord.Color.blue()` para todos los embeds.
- Cada skill = 1 embed de resumen + 1 o más embeds de detalle (halberd usa `SKILL_EXTRA` para contenido que no entra).
- Las definiciones de skills viven en `data/es_*.py`, los builders en `embeds/*.py`.
- El bot solo envía embeds predefinidos — sin generación dinámica de contenido.
- Código simple, modular y escalable. Sin complejidad innecesaria.

## Patrón de Ramas

Cada rama de skill sigue:
```
data/*.txt → data/es_*.py → embeds/*.py → branches/*.py → bot.py
```

## Ramas Completadas

- Shot (25 skills, `!skshot`)
- Magic (24 skills, `!skmagic`)
- Blade (24 skills, `!skblade`)
- Martial (23 skills, `!skmartial`)
- Halberd (24 skills, `!skhalberd`)

## Ramas en Progreso (WIP)

- Katana (`data/es_skatana.py` traducida, faltan embeds/storage/branches)
- Dual (solo existe `data/sdual.txt` fuente)

## Traducción

Al trabajar en traducciones, **vuelve a leer** `.opencode/skills/translate-en-es/STYLE_GUIDE.md`,
`.opencode/skills/translate-en-es/SKILL.md`,
`words_custom.txt` y `words_excluded.txt` por completo antes de traducir o
responder preguntas sobre reglas existentes. **NO respondas de memoria o
por intuición — primero lee, luego responde.**

- Las traducciones personalizadas (`words_custom.txt`) tienen prioridad (incluso sobre palabras excluidas).
- Las palabras excluidas (`words_excluded.txt`) nunca se traducen (a menos que tengan una personalizada).
- El resto usa traducción asistida por IA.
- Las variables `{placeholder}` en details deben preservarse exactamente.

## Reglas de comportamiento

- NO asumas decisiones que afecten al usuario.
- Ante cualquier duda, pregunta al usuario antes de proceder.
- Esto aplica a: formato de código, decisiones de traducción, estructura de archivos y cualquier otra elección.