# STYLE_GUIDE.md

Esta guía contiene los estándares técnicos y gramaticales para las localizaciones. El sistema de localización debe consultar este documento para garantizar la consistencia y naturalidad de los embeds.

## 1. Terminología Oficial
- **Magic Tree** → **Magic Skills**
- **Dark Tree** → **Dark Skills**
- **Halberd Tree** → **Halberd Skills**
- **Scroll Tree** → **Scroll Skills**
- **Skill Tree LvX** → **Skill Tier X** (Ej: "Skill Tier 3")
- **Tuning Point** → **Punto de Ajuste**
- **miss** → **Miss** (Mantener como término técnico del juego, usar construcciones como "resultará en Miss")
- **Anticipate** → **Anticipate** (Mantener como término técnico del juego, similar a Graze)
- **Absolute Critical** → **Absolute Critical** (Mantener como estado del ataque: indica que el golpe siempre será crítico)
- **Guard** → **Guard** (Mantener como término técnico del juego, usar construcciones como "ignorar Guard")
- **Evasion** → **Evasion** (Mantener como término técnico del juego, usar construcciones como "resultará en Evasion")
- **Graze** → **Graze** (Mantener como término técnico del juego, usar construcciones como "resultará en Graze")

## 2. Reglas de Naturalidad ("Regla de Oro")
Prioriza siempre la fluidez del lenguaje jugador sobre la literalidad.
- **Estructuras activas:** En lugar de "Se realizan los cálculos...", prefiere "El cálculo se realiza...".
- **Estados de Alteración:** Los estados de alteración siempre deben estar capitalizados (ej: `Flinch`, `Tumble`, `Stun`, `Bleed`, `Fatigue`).
- **Términos Técnicos Inalterables:** `Miss`, `Anticipate`, `Guard`, `Evasion`, `Graze` y `swift` (junto con otros combo tags) se mantienen en inglés y sin cambios.
- **Acciones con Términos Técnicos:**
    - Para "Miss": usar "resultará en Miss", "puede ser Miss". "no Miss" se mantiene como "no Miss" (no traducir como "no fallar").
    - Para "Guard": usar "ignorar Guard", "no ser bloqueado (Guard)".
    - Para "Evasion": usar "resultará en Evasion", "será Evasion".
    - Para "Graze": usar "resultará en Graze", "será Graze".
    - Para "Anticipate": usar "resultará en Anticipate", similar a Graze.
    - **NO** usar verbos conjugados como `falla`, `evadido`, `grazed`. Usar
      siempre los sustantivos mecánicos: `resulta en Miss`, `resulta en Evasion`,
      `resulta en Graze`.
- **Evitar redundancia nominal:** Reemplaza la repetición innecesaria de sustantivos con pronombres o construcciones más naturales.
  - *Ejemplo:* "refrescará el HP de la Barrera (solo cambia su posición)" en vez de "refrescará el HP de la Barrera (solo cambia la posición de la barrera)".
- **Género de términos en inglés:** Todos los términos técnicos en inglés se tratan como masculinos. Se omite el artículo definido cuando la frase se lee naturalmente sin él (ver §7 para la regla completa).
- **Términos de categoría en contexto genérico:** Cuando un término traduzca una categoría o clase (`non-boss map`, `boss map`) y el contexto sea genérico, prefiere el plural para sonar más natural.
  - *Ejemplo:* `"solo en mapas que no son de Boss"` en vez de `"solo en el mapa que no es de jefe"`.
- **Evitar calcos del inglés:** No traduzcas literalmente adverbios modales ingleses (`mostly`, `basically`, `actually`) como "mayormente", "básicamente", "actualmente". Prefiere adjetivos o paráfrasis naturales.
  - *Ejemplo incorrecto:* `"mayormente problema común"`
  - *Ejemplo correcto:* `"problema muy habitual"`
  - *Ejemplo:* `For THS only` → NO `"Para THS solamente"`; SÍ `"Solo para THS"`
  - *Ejemplo:* `1m otherwise` → NO `"1m de lo contrario"`; SÍ `"de lo contrario será 1m"`
  - **Labels de categoría de bonus:** Siguen el patrón `{Weapon} {modificador}:`
    del inglés. `Only` se traduce y reordena para naturalidad.
    `Main`/`Sub` se mantienen como jerga técnica.
    *Ejemplo:* `Knuckle Main Only` → `Solo Main Knuckle`
- **Descriptores posicionales en etiquetas compuestas:** Palabras como `First`,
  `Second`, `Last` describen orden/posición y SE TRADUCEN (`Primer`, `Segundo`,
  `Último`). No son términos mecánicos del juego, incluso si están junto a
  palabras excluidas como `Hit`.
  - *Ejemplo:* `First Hit Ailment Chance` → `Chance de Ailment del Primer Hit`
  - *Ejemplo:* `Second Hit Ailment Duration` → `Duración de Ailment del Segundo Hit`
- **Reorganización de etiquetas compuestas con palabras custom:** Cuando una
  custom word está embebida en un label de la forma `{Prefijo} {TerminoCustom}`:
  - Si el prefijo es **descriptor ordinal/posicional** → se traduce y conecta
    con preposición (`del`/`de`): `Chance de Ailment del Primer Hit`,
    `Duración de Ailment del Segundo Hit`
  - Si el prefijo es **nombre de mecánica** (Wave, Tornado, etc.) → se mantiene
    en inglés como paréntesis: `Número de golpes (Wave)`, `Ailment (Wave)`,
    `Chance de Ailment (Wave)`
- **Precisión técnica:** Mantén intactos los placeholders `{ohs}`, `{staff}`, `{all}`.
- **Género de "pasivo/a":** Cuando "passive" se usa como **sustantivo**
  (abreviatura de "passive skill"), debe ser femenino: `una pasiva`, `esta
  pasiva`. El masculino `un pasivo` solo es correcto cuando modifica a un
  sustantivo masculino explícito como `Efecto Pasivo`.
- **"Subhand":** Traducir como `mano secundaria` para naturalidad y
  consistencia. Ej: `subhand damage` → `daño de la mano secundaria`,
  `subhand sword` → `espada de la mano secundaria`,
  `Subhand Stability` → `Stability de la mano secundaria`.
  No usar `submano`, `sub mano` ni `segunda espada`.


## 3. Formato y Markdown
- **Fórmulas:** Usa `~~tachado~~` para indicar fórmulas antiguas o cambios de nivel si es necesario mostrar el histórico.
- **Listas:** Usa siempre `*` como viñeta inicial (no usar `•`).
- **Ailments:** Usa corchetes para estados de alteración: `[Flinch]`, `[Bleed]`.

## 4. Ejemplos de referencia (Estándar de calidad)
| Original | Localización mejorada |
|----------|----------------------|
| "Using aoe magic... beam stack is used" | "Al usar magia AoE (como Burst, Storm, Wall, etc.) que golpee a varios objetivos sin matarlos, se consumirá un beam stack..." |
| "has an innate Motion Speed penalty" | "tiene una reducción innata de Motion Speed" |
| "gains Critical Rate" | "obtiene Critical Rate" |

## 5. Anglicismos Naturalizados

Términos ingleses tan asimilados en el español gamer que se tratan como
palabras españolas a efectos de artículos y preposiciones.

| Término | Regla | Ejemplo |
|---------|-------|---------|
| Buff | Usar `del Buff`, `al Buff`, `el Buff` con normalidad. | `Duración del Buff`, `Efecto del Buff` |
| Cooldown | Usar `el cooldown`, `del cooldown` con normalidad. | `el Cooldown comienza`, `duración del cooldown` |
| Slot | Usar `el slot de arma principal`, `el slot de arma secundaria`. No usar "ranura". | `Knuckles en el slot de arma principal` |
| Hit | Usar `el hit`, `los hits`, `del hit`, `al hit` con normalidad en frases fluidas. | `el primer hit`, `al otro hit`, `los otros hits` |
| DEF | Usar `la DEF`, `de la DEF` con normalidad. Asociado a `Defensa` en español. | `mayor es la DEF del objetivo` |
| Main/Sub | "Main" y "Sub" como estado del arma, con mayúscula inicial. No traducir a "principal"/"secundaria". | `"Main Katana (no Sub-Katana)"`, `"para Main Knuckle"` |

## 6. Traducción Fiel — No inventar contenido

No añadas texto que no esté presente en el original. Si el original dice
"Defaults to the weapon's Auto Attack Max Range", la traducción debe ser
"Por defecto el rango máximo de Auto Attack del arma" — sin añadir lógica
de slots, armas específicas, ni condiciones como "de lo contrario será 1m".

- *Incorrecto:* `"Por defecto el rango máximo de Auto Attack de {halberd}
  si está equipado en el slot de arma principal o secundaria; de lo
  contrario será 1m"`
- *Correcto:* `"Por defecto el rango máximo de Auto Attack del arma"`
- **"current" → "actual":** En contextos de estadísticas o valores vigentes, `current` se traduce como `actual`. No mantener "current" en inglés ni usar "corriente".
  - *Ejemplos:* `current HP` → `HP actual`, `current stack` → `stack actual`, `current position` → `posición actual`, `Current Lightning Hail's Base Skill Constant` → `Base Skill Constant Actual de Lightning Hail`

Excepción: si el original menciona explícitamente el arma
(`"the Katana's Auto Attack Max Range"`), tradúcelo como
`"rango máximo de Auto Attack de katana"`.

## 7. Términos Técnicos en Inglés — Género y Artículo

Todos los términos técnicos en inglés (compuestos o abreviaciones) se tratan
como masculinos a efectos de género gramatical.

**Siempre se omite el artículo cuando la frase se lee de forma natural sin él.**

- **Bullets, fórmulas y listados:** nunca llevan artículo.
  - `* Critical Rate +25`  ✓
  - `* ATK +1%`  ✓
- **Inicio de oración o cláusula:** se omite el artículo.
  - `Skill Multiplier aumenta con el nivel`  ✓
  - `Critical Rate se duplica durante el buff`  ✓
- **Texto fluido:** se omite si suena natural; solo se usa `el` cuando la
  estructura de la oración lo exige.
  - `Aumenta Skill Multiplier del autoataque`  ✓ (preferido)
  - `Aumenta el Skill Multiplier del autoataque`  ✓ (alternativa válida)
  - `según MP restante`  ✓
  - `ir a Town`  ✓ (preferido sobre `ir al Town`)

Los anglicismos naturalizados (§5) mantienen su regla específica.

- **Adjetivos con términos técnicos:** Los adjetivos que modifican
  términos en inglés concuerdan en masculino.
  - `Alto Critical Rate`  ✓ (no `Alta Critical Rate`)
  - `bajo Accuracy`  ✓ (no `baja Accuracy`)
  - `el segundo hit tiene un boost de Critical Rate`  ✓

## 8. Desambiguación Stat vs. Descriptivo

Cuando un término inglés puede ser nombre de estadística o descripción narrativa, se distingue por contexto:

- **Stat** → inglés, mayúscula inicial: `Critical Damage`, `Magic Pierce`
- **Descriptivo** → español: `daño crítico`, `daño mágico`

Regla práctica: si puedes reemplazarlo por "la estadística X" o "el valor de X", es stat y va en inglés. Si describe la naturaleza del daño, es descriptivo y va en español.

| Contexto | Stat | Descriptivo |
|----------|------|-------------|
| `Aumenta Critical Damage en +X%` | ✅ | ❌ |
| `chance de infligir daño crítico` (hit crítico) | ❌ | ✅ |
| `usan Critical Damage mágico` (la stat) | ✅ | ❌ |
