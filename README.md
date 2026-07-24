[🇺🇸 English version](README_EN.md)

# 🎯 MMOSkill-embeds

> **Pipeline de localización y transformación de contenido** para habilidades de un MMO.
>
> Convierte texto plano en inglés en un modelo de dominio estructurado, aplicando traducción asistida y reglas específicas del juego, para generar automáticamente embeds de Discord.

## ¿Qué problema resuelve?

Mantener documentación de habilidades de un MMO en Discord es un proceso repetitivo:

- copiar información del juego
- traducirla manualmente
- mantener consistencia terminológica
- crear embeds uno por uno
- mantener índices actualizados

Este proyecto automatiza ese flujo separando el procesamiento de la presentación.

## Arquitectura

```text
Texto plano (EN)
        │
        ▼
Traducción asistida
        │
        ▼
Reglas de localización
(diccionarios, exclusiones, terminología)
        │
        ▼
Modelo de dominio
SkillText
        │
        ▼
Builders de presentación
        │
        ▼
Embeds de Discord
```

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

## Modelo de dominio

Cada skill se convierte en un modelo estructurado antes de generar cualquier salida:

```python
@dataclass(frozen=True)
class SkillText:
    title: str        # Nombre de la habilidad
    description: str  # Descripción del juego
    details: str      # Stats, fórmulas, efectos y bonuses
```

Esta representación intermedia mantiene el procesamiento independiente de la presentación y permite reutilizar la información en otros formatos.

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

## Estructura del proyecto

```text
MMOSkill-embeds/
│
├── bot.py
│
├── branches/
│   ├── _base.py          # BranchHandlers genérico
│   ├── shot.py
│   ├── magic.py
│   ├── sblade.py
│   ├── martial.py
│   └── halberd.py
│
├── embeds/               # Builders de embeds
│
├── data/                 # Traducciones (es_*.py) + fuentes EN
│
├── storage/              # Persistencia JSON por rama
│
├── imgs/                 # Assets por rama
│
├── sort_lists.py         # Ordena listas de traducción
│
├── .env.example
└── requirements.txt
```

## Instalación

```bash
git clone https://github.com/a-vil/MMOSkill-embeds.git
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

---

## Licencia

[MIT](LICENSE)