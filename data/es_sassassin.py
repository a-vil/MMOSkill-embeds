from dataclasses import dataclass


@dataclass(frozen=True)
class SkillText:
    title: str
    description: str
    details: str


FOOTER = "Créditos: Phantom's Library"

INDEX_HEADER = [
    "**Nivel requerido:** T1 15, T2 Lv35, T3 Lv125, T4 Lv205, T5 lv285",
    '**Selecciona un "Texto Azul" para guiarte hacia él.**',
    "",
]


ASSASSIN_STAB = SkillText(
    title="Assassin Stab",
    description="**Descripción del juego:** *\"Asesta un golpe mortal al objetivo. La efectividad del ataque depende de la dirección del golpe. Apunta a la espalda del objetivo para maximizarlo.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  **Base Skill Constant:** 30 * Skill Level\n"
        "*  El **Base Skill Multiplier** varía según la dirección de uso:\n"
        "  [315°-40°]Frente: 1 + 0.01 * Skill Level\n"
        "  [225°-315°,45°-135°]Lado: 1.05 + 0.03 * Skill Level\n"
        "  [225°-135°]Atrás: 1.1 + 0.09 * Skill Level\n\n"
        "**Dagger/Scroll bonus:** Skill Multiplier +0.5 (Frente), +1 (Lado), +3 (Atrás)\n\n"
        "{image}"
    ),
)

EVASION = SkillText(
    title="Evasion",
    description="**Descripción del juego:** *\"Técnica para mejorar la capacidad de esquivar. Aumenta la tasa de dodge durante cierto tiempo y elimina el Ailment: [Slow].\"*",
    details=(
        "**Habilidad Tier 1;** Activa (Party-Buff); Sin Restricciones {all}\n"
        "**Coste MP:** 200\n\n"
        "**Efecto del Buff:**\n"
        "*  Otorga Flat Dodge y Dodge% durante (20 + Skill Level) segundos\n"
        "*  Elimina el Ailment Slow mientras esté activo\n"
        "*  Dodge: +Skill Level\n"
        "*  Dodge%: +Skill Level%\n\n"
        "**Dagger/Scroll bonus:** La duración se duplica\n"
        "**Dagger/Scroll bonus:** +10 Dodge"
    ),
)

BACKSTEP = SkillText(
    title="Backstep",
    description="**Descripción del juego:** *\"Técnica para escapar instantáneamente del peligro. Recupera un poco de MP al usarla contra la advertencia de ataque de un monstruo. Aumenta el poder de Assassin Stab cuando se usa junto a esta habilidad.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Coste MP:** 100\n"
        "**Efecto de la habilidad:**\n"
        "*  Retrocede 5m y otorga un aumento de daño para Assassin Stab (si se usa a continuación)\n"
        "*  Recupera MP al usar esta habilidad durante la advertencia de ataque AoE de un Boss (refiriéndose al signo de exclamación \"?\" que aparece sobre la cabeza del personaje)\n"
        "*  Recuperación de MP: 5 * Skill Level\n"
        "*  Aumenta el daño de Assassin Stab en (5 * Skill Level)% [se aplica aditivamente con el buff de Foresight]\n\n"
        "Si tienes Backstep y Foresight al mismo tiempo, obtienes un +100% de daño adicional a Assassin Stab como bonificación.\n"
        "Total cuando Backstep y Foresight están activos = +(100 + 5 * Backstep Lv + 5 * Foresight Lv)%\n\n"
        "**Dagger/Scroll bonus:** La recuperación de MP se duplica"
    ),
)

SERUM = SkillText(
    title="Serum",
    description="**Descripción del juego:** *\"Técnica para aliviar y calmar el dolor. Reduce el daño en el tiempo debido a los Ailments: [Poison] e [Ignite] durante cierto tiempo.\"*",
    details=(
        "**Habilidad Tier 2;** Activa (Party-Buff); Sin Restricciones {all}\n"
        "**Coste MP:** 300\n\n"
        "**Duración:** 10 + Skill Level\n\n"
        "**Efecto del Buff:**\n"
        "*  Reduce el DOT del jugador en un porcentaje.\n"
        "*  Daño reducido (Ignite): (10 + 2 * Skill Level)% [se aplica aditivamente con Stone Barrier]\n"
        "*  Daño reducido (Poison): (25 + 2.5 * Skill Level)% [se aplica aditivamente con Stone Barrier]\n\n"
        "**Dagger/Scroll bonus:** La duración se triplica"
    ),
)

ARCANE_STRIKE = SkillText(
    title="Arcane Strike",
    description="**Descripción del juego:** *\"Técnica secreta transmitida por un escuadrón de asesinos. Usa todo el MP y mejora la recuperación de MP de ataque hasta que se active la siguiente habilidad. Reduce significativamente el Aggro cuando no estás siendo objetivo.\"*",
    details=(
        "**Habilidad Tier 3;** Solo Dagger/Scroll\n"
        "**Coste MP:** 100 + MP restante de la barra de MP\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  **Base Skill Constant:** 500 + 50 * Skill Level\n"
        "*  **Base Skill Multiplier:** 0.1 * Skill Level + (0.6 + 0.04 * Skill Level) * (MP/100) {{este MP es solo de la barra de MP}}\n"
        "*  AMPR: +10 (niveles 1-5), +20 (niveles 6-10)"
    ),
)

FORESIGHT = SkillText(
    title="Foresight",
    description="**Descripción del juego:** *\"Supera el límite de tu capacidad de esquivar. Reduce la accuracy mínima del monstruo y facilita esquivar ataques. También aumenta el poder de Assassin Stab.\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Efecto Pasivo:**\n"
        "*  Aumenta el bonus de daño para Assassin Stab pasivamente\n"
        "*  Reduce la accuracy mínima del enemigo (hit) SOLO para ti\n"
        "*  Aumenta el límite máximo de tasa de proceso de Dodge\n"
        "*  Accuracy mínima del enemigo: (25 - Skill Level)%\n"
        "*  Chance máxima de Dodge: (75 + Skill Level)%\n"
        "*  Aumenta el daño de Assassin Stab en (5 * Skill Level)% [se aplica aditivamente con el buff de Backstep]\n\n"
        "Si tienes Backstep y Foresight al mismo tiempo, obtienes un +100% de daño adicional a Assassin Stab como bonificación.\n"
        "Total cuando Backstep y Foresight están activos = +(100 + 5 * Backstep Lv + 5 * Foresight Lv)%\n\n"
        "Los ataques que incluyen Perfect Aim de un enemigo ignorarán esta verificación de hit de esta habilidad."
    ),
)

SICARIUS = SkillText(
    title="Sicarius",
    description="**Descripción del juego:** *\"Aumenta el poder de Back Stab con efecto duradero. Una ejecución exitosa de Back Stab mejorará ligeramente el ATK y Physical Pierce por un breve tiempo. El daño recibido se reducirá ligeramente y el efecto de mejora se perderá.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Efecto Pasivo:**\n"
        "*  Aumenta pasivamente el multiplicador \"Atrás\" (no frente ni lado) de Assassin Stab.\n"
        "*  Al usar Assassin Stab exitosamente en la espalda del objetivo, otorga un buff de Physical Pierce%, Flat ATK y reducción de daño recibido. El buff termina al recibir un hit.\n"
        "*  Multiplicador [Atrás] de Assassin Stab: +0.15 * Skill Level [+1 con Dagger/Scroll Bonus]\n"
        "*  Flat ATK: 5 * Skill Level * 2[con Dagger/Scroll Bonus]\n"
        "*  Physical Pierce%:\n"
        "  * > Con Dagger/Scroll: (15 + Skill Level)%\n"
        "  * > Sin Dagger/Scroll: (Skill Level)%\n"
        "*  Reducción de daño recibido: (10 + Skill Level + Floor[(0.5 + Skill Level * 0.05) * Nivel de Foresight])%\n"
        "*  Duración del Buff: 30 segundos o hasta recibir un hit"
    ),
)

SHADOW_WALK = SkillText(
    title="Shadow Walk",
    description="**Descripción del juego:** *\"Otorga brevemente un efecto de ataque adicional junto con Evasion si no estás siendo objetivo. (El rango depende del arma.) Ciertos movimientos mejoran el ataque adicional, pero el efecto se reinicia si recibes daño mientras eres objetivo. No puede usarse repetidamente.\"*",
    details=(
        "**Habilidad Tier 4;** Solo Dagger/Scroll\n"
        "**Coste MP:** 100\n"
        "**Alcance de acción:** Infinito\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Al usar esta habilidad, otorga un stack inicial de (1 * Skill Level). Puedes generar hasta (10 + Skill Level) stacks.\n"
        "*  Duración del Buff: 3 minutos independientemente del nivel\n"
        "*  Para generar stacks, debes usar estas habilidades sin tener aggro del objetivo:\n"
        "  *  Backstep puede generar 3 stk\n"
        "  *  Assassin Stab, Evasión manual, Back Stab pueden generar 1 stk\n"
        "  Nota: usar Back Stab puede activar Assassin Stab y Back Stab al mismo tiempo, y otorga 2 stk.\n"
        "*  Si recibes un hit de un enemigo que tiene aggro sobre ti, tus stacks se reducen a 0.\n"
        "*  Esta habilidad no puede usarse repetidamente para reiniciar la duración o los stacks después de la activación inicial.\n\n"
        "*  Durante el buff de Shadow Walk, cada vez que hagas Evasion y el objetivo esté dentro de tu rango de autoataque por defecto, esta habilidad infligirá daño. Cuantos más stacks, más daño.\n"
        "*  **Base Skill Constant:** 100 (para todos los hits)\n"
        "*  **Base Skill Multiplier** (para todos los hits):\n"
        "  = (1 + 0.1 * Skill Level) * (1 + Floor((stack - 1)/4) * 0.25)% * ATK de Dagger o Scroll\n"
        "*  **Número de golpes:** 1 + Floor((stack - 1)/4)\n\n"
        "*  Si tu stack es superior a 10, la habilidad infligirá daño mejorado al esquivar exitosamente un ataque enemigo (incluyendo AoE) con Evasion (manual y automática funcionan). Al infligir daño mejorado, consume 10 stacks. Nota: Evasion otorga invencibilidad cuando estás a punto de recibir un hit durante la animación de Evasion.\n"
        "*  **Base Skill Constant (mejorado):** 100 (para todos los hits)\n"
        "*  **Base Skill Multiplier (mejorado):** 10 + 2 * Skill Level (para todos los hits)\n"
        "*  **Número de golpes (mejorado):** 10 hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits"
    ),
)

VENOM_INJECTION = SkillText(
    title="Venom Injection",
    description="**Descripción del juego:** *\"Técnica de asesinato que aplica veneno a tu arma. Consume tu HP para obtener la chance de infligir poison durante los ataques normales. La chance depende de las stats de la daga, el ninjutsu scroll y cambia según Critical o Graze.\"*",
    details=(
        "**Habilidad Tier 1;** Solo Dagger/Scroll/BH\n"
        "**Coste MP:** 100\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Usar esta habilidad cuesta un 5% de tu MaxHP y te otorga +(Skill Level) Venom Stack. Puedes almacenar hasta (2 * Skill Level) Venom Stacks.\n"
        "*  Si tienes Venom Stacks, tu autoataque tiene chance de infligir Poison ailment. Al infligir Poison exitosamente con esta habilidad, se reduce 1 Venom Stack.\n\n"
        "**Ailment:** Poison\n"
        "**Chance Base de Ailment:** MAX[1% ; (Sub Weapon Atk/50)%] * 2[si crit] / 2[si graze]\n"
        "Nota: Sub Weapon Atk =\n"
        "  Scroll: +(Scroll ATK * 0.8)\n"
        "  Dagger: +(Dagger ATK)\n"
        "  OHS/HB Bonus: Chance Base de Ailment multiplicada por (Skill Level)\n"
        "  BH Bonus: Cambia la Chance Base de Ailment a:\n"
        "  (10 * Skill Level)% * 2[si crit] / 2[si graze]\n\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "*Nota sobre la chance de ailment: Calcula la chance base de ailment primero, luego redondea hacia abajo… luego multiplica por el bonus OHS/HB según Skill Level (aunque no está claro si este redondeo ocurre \"después\" o \"antes\" de los cambios por crit/graze, pero muy probablemente \"después\").\n"
        "*Otra nota sobre BH: la chance de BH sub es exactamente la misma que la chance de BH main solamente, lo que significa que como BH sub, el arma secundaria no aumenta la chance de poison en absoluto… es como si el arma secundaria se ignorara debido a cambios en [main bh]. Por eso dice \"Cambia la chance base de ail\" en el bonus BH.\n\n"
        "No puedes usar esta habilidad si no tienes suficiente HP."
    ),
)

CORROSIVE_POISON = SkillText(
    title="Corrosive Poison",
    description="**Descripción del juego:** *\"Permite acumular poison con Venom Injection (máx +2). Si se convierte en poison mejorado debido a la acumulación, el ataque del jugador también podrá infligir daño de poison.\"*",
    details=(
        "**Habilidad Tier 2;** Solo Dagger/Scroll/BH\n\n"
        "**Efecto Pasivo:**\n"
        "*  Permite acumular poison múltiples veces hasta +2 solo con Venom Injection. Nota: Puedes infligir otro poison (como Poison Dagger/Draconic Charge/etc.) para el poison inicial (+0), pero solo Venom Injection puede acumular poison encima (Poison+0 a +1, luego +1 a +2).\n"
        "*  La chance depende del nivel de esta habilidad:\n"
        "  Poison+1 chance: (25 + Skill Level * 5)% de la Chance Final de Poison+0 (Venom Inject)\n"
        "  Poison+2 chance: (Skill Level * 5)% de la Chance Final de Poison+0 (Venom Inject)\n"
        "*  La duración de Poison se extiende +10s cada vez que infliges Poison+1 o Poison+2 exitosamente.\n"
        "*  Si un objetivo tiene Poison+1 o Poison+2, atacar a ese objetivo infligirá automáticamente daño de poison (incluso otros jugadores/mascotas/mercenarios pueden infligir daño de poison). Pero este poison solo puede infligirse/activarse una vez como máximo cada 1 segundo. Esto significa que usar una habilidad de múltiples hits no activará este poison múltiples veces en 1 segundo, incluso si tú y tus aliados golpean al mismo tiempo, ¡solo se activa una vez! Nota: aunque es posible obtener múltiples poison en 1 segundo, solo se logra cuando los enemigos atacan.\n\n"
        "El daño de poison de esta habilidad:\n"
        "  Poison dmg = escala dex + escala (ATK+MATK)\n"
        "  Poison+1 dmg = escala dex + 2 * escala (ATK+MATK)\n"
        "  Poison+2 dmg = escala dex + 3 * escala (ATK+MATK)"
        " Poison Damage Calculation = [Total DEX + (Total ATK + Total MATK) * MIN(0.5, (EnemyDEF + EnemyMDEF) ÷ 2 ÷ (EnemyLvl * 6))] * ((200% - E.P.res% - E.M.res%) ÷ 2). Formula por Joji, Insane23, and xenesis5"
    ),
)

VENOM_THIEF = SkillText(
    title="Venom Thief",
    description="**Descripción del juego:** *\"Absorbe el poison corrosivo del objetivo para restaurar tu propio HP y eliminar el estado de poison. Si es poison mejorado, también se restaurará MP. Si no estás envenenado, obtendrás un efecto que te previene de ser envenenado.\"*",
    details=(
        "**Habilidad Tier 3;** Solo Dagger/Scroll/BH\n"
        "**Coste MP:** 200\n"
        "**Alcance máximo de Cast:** 12m\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Solo puedes usar esta habilidad si el objetivo tiene poison ailment.\n"
        "*  Usar esta habilidad eliminará el poison ailment de ti si estás envenenado.\n\n"
        "*  Usar esta habilidad en Poison =\n"
        "  Recuperación de HP: (1000 + TotalDEX) * Skill Level / 10\n"
        "  Si ya has aprendido Death Reception, obtienes (Deadly Poison 0 stack)\n\n"
        "*  Usar esta habilidad en Poison+1 =\n"
        "  Recuperación de HP: (1000 + TotalDEX) * 2 * Skill Level / 10\n"
        "  Recuperación de MP: (10 * Skill Level)\n"
        "  Si no estás envenenado, obtienes efecto \"Recovery (de Support Tree)\" que anula ailments durante 10 segundos\n"
        "  Si ya has aprendido Death Reception, obtienes (Deadly Poison 1 stack)\n\n"
        "*  Usar esta habilidad en Poison+2 =\n"
        "  Recuperación de HP: (1000 + TotalDEX) * 4 * Skill Level / 10\n"
        "  Recuperación de MP: (20 * Skill Level)\n"
        "  Si no estás envenenado, obtienes efecto \"Recovery (de Support Tree)\" que anula ailments durante 30 segundos\n"
        "  Si ya has aprendido Death Reception, obtienes (Deadly Poison 2 stack)\n\n"
        "No puedes acumular Deadly Poison anterior con un nuevo Deadly Poison, ya que el nuevo stack sobrescribirá el anterior.\n\n"
        "Nota: Usar Recovery de Support Tree (ej. lv 1: 12s) cuando ya tienes un efecto Recovery de esta habilidad (ej. +30s con Poison+2), resultará en obtener 12s de Recovery lv 1 debido a que el nuevo Recovery sobrescribe el anterior. En cambio, usar esta habilidad para obtener Recovery cuando ya tienes Recovery (Support Tree) no sobrescribe ese Recovery (Support Tree), independientemente del nivel de habilidad."
    ),
)

DEATH_RECEPTION = SkillText(
    title="Death Reception",
    description="**Descripción del juego:** *\"Usa el poison absorbido con Venom Thief para infligir daño y Deadly Poison al objetivo. Dependiendo del poison usado, también se generará daño que inflige poison a tu alrededor.\"*",
    details=(
        "**Habilidad Tier 4;** Solo Dagger/Scroll/BH\n"
        "**Coste MP:** 300\n\n"
        "**Base Skill Constant (Objetivo Principal):** 30 * Skill Level\n"
        "**Base Skill Multiplier (Objetivo Principal):** 2.5 + 0.25 * Skill Level + SubWeapon Bonus\n"
        "Nota: SubWeapon Bonus =\n"
        "  Scroll: +(Scroll ATK/100 * 0.8) mult\n"
        "  Dagger: +(Dagger ATK/100) mult\n"
        "  One-Handed Sword Bonus: Skill Multiplier +(TotalDEX/100)\n"
        "  Halberd Bonus: Skill Multiplier +(BaseAGI/100)\n"
        "  Barehand Bonus: Cambia el Base Skill Multiplier a:\n"
        "  2.5 + 0.25 * Skill Level + PlayerLevel/80 + Accumulated Qi/100\n\n"
        "*Nota sobre Main BH: esta habilidad podría tener un bug o penalización de ataque extraña… usa el ATK total después del coste de qi[de usar esta habilidad con skill que no sea BH], haciendo imposible tener el ATK máximo debido al coste de qi primero. Pero según lo que probé en otras habilidades de ataque como Kick (Hunter Skills), Smash & Bash (Martial Skills), usan el ATK total antes del coste de qi[lo que permite tener ATK máximo]. Supongo que esta nueva habilidad es especial entonces [debido al daño separado: hit principal y hit AoE]. Afortunadamente, el qi acumulado en la fórmula del multiplicador permanece intacto/antes del coste de qi.\n"
        "*Otra nota: no sé si esto es un bug o no, pero cuando BH sub usa esta habilidad es lo mismo que Main BH usando esta habilidad pero sin qi stack. Es decir, BH sub no recibe el bonus de multi del arma secundaria [el bonus de sub weapon se ignora]. Este es el mismo caso que Venom Injection [cambia a fórmula sin sub weapon].\n\n"
        "**Base Skill Constant (AoE):** 0\n"
        "**Base Skill Multiplier (AoE):** 50% del Base Skill Multiplier (Objetivo Principal)\n\n"
        "**Número de golpes:** 1 hit principal en el objetivo principal; 1 hit adicional en los alrededores del objetivo principal\n"
        "**Alcance del golpe AoE:** 8m alrededor del objetivo principal\n"
        "**Alcance máximo de Cast:** 8m\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Solo puedes usar esta habilidad si tienes Deadly Poison stacks (vía Venom Thief).\n"
        "*  Esta habilidad (Objetivo Principal y AoE) tiene Physical Pierce según el Deadly Poison stack:\n"
        "  Deadly Poison 0 = +0% Physical Pierce\n"
        "  Deadly Poison 1 = +25% Physical Pierce\n"
        "  Deadly Poison 2 = +50% Physical Pierce\n"
        "  One-Handed Sword/Halberd/Barehand Bonus: Physical Pierce de esta habilidad +25%\n\n"
        "*  Al usar esta habilidad, inflige Deadly Poison debuff al objetivo principal. Deadly Poison 0 debuff = 10 ticks de daño de deadly poison comenzando con 1% de daño de (Death Reception Damage al Objetivo Principal) en el primer tick, luego el siguiente tick aumenta +1% de daño, y así hasta el último tick con 10% de daño.\n"
        "  Tener un Deadly Poison stack más alto significa más daño de deadly poison. Deadly Poison 1 damage = 2x del Deadly Poison 0 Damage. Deadly Poison 2 damage = 3x del Deadly Poison 0 Damage.\n\n"
        "*  Mientras tanto, el AoE de esta habilidad puede infligir +100% de Poison (según el Deadly Poison stack) a los otros objetivos alrededor del principal. [Inflige Poison con 0 stacks, Poison+1 con 1 stack, o Poison+2 con 2 stacks]. Nota: el AoE de esta habilidad no puede matar a otros, ya que siempre los deja con 1 HP.\n\n"
        "*  Usar Arcane Strike en el objetivo que tiene Deadly Poison debuff provocará daño de Deadly Poison Explode y finalizará la duración del Deadly Poison debuff. El daño de Deadly Poison Explode depende del stack:\n"
        "  Arcane Strike en Poison+0 = daño de Explode: 20% del \"Death Reception Damage al Objetivo Principal\"\n"
        "  Arcane Strike en Poison+1 = 40% de Death Reception Damage\n"
        "  Arcane Strike en Poison+2 = 60% de Death Reception Damage\n"
        "*  Además, el Coste MP de Arcane Strike con Deadly Poison debuff dependerá del Deadly Poison stack. Arcane Strike en Deadly Poison 1 tendrá la mitad del coste de MP. Arcane Strike en Deadly Poison 2 no tendrá coste de MP. Nota: el daño de Arcane Strike permanece igual que antes de esta reducción de MP, es decir, igual que cuando se usó todo el MP."
    ),
)

SECRET_ASSASSIN = SkillText(
    title="Secret Assassin",
    description="**Descripción del juego:** *\"Profundiza tu comprensión de las técnicas de asesinato. Aumenta el poder de las habilidades \"Assassin Stab\" y \"Arcane Strike\".\"*",
    details=(
        "**Habilidad Tier 5;** [Pasivo] Sin Restricciones {all}\n"
        "**Efecto Pasivo:**\n"
        "*  Aumenta el Base Skill Multiplier de Arcane Strike en +(0.025 * Skill Level * Barra MP). Multiplicador Final = 0.1 * Nivel de Arcane Strike + (0.6 + 0.04 * Nivel de Arcane Strike + 0.025 * Skill Level) * Barra MP\n"
        "*  Aumenta el Base Skill Multiplier de Assassin Stab (Front Stab, Side Stab, Back Stab) en:\n"
        "  > [Halberd]\n"
        "  > Assassin Stab Skill Multiplier + 0.02 * Skill Level\n"
        "  > [Dagger]\n"
        "  > Assassin Stab Skill Multiplier + 0.3\n"
        "  > [Otras Armas]\n"
        "  > Assassin Stab Skill Multiplier + 0.1 * Skill Level\n"
        "  > [Dagger/Ninjutsu Scroll]\n"
        "  > Assassin Stab Skill Multiplier + 2\n\n"
        "Este bonus de multiplicador se aplica primero junto con el bonus de multi de Sicarius, antes de multiplicarse por el multiplicador de aumento de daño de Backstep y Foresight. Así puedes alcanzar hasta 30 de multiplicador con esta habilidad.\n\n"
        "*Posible bug: el efecto registlet de Assassin Stab no funciona si tienes esta habilidad Secret Assassin… [el registlet es sobrescrito por esta habilidad por alguna razón].\n\n"
        "**Dagger/Ninjutsu Scroll bonus:** Aumenta aún más el poder de Assassin Stab."
    ),
)

ASSAULT_CHASE = SkillText(
    title="Assault Chase",
    description="**Descripción del juego:** *\"Restaura la Evasion en un 50% si se obtiene un nuevo buff y disminuye el consumo de Evasion hacia (o alrededor) del objetivo del ataque durante 180 segundos. El efecto del buff terminará cuando el contador de Evasion restante llegue a 0.\"*",
    details=(
        "**Habilidad Tier 5;** [Activo] Sin Restricciones {all}\n"
        "**Coste MP:** 800\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Restaura tu Evasion en un 50% de tu Evasion total. Puedes restaurar Evasion al usarla solo si no tienes este buff activo.\n"
        "*  El efecto del buff termina inmediatamente cuando tu Evasion actual llega a 0.\n"
        "*  Si esta habilidad está en nivel 10, obtienes Evasion automática (puede esquivar solo autoataques) durante la animación de esta habilidad.\n\n"
        "**Efecto del Buff:**\n"
        "*  Duración del Buff: 3 minutos O cuando tu Evasion actual llega a 0\n"
        "*  Reduce el consumo de Evasion al usarla hacia tu objetivo o cerca del objetivo dentro de 7m en (2.5 * Skill Level)% [Dagger/Ninjutsu Bonus: +25%]. Esta reducción de Evasion se acumula multiplicativamente con la reducción de Evasion de Combat Knife.\n"
        "*  Otorga SRD% por cada vez que evitas daño exitosamente con Evasion en 1% [Dagger/Ninjutsu Bonus: duplica esta ganancia de SRD%]. Puedes obtener hasta un 20% de SRD independientemente del Skill Level. Nota: si usas esta habilidad de nuevo cuando tienes SRD%, empezarás desde 0% SRD.\n\n"
        "* Un Dodge exitoso con Evasion mientras el buff está activo añade un efecto que aumenta el poder de ataque cuerpo a cuerpo.\n"
        "* Añade efecto de Evasion a la animación de activación de Assault Chase solo si el nivel de habilidad es 10.\n"
        "**Dagger/Ninjutsu Scroll bonus:** * Reduce aún más el consumo de Evasion. * Aumenta la cantidad de poder de ataque cuerpo a cuerpo añadido cuando Evasion es exitosa. (el límite máximo permanece igual)."
    ),
)

POISON_MASTER = SkillText(
    title="Poison Master",
    description="**Descripción del juego:** *\"Aumenta la duración del Ailment [Poison] y el poder de la habilidad \"Death Reception\". El daño de Deadly Poison también puede infligir [Poison] (depende de Venom Injection).\"*",
    details=(
        "**Habilidad Tier 5;** [Pasivo] Solo Dagger/Ninjutsu Scroll/Main Bare Hand\n\n"
        "**Efecto Pasivo:**\n"
        "*  Aumenta el Base Skill Multiplier de Death Reception:\n"
        "  Con OHS o Barehand:\n"
        "  > Death Reception Single Target Multiplier + 0.75 * Skill Level\n"
        "  > Death Reception AOE Multiplier + 0.45 * Skill Level\n"
        "  Con todas las demás armas:\n"
        "  > Death Reception Single Target Multiplier + 0.5 * Skill Level\n"
        "  > Death Reception AOE Multiplier + 0.3 * Skill Level\n"
        "  Este multiplicador extra se aplica después de determinar los valores originales del Single Target y AOE Hit Multiplier de Death Reception.\n\n"
        "*  Aumenta la duración del Poison infligido por Venom Injection en +(Skill Level) segundos. Esto también aplica a la extensión de duración de Poison+1 y Poison+2, por lo que todos pasan de 30 segundos a 60 segundos de duración máxima.\n"
        "*  Permite que cada tick de daño de Deadly Poison tenga chance de infligir Poison/Poison+1/Poison+2 de (10 + 3 * Skill Level)% de la Chance Final de Poison+0 sin Critical/Graze (Venom Inject). [esta es una fórmula estimada de prueba y error, no es exacta; podría ser 2.5%... pero no lo sé, además Corrosive Poison no afecta mucho esto por alguna razón… así que basado solo en Venom Injection seguramente]."
    ),
)
