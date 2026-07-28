[🇺🇸 English version](README_EN.md)

# 🎯 MMOSkill-embeds

Toolkit de localización asistida por IA para documentar habilidades de un MMO en Discord.
Transforma texto inglés en un modelo de datos (SkillText) en español mediante un flujo estructurado, y lo integra en un bot que publica los resultados como embeds.
Texto fuente (EN) → data/*.txt → translate-en-es → SkillText → embed-integration → Bot → Discord

## Características

- 🌐 Localización EN → ES mediante la skill translate-en-es con guía de estilo
- 📚 Diccionarios personalizados para forzar términos específicos
- 🚫 Exclusiones para preservar vocabulario del juego en inglés
- 🧩 Modelo de dominio (SkillText) — datos estructurados por habilidad
- 🔧 Integración al bot mediante la skill embed-integration
- 🏗 Estructura modular: cada rama de habilidades es independiente
- 🔗 Índices automáticos en Discord con navegación clicable
- 😀 Emojis personalizados con fallback a texto
- ⚡ Alias para acceso rápido a cualquier habilidad
- 🌍 Compatible con múltiples servidores
- 🔄 Fácil de extender con nuevas ramas de habilidades

## Flujo de trabajo

1. Texto fuente — Ingresa las skills en inglés en un archivo de texto dentro de data/.
2. Localización con IA — Usa la skill translate-en-es para transformar el texto a español:
- Aplica diccionarios personalizados y términos excluidos
- Preserva vocabulario del juego y nombres de skills en inglés
- Mantiene placeholders {variable} intactos
- Sigue reglas de estilo para que suene natural, no traducido literal
- El resultado es data/es_*.py con SkillText: título, descripción y detalles por skill
3. Integración con IA — Usa la skill embed-integration para conectar ese SkillText al bot:
- Genera los builders de embeds, almacenamiento y comando
- _base.py maneja la lógica repetitiva; solo configuras
4. Ejecución — El bot escucha comandos (!skshot, !skmagic, etc.) y responde con embeds desde los datos integrados.

## Arquitectura

```text
Texto fuente (EN)
      │
      ▼
data/*.txt
      │
      ▼
translate-en-es  (skill de IA)
      │
      ▼
SkillText  (título, descripción, detalles en español)
      │
      ▼
embed-integration  (skill de IA)
      │
      ▼
Bot  (comandos !skshot, !skmagic, ...)
      │
      ▼
Discord Embeds
```

Para conocer el diseño interno consulta:

> 📖 **[ARCHITECTURE.md](./ARCHITECTURE.md)**

## Ramas implementadas

El texto fuente incluido en el repositorio corresponde a **Toram Online**, el juego con el que se desarrolló y probó el proyecto. Sirven como referencia y base funcional para adaptar a otros MMO.

| Rama | Skills | Comando |
|------|-------:|---------|
| Shot | 25 | `!skshot` |
| Magic | 24 | `!skmagic` |
| Blade | 24 | `!skblade` |
| Martial | 23 | `!skmartial` |
| Halberd | 24 | `!skhalberd` |

**Más de 120 habilidades documentadas.**

## Comandos

Cada rama soporta los mismos subcomandos:

```
<skill>        Muestra una skill
<skill> save   Muestra y registra en el índice
<tier>         Muestra un tier completo (t1-t5)
all            Muestra todas las skills
list           Lista de skills disponibles
index          Muestra o actualiza el índice
scan           Escanea el canal y registra skills ya enviadas
nuke           Elimina mensajes del bot e índice en el canal
```

## Instalación

```bash
git clone https://github.com/a-vil/MMOSkill-embeds
cd MMOSkill-embeds
pip install -r requirements.txt
```

Copia `.env.example` a `.env`, agrega tu `DISCORD_TOKEN`:

```env
DISCORD_TOKEN=tu_token_aqui
```

Ejecuta:

```bash
python bot.py
```

> 💡 Incluye `sort_lists.py` para mantener ordenados los diccionarios de traducción.

## Roadmap

- [x] Pipeline como flujo conversacional (asistido por agente IA)
- [ ] Pipeline como CLI autónomo (sin depender del agente)
- [ ] Tests unitarios
- [ ] CI/CD
- [ ] Docker

## Créditos

El texto fuente en inglés y las imágenes utilizadas en los embeds provienen del servidor de Discord **[Phantom's Library](https://discord.gg/fnhkyz5B4E)**. Este repositorio solo contiene la transformación y estructuración de dicho contenido; los datos originales no son de mi autoría.

## Licencia

[PolyForm Noncommercial 1.0.0](LICENSE)