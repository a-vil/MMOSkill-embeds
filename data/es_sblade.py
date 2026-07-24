from dataclasses import dataclass


FOOTER = "Créditos: Phantom's Library"

INDEX_HEADER = [
    "**Nivel requerido:** T1 ninguno, T2 Lv30, T3 Lv70, T4 Lv150, T5 Lv240",
    '**Selecciona un "Texto Azul" para guiarte hacia el.**',
    "",
]


@dataclass(frozen=True)
class SkillText:
    title: str
    description: str
    details: str


HARD_HIT = SkillText(
    title="Hard Hit",
    description="**Descripción del juego:** *\"Golpea brutalmente al objetivo con el arma. Chance de infligir [Flinch] en el objetivo.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 50 + 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n\n"
        "**Ailment:** Flinch\n"
        "**Chance Base de Ailment:** 9% (nivel 1)/ 14% (nivel 2)/ 19% (nivel 3)/ 23% (nivel 4)/ 27% (nivel 5)/ 32% (nivel 6)/ 37% (nivel 7)/ 41% (nivel 8)/ 45% (nivel 9)/ 50% (nivel 10)\n"
        "**Duración de Ailment:** 2 segundos\n"
        "**Resistencia a Ailment:** 1 segundo (Easy y Normal); 3 segundos (Hard); 6 segundos (Nightmare); 9 segundos (Ultimate)\n\n"
        "**One-Handed Sword bonus:** Flinch chance +50%\n"
        "**Two-Handed Sword bonus:** Skill Multiplier +0.5"
    ),
)

ASTUTE = SkillText(
    title="Astute",
    description="**Descripción del juego:** *\"Golpea fuertemente al objetivo con un movimiento rápido. Critical Rate +25 cuando esta habilidad se activa.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1.5 + 0.1 * Skill Level\n"
        "**Base Skill Constant:** 150 + 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad tiene un incremento de Motion Speed de (5 * Skill Level)%\n"
        "**Efecto del Buff:** Critical Rate +25\n"
        "**Duración del Buff:** 5 segundos (niveles 1 a 5); 10 segundos (niveles 6 a 10)\n\n"
        "**One-Handed Sword bonus:** Coste MP -100\n"
        "**Two-Handed Sword bonus:** Skill Multiplier +0.5\n"
        "**Two-Handed Sword bonus:** El Critical Rate del buff se duplica"
    ),
)

TRIGGER_SLASH = SkillText(
    title="Trigger Slash",
    description="**Descripción del juego:** *\"Aplica fuerza mientras cortas al objetivo. Mejora la recuperación de Attack MP hasta la siguiente habilidad. Motion Speed aumenta una vez con esta habilidad.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 300 (niveles 1 a 5); 200 (niveles 6 a 10)\n"
        "**Tipo de daño:** Físico\n"
        "**Elemento:** Fire\n\n"
        "**Base Skill Multiplier:** 1.5 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 200 + 10 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n\n"
        "**Efecto del Buff:**\n"
        "* Attack MP Recovery +(2 * Skill Level)\n"
        "* Establece el \"modificador del tiempo de animación\" de la siguiente habilidad al 50 %\n"
        "**Duración del Buff:** Hasta que se use una habilidad\n\n"
        "**One-Handed Sword bonus:** Obtiene el atributo Perfect Aim\n"
        "**Two-Handed Sword bonus:** Skill Multiplier +1\n\n"
        "El buff de \"modificador del tiempo de animación\" de esta habilidad anula todos los demás modificadores de Motion Speed"
    ),
)

RAMPAGE = SkillText(
    title="Rampage",
    description="**Descripción del juego:** *\"Ataca furiosa y consecutivamente a un objetivo. Mejora enormemente los ataques normales 10 veces, tras lo cual se activará un ataque fuerte. No se puede usar de forma redundante.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Primeros 10 Auto Ataques**\n"
        "* **Skill Multiplier:** 0.1 + 0.04 * Skill Level; multiplicador total para todos los golpes\n"
        "* **Skill Constant:** 10 * Skill Level; constante total para todos los golpes\n"
        "* **Número de golpes:** 4; el cálculo de daño se realiza una vez y se divide entre los golpes\n"
        "* **Número de golpes (Dual Swords):** 7; el cálculo de daño se realiza una vez y se divide entre los golpes junto con el daño de la mano secundaria\n\n"
        "**Golpe Final**\n"
        "* **Skill Multiplier (Primeros 2 Hits):** 0.5 + 0.05 * Skill Level; multiplicador para cada golpe\n"
        "* **Skill Multiplier (Tercer Hit):** 2.5 + 0.05 * Skill Level\n"
        "* **Skill Constant (Los 3 Hits):** 300 + 20 * Skill Level; constante para cada golpe\n"
        "* **Número de golpes:** 3 hits; el cálculo de daño se realiza para cada golpe\n\n"
        "**Efecto del Buff:**\n"
        "* Aumenta el daño de los siguientes 10 autoataques del usuario (Rampage Stack) y cambia su número de golpes\n"
        "* Attack MP Recovery +(2.5 * Skill Level)\n"
        "* En el 11.° autoataque, inflige un golpe final tratado como una habilidad Física con el atributo Perfect Aim. Durante la animación del golpe final, obtienes un 90% de reducción de daño (el buff de Ogre Slash de THS con 99% de reducción de daño anula esto).\n"
        "**Duración del Buff:** 11 autoataques O hasta que sufras cualquier Ailment O 10 minutos\n\n"
        "**One-Handed Sword bonus:** Primeros 10 Auto Ataques Skill Multiplier +(0.05 * Skill Level)\n"
        "**Two-Handed Sword bonus:** Golpe Final Skill Multiplier (Primeros 2 Hits) +1\n"
        "**Two-Handed Sword bonus:** Golpe Final Skill Multiplier (Tercer Hit) +3\n\n"
        "* Esta habilidad no se puede reutilizar si el buff ya está activo; si esta habilidad está en un combo y no es la primera habilidad de ese combo, el combo termina en la primera habilidad si el buff ya está activo\n"
        "* Los cambios de Skill Multiplier y Skill Constant de los autoataques solo se aplican a la mano principal de Dual Swords\n"
        "* Los tags de combos no afectan al daño total de Rampage\n"
        "* El buff de Attack MP Recovery de esta habilidad no se duplica en Dual Swords\n"
        "* El Golpe Final no se ve afectado por Sword Techniques\n"
        "* El Golpe Final no se ve afectado por la estadística Motion Speed, pero sí por Freeze y Trigger Slash\n"
        "* Rampage Stack no disminuirá si tu autoataque resulta en Miss o Evasion\n"
        "* El buff desactiva Power Wave mientras esté activo"
    ),
)

METEOR_BREAKER = SkillText(
    title="Meteor Breaker",
    description="**Descripción del juego:** *\"Un fuerte ataque como un meteorito. Chance de infligir Dizzy a un objetivo y generar un Área de Efecto al aterrizar. Te vuelves invencible mientras la habilidad está activada.\"*",
    details=(
        "**Habilidad Tier 4;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 600\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 4 + 0.2 * Skill Level\n"
        "**Base Skill Multiplier (Segundo Hit):** 1 + 0.5 * Skill Level\n"
        "**Base Skill Constant (Primer Hit):** 400 + 20 * Skill Level\n"
        "**Base Skill Constant (Segundo Hit):** 0\n"
        "**Número de golpes:** 2 hits en el objetivo principal; 1 hit en todos los demás objetivos; el cálculo de daño se realiza para cada golpe\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n"
        "**Alcance del Segundo Golpe:** 2m (niveles 1 a 3)/ 2.5m (niveles 4 a 6)/ 3m (niveles 7 a 9)/ 3.5m (nivel 10); alrededor del objetivo principal\n\n"
        "**Efecto del Buff:** Te vuelves completamente invencible\n"
        "**Duración del Buff:** 2 segundos O hasta que el usuario aterrice durante la animación\n\n"
        "**Ailment (Primer Hit):** Dizzy\n"
        "**Chance de Ailment del Primer Hit:** 2% (nivel 1)/ 5% (nivel 2)/ 7% (nivel 3)/ 10% (nivel 4)/ 12% (nivel 5)/ 15% (nivel 6)/ 17% (nivel 7)/ 20% (nivel 8)/ 22% (nivel 9)/ 25% (nivel 10)\n"
        "**Duración de Ailment del Primer Hit:** 10 segundos\n"
        "**Resistencia a Ailment del Primer Hit:** Ninguna\n\n"
        "**One-Handed Sword bonus:** Dizzy chance +75%\n"
        "**One-Handed Sword bonus:** Segundo Hit Skill Multiplier +(baseDEX/200)\n"
        "**Two-Handed Sword bonus:** Primer Hit Skill Multiplier +(2 + baseSTR/1000)\n\n"
        "El buff a la constante de Triple Thrust's se divide por 2\n"
        "El centro de Meteor Breaker es la posición del objetivo durante el cast, por lo que puede no infligir daño si el objetivo se mueve."
    ),
)

SONIC_BLADE = SkillText(
    title="Sonic Blade",
    description="**Descripción del juego:** *\"Atraviesa enemigos moviéndose rápidamente hacia ellos. El alcance y Critical Rate aumentan a medida que la habilidad sube de nivel. Se vuelve más poderosa al usarla consecutivamente.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 100 + 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 8m (niveles 1 a 3); 12m (niveles 4 a 6); 16m (niveles 7 a 9); 20m (nivel 10)\n"
        "**Alcance del golpe:** 1m; alrededor del casteador\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad te moverá frente al objetivo principal, golpeando todo lo que esté en el camino\n"
        "* Esta habilidad tiene Critical Rate +(10 * Skill Level)\n"
        "* Esta habilidad tiene un bonus de multiplicador cuando se lanza desde 8m o más: + 0.1 * (Distancia - 7m)\n"
        "**Efecto del Buff:** Cambia el nombre de la habilidad a Super Sonic Blade, duplica su Skill Multiplier, cambia la animación y aumenta el Alcance del golpe en 1m\n"
        "**Duración del Buff:** 5 segundos\n\n"
        "**One-Handed Sword bonus:** Alcance máximo de Cast +4m\n"
        "**Two-Handed Sword bonus:** Alcance del golpe +2m\n"
        "**Two-Handed Sword bonus:** Skill Multiplier +0.5\n"
        "**Two-Handed Sword penalty:** El aumento de Critical Rate de la habilidad se divide por 10\n\n"
        "Cuando se usa lo suficientemente cerca, Super Sonic Blade puede atravesar al objetivo, similar a Triple Thrust"
    ),
)

SPIRAL_AIR = SkillText(
    title="Spiral Air",
    description="**Descripción del juego:** *\"Lanza un golpe certero contra el objetivo, provocando cortes de viento. Sin daño crítico. Cuando Spiral Air golpea a un objetivo, el Critical Damage aumenta durante unos segundos.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 0.1 + 0.03 * Skill Level; multiplicador para cada golpe\n"
        "**Base Skill Constant:** 30; constante para cada golpe\n"
        "**Número de golpes:** 10 hits; el cálculo de daño se realiza una vez y se copia para los golpes restantes\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n\n"
        "**Efecto de la habilidad:**\n"
        "* Los golpes tienen un Physical Pierce que aumenta linealmente a partir del 2.° golpe.\n"
        "* Physical Pierce% Innato para Cada Golpe: (Orden del Golpe Actual - 1) * 5.55555...\n\n"
        "**Efecto del Buff:** Critical Damage +(0.5 + 0.5 * Skill Level + TotalDEX/(60 - Skill Level)); mínimo de 1 y máximo de 10\n"
        "**Duración del Buff:** 1 segundo * Skill Level\n\n"
        "**Two-Handed Sword bonus:** Skill Multiplier +0.05\n"
        "**Two-Handed Sword penalty:** El buff de Critical Damage se reduce a la mitad; mínimo es 1 y máximo es 5"
    ),
)

SWORD_TEMPEST = SkillText(
    title="Sword Tempest",
    description="**Descripción del juego:** *\"Un fuerte corte que genera una tempestad. La tempestad infligirá daño con el tiempo. Los enemigos serán succionados una vez.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Onda):** 1.5 + 0.1 * Skill Level\n"
        "**Base Skill Multiplier (Tornado):** 0.5 + 0.05 * Skill Level; multiplicador para cada golpe\n"
        "**Base Skill Constant (Onda):** 0\n"
        "**Base Skill Constant (Tornado):** 80; constante para cada golpe\n"
        "**Número de golpes (Onda):** 1 hit\n"
        "**Número de golpes (Tornado):** 2 hits (niveles 1 y 2); 3 hits (niveles 3 y 4); 4 hits (niveles 5 y 6); 5 hits (niveles 7 y 8); 6 hits (niveles 9 y 10)\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe:** 2m (niveles 1 y 2); 3m (niveles 3 a 5); 4m (niveles 6 a 8); 5m (niveles 9 y 10); alrededor de la zona de impacto de la onda con el objetivo inicial\n\n"
        "**Ailment (Onda):** Suction\n"
        "**Chance de Ailment (Onda):** 100% en mobs; 50% en jefes\n"
        "**Duración de Ailment:** 1 segundo\n"
        "**Resistencia a Ailment:** 0.001 segundos\n\n"
        "**One-Handed Sword bonus:** Skill Multiplier (Tornado) +(baseDEX/500)\n"
        "**Two-Handed Sword bonus:** Skill Multiplier (Onda) +(1 + baseSTR/500)\n\n"
        "* Esta habilidad inflige Proration Mágica\n"
        "* Solo los Tornado Hits no se ven afectados por Whack, Long Range y Short Range Damage/Long Range Damage stats.\n"
        "* La onda rastreará al objetivo inicial y soltará el tornado al impactar\n"
        "* El buff a la constante de Triple Thrust's se divide por la suma de Número de golpes de la Onda y el Tornado"
    ),
)

BUSTER_BLADE = SkillText(
    title="Buster Blade",
    description="**Descripción del juego:** *\"Agrega un aura y corta consecutivamente. El Weapon ATK aumenta durante unos segundos al activar Buster Blade. Restaura una pequeña cantidad de HP cuando se añade el buff. El buff no se sobrescribe.\"*",
    details=(
        "**Habilidad Tier 4;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 0.75 * Skill Level; multiplicador total de todos los golpes\n"
        "**Base Skill Constant:** 30 * Skill Level; constante total de todos los golpes\n"
        "**Número de golpes:** 3 hits; el cálculo de daño se realiza una vez y se distribuye uniformemente entre los golpes\n"
        "**Alcance máximo de Cast:** 7m\n\n"
        "**Efecto de la habilidad:**\n"
        "* Restaura 1000 HP si el buff se aplica correctamente\n"
        "* Esta habilidad siempre hace crítico\n"
        "* En el bonus de OHS, Aura Blade tiene una pasiva que otorga Skill Multiplier adicional a Buster Blade de +(0.2 * Skill Level de Aura Blade) + baseDEX/200 mult aditivamente.\n\n"
        "**Efecto del Buff:**\n"
        "* Weapon ATK +(1 * Skill Level)%\n"
        "* La duración del buff no se renueva al usar esta habilidad mientras el buff está activo\n"
        "**Duración del Buff:** 10 segundos\n\n"
        "**One-Handed Sword bonus:** HP heal +2 * baseVIT\n"
        "**One-Handed Sword bonus:** Skill Multiplier +(baseDEX/200)\n"
        "**Two-Handed Sword bonus:** Skill Multiplier +(baseSTR/100)\n"
        "**Shield bonus:** Weapon ATK +(10 + Shield Refine)%\n\n"
        "El buff no se renueva si ya está activo"
    ),
)

SWORD_MASTERY = SkillText(
    title="Sword Mastery",
    description="**Descripción del juego:** *\"Mejora tu habilidad con la espada. El ATK de las espadas de una/dos manos aumenta.\"*",
    details=(
        "**Habilidad Tier 1;** Pasiva; Solo {ohs} / {ths}\n\n"
        "**Efecto Pasivo:** Weapon ATK +(3 * Skill Level)%; ATK +1% (niveles 1 y 2)/ +2% (niveles 3 a 7)/ +3% (niveles 8 a 10)\n\n"
        "En Dual Swords, esta habilidad también afecta a Weapon ATK y ATK de la espada de la mano secundaria"
    ),
)

QUICK_SLASH = SkillText(
    title="Quick Slash",
    description="**Descripción del juego:** *\"Acorta los intervalos de ataque de las espadas de una/dos manos.\"*",
    details=(
        "**Habilidad Tier 1;** Pasiva; Solo {ohs} / {ths}\n\n"
        "**Efecto Pasivo:** Attack Speed +(Skill Level)% y +(10 * Skill Level)"
    ),
)

SWORD_TECHNIQUES = SkillText(
    title="Sword Techniques",
    description="**Descripción del juego:** *\"Aprende el dominio de las espadas. El daño infligido de las habilidades de espada aumenta.\"*",
    details=(
        "**Habilidad Tier 2;** Pasiva; Solo {ohs} / {ths}\n\n"
        "**Efecto Pasivo:** Aumenta el daño de las Blade Skills en un (2 * Skill Level)%"
    ),
)

WAR_CRY = SkillText(
    title="War Cry",
    description="**Descripción del juego:** *\"Realiza un grito de guerra. Aumenta el ATK durante un tiempo. Elimina el Ailment de estado: [Fear].\"*",
    details=(
        "**Habilidad Tier 3;** Sin restricciones {all}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto de la habilidad:** Cuando la habilidad se lanza correctamente, elimina el Ailment Fear de cualquier miembro del grupo que lo tenga\n\n"
        "**Efecto del Buff:** Otorga un buff que aumenta el ATK en un (Skill Level)% a todo el grupo\n"
        "**Duración del Buff:** (15 + Skill Level) segundos\n\n"
        "**One-Handed Sword bonus:** Duración del Buff +50 segundos\n"
        "**Two-Handed Sword bonus:** ATK% del buff +5%\n\n"
        "Regla de superposición de War Cry entre compañeros: El skill level más alto anula al más bajo; si el skill level es el mismo, entonces la duración más larga anula a la más corta."
    ),
)

BERSERK = SkillText(
    title="Berserk",
    description="**Descripción del juego:** *\"Deja de pensar y empuña un arma como un berserker. Aumenta el poder de los ataques normales, Attack Speed y Critical Rate durante unos segundos y disminuye enormemente Stability/DEF/MDEF. Rampage no se elimina por Ailments de estado mientras esté activo.\"*",
    details=(
        "**Habilidad Tier 4;** Sin restricciones {all}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto del Buff:**\n"
        "* Attack Speed +(10 * Skill Level)% y +(100 * Skill Level)\n"
        "* Critical Rate +(2.5 * Skill Level)\n"
        "* Aumenta el Skill Multiplier de tus autoataques en (0.1 * Skill Level)\n"
        "* Rampage no se elimina por Ailments mientras el buff está activo\n"
        "* DEF -(100 - Skill Level)%; MDEF -(100 - Skill Level)%\n"
        "* Stability -(100 - 5 * Skill Level)%\n"
        "**Duración del Buff:** 10 segundos\n\n"
        "**One-Handed Sword bonus:** Duración del Buff +20 segundos\n"
        "**One-Handed Sword bonus:** La reducción de Stability se reduce a la mitad\n"
        "**One-Handed Sword (no Dual Swords) bonus:** La reducción de DEF% y MDEF% se reduce a la mitad\n"
        "**Two-Handed Sword bonus:** Duración del Buff +20 segundos\n"
        "**Two-Handed Sword bonus:** La reducción de Stability se reduce a la mitad\n"
        "**Two-Handed Sword bonus:** El Critical Rate del buff se duplica\n\n"
        "Si Rampage está activo, el Skill Multiplier de los primeros 10 autoataques aumenta con el incremento de Skill Multiplier aditivamente, pero no los multiplicadores de Golpe Final\n"
        "El incremento de Skill Multiplier de los autoataques solo se aplica a la mano principal de Dual Swords\n"
        "La reducción de Stability no afecta a Stability de la mano secundaria de Dual Swords"
    ),
)

SWIFT_ATTACK = SkillText(
    title="Swift Attack",
    description="**Descripción del juego:** *\"Patea mientras pretendes atacar con una espada. Esta habilidad tiene proration de ataque normal. El Coste MP de la siguiente habilidad usada se reducirá cuando la habilidad alcance su nivel máximo.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:**\n"
        "> One-Handed Sword: MIN((0.05 + 0.05 * Skill Level);0.5) + TotalDEX/500\n"
        "> Two-Handed Sword: MIN((0.05 + 0.05 * Skill Level);0.5) + TotalSTR/500\n"
        "> Dual Swords: MIN((0.05 + 0.05 * Skill Level);0.5) + TotalAGI/500\n\n"
        "**Base Skill Constant:** (Skill Level+1)^2 * 3 (Máx. 300)\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n\n"
        "**Efecto de la habilidad:**\n"
        "* Si esta habilidad está en el nivel 10, entonces la siguiente habilidad tiene su Coste MP dividido por la mitad y redondeado al múltiplo de 100 más cercano (ej: 300/2 = 150 -> 200 MP; 600/2 = 300 -> 300 MP)\n\n"
        "**Dual Swords bonus:** Coste MP reducido en 100\n"
        "**Dual Swords bonus:** Chance de Tumble 100% en nivel 10\n\n"
        "Esta habilidad inflige Proration Normal/Auto Attack. Pero el daño depende de Proration Física."
    ),
)

SHUTOUT = SkillText(
    title="Shutout",
    description="**Descripción del juego:** *\"Un golpe despiadado. Si el objetivo está afectado por Flinch, Tumble, Stun y no está sangrando(Bleed), el daño aumentará y el objetivo sufrirá [Bleed].\"*",
    details=(
        "**Habilidad Tier 5;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 5\n"
        "**Base Skill Constant:** 100\n"
        "**Enhanced Base Skill Multiplier:** 10 + Skill Level\n"
        "**Enhanced Base Skill Constant:** 100\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n\n"
        "**Efecto de la habilidad:**\n"
        "* Al usar esta habilidad en un objetivo bajo estado Flinch/Tumble/Stun y el objetivo no tiene el Ailment Bleed, esta habilidad se convierte en una habilidad mejorada que inflige más daño y también puede infligir Bleed 100% durante 10 segundos, sin resistencia.\n\n"
        "**OHS bonus:** Base Skill Multiplier +(BaseDEX/200)\n"
        "**OHS bonus:** Enhanced Base Skill Multiplier +(0.5 * Skill Level + BaseDEX/100)\n"
        "**OHS bonus:** El Physical Pierce total de la habilidad mejorada se cuadruplica.\n"
        "**Dual Swords bonus:** Base Skill Multiplier +(BaseAGI/400)\n"
        "**Dual Swords bonus:** Enhanced Base Skill Multiplier +(0.5 * Skill Level + BaseAGI/200)\n"
        "**Dual Swords bonus:** El Physical Pierce total de la habilidad mejorada se duplica.\n"
        "**THS bonus:** Base Skill Multiplier +(Skill Level)\n"
        "**THS nerf:** Esta habilidad no se ve afectada por motion speed%. A diferencia de OHS, que sí puede ser afectada por motion speed%"
    ),
)

LUNAR_SLASH = SkillText(
    title="Lunar Slash",
    description="**Descripción del juego:** *\"Corta al objetivo y una hoja mágica infligirá daño adicional tras un ligero retraso. La hoja mágica puede infligir [Fatigue].\"*",
    details=(
        "**Habilidad Tier 5;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 10\n"
        "**Base Skill Constant (Primer Hit):** 400\n"
        "**Base Skill Multiplier (Segundo Hit):** (TotalSTR * Skill Level * 0.1)/100\n"
        "**Base Skill Constant (Segundo Hit):** BaseINT/2\n"
        "**Base Skill Multiplier (Stack Hit):** (TotalSTR * Skill Level * 0.1)/100\n"
        "**Base Skill Constant (Stack Hit):** BaseINT\n"
        "**Número de golpes:** 2 hits en el objetivo principal; el cálculo de daño se realiza para cada golpe\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n\n"
        "**Ailment (Segundo Hit):** Fatigue\n"
        "**Chance de Ailment del Segundo Hit:** 4 * Skill Level %\n"
        "**Duración de Ailment del Segundo Hit:** 10 segundos\n"
        "**Resistencia a Ailment del Segundo Hit:** Ninguna\n\n"
        "**Efecto de la habilidad:**\n"
        "* Solo para THS, al usar esta habilidad, otorga +(CC) stacks de Lunar Slash. Se pueden consumir para infligir daño adicional al objetivo. Usar cualquier habilidad de ataque (excepto Lunar Slash) consumirá 1 stack de Lunar Slash para infligir/activar daño de Stack en el objetivo. Máximo de stacks: 9.\n"
        "* Stack/Golpes Adicionales tiene Critical Rate fija de +(10 * Skill Level + CRT). Nota: CRT es la estadística personal.\n"
        "* Todos los golpes de esta habilidad pueden verse afectados por SRD% y Sword Techniques. Sin embargo, el stack no se ve afectado por combo tags.\n\n"
        "**THS Bonus:** Realiza un ataque adicional si se usa otra habilidad de ataque. Este ataque adicional no puede infligir [Fatigue], pero el Critical Rate aumenta según el Skill Level.\n\n"
        "* Incluso si tu ataque de Lunar Slash resulta en Miss/Evasion, esta habilidad sigue otorgando stacks.\n"
        "* Si golpeas a múltiples objetivos con una habilidad AoE, consumirá varios stacks en múltiples objetivos, 1 stack por objetivo.\n"
        "* CC se refiere a Combo count. Que es Opener(1CC) > 2CC > 3CC y así sucesivamente."
    ),
)

AURA_BLADE = SkillText(
    title="Aura Blade",
    description="**Descripción del juego:** *\"Corta y despeja tu entorno con una hoja rodeada de un aura. El poder de la siguiente habilidad usada es 1.2x más fuerte. Otorga Additional Melee al arma mientras esté activo.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 5 + Skill Level\n"
        "**Base Skill Constant:** 200\n"
        "**Número de golpes:** 2 hits (para OHS) o 1 hit (para THS); el cálculo de daño se realiza una vez y se distribuye uniformemente entre los golpes\n"
        "**Alcance máximo de Cast:** 100m, teóricamente infinito (pero necesita objetivo para lanzar)\n"
        "**Alcance del golpe:** 3.5m de radio\n\n"
        "**Efecto del Buff:**\n"
        "* Aumenta el daño de la siguiente habilidad en 1.2x (+20%; se aplica multiplicativamente al final del cálculo de daño después de sumarse con el bonus de Brave Aura y la reducción de Mana Recharge)\n"
        "* Obtienes Additional Melee% de (10 * Skill Level)%\n"
        "* Duración del Buff: 40 segundos O hasta que uses habilidades\n\n"
        "**Efecto Pasivo:**\n"
        "* Otorga pasivamente un multiplicador de Skill adicional a Buster Blade de +(0.2 * Skill Level) + baseDEX/200 mult aditivamente.\n\n"
        "**OHS bonus:** Los buffs no se consumen al usar habilidades\n"
        "**OHS bonus:** Extiende los buffs de Aura Blade en 10 segundos cada vez que obtienes el buff de Buster Blade\n"
        "**Dual Swords bonus:** El poder/daño de la siguiente habilidad se vuelve 1.1x más fuerte\n"
        "**THS penalty:** El Additional Melee otorgado se reduce al 50%\n"
        "**THS bonus:** El poder/daño de la siguiente habilidad se vuelve 1.3x más fuerte\n\n"
        "Este buff de daño puede afectar cualquier habilidad, excepto su propia habilidad Aura Blade"
    ),
)

GLADIATE = SkillText(
    title="Gladiate",
    description="**Descripción del juego:** *\"Reduce el daño recibido un número determinado de veces durante 10 segundos. Restaura ligeramente MP cuando se reduce el daño. Recupera 10 MP por cada efecto de reducción de daño restante cuando se acabe el tiempo.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {ohs} / {ths}\n"
        "**Coste MP:** 0\n\n"
        "**Efecto de la habilidad:**\n"
        "* Al usar esta habilidad, otorga (Skill Level) stacks de Gladiate.\n"
        "* Cada vez que recibas daño durante este buff, perderás 1 stack y recuperarás MP dependiendo del arma que estés usando y también de Total AMPR que tengas.\n\n"
        "**Efecto del Buff:**\n"
        "* Reduce cualquier daño recibido en un (Skill Level)%\n"
        "* Cuando este buff termine, recupera tu MP en (10 por cada stack de Gladiate actual). Nota: si relanzas este buff de nuevo, no terminará este buff, sino que su duración se renovará a 10 segundos.\n"
        "* Duración del Buff: 10 segundos\n\n"
        "**OHS bonus:** Cantidad de MP recuperado al perder un stack: (Total AMPR * Skill Level/10)\n"
        "**Dual Swords penalty(bonus):** Cantidad de MP recuperado al perder un stack: (Total AMPR/4 * Skill Level/10)\n"
        "**Dual Swords bonus:** La reducción de daño total se duplica\n"
        "**THS penalty(bonus):** Cantidad de MP recuperado al perder un stack: (Total AMPR * 75% * Skill Level/10)\n"
        "**THS bonus:** La reducción de daño total se duplica\n"
        "**Shield bonus:** La reducción de daño total se duplica (se convierte en 2 * Skill Level)\n\n"
        "Esta habilidad no se puede usar como la primera habilidad de un combo."
    ),
)

HAMMER_SLAM = SkillText(
    title="Hammer Slam",
    description="**Descripción del juego:** *\"Realiza un ataque de corto alcance alrededor de los objetivos como si los estuvieras aplastando. Garantiza un golpe crítico en objetivos inmovilizados por Flinch u otros Ailments de estado. El Coste MP se vuelve 0 si se usa consecutivamente.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {ths}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Constant:** 100\n"
        "**Base Skill Multiplier:** 1 + Skill Level * 0.05 + TotalVIT/100 + baseSTR/500\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n"
        "**Alcance del golpe:** [¿Por defecto el rango máximo del autoataque del arma o 2.5m?] alrededor del objetivo\n\n"
        "**Efecto de la habilidad:**\n"
        "* Si se usa consecutivamente, ej. tu última acción de habilidad fue esta habilidad, entonces su Coste MP se vuelve 0 MP e inflige proration normal (su daño siempre es 100% proration, el daño no se ve afectado por la Proration Normal/Física). Pero, este coste 0 MP consecutivo no funciona como opener, ya que necesita 1 coste MP para ese opener.\n"
        "* Esta habilidad tiene Absolute Critical contra objetivos interrumpidos."
    ),
)

CLEAVING_ATTACK = SkillText(
    title="Cleaving Attack",
    description="**Descripción del juego:** *\"Blande la espada horizontalmente para lidiar con múltiples oponentes. Si hay 2 o más objetivos involucrados, el poder aumentará proporcionalmente y el MP consumido se restaurará.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {ths}\n"
        "**Coste MP:** 300\n\n"
        "**Base Skill Constant:** 150 + Skill Level * 15 + TotalVIT\n"
        "**Base Skill Multiplier:** 1.5 + Skill Level * 0.1 + TotalSTR/200 * (Número de Enemigos Golpeados - 1)\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n"
        "**Alcance del golpe:** Por defecto el rango máximo del autoataque del arma alrededor del casteador\n\n"
        "**Efecto de la habilidad:**\n"
        "* Al usarla, recuperarás MP en (cada objetivo golpeado - 1) barra de MP. Nota: no puede exceder el consumo de MP de esta habilidad. Ej: Usar esta habilidad con 0 coste MP debido a combo, resultará en ninguna ganancia de MP ya que es 0 coste MP. Si fuera 6 barras de coste MP, entonces ganarás 6 barras de MP si puedes golpear a 7 objetivos."
    ),
)

STORM_BLAZE = SkillText(
    title="Storm Blaze",
    description="**Descripción del juego:** *\"Ataca a los enemigos en línea recta con un corte aéreo. El poder del viento se acumulará cuando un ataque normal golpee. El poder del viento se consume al activar la habilidad. El poder, el alcance de ataque y la recuperación de MP aumentan según la cantidad consumida.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {ths}\n"
        "**Coste MP:** 200\n\n"
        "**Base Skill Constant:** 100 + Skill Level * 10 + TotalVIT\n"
        "**Base Skill Multiplier:** (0.5 + Skill Level * 0.05) * Blaze Stack consumido\n"
        "**Número de golpes:** 1\n"
        "**Alcance máximo de Cast:** 16m\n"
        "**Alcance del golpe:** Longitud de 16m y radio de (2 + 0.4 * Blaze Stack)m, desde el casteador hacia el objetivo principal\n\n"
        "**Efecto de la habilidad:**\n"
        "* Obtendrás pasivamente 1 stack de Blaze por cada autoataque o 2 stacks si es con autoataque de Rampage. También puedes usar Hammer Slam (solo si se usa consecutivamente) para ganar +1 Blaze Stack. Puedes almacenar Blaze Stack hasta (10 + BaseDEX/25) stacks. Pero al usar, solo puedes consumir hasta 10 stacks para el daño y la fórmula de ganancia de MP.\n"
        "* Al usarla, ganarás MP de (Blaze Stack consumido^2 * 4)."
    ),
)

GARDE_BLADE = SkillText(
    title="Garde Blade",
    description="**Descripción del juego:** *\"Una técnica de defensa que usa una espada de dos manos. Aumenta la Physical/Magic Resistance y mejora la habilidad de Guard durante 70 segundos. Recupera un poco de Guard Power cuando se aplica el buff. Sobrescribir no activará esta recuperación.\"*",
    details=(
        "**Habilidad Tier 4;** Solo {ths}\n"
        "**Coste MP:** 300\n\n"
        "**Efecto del Buff:**\n"
        "* El refinamiento de tu arma ahora funcionará como el valor de refinamiento de un escudo\n"
        "* Aumenta tu Physical Resistance y Magic Resistance en un +(Skill Level)%\n"
        "* Si aún no tienes el buff de esta habilidad, al usarla recuperarás Guard Gauge en (2.5 * Skill Level + VIT/100). Solo puede recuperar hasta llegar a 100 Guard Gauge.\n"
        "* Serás inmune a interrupciones (Flinch/Tumble/Stun/Knockback) si haces Perfect Guard\n"
        "**Duración del Buff:** 70 segundos O hasta que sufras \"Guard Power Break\"\n\n"
        "No puedes usar esta habilidad si tienes \"Guard Power Break\""
    ),
)

OGRE_SLASH = SkillText(
    title="Ogre Slash",
    description="**Descripción del juego:** *\"Inflige daño al objetivo y, tras un breve periodo, causa una explosión en los pies del objetivo, infligiendo daño adicional. Si se cumplen las condiciones, el poder de Ogre se acumulará y consumirá al activar la habilidad para aumentar el poder y el buff.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {ths}\n"
        "**Coste MP:** 500\n\n"
        "**Base Skill Constant (Primer Hit):** TotalDEX\n"
        "**Base Skill Multiplier (Primer Hit):** (BaseSTR + BaseVIT)/100\n"
        "**Base Skill Constant (Segundo AOE Hit):** 500\n"
        "**Base Skill Multiplier (Segundo AOE Hit):** 2 * Ogre Stack Consumido\n"
        "**Número de golpes:** 2 hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo del autoataque del arma\n"
        "**Alcance del Segundo Golpe:** 2m alrededor del objetivo\n\n"
        "**Efecto de la habilidad:**\n"
        "* Obtendrás pasivamente Ogre Stacks de las siguientes formas: +Floor(Skill Level ÷ 2) cuando seas el primero en entrar en batalla, +1 cuando seas objetivo de un AoE de advertencia rojo/azul (1 segundo + duración de AoE de cooldown), +1 al recibir daño (1 segundo de cooldown), y +1 por un Guard perfectamente sincronizado. Puedes almacenar hasta 20 Ogre Stacks, pero solo se pueden consumir hasta 10 por activación.\n"
        "* Esta habilidad tiene Physical Pierce de (10 * Ogre Stack Consumido)%; si este efecto hace que el Physical Pierce total de esta habilidad supere el 100%, cada 1% excesivo se convierte en 0.01 de multiplicador adicional al Primer Golpe\n"
        "* El segundo daño AoE de esta habilidad puede verse afectado por SRD%, tiene un radio de explosión de 1.5m que ignora Guard, y detona después de 2.5 segundos. La proration del segundo AoE es la misma que la del primer golpe.\n"
        "* Durante la animación de esta habilidad, eres inmune a Ailments de interrupción (Flinch/Tumble/Stun/Knockback)\n\n"
        "**Efecto del Buff:**\n"
        "* Duplica el daño de Rampage Auto Attack y Golpe Final.\n"
        "* Mitiga la penalidad de Stability de Berserk en un 50%. Así que Berserk en nivel 10, -25% Stability se convertirá en -12% Stability.\n"
        "* También mitiga la penalidad de DEF%/MDEF% de Berserk en un 50%.\n"
        "* Recuperarás HP basado en el consumo de barras de MP: (Barras de MP Consumidas ^ 2) * 100 HP.\n"
        "* Reducirás el 99% del daño entrante durante la animación de los últimos golpes de Rampage.\n"
        "**Duración del Buff:** ~~3 + 2 * Skill~~ (10 + 5 * Skill Level) segundos."
    ),
)
