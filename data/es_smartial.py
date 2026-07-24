from dataclasses import dataclass


FOOTER = "Créditos: Phantom's Library"

INDEX_HEADER = [
    "**Nivel requerido:** T1 ninguno, T2 Lv30, T3 Lv70, T4 Lv150, T5 Lv240",
    '**Selecciona un "Texto Azul" para guiarte hacia él.**',
    "",
]


@dataclass(frozen=True)
class SkillText:
    title: str
    description: str
    details: str


SMASH = SkillText(
    title="Smash",
    description="**Descripción del juego:** *\"Golpea fuertemente al objetivo. Chance de infligir [Flinch] en el objetivo.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 0.5 + 0.02 * Skill Level\n"
        "**Base Skill Constant:** 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de Knuckle si está equipado en el slot de arma principal o secundaria; de lo contrario será 1m\n\n"
        "**Ailment:** Flinch\n"
        "**Chance Base de Ailment:** 50% (niveles 1 a 5); 75% (niveles 6 a 10)\n"
        "**Duración de Ailment:** 2 segundos\n"
        "**Resistencia a Ailment:** 1 segundo (Easy y Normal); 3 segundos (Hard); 6 segundos (Nightmare); 9 segundos (Ultimate)\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +0.5\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +(25 + TotalAGI/10)\n"
        "**Knuckle Main/Sub bonus:** Flinch chance +25%"
    ),
)

BASH = SkillText(
    title="Bash",
    description="**Descripción del juego:** *\"Asesta un golpe pesado en la cabeza. Chance de infligir [Stun] en el objetivo.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 10 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de Knuckle si está equipado en el slot de arma principal o secundaria; de lo contrario será 1m\n\n"
        "**Ailment:** Stun\n"
        "**Chance Base de Ailment:** 25% (niveles 1 a 5); 50% (niveles 6 a 10)\n"
        "**Duración de Ailment:** 5 segundos\n"
        "**Resistencia a Ailment:** 25 segundos (Easy, Normal, Hard y Nightmare); 30 segundos (Ultimate)\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +(1 + TotalAGI/500)\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +(50 + TotalAGI/5)\n"
        "**Knuckle Main/Sub bonus:** Stun chance +(25 + TotalAGI/10)%"
    ),
)

SHELL_BREAK = SkillText(
    title="Shell Break",
    description="**Descripción del juego:** *\"Un golpe directo que penetra armaduras duras. El daño aumenta cuanto mayor es la DEF del objetivo. Baja chance de infligir [Armor Break]. Recupera MP si tiene éxito.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 50 + 10 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de Knuckle si está equipado en el slot de arma principal o secundaria; de lo contrario será 1m\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad tiene Physical Pierce +(5 * Skill Level)%\n"
        "* Si inflige Armor Break, recuperas 400 MP\n\n"
        "**Ailment:** Armor Break\n"
        "**Chance Base de Ailment:** 10% + (1.5 * Skill Level)%\n"
        "**Duración de Ailment:** 5 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +0.5\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +((DEF del objetivo - Nivel del objetivo)/50); este bonus no puede ser menor a -1 ni mayor a 5\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +150\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +((DEF del objetivo - Nivel del objetivo) * 2); este bonus no puede ser menor a -100 ni mayor a 500\n"
        "**Solo Main Knuckle:** Armor Break Chance +25%"
    ),
)

HEAVY_SMASH = SkillText(
    title="Heavy Smash",
    description="**Descripción del juego:** *\"Golpea muy fuerte al objetivo. Chance de infligir [Lethargy] en el objetivo. Inflige daño adicional si tiene [Armor Break].\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.15 * Skill Level\n"
        "**Base Skill Multiplier (Additional Hit):** 1 + 0.15 * Skill Level\n"
        "**Base Skill Constant:** 100 + 10 * Skill Level; constante para cada hit\n"
        "**Número de golpes:** 1 hit; 2 hits si el objetivo tiene Armor Break; los cálculos de Dodge, Evasion, Guard, Anticipate y Guard Break se hacen en el primer hit y se copian al otro hit; el resto del cálculo de daño se hace para cada hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de Knuckle si está equipado en el slot de arma principal o secundaria; de lo contrario será 1m\n\n"
        "**Efecto de la habilidad:** Si el objetivo tiene Armor Break, esta habilidad obtiene un segundo golpe mucho más fuerte que siempre es crítico\n\n"
        "**Ailment:** Lethargy\n"
        "**Chance Base de Ailment:** 20% + (3 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +1.5\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier (Additional Hit) +5\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +100\n"
        "**Knuckle Main/Sub bonus:** Lethargy chance +50%\n\n"
        "El buff a la constante de Triple Thrust's aplica al primer hit, pero no al segundo hit"
    ),
)

CHARIOT = SkillText(
    title="Chariot",
    description="**Descripción del juego:** *\"Libera la energía interna del personaje. Chance de infligir [Fear] en el objetivo. El tiempo de carga se reduce según el nivel de la habilidad.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 9.9 + 0.01 * Skill Level\n"
        "**Base Skill Constant:** 50 + 20 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe:** Objetivo único sin Knuckles en el slot de arma principal o secundaria; longitud de 12m y radio de 0.75m desde la posición del lanzador con Knuckles en el slot de arma principal o secundaria\n"
        "**Tiempo de carga base:** 11 segundos (nivel 1); 9 segundos (niveles 2 y 3); 7 segundos (niveles 4 y 5); 5 segundos (niveles 6 y 7); 3 segundos (niveles 8 y 9); 1 segundo (nivel 10)\n\n"
        "**Ailment:** Fear\n"
        "**Chance Base de Ailment:** (5 * Skill Level)%; el chance total se reduce a la mitad en jefes\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +(2.5 + BaseAGI/100)\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +250\n"
        "**Knuckle Main/Sub bonus:** Fear chance +50%\n"
        "**Knuckle Main/Sub bonus:** Tiempo de carga -1 segundo"
    ),
)

SONIC_WAVE = SkillText(
    title="Sonic Wave",
    description="**Descripción del juego:** *\"Ataca con una onda impulsiva. Chance de infligir [Tumble] en el objetivo.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 0.75 + 0.025 * Skill Level\n"
        "**Base Skill Constant:** 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 4m (niveles 1 a 3); 8m (niveles 4 a 6); 12m (niveles 7 a 9); 16m (nivel 10)\n\n"
        "**Ailment:** Tumble\n"
        "**Chance Base de Ailment:** (5 * Skill Level)%\n"
        "**Duración de Ailment:** 3 segundos\n"
        "**Resistencia a Ailment:** 3 segundos (Easy y Normal); 6 segundos (Hard); 12 segundos (Nightmare); 18 segundos (Ultimate)\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +0.25\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +25\n"
        "**Knuckle Main/Sub bonus:** Tumble chance +50%\n"
        "**Knuckle Main/Sub bonus:** Alcance máximo de Cast +4m"
    ),
)

EARTHBIND = SkillText(
    title="Earthbind",
    description="**Descripción del juego:** *\"Ataca a los enemigos a tu alrededor sacudiendo el suelo. Chance de infligir [Stop] en los objetivos. Restaura una pequeña cantidad de HP al golpear a un objetivo.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.025 * Skill Level\n"
        "**Base Skill Constant:** 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de Knuckle si está equipado en el slot de arma principal o secundaria; de lo contrario será 1m\n"
        "**Alcance del golpe:** 1m (niveles 1 y 2); 1.5m (niveles 3 a 5); 2m (niveles 6 a 8); 2.5m (niveles 9 y 10)\n\n"
        "**Efecto de la habilidad:** Por cada objetivo golpeado con esta habilidad, recuperas 5% de tu MaxHP; no puedes recuperar más de 500 HP de esa forma\n\n"
        "**Ailment:** Stop\n"
        "**Chance Base de Ailment:** (5 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** 50 segundos\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +(0.25 + TotalAGI/500)\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +25\n"
        "**Knuckle Main/Sub bonus:** Alcance del golpe +1.5m\n"
        "**Knuckle Main/Sub bonus:** Límite de recuperación de HP +500 HP\n"
        "**Knuckle Main/Sub bonus:** Stop chance +50%"
    ),
)

TRIPLE_KICK = SkillText(
    title="Triple Kick",
    description="**Descripción del juego:** *\"Ataca al objetivo tres veces rápidamente. Critical Rate más alta que la de ataques normales.\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.1 * Skill Level; multiplicador para cada hit\n"
        "**Base Skill Constant:** 25 + 2 * Skill Level; constante para cada hit\n"
        "**Número de golpes:** 3 hits; el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** 3m\n\n"
        "**Efecto de la habilidad:** Esta habilidad tiene Critical Rate +(2 * Skill Level) en el segundo hit y Critical Rate +(4 * Skill Level) en el tercer hit\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +1\n"
        "**Knuckle Main/Sub bonus:** Critical Rate +50 para todos los hits de la habilidad"
    ),
)

RUSH = SkillText(
    title="Rush",
    description="**Descripción del juego:** *\"Ataques consecutivos rápidos. Action Speed aumenta por unos segundos, incluso en el momento de activar Rush.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 3 + 0.4 * Skill Level; multiplicador total de todos los hits\n"
        "**Base Skill Constant:** 20 * Skill Level; constante total de todos los hits\n"
        "**Número de golpes:** 4 hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de Knuckle si está equipado en el slot de arma principal o secundaria; de lo contrario será 1m\n\n"
        "**Efecto del Buff:** Motion Speed +2% (niveles 1 a 3)/ +3% (niveles 4 a 6)/ +4% (niveles 7 a 9)/ +5% (nivel 10); este buff se aplica inmediatamente en lugar de después de lanzar esta habilidad\n"
        "**Duración del Buff:** 10 segundos\n\n"
        "**Knuckle Main/Sub bonus:** Skill Multiplier +(2 + BaseAGI/50)\n"
        "**Knuckle Main/Sub bonus:** Skill Constant +200\n"
        "**Knuckle Main/Sub bonus:** Motion Speed del buff se duplica"
    ),
)

MARTIAL_MASTERY = SkillText(
    title="Martial Mastery",
    description="**Descripción del juego:** *\"Mejora el uso de Knuckles. ATK de Knuckles aumenta.\"*",
    details=(
        "**Habilidad Tier 1;** Solo Main {knuckle}\n\n"
        "**Efecto Pasivo:**\n"
        "* Weapon ATK +(3 * Skill Level)%\n"
        "* ATK +1% (niveles 1 y 2)/ +2% (niveles 3 a 7)/ +3% (niveles 8 a 10)"
    ),
)

MARTIAL_DISCIPLINE = SkillText(
    title="Martial Discipline",
    description="**Descripción del juego:** *\"Profundiza el conocimiento de Knuckles. Aumenta Attack Speed de Knuckles. Aumenta ligeramente el daño de las habilidades de Knuckle.\"*",
    details=(
        "**Habilidad Tier 3;** {knuckle} Main o Sub / Solo Main {knuckle} (según el efecto)\n\n"
        "**Efecto Pasivo:**\n"
        "* Aumenta el daño de las Martial Skills en (1 * Skill Level)%; este efecto solo aplica cuando equipas Knuckles en el slot de arma principal o secundaria\n"
        "* Attack Speed +(Skill Level)% y +(10 * Skill Level); este efecto solo aplica cuando equipas Knuckles en el slot de arma principal"
    ),
)

CHAKRA = SkillText(
    title="Chakra",
    description="**Descripción del juego:** *\"Restaura un poco de MP y añade un buff para reducir el próximo daño por unos segundos. Aumenta ligeramente el Attack MP Recovery durante el efecto. Funciona en los miembros del grupo.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Tiempo de carga base:** 3 segundos; afectado por Cast Speed\n\n"
        "**Efecto de la habilidad:** Restaura 50 MP al lanzador y a los miembros del grupo al lanzar esta habilidad con éxito\n\n"
        "**Efecto del Buff:** Otorga un buff a todo el grupo que añade:\n"
        "* Attack MP Recovery +(Skill Level + MAX(0, Skill Level - 5))\n"
        "* Flat Skill Based Damage Reduction +0 (para el lanzador)/ +2 * BaseVIT de los demás (para los demás); esta reducción se aplica después de la reducción de DEF/MDEF y antes de Percentage Skill Based Damage Reduction\n"
        "* Percentage Skill Based Damage Reduction +10% + (2 * Skill Level)%; esta reducción se aplica después de Flat Skill Based Damage Reduction y antes de Equipment Refine Damage Reduction\n"
        "**Duración del Buff:** 10 + (Skill Level) segundos O hasta que recibas daño\n\n"
        "**Knuckle Main/Sub bonus:** Curación de MP +50\n"
        "**Knuckle Main/Sub bonus:** Percentage Skill Based Damage Reduction +20%\n"
        "**Knuckle Main/Sub bonus:** Duración del Buff +10 segundos"
    ),
)

AGGRAVATE = SkillText(
    title="Aggravate",
    description="**Descripción del juego:** *\"Ataca de nuevo al objetivo con agudeza. Tienes chance de infligir daño adicional con los ataques normales de Knuckles.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {knuckle} / Main {barehand}\n\n"
        "**Efecto Pasivo:**\n"
        "* Attack MP Recovery +(0.5 * Skill Level)\n"
        "* En autoataques que no resultan en Miss, tienes un (10 + 4 * Skill Level)% de chance de añadir un ataque adicional que no puede ser crítico\n\n"
        "**Aggravate Damage Type:** Neutral\n"
        "**Aggravate Element:** Neutral\n"
        "**Aggravate Skill Multiplier:** 0.05 * Skill Level; multiplicador para cada hit\n\n"
        "**Cálculo de daño de Aggravate:**\n"
        "Aggravate Damage = (Physical Base Damage - DEF del objetivo) * Aggravate Skill Multiplier * RNG Stability/100 * Current Neutral Proration/100 * (1 - Base Drop Gem Damage Reducer/100) [Si usa una Base Drop Gem; repetir por cada Gema]\n\n"
        "**Número de golpes:** El mismo que el del autoataque que lo activó; el cálculo de daño es independiente del autoataque; si el Número de golpes del autoataque es mayor a 1, el cálculo de daño se hace una vez y se divide equitativamente entre los hits\n\n"
        "**Aggravate Ailment:** Armor Break\n"
        "**Aggravate Ailment Chance:** 0%\n\n"
        "* Esta habilidad no parece ser afectada por Guard\n"
        "* Martial Discipline no afecta el daño de esta habilidad"
    ),
)

STRONG_CHASE_ATTACK = SkillText(
    title="Strong Chase Attack",
    description="**Descripción del juego:** *\"Potencia el poder de los ataques pequeños. Aumenta tu Accuracy y mejora el daño adicional de [Aggravate].\"*",
    details=(
        "**Habilidad Tier 2;** Solo {knuckle} / Main {barehand}\n\n"
        "**Efecto Pasivo:**\n"
        "* Ganas Accuracy% pasivamente en (Skill Level)%\n\n"
        "**Solo Main Knuckle:**\n"
        "* Aggravate Skill Multiplier +(0.05 * Skill Level)\n"
        "* Physical Pierce del daño de Aggravate = aún en investigación\n"
        "* Duplica el boost de Accuracy% [ahora es (Skill Level * 2)%]\n\n"
        "*Esta habilidad no afecta al Accuracy de los mercenarios."
    ),
)

SLIDE = SkillText(
    title="Slide",
    description="**Descripción del juego:** *\"Deslízate a alta velocidad para acortar la distancia y acercarte al enemigo. Accuracy de la siguiente habilidad aumentará.\"*",
    details=(
        "**Habilidad Tier 3;** Solo Main {knuckle}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Alcance máximo de Cast:** 8 metros\n\n"
        "**Efecto del Buff:**\n"
        "* Aumenta Accuracy de la siguiente habilidad en +(Skill Level^2)\n\n"
        "Si usas esta habilidad a 0m de rango, omitirá la animación de deslizamiento instantáneamente. Pero hay chance de que te quedes atascado en la animación a 0m [parece un bug, así que un consejo para evitarlo: simplemente sigue moviéndote un poco cada vez que uses Slide]"
    ),
)

ABSTRACT_ARMS = SkillText(
    title="Abstract Arms",
    description="**Descripción del juego:** *\"Permite usar Evasion (Solo Manual) mientras usas ciertas Martial Skills. Después de activarlo, debes esperar antes de poder usarlo de nuevo. No disponible para algunas habilidades que realizan acciones especiales.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {knuckle}\n\n"
        "**Efecto Pasivo:**\n"
        "* Permite realizar evasion dash durante la animación de la habilidad. Así puedes saltarte la animación tras hacer evasion, gracias a un señuelo de sombra que continúa la animación. Tiene un cooldown al activarse: (10 - Skill Level) segundos para Main Knuckle, o (20 - Skill Level) segundos para Sub Knuckle, y no puede usarse de nuevo si tu sombra está ejecutando una animación. [Nota: el Cooldown comienza después de que el clon termine su cast o animación]\n"
        "* Si usas esta habilidad mientras estás en estado de combo, cancelas ese combo inmediatamente\n\n"
        "Habilidades que pueden usarse con esto por sus acciones especiales:\n"
        "Todas las Martial Skills excepto Slide, Energy Control, Asura Aura\n"
        "Habilidades Crusher = Breathworks, Combination, God Hand\n"
        "MP Charge, War Cry, War Cry of Struggle, Quick Aura, Kairiki Ranshin, Guardian\n\n"
        "**Notas sobre Abstract Arms:**\n\n"
        "* El bonus de SRD/LRD% en Abstract Chariot se aplica cuando Chariot inflige daño (no al lanzar la habilidad ni al activar Abstract).\n"
        "* Abstract God Hand no otorga el buff cuando tu clon/sombra recibe daño."
    ),
)

ASURA_AURA = SkillText(
    title="Asura Aura",
    description="**Descripción del juego:** *\"Libera el poder demoníaco oculto en el interior. Mientras está activo, ATK aumenta y si recibes daño, se usa MP para mitigarlo, pero a cambio pierdes Attack MP Recovery y el coste de MP aumenta.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {knuckle}\n"
        "**Coste MP:** 0\n\n"
        "**Punch Damage Multiplier:** 0.95 + BaseAGI/(2400 - Skill Level * 200)\n"
        "[Penalidad de Sub-Knuckle: 0.5 + BaseAGI/(2400 - Skill Level * 200)]\n"
        "**Punch Damage Constant:** 0\n\n"
        "**Trigger/Hit Range:** 2.5m; el cálculo de daño se realiza para cada hit\n"
        "**Interval Hit:** 1 golpe cada 0.25 s; no afectado por Motion Speed%, swift y freeze\n\n"
        "**Efecto del Buff (Asura Mode):**\n"
        "* Aumenta el coste base de MP de todas las habilidades excepto Martial y Crusher en +100 MP.\n"
        "* Obtienes stacks según el MP usado. Cada 100 MP = 1 Asura stack. Nota: el coste de MP después de combo tags y half-buff como Impact. Advertencia: no intentes llegar a 40 stacks (te matará al instante en cuanto los alcances). Nota: pierdes HP cada vez que usas una habilidad (5% de MaxHP por stack ganado) solo cuando tienes al menos 20 Asura stacks.\n"
        "* Cada vez que recibes daño de un monstruo, pierdes 100 MP a cambio de reducir el daño recibido en (tu barra de MP actual * 4%) [Máx 75%] y también ganas 1 Asura stack (solo ocurre cuando pierdes MP).\n"
        "* Desactiva la recuperación de MP de autoataques (incluso Decoy) durante este buff, sin importar cuánto AMPR tengas. Sin embargo, cualquier acción (como Burning Spirit, Manual Guard, Gladiate, etc.) aún puede recuperar MP basado en el AMPR Total normalmente durante este buff.\n"
        "* Aumenta Skill Constant de todos los ataques (excepto Asura) en 20 * Skill Level. [Penalidad de Sub-Knuckle: Skill Constant de esta habilidad se reduce a la mitad]\n"
        "* **[Solo Main Knuckle]** El daño infligido de las habilidades \"Martial\", \"Crusher\", \"Dagger\", \"Assassin\" y \"Dark Power\" aumenta en 30% sin importar el Skill Level (se aplica multiplicativamente al final del cálculo de daño, después de sumar el bonus de Brave Aura y la reducción de Mana Recharge). Mientras que para otros ataques, el daño aumenta en 10%.\n"
        "* Otorga Flat Critical de (7.5 * Skill Level) [Penalidad de Sub-Knuckle: el Flat Cr de esta habilidad se divide entre 3]\n"
        "* Tienes un chance de resistir Ailment según cada 10 MP actuales = +1% de chance, máx +100%. Funciona aditivamente con AilRes% de MTL/equipo. Nota: el Ailment Sick puede afectar esta habilidad.\n"
        "* Duración del Buff: Hasta que uses Asura Aura de nuevo o 40 stacks (muerte instantánea)\n"
        "* Usar un autoataque en un objetivo durante este buff activa golpes consecutivos infinitos que infligen daño, con atributo Perfect Aim [solo Main Knuckle].\n\n"
        "Los golpes consecutivos infinitos se detienen cuando el objetivo está demasiado lejos, usas una habilidad, o usas Guard manual y Evasion. Debes reactivarlos con un autoataque. Estos golpes no infligen proration, y su daño se basa en Proration Física."
    ),
)

ASURA_AURA_EXTRA = (
    "**Efecto de la habilidad:**\n"
    "* Usar Asura Aura activa/desactiva el Asura Mode. Si activas Asura cuando tienes stacks restantes, se reinician a 0 y entras en Asura Mode.\n"
    "* Hay 2 segundos de Iframe al entrar en Asura Mode. Pero no al desactivarlo. Sin embargo, si desactivas Asura Mode mientras tienes este Iframe de activación, el Iframe termina inmediatamente.\n"
    "* Cuando tienes un Asura stack y no estás en Asura Mode, usar autoataque en un objetivo activa golpes consecutivos, también con Perfect Aim [solo Main Knuckle]. Pero esta vez no son ilimitados sino que usan stacks: cada 1 Asura stack = 1 golpe/hit. Además, cada golpe/stack puede recuperar MP por (Total AMPR/10 * Skill Level) [Penalidad de Sub-Knuckle: la recuperación de MP de stacks se reduce a la mitad].\n\n"
    "Sin embargo, esos golpes consecutivos se detienen cuando el objetivo está demasiado lejos o usas Guard manual y Evasion. Debes reactivarlos con autoataque si tienes stacks. Estos golpes no infligen proration, y su daño se basa en Proration Física.\n\n"
    "**Si tienes al menos 1 Asura stack y no estás en Asura Mode, conservas estos 3 buffs:**\n"
    "* Aumenta tu Critical Rate en +(7.5 * Skill Level). Penalidad de Sub-Knuckle: dividido entre 3.\n"
    "* Aumenta la constante de todas las habilidades en (20 * Skill Level). Penalidad de Sub-Knuckle: reducido a la mitad.\n"
    "* **[Solo Main Knuckle]** El daño de todos los ataques aumenta en 10% sin importar el Skill Level (aditivamente con Brave). [Solo cambia esta parte: 30% a 10%, Asura OFF tiene menos efecto que Asura ON]\n\n"
    "**Notas adicionales:**\n"
    "* El stack de Asura Aura recupera MP inmediatamente al salir del mapa. Pero su recuperación de MP parece fijarse en (stack * 50 MP).\n"
    "* Aunque tu autoataque resulte en Miss, igual activa los golpes consecutivos.\n"
    "* Si un golpe/stack de Asura Aura resulta en Miss, ese golpe no recupera MP (desperdicia el stack, necesita acertar para recuperar MP).\n"
    "* El daño de Asura Punch no es afectado por SRD/LRD, aumentos de daño (como Brave Aura, Asura Aura), ni combo tags."
)

FLASH_BLINK = SkillText(
    title="Flash Blink",
    description="**Descripción del juego:** *\"Envía una imagen residual para atacar. Esta habilidad ataca con \"normal attack proration\". El número de golpes aumenta según los Evasion stacks. Aumenta el poder de ataque a corta distancia de la siguiente habilidad.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {knuckle}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 3 + 0.3 * Skill Level\n"
        "**Base Skill Constant:** 100\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 6m\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad inflige Normal Auto Attack Proration, pero su daño se basa en Normal Auto Attack Proration.\n"
        "* El número de golpes adicionales aumenta según los Evasion stacks que tengas. Golpes adicionales = INT(Evasion Stacks Disponibles / 2).\n"
        "* El cálculo del daño adicional es algo así: golpe principal = 100% del daño; 1er golpe adicional = 50%; 2do = 25%; 3ro = 12.5%; 4to = 6.25%; y así sucesivamente.\n"
        "* El daño de esta habilidad es afectado por SRD%.\n\n"
        "**Efecto del Buff:**\n"
        "* Otorga un bonus de SRD% para la siguiente habilidad en (Skill Level)% después de usar esta habilidad\n"
        "* Duración del Buff: hasta que uses cualquier habilidad\n\n"
        "**Main Knuckle bonus:** Base Skill Multiplier +(BaseAGI/400)"
    ),
)

ENERGY_CONTROL = SkillText(
    title="Energy Control",
    description="**Descripción del juego:** *\"Controla el flujo de energía y lo desvía. Anula el daño recibido mientras se ejecuta y recibe los buffs de Chakra excepto el de recuperación de MP. El nivel de Chakra que se activa no supera el nivel de Energy Control adquirido.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {knuckle}\n"
        "**Coste MP:** 100\n\n"
        "**Efecto de la habilidad:**\n"
        "* Reduce el daño recibido a 0 durante esta animación. Nota: Support Aura aún desaparece al reducir daño con éxito.\n"
        "* Al hacer un parry exitoso con esta habilidad, obtienes el buff de Chakra sin la restauración de MP. El efecto/nivel de Chakra sin restauración de MP depende del nivel de Chakra, pero el nivel de Chakra activado no puede exceder el nivel de Energy Control.\n"
        "* También obtienes un buff de Base Watk% y Stability al hacer un parry exitoso.\n\n"
        "**Efecto del Buff:**\n"
        "* Si tienes el buff de esta habilidad, no puedes ganar stack de Eburst/Buff de Eburst (se eliminan al obtener este buff).\n"
        "* Attack MP Recovery +(Nivel de Chakra + MAX(0, Nivel de Chakra - 5))\n"
        "* Percentage Skill Based Damage Reduction +10% + (2 * Nivel de Chakra)%; esta reducción se aplica después de Flat Skill Based Damage Reduction y antes de Equipment Refine Damage Reduction\n"
        "* Duración del Buff de Chakra: 10 + (Nivel de Chakra) segundos O hasta que recibas daño\n\n"
        "* [Solo Main Knuckle] Aumenta Base Weapon ATK en +(5% * Skill Level). Junto con la habilidad \"Annihilator\", este aumento de Weapon ATK llega hasta 50%. Nota: los buffs de Watk de Energy Control y Annihilator se acumulan, pero el máximo es 50% en lugar de 100% (no es 50% EC + 50% Anni).\n"
        "* Aumenta Stability en +10% sin importar el nivel.\n"
        "* Duración del buff de Base Watk% y Stability%:\n\n"
        "(30 + MAX((SLvl-1) * 2.5 ; (SLvl-2) * 5 ; (SLvl-4) * 10)) segundos.\n\n"
        "Nivel 1 = 30s; Nivel 2 = 32s; Nivel 3 = 35s; Nivel 4 = 40s; Nivel 5 = 45s; Nivel 6 = 50s; Nivel 7 = 60s; Nivel 8 = 70s; Nivel 9 = 80s; Nivel 10 = 90s.\n\n"
        "**Main Knuckle bonus:** La duración del Buff de Chakra se extiende en +10 s.\n"
        "**Main Knuckle bonus:** Chakra Percentage Skill Based Damage Reduction +20%"
    ),
)

MOUNTAIN_PRESS = SkillText(
    title="Mountain Press",
    description="**Descripción del juego:** *\"Un poderoso golpe de hombro. Chance de infligir [Stun] en el objetivo.\"*",
    details=(
        "**Habilidad Tier 5;** [Activo] Solo {knuckle} / Main {barehand}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:**\n"
        "> Knuckles: 7.5 + 0.25 * Skill Level\n"
        "> Barehand/Sub-weapon: 7.5 + 0.25 * Skill Level + TotalDEX o TotalAGI/100 (usa el más alto)\n\n"
        "**Base Skill Constant:** 500\n\n"
        "**Alcance máximo de Cast:** 4m\n\n"
        "**Efecto del Buff:** El golpe adicional de \"Aggravate\" se vuelve \"crítico\" si el autoataque es \"crítico\". La tasa de activación del golpe adicional de Aggravate con Knuckles en el slot de arma principal se vuelve 100%. Añade un bonus de multiplicador para los golpes adicionales de Aggravate en sucesión: +10% * activaciones totales de Aggravate durante el periodo del buff (MÁX: 50×; 5 de multiplicador).\n"
        "**Duración del Buff:** coincide con la duración del cooldown de Stun\n\n"
        "**Ailment:** Stun\n"
        "**Chance Base de Ailment:** 100% (Main Knuckles); 7% * Skill Level (Sub-weapon); 30% + 7% * Skill Level (Barehand)\n"
        "**Duración de Ailment:** 5 segundos\n"
        "**Resistencia a Ailment:** 30 segundos (Easy, Normal, Hard y Nightmare); 35 segundos (Ultimate)\n\n"
        "Esta habilidad es afectada por Short Range Damage; usa e inflige Proration Física.\n\n"
        "*Si el debuff de Stun se previene por resistencia activa, el efecto del buff de \"Aggravate\" se aplicará."
    ),
)

SEISMIC_STOMP = SkillText(
    title="Seismic Stomp",
    description="**Descripción del juego:** *\"Desestabiliza a tu oponente con un fuerte pisoteo. Chance de infligir [Flinch] en el objetivo. Si tiene éxito, se restaura una gran cantidad de MP.\"*",
    details=(
        "**Habilidad Tier 5;** [Activo] Solo {knuckle} / Main {barehand}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:**\n"
        "> Knuckles: 7.5 + 0.25 * Skill Level\n"
        "> Barehand/Sub-weapon: 7.5 + 0.25 * Skill Level + TotalDEX o TotalSTR/100 (usa el más alto)\n\n"
        "**Base Skill Constant:** 300\n"
        "**Alcance máximo de Cast:** 2m\n\n"
        "**Recuperación de MP:** 600 + Attack MP Recovery Total del personaje * 2\n"
        "Esta recuperación de MP es afectada por Chakra, Aggravate, Quick Motion/High Cycle, Raving Storm, Ether Flame, Hidden Talent Crysta, Consumibles, Equipamiento/Crystas/Avatars, Infinity Gem, Stoodie Experiment AMPR buff.\n\n"
        "**Ailment:** Flinch\n"
        "**Chance Base de Ailment:** 10 * Skill Level%\n"
        "**Duración de Ailment:** 2 segundos\n"
        "**Resistencia a Ailment:** 6 segundos (Easy, Normal y Hard); 7 segundos (Nightmare); 10 segundos (Ultimate)\n\n"
        "Esta habilidad es afectada por Short Range Damage; usa e inflige Proration Física."
    ),
)

SPIN_SWEEP = SkillText(
    title="Spin Sweep",
    description="**Descripción del juego:** *\"Derriba a tu oponente con una barrida de pierna. Chance de infligir [Tumble] en el objetivo. Si tiene éxito, realizas ataques adicionales y obtienes un buff por unos segundos.\"*",
    details=(
        "**Habilidad Tier 5;** [Activo] Solo {knuckle} / Main {barehand}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:**\n"
        "> Knuckles: 2.5 + 0.25 * Skill Level\n"
        "> Barehand/Sub-weapon: 2.5 + 0.25 * Skill Level + TotalAGI o TotalSTR/100 (usa el más alto)\n\n"
        "**Base Skill Constant:** 400\n\n"
        "**Golpe adicional (wheel kick):**\n"
        "**Base Skill Multiplier:**\n"
        "> Knuckles: 5 + 0.5 * Skill Level + BaseAGI/100\n"
        "> Barehand: 5 + 0.5 * Skill Level\n"
        "**Base Skill Constant:** 400 + 40 * Skill Level\n\n"
        "**Alcance máximo de Cast:** 2m\n\n"
        "**Efecto del Buff:** Ignora [Suction]; previene [Slow] y [Stop]. Recupera el contador de Evasion en: 1 (Barehand/Sub-Magic Device); 1.7 (Sub-Knuckles); 2 (Sub-Dagger); 3 (Main Knuckles).\n"
        "**Duración del Buff:** 2 + ROUNDDOWN(slv/2;0) segundos\n\n"
        "**Ailment:** Tumble\n"
        "**Chance Base de Ailment:** 100%\n"
        "**Duración de Ailment:** 3 segundos\n"
        "**Resistencia a Ailment:** 8 segundos (Easy, Normal y Hard); 14 segundos (Nightmare); 20 segundos (Ultimate)\n\n"
        "Esta habilidad es afectada por Short Range Damage; usa e inflige 1 Proration Física.\n\n"
        "**All Weapons Bonus:** Evasion se restaura ligeramente al obtener el buff. El buff dura unos segundos y durante ese tiempo se previene la interrupción de movimiento por [Slow], [Stop] y ataques de arrastre."
    ),
)
