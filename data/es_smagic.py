from dataclasses import dataclass


@dataclass(frozen=True)
class SkillText:
    title: str
    description: str
    details: str

FOOTER = "Créditos: Phantom's Library"

INDEX_HEADER = [
    "**Nivel requerido:** T1 ninguno, T2 Lv30, T3 Lv70, T4 Lv150, T5 Lv240",
    '**Selecciona un "Texto Azul" para guiarte hacia el.**',
    "",
]

ELEMENTAL_NAMES = SkillText(
    title="Nombres de las skills segun elemento",
    description="**Nombre de las skills con Fire - Water - Wind - Earth - Light - Dark, respectivamente**\n\n**Magic: Arrows**\nFire Arrows - Water Arrows - Wind Arrows - Earth Arrows - Light Arrows - Dark Arrows\n\n**Magic: Javelin**\nFire Javelin - Ice Javelin - Wind Javelin - Rock Javelin - Holy Javelin - Dark Javelin\n\n**Magic: Lances**\nVulcan - Icicles - Wind Thrust - Rock Cannon - Vanishment - Eclipse\n\n**Magic: Wall**\nFire Wall - Aqua Screen - Gale Zone - Earthquake - Holy Wall - Evil Gate\n\n**Magic: Blast**\nExplosion - Absolute Zero - Aero Blast - Geo Impact - Shining Blast - Evil Blast\n\n**Magic: Storm**\nFire Storm - Frozen Cyclone - Thunder Storm - Sandstorm - Lux Vortex - Evil Tempest\n\n**Magic: Burst**\nHell Inferno - Eternal Blizzard - Force Tempest - Gravity Turn - Punishment - Eclipse\n\n**Magic: Crash**\nMeteor Rain - Hail - Fulgurite - Rockfall - Meteor Light - Cosmos",
    details=(
        "**Nota sobre el cambio de elemento:**\n"
        "* **M.arrows:** cambia la apariencia de las flechas\n"
        "* **M.javelin:** cambia la animación del impacto\n"
        "* **M.lances:** cambia el efecto de golpe de las lanzas\n"
        "* **M.wall:** cambia toda la formación mágica y su animación de efecto\n"
        "* **M.blast:** cambia el efecto de explosión\n"
        "* **M.storm:** cambia su color\n"
        "* **M.burst:** cambia toda la animación de efecto\n"
        "* **M.crash:** solo cambia el color"
    ),
)

MAGIC_ARROWS = SkillText(
    title="Magic: Arrows",
    description="**Descripción del juego:** *\"Dispara pequeñas flechas mágicas. Las flechas aumentan a medida que la habilidad sube de nivel.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** 0.65 + 0.06 * Skill Level; multiplicador para cada hit\n"
        "**Base Skill Constant:** 90 + 5 * Skill Level; constante para cada hit\n"
        "**Número de golpes:** 2 hits (niveles 1 y 2); 3 hits (niveles 3 y 4); 4 hits (niveles 5 y 6); 5 hits (niveles 7 y 8); 6 hits (niveles 9 y 10); el cálculo de daño se realiza para el primer hit, luego el resto de hits copiarán el primero[se copia crit/Guard/etc.]\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Tiempo de Cast base:** 2 segundos; afectado por Cast Speed\n\n"
        "**Staff bonus:** Skill Multiplier +0.25\n"
        "**Magic Device bonus:** Número de golpes +2\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*"
    ),
)

MAGIC_JAVELIN = SkillText(
    title="Magic: Javelin",
    description="**Descripción del juego:** *\"Deja caer una gran jabalina mágica sobre el objetivo. Chance de infligir un ailment. El ailment depende del elemento.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** 1.5 + 0.1 * Skill Level\n"
        "**Base Skill Constant:** 50 + 15 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 8m\n\n"
        "**Ailment:** Flinch (con elemento Neutral); Ignite (con elemento Fire); Freeze (con elemento Water); Blind (con elemento Wind); Slow (con elemento Earth); Dizzy (con elemento Light); Fear (con elemento Dark)\n"
        "**Chance Base de Ailment:** (7.5 * Skill Level)%\n"
        "**Duración de Ailment:** 2 segundos para Flinch; 10 segundos para otros\n"
        "**Resistencia a Ailment:**\n"
        "* Para Flinch: 5 segundos (Easy, Normal y Hard); 6 segundos (Nightmare); 9 segundos (Ultimate)\n"
        "* Para otros: Ninguna\n\n"
        "**Staff bonus:** Skill Multiplier +0.5\n"
        "**Magic Device:** Ailment chance +25%\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*"
    ),
)

MAGIC_LANCES = SkillText(
    title="Magic: Lances",
    description="**Descripción del juego:** *\"Dispara lanzas mágicas una tras otra. Las lanzas aumentan a medida que la habilidad sube de nivel. Chance de infligir [Stop] al objetivo.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** 2.5 + 0.15 * Skill Level; multiplicador para cada hit\n"
        "**Base Skill Constant:** 300 + 40 * Skill Level; constante para cada hit\n"
        "**Número de golpes:** 2 hits (niveles 1 a 5); 3 hits (niveles 6 a 10); el cálculo de daño se realiza para el primer hit, luego el resto de hits copiarán el primero[se copia crit/Guard/etc.]\n"
        "**Alcance máximo de Cast:** 14m\n"
        "**Tiempo de Cast base:** 2 segundos; afectado por Cast Speed\n\n"
        "**Ailment:** Stop\n"
        "**Chance Base de Ailment:** 10% + (2 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** 10 segundos\n\n"
        "**Staff bonus:** Skill Multiplier (+1.5 + TotalINT/500)\n"
        "**Staff bonus:** La chance de Stop se triplica\n"
        "**Magic Device bonus:** Skill Multiplier (TotalINT/500)\n"
        "**Magic Device bonus:** Número de golpes +2\n"
        "**Magic Device bonus:** La chance de Stop se triplica\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*"
    ),
)

MAGIC_IMPACT = SkillText(
    title="Magic: Impact",
    description="**Descripción del juego:** *\"Ataca a los enemigos a tu alrededor con una onda de choque. Reduce a la mitad el Coste MP de la siguiente habilidad. El efecto se debilitará si usas esta habilidad consecutivamente.\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Mágico\n"
        "**Elemento:** Neutral\n\n"
        "**Base Skill Multiplier:** 0.25 * Skill Level\n"
        "**Skill Multiplier (Buff de Impact activo):** 0.1 * Skill Level\n"
        "**Base Skill Constant:** 100 + 10 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Teóricamente infinito (limitado a 100m)\n"
        "**Alcance del golpe:** 3m; alrededor del lanzador\n"
        "**Tiempo de Cast Base:** 2 segundos (niveles 1 y 2); 1 segundo (niveles 3 a 6); ninguno (niveles 7 a 10); afectado por Cast Speed\n\n"
        "**Efecto del Buff:**\n"
        "* La siguiente habilidad tiene su Coste MP dividido a la mitad y redondeado al múltiplo de 100 más cercano (ej. 300/2 = 150 → 200 MP; 600/2 = 300 → 300 MP)\n"
        "* Mientras este buff esté activo, el multiplcador y la chance de Tumble de esta habilidad se reducen y los bonus específicos de arma se desactivan\n"
        "**Duración del Buff:** Hasta que se use una habilidad\n\n"
        "**Ailment:** Tumble\n"
        "**Chance Base de Ailment:** 15% + (5 * Skill Level)%\n"
        "**Chance de Ailment (Buff de Impact activo):** (Skill Level)%\n"
        "**Duración de Ailment:** 3 segundos\n"
        "**Resistencia a Ailment:** 3 segundos (Easy y Normal); 6 segundos (Hard); 12 segundos (Nightmare); 18 segundos (Ultimate)\n\n"
        "**Staff bonus:** Tumble chance +25%\n"
        "**Magic Device bonus:** Skill Multiplier +2.5"
    ),
)

MAGIC_FINALE = SkillText(
    title="Magic: Finale",
    description="**Descripción del juego:** *\"Área de efecto súper amplia. Inflige más daño a los enemigos cerca del centro. El Tiempo de Cast es largo y no se puede reducir con CSPD. Genera Aggro mientras casteas.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 1600\n"
        "**Tipo de daño:** Mágico\n"
        "**Elemento:** Neutral\n\n"
        "**Primer Radio Skill Multiplier:** 30\n"
        "**Segundo Radio Skill Multiplier:** 20\n"
        "**Tercer Radio Skill Multiplier:** 10\n"
        "**Primer Radio Skill Constant:** 300 * Skill Level\n"
        "**Segundo Radio Skill Constant:** 30 * Skill Level\n"
        "**Tercer Radio Skill Constant:** 3 * Skill Level\n"
        "**Número de golpes:** 3 hits (si está dentro del Primer Radio) / 2 hits (si está dentro del Segundo Radio pero no del Primer Radio) / 1 hit (si está dentro del Tercer Radio pero no en los otros); el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe:** 0.5m (Primer Radio); 4m (Segundo Radio); 10m (Tercer Radio)\n"
        "**Tiempo de Cast base:** (13 - Skill Level) segundos\n\n"
        "**Efecto de la habilidad:**\n"
        "* En el objetivo principal, genera 1000 Aggro por segundo de tiempo de cast[aggro basado en 1MP = 10Aggro], luego genera el aggro restante al golpear. Funciona normalmente en otros objetivos. CSPD puede reducir ese aggro por tiempo de cast. Dentro de 1k CSPD, cada 20 CSPD = 1% de reducción de aggro, y después de 1k CSPD, cada 180 CSPD = 1% de reducción de aggro. Similar a cómo se calcula el tiempo de cast con CSPD.\n"
        "* Cast Speed puede reducir ligeramente el tiempo de cast (máximo de 1 segundo de reducción a 10k CSPD). Por lo tanto, Magic: Finale Cast Time = (13 - Skill Level) - (MAX(0; MIN(10000; Total CSPD))/10000).\n\n"
        "**Staff bonus:** Primer Radio Skill Multiplier +7.5+(BaseINT/100)\n"
        "**Magic Device bonus:** Primer Radio Skill Multiplier +(BaseINT/100)\n"
        "**Magic Device bonus:** El Primer Radio se cuadruplica\n"
        "**Magic Device bonus:** El Segundo y Tercer Radio se duplican\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*\n"
        "Esta habilidad no se ve afectada por Chain Cast\n"
        "El aggro generado durante la animación de cast no se ve afectado por Sneak Attack o estadísticas de Aggro%"
    ),
)

MAGIC_WALL = SkillText(
    title="Magic: Wall",
    description="**Descripción del juego:** *\"Crea un muro mágico en los pies. Inflige daño y repele a los enemigos.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** 0.8 + 0.04 * Skill Level + BaseINT/1000; multiplicador para cada hit\n"
        "**Base Skill Constant:** 120 + 10 * Skill Level; constante para cada hit\n"
        "**Número de golpes:** 5 hits (nivel 1); 6 hits (niveles 2 y 3); 7 hits (niveles 4 y 5); 8 hits (niveles 6 y 7); 9 hits (niveles 8 y 9); 10 hits (nivel 10); el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** Teóricamente infinito\n"
        "**Alcance del golpe:** 2m; alrededor de la posición del lanzador cuando se lanza la habilidad\n"
        "**Tiempo de Cast base:** 1 segundo; afectado por Cast Speed\n\n"
        "**Ailment:** Knockback\n"
        "**Chance Base de Ailment:** 100% mientras tengas aggro\n"
        "**Distancia de Knockback:** 5m; reducida a la mitad para jefes\n"
        "**Resistencia a Ailment:** 0.8 segundos\n\n"
        "**Staff bonus:** Skill Multiplier +0.3\n"
        "**Magic Device bonus:** Alcance del golpe +1m\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*\n"
        "El Buff a la constante de Triple Thrust's se divide por el Número de golpes"
    ),
)

MAGIC_BLAST = SkillText(
    title="Magic: Blast",
    description="**Descripción del juego:** *\"Provoca una explosión concentrando poder mágico. Chance de infligir un ailment. El ailment depende del elemento.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** 7 + 0.3 * Skill Level\n"
        "**Base Skill Constant:** 180 + 20 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 8m\n"
        "**Alcance del golpe:** 2m alrededor del objetivo\n"
        "**Tiempo de Cast base:** 4 segundos; afectado por Cast Speed\n\n"
        "**Ailment:** Flinch (con elemento Neutral); Ignite (con elemento Fire); Freeze (con elemento Water); Blind (con elemento Wind); Slow (con elemento Earth); Dizzy (con elemento Light); Fear (con elemento Dark)\n"
        "**Chance Base de Ailment:** (5 * Skill Level)%\n"
        "**Duración de Ailment:** 2 segundos para Flinch; 10 segundos para otros\n"
        "**Resistencia a Ailment:**\n"
        "* Para Flinch: 5 segundos (Easy, Normal y Hard); 6 segundos (Nightmare); 9 segundos (Ultimate)\n"
        "* Para otros: Ninguna\n\n"
        "**Staff bonus:** Skill Multiplier +(1.5 + TotalINT/500)\n"
        "**Magic Device bonus:** Skill Multiplier +(TotalINT/500)\n"
        "**Magic Device bonus:** Ailment chance +50%\n"
        "**Magic Device bonus:** Alcance del golpe +2m\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*"
    ),
)

MAGIC_STORM = SkillText(
    title="Magic: Storm",
    description="**Descripción del juego:** *\"Magia para generar una tormenta. Los enemigos serán succionados hacia ella. Los monstruos fuertes pueden no ser succionados.\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** 1.8 + 0.02 * Skill Level; multiplicador para cada hit\n"
        "**Base Skill Constant:** 420; constante para cada hit\n"
        "**Número de golpes:** 1 hit (nivel 1); 2 hits (niveles 2 y 3); 3 hits (niveles 4 y 5); 4 hits (niveles 6 y 7); 5 hits (niveles 8 y 9); 6 hits (nivel 10); el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** 8m\n"
        "**Alcance del golpe:** 1.75m (niveles 1 a 3); 2.75m (niveles 4 a 7); 3.75m (niveles 8 a 10); alrededor de la posición del objetivo cuando se lanza la habilidad\n"
        "**Tiempo de Cast base:** 1 segundo; afectado por Cast Speed\n\n"
        "**Ailment:** Suction\n"
        "**Chance Base de Ailment:** 100% en mobs; 50% en jefes\n"
        "**Duración de Ailment:** 1 segundo\n"
        "**Resistencia a Ailment:** 0.001 segundos\n\n"
        "**Staff bonus:** Skill Multiplier +1\n"
        "**Magic Device bonus:** Alcance del golpe +2m\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*\n"
        "El Buff a la constante de Triple Thrust's se divide por el Número de golpes"
    ),
)

MAGIC_BURST = SkillText(
    title="Magic: Burst",
    description="**Descripción del juego:** *\"Potencia el poder mágico y dispara. Chance de hacer Knockback al objetivo que te apunta. El Tiempo de Cast es muy largo, sin embargo, se acorta usando Magic Skills antes de castear.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** 15 + 0.6 * Skill Level\n"
        "**Base Skill Constant:** 200 + 30 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 8m\n"
        "**Alcance del golpe:** Abanico de 8m (niveles 1 a 5) / 9m (nivel 6) / 10m (nivel 7) / 11m (nivel 8) / 12m (nivel 9) / 13m (nivel 10) de radio y un ángulo de (40 + 2 * Skill Level)°\n"
        "**Tiempo de Cast base:** 8 segundos; afectado por Cast Speed\n\n"
        "**Efecto del Buff:**\n"
        "* Por cada otra habilidad de ataque de Magic Skills usada, el buff gana un contador; esta habilidad puede tener un máximo de 8 contadores\n"
        "* El Tiempo de Cast total de esta habilidad se reduce en 1 segundo por cada contador; esto se aplica después de los cálculos de Cast Speed y Chain Cast; solo se puede reducir un máximo de 8 segundos de esta manera\n"
        "**Duración del Buff:** Hasta que uses Magic: Burst\n"
        "* Después de que termine el cast de esta habilidad, obtienes un buff de Invencibilidad sobre ti mismo durante 2 segundos, pero termina inmediatamente cuando la animación de esta habilidad termina. Sin embargo, si usas esta habilidad como Staff o Main MD, su buff de invencibilidad es fijo de 2 segundos [de hecho, este buff de iframe no termina inmediatamente cuando termina la animación de esta habilidad].\n\n"
        "**Ailment:** Knockback (no disponible en jefes)\n"
        "**Chance Base de Ailment:** (10 * Skill Level)%\n"
        "**Distancia de Knockback:** 15m - 2 * tamaño del mob en metros del juego\n"
        "**Resistencia a Ailment:** Distancia de Knockback del mob en segundos\n\n"
        "Ahora, la Reducción de Tiempo de Cast total afectará este límite máximo de contadores.\n"
        "Contador de Stacks Visuales 0/8 si tienes 0 CSPD, 0/4 si tienes 1k CSPD, 0/3 si tienes 3250 CSPD, 0/2 si tienes 5500 CSPD, 0/1 si tienes 7750 CSPD, por último 0/0 si tienes 10k CSPD. Básicamente es solo un contador visual de stacks que te ayuda a ver cuántos stacks necesitas para obtener un burst instantáneo. [Nota: la última vez funcionaba así, pero ahora está bugueado y no cambia el Contador de Stacks Visuales]\n\n"
        "**Staff bonus:** Skill Multiplier +(BaseINT/100)\n"
        "**Magic Device bonus:** Skill Multiplier +(BaseINT/200)\n"
        "**Magic Device bonus:** Radio del abanico +1m (niveles 1 a 3) / +2m (niveles 4 a 6) / +3m (niveles 7 a 10)\n"
        "**Magic Device bonus:** Ángulo del abanico +5° (niveles 1 a 3) / +10° (niveles 4 a 6) / +15° (niveles 7 a 10)\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*\n\n"
        "**Rango de Magic: Burst:**\n"
        "Rojo: posición del lanzador principal\n"
        "Azul: posible posición del objetivo principal (la posición realmente no importa)\n"
        "Verde: área de Magic: Burst\n"
        "Púrpura: ángulo de Magic: Burst\n"
        "Negro: el área de una habilidad circular si tuviera el mismo radio que Magic: Burst; esto es principalmente para describir el radio y el arco de Magic: Burst\n\n"
        "{image}"
    ),
)

MAGIC_MASTERY = SkillText(
    title="Magic Mastery",
    description="**Descripción del juego:** *\"Mejora en el uso de armas mágicas. El ATK de los Staffs y Magic Devices aumenta.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {staff} / {magicdevice}\n"
        "**Efecto Pasivo:** Weapon ATK +(3 * Skill Level)%; MATK +1% (niveles 1 y 2) / +2% (niveles 3 a 7) / +3% (niveles 8 a 10)"
    ),
)

MP_CHARGE = SkillText(
    title="MP Charge",
    description="**Descripción del juego:** *\"Recupera MP cargando poder mágico. El tiempo de carga se reduce a medida que la habilidad sube de nivel.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 0\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Tiempo de Carga base:** 9 segundos (niveles 1 a 3); 8 segundos (niveles 4 a 6); 7 segundos (niveles 7 a 9); 6 segundos (nivel 10); afectado por Cast Speed\n"
        "Reducción de tiempo de carga por CSPD = Tiempo de carga base - MIN [1 ; CSPD/1000]\n\n"
        "**Efecto de la habilidad:** Recupera (200 + 10 * Skill Level) MP si la habilidad se lanza correctamente\n\n"
        "**Efecto del Buff:** Reduce el Tiempo de Cast de Maximizer en (Skill Level) segundos; este efecto solo ocurre si tienes un Staff o Magic Device al usar Maximizer\n"
        "**Duración del Buff:** Hasta que se use una habilidad\n\n"
        "**Staff bonus:** El Tiempo de Carga se reduce a la mitad\n"
        "**Magic Device bonus:** El Tiempo de Carga se divide por 1.5\n"
        "**Magic Device bonus:** MP restaurado +50\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*\n"
        "Esta habilidad no se puede usar como primera habilidad de un combo"
    ),
)

CHAIN_CAST = SkillText(
    title="Chain Cast",
    description="**Descripción del juego:** *\"Castea magia eficientemente. La velocidad de cast de la habilidad mágica usada después de \"Magic: Arrows\" aumenta. Efecto adicional con staff o magic device (main): Velocidad de cast, MATK y estabilidad mágica aumentan cada vez que una habilidad de ataque con tiempo de cast golpea. Este efecto se puede obtener hasta 10 veces.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n\n"
        "**Efecto Pasivo:**\n"
        "Cada vez que usas Magic: Arrow, se concede uno de los siguientes dos efectos:\n"
        "* Si la siguiente habilidad de ataque de Magic Skills tiene tiempo de cast, el Tiempo de Cast de esa siguiente habilidad se reduce en (5 * Skill Level)%. SE APLICA DESPUÉS de la reducción de CSPD en el tiempo de cast\n"
        "* Si la siguiente habilidad de ataque de Magic Skills no tiene tiempo de cast, esa siguiente habilidad obtiene un aumento de Motion Speed de (5 * Skill Level)%.\n"
        "**Duración del Efecto Pasivo:** Hasta que uses cualquier habilidad de ataque de Magic Skills\n\n"
        "**Staff/MD bonus:**\n"
        "* Obtienes un Efecto Pasivo que concede +1 Chain stack cada vez que una habilidad de ataque que necesita tiempo de cast golpea a enemigos (con excepción, Ether Flare también puede añadir este stack). ¡Nota: +1 stack por cada golpe!\n"
        "* El Tiempo de Cast base de cualquier habilidad que necesite tiempo de cast se reducirá en (0.1 * Chain Stack) segundos. Este buff se aplica antes de la reducción de Tiempo de Cast por CSPD. Nota: esta reducción de tiempo de cast base de esta habilidad, parece no poder reducir ninguna habilidad que tenga 1 segundo de Tiempo de Cast base (Magic: Storm/Wall)\n"
        "* Aumenta tu Magic Stability en (Skill Level * 0.1 * Chain Stack)%. Staff Bonus: ¡2x Magic Stability Bonus!\n"
        "* Aumenta MATK en +(Skill Level * Chain Stack). MD Bonus: ¡2x MATK Bonus!\n"
        "**Duración de Chain Stack:** Se pierde 1 Chain stack cada 30 segundos (se puede refrescar la duración cada vez que se gana un stack)\n\n"
        "El aumento de Motion Speed se acumula multiplicativamente con los efectos de Freeze y el combo tag \"swift\""
    ),
)

POWER_WAVE = SkillText(
    title="Power Wave",
    description="**Descripción del juego:** *\"Dispara una onda mágica si el objetivo está fuera de alcance. Disponible desde 5m o menos de distancia. El alcance se extiende hasta 10m a medida que la habilidad sube de nivel. Attack MP Recovery se aplica a esta habilidad.\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Tipo de daño:** Neutral\n\n"
        "**Alcance máximo de Power Wave Auto Attack:** 5m + (0.5 * Skill Level)m\n"
        "**Efecto Pasivo:** Cuando estás fuera de tu alcance de autoataque predeterminado, pero dentro del alcance de Power Wave Auto Attack, puedes usar un autoataque que aún recupera MP a través de Attack MP Recovery y aún inflige proration neutral, pero su daño total se reduce en (100 - 5 * Skill Level)%\n\n"
        "**Staff bonus:** Alcance máximo de Power Wave Auto Attack +2m\n"
        "**Staff bonus:** Penalización de daño de autoataque -40%\n"
        "**Magic Device bonus:** Penalización de daño de autoataque -70%; una \"penalización\" de daño negativa resulta en un aumento de daño positivo\n"
        "En Dual Swords, la fórmula de cálculo de daño para Power Wave auto attacks cambia: el daño de autoataque de la mano principal y la mano secundaria se suman antes de distribuir el resultado uniformemente entre los golpes\n"
        "Power Wave se desactiva cuando Rampage está activo"
    ),
)

MAXIMIZER = SkillText(
    title="Maximizer",
    description="**Descripción del juego:** *\"Restaura enormemente el MP. El Tiempo de Cast se acorta a medida que la habilidad sube de nivel. Si usas MP Charge antes de esta habilidad, el Tiempo de Cast de Maximizer se acortará según el nivel de MP Charge al usar la habilidad con un Staff o Magic Device.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Tiempo de Cast base:** 17 segundos (nivel 1); 16.5 segundos (nivel 2) / 16 segundos (nivel 3) / 15.5 segundos (nivel 4) / 15 segundos (nivel 5) / 14 segundos (nivel 6) / 13 segundos (nivel 7) / 12 segundos (nivel 8) / 11 segundos (nivel 9) / 10 segundos (nivel 10)\n"
        "**Efecto de la habilidad:** Recupera 1000 MP si la habilidad se lanza correctamente\n"
        "Si tienes MP Charge, cada nivel de MP Charge puede reducir 1 segundo de tiempo de cast de esta habilidad. SOLO para STAFF y MD\n\n"
        "**Staff bonus:** MP restaurado +500\n"
        "**Magic Device bonus:** MP restaurado +700\n"
        "*Staff bonus tiene prioridad sobre Magic Device bonus*\n"
        "El tiempo de cast de esta habilidad no se ve afectado por CSPD"
    ),
)

GUARDIAN_BEAM = SkillText(
    title="Magic: Guardian Beam",
    description="**Descripción del juego:** *\"Emite luz para proteger al lanzador. Mientras está activo, los ataques mágicos se ejecutarán en un momento determinado, como después de que se lancen otras habilidades mágicas, o después de infligir daño a un enemigo.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {staff} / Main {magicdevice}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier lv 10:** 0.5 + TotalINT/100; multiplicador para cada hit\n"
        "**Base Skill Constant:** 50 + 3 * Skill Level; constante para cada hit\n"
        "**Alcance máximo de Cast:** Infinito\n\n"
        "**Efecto del Buff:**\n"
        "* Tu Beam Stack al usarlo será (Skill Level * (Skill Level + 1)/2). Así que en nivel 10, tendrás 55 Beam Stacks.\n"
        "* La duración de la habilidad es ilimitada y durará hasta que todos los beam stacks se agoten.\n"
        "* Si tienes aggro del objetivo y el objetivo está a 8m, usar una habilidad mágica durante el tiempo de cast = 1 beam stack se usará para atacar por cada 1 segundo de tiempo de cast, en el objetivo a 8m que tenga aggro sobre ti.\n"
        "* Mientras tanto, 1 beam stack se usará para atacar [después de que termine el tiempo de cast de la habilidad mágica?] sin necesidad de aggro y debe estar dentro de 24m.\n"
"* Al usar magia AoE (como Burst, Storm, Wall, etc.) que golpee a varios objetivos sin matarlos, se consumirá un beam stack por cada objetivo que haya sobrevivido.\n"
"(cantidad de beams usados = número de objetivos sobrevivientes)\n"
        "* Los beams causan Knockback de 4m en monstruos normales (no pueden hacer Knockback a jefes/mini jefes)\n"
        "* Este ataque de beam no inflige Proration mágica\n"
        "* Esta habilidad está fijada como Neutral/sin elemento.\n\n"
        "Los Combo Tags no afectan esta habilidad"
    ),
)

CHRONOS_SHIFT = SkillText(
    title="Chronos Shift",
    description="**Descripción del juego:** *\"Una técnica prohibida que permite retroceder en el tiempo y volver a lanzar un hechizo. Reactiva al instante la última habilidad mágica utilizada. Tras usar esta habilidad, hay que esperar un tiempo para poder volver a utilizarla\"*",
    details=(
        "**Habilidad Tier 5;** Solo Main {magicdevice}\n"
        "**Coste MP:** 0\n\n"
        "**Efecto de la habilidad:**\n"
        "* Usar esta habilidad relanzará tu última habilidad de Magic Skills usada. Hay un tiempo de reutilización tras esta activación, es de (16 - Skill Level) segundos.\n\n"
        "* Esta habilidad copia los valores exactos de la habilidad original cuando esa habilidad fue lanzada, (Constante, Multiplicador, Alcance, Efecto... pero no efectos de combo tag), independientemente del nivel de esta habilidad. También se trata como si fuera la misma habilidad que la original, por lo tanto, habilidades que duran después del cast como Magic: Wall se \"reiniciarán\" como si hubieras relanzado un nuevo Magic: Wall.\n\n"
        "* La habilidad lanzada a través de esta habilidad puede ser insta cast independientemente de tu CSPD (usa la animación de cast de esta habilidad). Incluso Finale es instantáneo. Sin embargo, la habilidad no puede otorgar stack de Magic: Burst ni cargar Magic: Magic Cannon.\n\n"
        "* El Coste MP de esta habilidad depende del coste mp final de tu última habilidad (incluyendo después de efectos de reducir mp a la mitad como Impact). ~~Se consumirá HP cuando no tengas suficiente MP para usar esta habilidad, el coste de HP es (110 - 10 * Skill Level)% de tu MaxHP por cada 100 MP.~~\n\n"
        "* Un Magic: Arrow copiado aún puede otorgar el buff de Chain Cast\n\n"
        "Esta habilidad no se puede incluir en un combo"
    ),
)

MAGIC_CANNON = SkillText(
    title="Magic: Magic Cannon",
    description="**Descripción del juego:** *\"Un cañón mágico que arrasa enemigos en línea recta (Habilidad de Carga). Cárgalo para aumentar su poder y número de golpes. Usar una habilidad que implique castear acelerará la carga.\"*",
    details=(
        "**Habilidad Tier 5;** Sin Restricciones {all}\n"
        "**Coste MP:** 0(buff cast) / 700 (attack cast)\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Constant:** 700 + Carga\n"
        "**Base Skill Multiplier:** 0.03 * Skill Level * Carga (para cada hit hasta 20% de carga, reinicia a un nuevo hit cada 20%); empieza a aumentar de nuevo de manera similar después del 100% (+0.03 * Skill Level * Carga, cambia al siguiente hit después de cada 20%), hasta +0.6 * Skill Level de multiplicador para todos los hits cada 200%\n"
        "**Número de golpes:** 1 hit cada 20%, máx. 5 hits\n"
        "**Alcance máximo de Cast:** infinito, limitado a 24m (alcance máximo de objetivo)\n"
        "**Alcance del golpe:** longitud de 100m y anchura de 2m, desde el lanzador hacia el objetivo principal\n\n"
        "**Efecto de la habilidad:**\n"
        "* La habilidad fallará si se lanza al 0%\n"
        "* Esta habilidad tiene chance de ignorar Guard por MAX[0 ; (MCannon Charge - 100)]%\n"
        "* Si el attack cast tiene el mismo Combo Tag que el buff cast, el Combo Tag del attack cast se ignorará\n"
        "* El Combo Multiplier se transfiere desde el buff cast; esto considera si el Combo Tag del attack cast se ignora; el Combo Multiplier total se calcula de la siguiente manera:\n"
        "Magic: Cannon Total Combo Multiplier = Attack Cast Combo Multiplier + Buff Cast Combo Multiplier - 100\n"
        "* ¡Recuerda! De todos los combo tags, solo Bloodsucker(lifesteal) y Mind's eye(siempre Graze/no Miss) no pueden aplicarse en el buff(Charge) cast, pero Bloodsucker after-effect(Spirit = boost dmg), Smite, Save y el resto pueden aplicarse en el buff cast.\n"
        "* Esta habilidad se ve afectada por Concentrate, Long Range passive, Short Range Damage y Long Range Damage stats; la estadística de Long Range Damage se aplicará a toda la habilidad en lugar de Short Range Damage si al menos 1 enemigo golpeado por esta habilidad está a 8m o más del lanzador, independientemente de dónde estén los otros enemigos\n\n"
        "**Efecto del Buff:**\n"
        "* El siguiente cast de Magic: Cannon cuesta 700 MP\n"
        "* Gana carga con el tiempo, 1% de carga cada segundo, se reduce a 1% cada 2 segundos después de alcanzar el 100% de carga.\n"
        "* Solo puede obtener hasta un 200% de carga, después de lo cual no puedes ganar más carga por ningún medio.\n"
        "* Duración del Buff: Hasta que lances Magic: Cannon (attack cast) de nuevo O al recibir daño de Mana Explosion\n"
        "* Si recibes Mana Explosion de enemigos, entonces tu carga con el tiempo permanece sin cambios hasta el 100% (por encima del 100%, se detendrá la carga) y desactiva tu capacidad de ganar % de carga de habilidades mágicas. Afortunadamente, usar esta habilidad eliminará el ailment de Mana Explosion si has sido afectado por él.\n\n"
        "* Usar ciertas habilidades también da carga dependiendo de su Tiempo de Cast Final[segundos], tu Reducción de Tiempo de Cast por tu CSPD y el nivel de esta habilidad.\n"
        "(la explicación se ha trasladado a otro embed más abajo)"
    ),
)

MAGIC_CANNON_EXTRA = (
        "**Mecánica de carga de Magic Cannon**\n"
        "## MODIFICADOR DE CAST SPEED\n\n"
        "> CastSpeedModifier (`CSM%`) es cuánto CSPD acelera el casteo "
        "y afecta la carga de Magic Cannon.\n\n"
        "* **Hasta** 1000 CSPD: *Cada 20 CSPD añade 1* `CSM%`\n"
        "* **Más allá de** 1000 CSPD: *Cada 180 CSPD añade 1* `CSM%`\n"
        "* *`CSM%` tiene un límite del 100% (10.000 CSPD).*\n\n"
        "Las habilidades se dividen en 3 categorías:\n\n"
        "◇ `Habilidades de Cast Instantáneo` (Guardian Beam...)\n"
        "* Si CSPD ≤ 1000: Carga = **80 × CSM%**\n"
        "* Si CSPD > 1000: Carga = **20 + (40 × CSM%)**\n\n"
        "◇ `Habilidades con Tiempo de Cast` "
        "(Magic: Storm, Crash, Arrows...)\n"
        "* Si CSPD ≤ 1000: Carga = "
        "**(Tiempo de Cast × 10) + (80 × CSM%)**\n"
        "* Si CSPD > 1000: Carga = "
        "**20 + (Tiempo de Cast × 10) + (40 × CSM%)**\n\n"
        "◇ `Habilidades sin tiempo de cast pero no \"instantáneas\"` "
        "(Resonance, Enchanted Sword...)\n"
        "* Si CSPD ≤ 1000: Carga = **40 × CSM%**\n"
        "* Si CSPD > 1000: Carga = **10 + (20 × CSM%)**\n\n"
        "### PENALIZACIONES DE CARGA\n\n"
        "> Después de alcanzar el 100% de carga, "
        "todas las habilidades de carga reciben "
        "una penalización de carga x0.5. "
        "Sin embargo, la transición de menos a más del 100% "
        "puede afectar la cantidad cargada.\n\n"
        "### Mecánica de breakpoint\n\n"
        "> Cuando se usa una habilidad por debajo del 100% "
        "pero por encima del breakpoint%, "
        "recibe una penalización reducida de x0.75.\n"
        "> `Breakpoint% = 100% - (Carga de la Habilidad / 2)`\n\n"
        "> Cuando se usa una habilidad por debajo del breakpoint%, "
        "incluso si supera el 100% de carga, "
        "otorga la carga completa prevista, "
        "sin pasar por las penalizaciones del 75% y 50%.\n\n"
        "### Ejemplo\n\n"
        "> *Lanzas Magic: Arrows con 2840 Total CSPD.*\n"
        "> `CSM%` = **50% (de los primeros 1000 CSPD)** "
        "+ ((2840 - 1000)/180 ≈ 10.22%) = **60.22%**\n"
        "> `Carga%` (habilidad con tiempo de cast) = "
        "20 + (0.77 × 10) + (40 × 60.22%) "
        "≈ 20 + 7.7 + 24.09 ≈ 51.79 = **51%**\n\n"
        "`Breakpoint%` = 100 - (51 / 2) = `74%`\n\n"
        "> **Al 73% o menos** ➔ Otorga la **carga completa** (+51%)\n"
        "> **Al 75% o más** ➔ Solo el **75% de la carga** (+38%)\n"
        "> **Al 100% o más** ➔ Solo el **50% de la carga** (+25%)\n\n"
        "**Staff bonus:** Skill Multiplier por hit +BaseINT/100\n"
        "**Magic Device bonus:** "
        "Skill Constant obtenido por carga se triplica\n"
        "**Magic Device bonus:** Anchura +1m\n\n"
        "-\n"
        "El Tiempo de Cast Final es después de la reducción "
        "de CSPD, mburst stack, chain cast, etc.\n"
        "-\n"
        "Lista de todas las habilidades que pueden ganar este % de carga:\n"
        "Todas las Magic Skills, excepto MP Charge, Qadal, Chronos Shift, "
        "Enchanted Barrier y Guardian Beam\n"
        "Priest = Bless, Gloria, Royal Heal, Holy Light, Prayer\n"
        "Magic Blade = Ether Flare y Enchant Sword\n"
        "Wizard = Mana Crystal e Imperial Rays\n"
        "Others = Red Tear (Dark Skills), Punish Ray (Halberd Skills)\n"
        "-\n"
        "La animación de carga de esta habilidad "
        "no se ve afectada por la motion speed del estado del personaje, "
        "pero puede usar el modificador de motion speed "
        "de combo tag \"swift\"."
    )

MAGIC_CRASH = SkillText(
    title="Magic: Crash",
    description="**Descripción del juego:** *\"Invoca 3 pequeños meteoritos. Al golpear al objetivo, cada meteorito puede caer de nuevo hasta 2 veces con poder decreciente, pero una mayor chance de infligir [Armor Break] o [Dizzy].\"*",
    details=(
        "**Habilidad Tier 5;** Sin Restricciones {all}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Mágico\n\n"
        "**Base Skill Multiplier:** (3 + 0.2 * Skill Level) para la primera oleada; (2 + 0.2 * Skill Level) para la segunda oleada; (1 + 0.2 * nivel) para la tercera oleada; multiplicador para cada hit de cada oleada\n"
        "**Base Skill Constant:** 400; constante para cada hit\n"
        "**Número de golpes:** 3 hits para la primera oleada, y hasta 3 hits para cada oleada subsiguiente, hasta un total de 9 hits de las 3 oleadas; el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe:** 1m de radio\n"
        "**Tiempo de Cast base:** 2 segundos; afectado por Cast Speed\n"
        "**Radio de caída:** 1m; todos los hits se lanzan sobre la posición del objetivo todo el tiempo\n"
        "**Hit de intervalo:** 1 meteoro cada 0.7 segundos; los meteoros de la segunda y tercera oleada caen después de aproximadamente 2-2.1 segundos de ser activados por los meteoros respectivos de la primera y segunda oleada.\n\n"
        "(Orden de golpes: Primero 1 > Primero 2 > Primero 3 > Segundo 1 > Segundo 2 > Segundo 3 > Tercero 1 > Tercero 2 > Tercero 3)\n\n"
        "**Chance de Ailment Armor Break:** 10%, x1.5 y x3 en la segunda y tercera oleada\n"
        "**Duración de Armor Break:** 5 segundos\n"
        "**Resistencia de Armor Break:** Ninguna\n\n"
        "**Chance de Ailment Dizzy:** 10%, x1.5 y x3 en la segunda y tercera oleada; válido solo si Armor Break ya está infligido\n"
        "**Duración de Dizzy:** 10 segundos\n"
        "**Resistencia de Dizzy:** Ninguna\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad puede dar un efecto de marca de caída oculta en el objetivo, para que pocos meteoritos caigan sobre ese objetivo marcado. ¡Los meteoritos pueden seguir el movimiento del objetivo, gracias al efecto de marca!\n"
        "* Hay una mayor chance crítica de meteoritos repetidos:\n"
        "* El Meteoro inicial no obtiene ningún bonus crítico.\n"
        "* El Meteoro de la 2da oleada obtiene un 50% de chance de Absolute Critical (separado del cálculo crítico).\n"
        "* El Meteoro de la 3ra oleada obtiene Absolute Critical.\n"
        "* Esta habilidad ignora la mitad de la defensa mágica enemiga ANTES de Magic Pierce%.\n\n"
        "**Staff bonus:** Skill Multiplier por hit de primera oleada +BaseINT/300\n"
        "**Staff bonus:** Chance de ailment x2\n"
        "**Staff bonus:** Alcance del golpe (radio) +0.5m\n"
        "**MD bonus:** Chance de ailment x4\n"
        "**MD bonus:** Alcance del golpe (radio) +1.5m"
    ),
)

RAPID_CHARGE = SkillText(
    title="Rapid Charge",
    description="**Descripción del juego:** *\"Acelera ligeramente MP Charge. (Hasta Lv5). Mejora MATK y Magic Pierce (máx. 50%) que depende de la Cantidad de MP Curado cuando va seguido de la activación de Maximizer. *A partir de Lv6, solo extenderá la duración del buff.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {staff} / {magicdevice}\n"
        "**Efecto Pasivo:**\n"
        "* Reduce MP Charge en (0.2 * Skill Lvl) segundos. Máx. 1 segundo de reducción.\n"
        "* Después de usar MP Charge para Maximizer instantáneo, otorga MATK que depende de la cantidad de mp recuperado de Maximizer y también, depende de tu Magic Pierce% total.\n"
        "Aumento de Flat MATK =\n"
        "> Para Staff = (MP restaurado)/10 + MAX[0 ; MIN((Magic Pierce - 20) * 5 ; 150) - (1500 - MP restaurado)/10]\n"
        "> Para MD = (MP restaurado)/10 + MAX[0 ; MIN((Magic Pierce - 16) * 5 ; 170) - (1700 - MP restaurado)/10]\n\n"
        "* Y, otorga buff de Magic Pierce% solo si no tienes más del 50% de m.pierce.\n"
        "Fórmula =\n"
        "> Para Staff = MAX(0 ; MP restaurado/50 - MAX[0 ; (Magic Pierce - 20)])\n"
        "> Para MD = MAX(0 ; MP restaurado/50 - MAX[0 ; (Magic Pierce - 16)])\n\n"
        "* Duración del Buff de Rapid Charge: MAX[40; 10 * (Skill Level - 1)] segundos\n\n"
        "Esto es complicado la verdad... como staff, si tienes 0% de m.pierce, entonces obtienes 30% de m.pierce de esta habilidad. Sin embargo, a partir del 21% de m.pierce, está limitado al 50%, a cambio de aumentar aún más el MATK. Hasta que tengas más del 50% de m.pierce para que esta habilidad no otorgue buff de m.pierce en absoluto."
    ),
)

ENCHANTED_BARRIERS = SkillText(
    title="Enchanted Barriers",
    description="**Descripción del juego:** *\"Crea una barrera para protegerte. Si estás dentro de la barrera, el daño será absorbido. Además, no te estremecerás mientras casteas y el aggro del consumo de MP se reducirá. Restaurar MP dentro de la barrera restaurará el HP de la barrera también.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {staff} / Main {magicdevice}\n"
        "**Coste MP:** 400\n\n"
        "**Efecto de la habilidad:**\n"
        "* Al usar esta habilidad, coloca una barrera en tu posición con radio de 2.5m. Esta barrera durará hasta que el HP de la Barrera llegue a 0.\n\n"
        "* Reutilizar esta habilidad no refrescará el HP de la Barrera (solo cambia su posición). Para recuperar HP de la Barrera, necesitas recuperar mp (excepto para el efecto de Maximizer instantáneo de E.barrier > Maximizer) dentro de la barrera. Fórmula = Floor(+1% HP de la Barrera * Barra de MP).\n"
        "Nota: Reutilizar esta habilidad cuando tu valor de HP de la Barrera ya está en 0, es decir... la barrera desapareció antes, aún coloca una barrera en tu posición, pero tu valor está al 1% de HP.\n\n"
        "* Esta barrera solo puede protegerte de cualquier daño mientras tenga HP de la Barrera y estés dentro de esta barrera.\n"
        "> HP de la Barrera = MAX[100 ; (Base Main Weap ATK * Base Main Weap Stability% * (TotalINT / 7.5) * (1 + MaxHP%) + Flat MaxHP)]\n"
        "Los modificadores de MaxHP (MaxHP % y flat; no VIT) que afectan a HP de la Barrera: equipamiento, avatares, equipamiento de gremio, consumibles, cocina de MaxHP, registlet.\n\n"
        "* Esta habilidad tiene Reducción de Daño Porcentual, que reduce el daño recibido en (25 + Skill Level * 5)%, independientemente de cuánto HP de la Barrera tuvieras.\n"
        "* Luego, después de ese porcentaje, la Reducción de Daño Plana toma lugar y su valor de absorción según el rango de ataque del enemigo. Absorberá ya sea 50% de daño (SRD/0-7m distancia entre jugador y enemigo) o 100% de daño (LRD/+8m distancia entre jugador y enemigo).\n"
        "Y esa parte de arriba es donde se pierde 1 HP de la Barrera por cada 1 Valor de Reducción Plana usado para absorber. Sin embargo, si no tienes suficiente HP de la Barrera, entonces convierte todo el HP de la Barrera actual en valor de reducción plana para absorber y… tu Barrera desaparecerá.\n"
        "* A partir de la actualización del 24 de abril de 2025, cualquier daño fraccional reducido de la Barrera saltará el 1er paso de reducción de daño (la reducción de daño porcentual) e irá directamente al 2do paso de reducción de daño (reducción de daño plana); esto significa, cualquier/todo daño fraccional reducido de la Barrera, te costará HP de la Barrera (sin reducción gratuita de hasta el 75% de daño como el daño físico/mágico).\n\n"
        "Se confirma que esta reducción de daño de la habilidad tiene lugar después de Cover (Pet Skills)... por lo tanto, esta habilidad debe estar al final del cálculo de daño recibido, y está antes de \"Cosas especiales que te salvan de la muerte como Guard Power Break, Saber Aura, Magic Skin, etc.\"\n\n"
        "**Efecto del Buff:**\n"
        "* Mientras estés dentro de esta Barrera, al usar cualquier habilidad de ataque de Magic Skills teniendo mburst aprendido, ganarás +2 mburst stacks por cada habilidad de ataque de Magic Skills usada en lugar de +1 mburst stack.\n"
        "* El Tiempo de Cast de Magic: Finale dentro de esta Barrera se acortará en 1 segundo.\n"
        "* Eres inmune a \"Magic Flinch\" mientras estés dentro de esta Barrera.\n\n"
        "* Mientras estés dentro de esta Barrera, esta barrera puede reducir el Aggro de Todas las Habilidades en MIN[75% ; (1 - 1/Coste de Barra de MP Base)]. Provoke no se ve afectado por esta reducción de aggro, ya que Provoke solo genera aggro fijo, no aggro de mp.\n"
        "NOTAS: El aumento de aggro no se acumula con las estadísticas de aggro% aditivamente pero se acumulan multiplicativamente. Incluso multiplicativamente con el Multiplicador de Aumento de Aggro% de Guardian.\n\n"
        "Ej.:\n"
        "1mp skill = 1mp aggro(-0%)\n"
        "2mp skill = 1mp aggro(-50%)\n"
        "3mp skill = 1mp aggro(-66%)\n"
        "4mp skill = 1mp aggro(-75%)\n"
        "5mp skill = 1.25mp aggro(-75%)\n"
        "7mp skill = 1.75mp aggro(-75%)\n"
        "16mp skill = 4mp aggro(-75%)\n\n"
    ),
)

ENCHANTED_BARRIERS_EXTRA = (
    "* Tu animación será más rápida mientras estés dentro de esta Barrera. "
    "Se estima que la fórmula es +((2 + 0.5[si tienes 1k ASPD]) * Skill Level)% Motion Speed\n\n"
    "* Tu Maximizer mientras estés dentro de esta Barrera, "
    "se volverá insta cast y recuperará MP, este dura hasta que uses Maximizer. "
    "Puedes relanzar esta habilidad y obtener este Maximizer insta cast de nuevo. "
    "[Esto está demasiado roto... podría ser un bug? "
    "Aun así... puedes usar Maximizer instantáneo fuera de esta barrera, pero sin ganancia de MP?!?]\n\n"
"* Mientras estés dentro de esta Barrera, "
    "si al usar Qadal tu carga superaría el 100% inmediatamente, "
    "en lugar de alcanzar el 99% (es decir, necesita ser menos del 99%), "
    "entonces esta Barrera mantendrá tu Qadal al 99% de carga "
    "(evita que tu Qadal supere el 100% de carga) "
    "y ese Qadal aún otorga los buffs de mp a la mitad/crítica del 100%, "
    "pero a cambio de esa prevención, tu HP de la Barrera actual se reducirá a la mitad.\n\n"
    "Nota: Mientras estés dentro de esta barrera si usas Qadal al 99% de carga "
    "(o digamos que esta barrera ya evitó que Qadal supere el 100% de carga antes), "
    "entonces aún recibes uno de los siguientes 4 efectos "
    "(Full Recovery, Stun, Sleep, Dead) tan pronto como uses Qadal "
    "(incluso si esperas a que termine el temporizador del buff de Qadal de 3 min). "
    "Afortunadamente, solo asegúrate de que E.barrier no haya evitado que tu Qadal supere el 99% "
    "y espera a que termine el temporizador del buff de Qadal, "
    "entonces puedes empezar Qadal de nuevo desde cero "
    "mientras mantienes la duración de batalla de Qadal intacta."
)

MAGIC_KNIFE = SkillText(
    title="Magic Knife",
    description="**Descripción del juego:** *\"Envía dagas mágicas para contener al enemigo. Esta habilidad tiene \"proration de ataque normal\". Garantiza un golpe con una pequeña cantidad de MP recuperado. Ataque adicional con proration de ataque normal aumenta cuando llega a Lv10.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {staff}\n"
        "**Coste MP:** 0\n"
        "**Tipo de daño:** Físico\n"
        "**Elemento:** Neutral\n\n"
        "**Base Skill Multiplier (Primeros 4 Hits):** MIN[0.6 + 0.1 * Skill Level; 1.5]; multiplicador total de todos los hits\n"
        "**Base Skill Constant (Primeros 4 Hits):** 0; constante total de todos los hits\n"
        "**Base Skill Multiplier (Último Hit):** 1.5\n"
        "**Base Skill Constant (Último Hit):** 0\n"
        "**Alcance máximo de Cast:** 8m\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad sigue la mecánica física (basada en ATK, Critical Rate física y Daño Crítico físico)\n"
        "* Esta habilidad tiene atributo Perfect Aim\n"
        "* Esta habilidad inflige Proration Normal. Pero si esta habilidad era nivel 10, entonces inflige 2x Proration Normal\n"
        "* En nivel 1-9, solo hace los 4 primeros hits, sin el último hit. Luego en nivel 10, hará los 4 primeros hits y el último hit.\n"
        "* Primeros 4 Hits, cada hit recupera (3 + Floor((Min[SLv ; 9] - 1)/3)) MP, mientras que la recuperación de MP del Último Hit es cuatro veces mas que cada hit. Nota: debe golpear, sin Evasion para obtener ese MP, tampoco recuperará mp si golpea a un objetivo que ya murió\n"
        "* Sin Tiempo de Cast\n\n"
        "Si los Primeros 4 Hits de esta habilidad resultan en Evasion, entonces el Último Hit no caerá/activará.\n"
        "Esta habilidad no otorga stack de Magic: Burst"
    ),
)

QADAL = SkillText(
    title="Qadal",
    description="**Descripción del juego:** *\"Una técnica prohibida que pone una pesada carga en la mente y el cuerpo. Consume HP actual y Max HP (valor aleatorio) para reducir a la mitad el Coste MP de la siguiente habilidad usada y garantizar crítico. Si la carga se vuelve demasiado pesada por el uso repetido, entonces…\"*",
    details=(
        "**Habilidad Tier 3;** Solo {staff}\n"
        "**Coste MP:** 200\n\n"
        "**Efecto de la habilidad:**\n"
        "* Usar esta habilidad consumirá tu HP en un 10% de tu HP actual\n"
        "* Si tu habilidad previamente lanzada es esta habilidad, entonces usar esta habilidad de nuevo solo costará MP, sin buff ni efecto.\n\n"
        "**Efecto del Buff:**\n"
        "* Duración del Buff: 180 segundos\n\n"
        "* Usar esta habilidad dará buff para que la siguiente habilidad tenga su Coste MP dividido a la mitad y redondeado al múltiplo de 100 más cercano (ej. 300/2 = 150 → 200 MP; 600/2 = 300 → 300 MP). También otorga buff de Absolute Critical para la siguiente habilidad (incluso habilidades físicas). Estos buffs de mp a la mitad y Absolute Critical terminarán cuando uses cualquier habilidad.\n\n"
        "* El debuff de MaxHP es el mismo que (QadalCharge%). Ej.: si tienes Qadal Charge 90%, entonces obtienes -90% MaxHP\n\n"
        "* Usar esta habilidad dará Qadal Charge aleatoriamente entre (MAX[30 - Floor(TotalDex/25); 10])% y (100 - 5 * Skill Level - Floor(BaseDex/25))%.\n\n"
        "* Si alcanzas más de Qadal Charge 100% al usar esta habilidad y no obtienes \"Full Recovery\", entonces esta habilidad no te dará los buffs de Absolute Critical y mp a la mitad, y obtendrás uno de los siguientes:\n"
        "1. [Full Recovery = obtener mp completo e invencibilidad 2 segundos] (probabilidad rara)\n"
        "2. [1HP Stunned]\n"
        "3. [1HP Sleep]\n"
        "4. [Dead]\n"
        "> - Skill Level puede afectar su probabilidad: menor probabilidad de muerte, probabilidad de sleep ligeramente menor, aumenta la probabilidad de stun, aumenta ligeramente la probabilidad de iframe.\n\n"
        "[Pero ten en cuenta, estos son RNG, no hay números confirmados/exactos, así que tómalo con pinzas. Por cierto, probé lv 1, seguía muriendo a menudo y ocasionalmente sleep, rara vez stun, nunca iframe pero quizá probabilidad ínfima. También, tener mayor LUK parece aumentar la probabilidad de obtener \"full recovery\" y menor probabilidad de sleep, aparentemente se espera que 255 LUK = +10% aunque]\n\n"
        "**Efecto Pasivo:**\n"
        "* Esta habilidad tiene una pasiva que aumenta el daño de **Todas las Habilidades de Magic Skills** según la duración de batalla y tu Qadal Charge. Esta pasiva funciona mientras tengas el temporizador del Buff de Qadal ACTIVADO y no debes tener \"Buff de MP a la mitad y CR de Qadal\". Cuanto más tiempo luchas = mayor bonus de daño.\n\n"
        "* La Duración de Batalla comenzará a contar tan pronto como te enfrentes/luches contra el objetivo (no necesitas activar Qadal al inicio).\n"
        "Y la duración de batalla se reiniciará SI:\n"
        "*  \"Tu grupo mató a cualquier objetivo solo en mapas que no son de Boss (incluso si hay otro objetivo vivo... Mientras tanto, en el mapa de Boss, la duración de batalla continúa contando, incluso cuando matas a un súbdito, este sigue contando hasta el final de la pelea)\"\n"
        "*  O \"no queda ningún objetivo\"\n"
        "*  O \"sales del mapa\"\n"
        "*  O \"te noquean\"\n\n"
        "* Aumenta el Daño Infligido de las habilidades de Magic Skills = +1% cada 3 segundos de batalla independientemente de Skill Level.\n"
        "Este bonus de Daño Infligido no puede exceder Qadal Charge% independientemente de Skill Level. (Aplicado multiplicativamente al final del cálculo de daño después de sumarse junto con el bonus de Brave Aura y la reducción de Mana Recharge)\n\n"
    ),
)

QADAL_EXTRA = (
    "Efecto oculto: Qadal tiene otra pasiva que podría ser un bug o incluso una característica???.... Bueno, hasta que se demuestre lo contrario\n"
    "Aparentemente, Qadal puede reducir tu Tiempo de Revive Final en 1 segundo por cada 1 Segundo de Duración de Batalla. Pero si la Duración de Batalla se reinicia, entonces, por supuesto, la Reducción de Tiempo de Revive Final también se reiniciará. Ya que tiene este efecto oculto, entonces, por supuesto, obtendrás una desventaja que es que tu Tiempo de Revive Base se incrementará en 150 segundos. "
    "[Nota: combínalo con Play Dead lv10 (que reduce el Tiempo de Revive Base en 150s) y tu Tiempo de Revive Base volverá a ser de 300 segundos].\n"
    "Nota: Si no mueres de la forma normal, por ejemplo, mueres por muerte de Qadal (incluso muriendo por sleep o stun) o muerte por Regretless… tu Tiempo de Revive Base se establece en 300 segundos y no hay Reducción de Tiempo de Revive Final por Duración de Batalla.\n\n"
    "*※ Este buff de Absolute Critical parece bugueado "
    "[o es una característica?] bueno por ahora "
    "(esta habilidad registra el buff lentamente "
    "si eres lo suficientemente rápido o tienes max motion, "
    "problema muy habitual = la siguiente habilidad después de Qadal "
    "a veces/siempre falla al obtener el buff de Qadal mientras está en combo).\n"
    "~~※ Si hay ataques en curso como Magic: Arrow/Storm/Crash "
    "entre Qadal y la siguiente habilidad, "
    "entonces puede fallar al dar buff a la siguiente habilidad "
    "ya que se desperdicia en ataques en curso.~~ "
    "**BUG ARREGLADO = ya no se desperdicia en ataques en curso**\n"
    "~~※ Este buff de Absolute Critical puede afectar DoT "
    "(como Nemesis) solo si no haces ninguna habilidad "
    "durante ese tiempo de DoT. "
    "De lo contrario, ese DoT no recibirá el Buff de Crítico Absoluto.~~ "
    "**BUG ARREGLADO = DoT aún recibe su buff después de hacer cualquier habilidad**"
)

SPELL_CALIBRATION = SkillText(
    title="Spell Calibration",
    description="**Descripción del juego:** *\"Puedes usar las habilidades desde el Menú de Habilidades. La habilidad para ajustar la magia según tus necesidades. Te permite ajustar ciertas Magic Skills hasta Skill Tree Tier 3. * No afecta a Enchanted Spell.\"*",
    details=(
        "**T4; [Ex Skill]** Solo {staff} / Main {magicdevice}\n\n"
        "**Punto de Ajuste:** 2 (si Skill Tree es Tier 5) + Skill Level\n"
        "**Coste de Punto de Ajuste:** 1 por ajuste. Si eliges dos ajustes para la misma habilidad, el segundo ajuste te costará 3 puntos de ajuste.\n\n"
        "{arrows} **Magic: Arrows**\n"
        "**Critical:** Garantiza un golpe crítico.\n"
        "**Double Shot:** Desata dos disparos a la vez. El total de golpes sigue siendo el mismo.\n\n"
        "{javelin} **Magic: Javelin**\n"
        "**Normalize:** Los ataques normales ahora tienen proration. Attack MP Recovery se aplica al golpear con éxito. (* la habilidad inflige proration normal pero aún usa proration mágica; y recupera el 100% de Attack MP Recovery del personaje al golpear).\n"
        "**Retry:** Activa la habilidad una vez más si falla al infligir un ailment.\n\n"
        "{wall} **Magic: Wall**\n"
        "**Follow:** Despliega la habilidad a tu alrededor. Sin embargo, ya no hará Knockback a los enemigos. El área de Magic: Wall te seguirá.\n"
        "**Extension:** Triplica la duración.\n\n"
        "{lances} **Magic: Lances**\n"
        "**Quick Shot:** Dispara el proyectil más rápido\n"
        "**Penetration:** Gana Magic Pierce igual a la probabilidad de infligir Stop.\n\n"
        "{blast} **Magic: Blast**\n"
        "**Single:** Ahora apunta a un solo enemigo y el tiempo de cast se reduce ligeramente. Tiempo de Cast base -1s.\n"
        "**Quick Spell:** Reduce la probabilidad de infligir un ailment (- Chance Base de Ailment * 75%? necesita más pruebas por RNG) para reducir el tiempo de cast. Tiempo de Cast base -2s.\n"
        "* Cuando ambas calibraciones de Magic: Blast están activadas, Tiempo de Cast base -3s.\n\n"
        "{impact} **Magic: Impact**\n"
        "**Next Q(uick):** En lugar de reducir el coste de MP a la mitad, se aplicará un efecto swift a la siguiente habilidad.\n"
        "**Reinforce:** Aumenta el poder (Multiplicador +2,5), alcance (+1m) y probabilidad de infligir [Tumble] (+35%). No aplicable cuando se usa consecutivamente (no funciona cuando el Buff de Impact está activo).\n\n"
        "{storm} **Magic: Storm**\n"
        "**Condensation:** Reduce su alcance a la mitad para aumentar su poder.\n"
        "Magic: Storm's base skill multiplier * 2\n"
        "**Induction:** La duración (segundos) cambia a número de golpes, y ahora perseguirá lentamente al objetivo hasta que se alcance el número de golpes (depende de Skill Level de Magic: Storm). Golpear múltiples objetivos consumirá la cuota de golpes (ej. cuando Magic: Storm nivel 10 golpea 6 objetivos a la vez, la habilidad terminará inmediatamente; mientras tanto, si Storm tiene 1 golpe restante y golpea 3 objetivos, todos los objetivos serán golpeados antes de que la habilidad termine).\n\n"
        "{guardianbeam} **Magic: Guardian Beam**\n"
        "**Counter:** Ahora se activa incluso cuando recibes daño.\n"
        "**Long-Range:** Los stacks consumidos se duplican para aumentar el rango de activación de los ataques mágicos.\n\n"
    ),
)

MAGIC_LASER = SkillText(
    title="Magic: Laser",
    description="**Descripción del juego:** *\"Una técnica para simplificar la magia y liberar su poder con la habilidad del lanzador. El poder aumenta según el MP restante cuando se activa. Baja probabilidad de infligir un ailment (elemento del arma). Después de la activación, tu Magic Pierce aumenta ligeramente.\"*",
    details=(
        "**T5; [Activo]** Solo {ohs}/{staff}/Main {magicdevice}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Mágico\n\n"
        "> **Base Skill Multiplier:** 0.75 * Skill Level + MIN(ROUNDDOWN(barra de mp restante después del láser; 0); 10)/2\n"
        "> **Base Skill Constant:** 0\n"
        "**Alcance máximo de Cast:** 21m\n\n"
        "**Efecto del Buff:** Magic Pierce +10% (+5% más con staff)\n"
        "**Duración del Buff:** 10 segundos\n\n"
        "**Ailment:** Stop (con elemento Neutral); Bleed (con elemento Fire); Dizzy (con elemento Water); Lethargy (con elemento Wind); Silence (con elemento Earth); Dazzled (con elemento Light); Curse (con elemento Dark)\n"
        "**Chance de Ailment:** 2% * Skill Level\n"
        "**Resistencia a Ailment:** 10 segundos\n\n"
        "Esta habilidad se ve afectada por short/long range damage; afectada por long range skill; usa e inflige proration mágica.\n\n"
        "**Staff Bonus:** Aumenta ligeramente el aumento de Magic Pierce.\n"
        "**Magic Device Bonus:** La probabilidad de infligir un ailment es 1.5 veces mayor.\n"
        "**OHS Penalty:** La probabilidad de infligir un ailment se reduce a la mitad."
    ),
)
