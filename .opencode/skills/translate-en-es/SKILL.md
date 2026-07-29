---
name: translate-en-es
description: Localiza archivos .txt de inglés a español. Se activa con "traduce", "localiza", "transforma" o "convierte". Lee words_excluded.txt y words_custom.txt de data/. Genera archivos .py con SkillText.
---

# Localización EN→ES

> **⚠️ Alcance de esta guía:** Cuando se haga referencia a "la guía y skill
> de localización", se entienden incluidos **los 4 archivos**:
> - `SKILL.md` (flujo, reglas, checklist)
> - `STYLE_GUIDE.md` (reglas de estilo detalladas)
> - `words_custom.txt` (traducciones personalizadas)
> - `words_excluded.txt` (palabras excluidas)
>
> **⚠️ Antes de localizar o responder**, releer los 4 archivos completos.
> No responder desde la memoria o intuición.

## Uso

```text
> traduce / localiza / transforma / convierte <archivo>         # Crea es_<archivo> como .py nuevo
> traduce / localiza / transforma / convierte <archivo> <salida>  # Agrega al final del archivo existente
```

## Ejemplos

```text
> traduce data/sshot.txt                      → Crea data/es_sshot.py
> localiza data/smartial.md                   → Crea data/es_smartial.py
> transforma data/sshot.txt                   → Crea data/es_sshot.py
```

## Flujo

> ⚠️ **Nuevas palabras en excluded/custom:** Cualquier palabra nueva propuesta para `words_excluded.txt` o `words_custom.txt` debe ser aprobada por el usuario antes de añadirla. No agregar palabras sin consentimiento explícito.

1. Leer archivo fuente (.txt o .md)
2. Leer `data/words_excluded.txt`
3. Leer `data/words_custom.txt`
4. Consultar `STYLE_GUIDE.md` para reglas de estilo y terminología
5. Identificar skills por su delimitador:
   - Archivos `.txt`: `<>` antes del nombre (ej: `<>Power Shot`)
   - Archivos `.md`: `#### **` con markdown (ej: `#### **Smash**`)
6. Para cada skill:
   - Aplicar traducciones personalizadas (custom > excluidas)
   - Localizar usando las reglas de naturalidad de `STYLE_GUIDE.md`
   - Mantener palabras excluidas sin localizar
7. Generar archivo .py con formato SkillText
8. Evaluar la localización — verificar TODAS las reglas de `STYLE_GUIDE.md`:
   - **§1 Terminología Oficial:** Miss, Guard, Evasion, Graze, Anticipate,
     Absolute Critical, etc. mantenidos en inglés.
   - **§2 Reglas de Naturalidad:** Verbos conjugados → sustantivos mecánicos
     (`resulta en Miss`, no `falla`); redundancia nominal; "pasivo/a" (femenino
     como sustantivo); plural en genéricos; calcos del inglés.
   - **§3 Formato y Markdown:** Viñetas `*`, corchetes para ailments.
   - **§4 Ejemplos de referencia:** Estándar de calidad.
   - **§5 Anglicismos Naturalizados:** Buff, Cooldown, Slot, Hit, DEF con
     artículos españoles normales.
   - **§6 Traducción Fiel:** No inventar contenido condicional; "current" →
     "actual".
   - **§7 Términos Técnicos en Inglés:** Género y artículo correctos.
   - **§8 Desambiguación Stat vs Descriptivo:** Critical Damage (stat) vs
     daño crítico (descriptivo), Absolute Critical (estado).
   - **words_excluded.txt:** Ninguna palabra excluida localizada al español.
   - **words_custom.txt:** Todas las traducciones custom aplicadas
     correctamente.
    - **Placeholders `{weapon}`:** Solo en líneas de restricción de arma, no
      en bonus/labels.
    - **"Main {weapon}" / "{weapon} Main" / "Sub {weapon}":** Cuando
      "Main" o "Sub" califican directamente al nombre del arma como
      estado (arma principal/secundaria), preservar "Main"/"Sub" en
      inglés con mayúscula inicial. NO traducir a "principal"/"secundaria".
      Ej: "Main Katana", "Sub Knuckle", "Main Magic Device Only".
   - Documentar los hallazgos para el paso siguiente.
9. Informe post-localización — documentar hallazgos para corrección manual y
   mantener consistencia.

## Reglas de localización

```text
1. Custom translations → se aplican PRIMERO (aunque la palabra esté excluida)
2. Excluded words → NO se localizan (solo si NO tienen traducción custom)
3. Texto restante → se localiza con IA de forma natural
4. Palabras excluidas en contexto → la palabra excluida se mantiene, pero las palabras a su alrededor se traducen si no están en excluded/custom
```

## Formato de salida

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class SkillText:
    title: str
    description: str
    details: str


SKILL_NAME = SkillText(
    title="Título",
    description="**Descripción del juego:** *\"...\"*",
    details="**Habilidad Tier X;** Solo {bow} / {bowgun}..."
)
```

> **Referencia:** `data/es_sshot.py` contiene el ejemplo completo con 25 skills en este formato.

## Matching de palabras

Ambos archivos (excluidas y custom) usan las mismas reglas:

- **Case-insensitive:** no distingue mayúsculas/minúsculas
- **Frase exacta:** solo coincide cuando la palabra/frase está completa
- **Ignorar formato:** caracteres como `[`, `]`, `*`, `**` se ignoran al comparar

### Palabras excluidas

- "ATK" excluye "ATK" pero no "ATKs"
- "Power Shot" excluye "Power Shot" pero no "Power Shots"
- "Tumble" excluye "[Tumble]" y "**Tumble**"
- "Hit" excluye "hit" e "hits", pero NO excluye las palabras a su alrededor
  - "for that hit only" → "solo para ese hit" (hit se mantiene, "for that" y "only" se traducen)
  - "on the second hit" → "en el segundo hit" (hit se mantiene, "on the" y "second" se traducen)

### Traducciones personalizadas

- "MP Cost" coincide con "MP Cost: 100" pero NO con "Cost: 50" ni "MP: 100"
- "Lv {n} Skill" coincide con "Lv 1 Skill", "Lv 2 Skill", etc.
- "Lv 1 Skill" NO coincide con "Lv 1 Skillset" (frase exacta)
- **Flexión de número:** La IA debe inflccionar el número
  (singular/plural) de los términos en `words_custom.txt` según el
  contexto de la frase para lograr naturalidad.
  - Ej: `non-boss map → mapas que no son de jefe` se inflcciona
    manteniendo la forma registrada en custom, pero adaptando
    concordancia si el contexto lo requiere.
- **Etiquetas compuestas:** Una custom word como `Hit Count` NO coincide dentro
  de `Wave Hit Count` o `First Hit Ailment Chance` por la regla de frase exacta.
  La corrección manual debe seguir el patrón de reorganización de `STYLE_GUIDE.md`.

## Archivos de datos

- `data/words_excluded.txt` — palabras excluidas (no se localizan)
- `data/words_custom.txt` — traducciones específicas con variables {n}

## Guía de Estilo

Para asegurar la calidad y naturalidad del texto final, el bot DEBE consultar siempre `.opencode/skills/translate-en-es/STYLE_GUIDE.md` durante el proceso de localización.

**Regla de Oro:** "Si una estructura suena robótica o poco natural, prefiere la fluidez del jugador (ej: uso de activos, oraciones breves) sobre la literalidad del original."
