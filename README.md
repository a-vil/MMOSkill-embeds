[🇺🇸 English version](README_EN.md)

# 🎯 MMOSkill-embeds

> **Pipeline de localización y publicación de contenido para habilidades de un MMO.**
>
> MMOSkill-embeds automatiza la transformación de texto plano en contenido estructurado y localizado, generando automáticamente embeds de Discord mediante un pipeline modular.

## ¿Qué hace?

El proyecto resuelve un proceso repetitivo:

- traducir habilidades
- mantener terminología consistente
- preservar vocabulario del juego
- generar embeds
- mantener índices

Todo el flujo se automatiza mediante un pipeline de procesamiento.

## Características

- 🌐 Pipeline de localización EN → ES
- 🤖 Traducción asistida por IA
- 📚 Diccionarios personalizados
- 🚫 Exclusión de términos técnicos
- 🧩 Modelo de dominio (`SkillText`) independiente de Discord
- 🏗 Arquitectura modular y desacoplada
- 🔗 Índices automáticos con navegación clicable
- 🌍 Compatible con múltiples servidores
- 😀 Emojis personalizados con fallback a texto
- ⚡ Sistema de alias para acceso rápido
- 🔄 Fácil de extender con nuevas ramas

## Arquitectura

```text
Texto fuente
      │
      ▼
Pipeline de localización
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

Para conocer el diseño interno consulta:

> 📖 **ARCHITECTURE.md**

## Ramas implementadas

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

### Ramas
- [x] Shot
- [x] Magic
- [x] Blade
- [x] Martial
- [x] Halberd
- [ ] Katana
- [ ] Dual Sword

### Proyecto
- [ ] Tests unitarios
- [ ] CI/CD
- [ ] Docker
- [ ] CLI

### Exportadores
- [ ] JSON
- [ ] Markdown
- [ ] HTML

## Contribuir

Las contribuciones son bienvenidas.

Antes de realizar cambios importantes, revisa:

- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [AGENTS.md](./AGENTS.md)

## Licencia

[PolyForm Noncommercial 1.0.0](LICENSE)