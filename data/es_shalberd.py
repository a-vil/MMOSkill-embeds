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


FLASH_STAB = SkillText(
    title="Flash Stab",
    description="**Descripción del juego:** *\"Ataca con fiereza a un enemigo con un movimiento rápido.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {ohs} / {halberd}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 50 + 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n\n"
        "**Efecto de la habilidad:** Esta habilidad tiene un boost de Motion Speed de +50%\n\n"
        "**Penalidad OHS:** Motion Speed boost -25%"
    ),
)

CANNON_SPEAR = SkillText(
    title="Cannon Spear",
    description="**Descripción del juego:** *\"Ataca a un enemigo lanzando la alabarda. El alcance aumenta a medida que la habilidad sube de nivel.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {halberd}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 0.4 + 0.01 * Skill Level\n"
        "**Base Skill Multiplier (Toss):** 1.5 + 0.1 * Skill Level\n"
        "**Base Skill Constant (Primer Hit):** 100 + 10 * Skill Level\n"
        "**Base Skill Constant (Toss):** 100 + 10 * Skill Level\n"
        "**Número de golpes:** 2 hits; el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n"
        "**Alcance del golpe (Toss):** Longitud de 8m (niveles 1 y 2)/ 9m (niveles 3 y 4)/ 10m (niveles 5 y 6)/ 11m (niveles 7 y 8)/ 12m (niveles 9 y 10); radio de 1m (niveles 1 a 5)/ 2m (niveles 6 a 10); desde la posición del lanzador\n\n"
        "El buff a la constante de Triple Thrust's se divide entre 2"
    ),
)

DRAGON_TAIL = SkillText(
    title="Dragon Tail",
    description="**Descripción del juego:** *\"Gira la alabarda y barre a los enemigos. Chance de infligir [Tumble]. No puede infligir Tumble en monstruos Boss.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {halberd}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 0.7 + 0.03 * Skill Level\n"
        "**Base Skill Multiplier (Segundo Hit):** 2 + 0.2 * Skill Level\n"
        "**Base Skill Constant (Primer Hit):** 100\n"
        "**Base Skill Constant (Segundo Hit):** 50 + 15 * Skill Level\n"
        "**Número de golpes:** 2 hits; el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** Infinito (pero necesita un objetivo para lanzar)\n"
        "**Alcance del golpe (Primer Hit):** 1.5m (niveles 1 a 5); 2m (niveles 6 a 10); alrededor del lanzador\n"
        "**Alcance del golpe (Segundo Hit):** 2.5m (niveles 1 a 3); 3m (niveles 4 a 6); 3.5m (niveles 7 a 9); 4m (nivel 10); alrededor del lanzador\n\n"
        "**Efecto del Buff:** Reduce el daño recibido mientras la habilidad está activa. No puede reducir daño fraccional\n"
        "**Efecto del Buff:**\n"
        "* Durante la animación de \"Número de golpes = 1\", recibirás 50% de daño una vez\n"
        "* Durante la animación de \"Número de golpes = 2\", recibirás (100 - 10 * Skill Level)% de daño una vez\n\n"
        "**Ailment:** Tumble\n"
        "**Chance Base de Ailment:** (10 * Skill Level)% en mobs; 0% en jefes\n"
        "**Duración de Ailment:** 3 segundos\n"
        "**Resistencia a Ailment:** 3 segundos\n\n"
        "El buff a la constante de Triple Thrust's se divide entre 2"
    ),
)

DIVE_IMPACT = SkillText(
    title="Dive Impact",
    description="**Descripción del juego:** *\"La alabarda perfora la tierra con el tiempo. Genera una explosión masiva e inflige daño adicional después de un momento con chance de infligir [Dazzled] al activar la habilidad.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {halberd}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 2 + 0.2 * Skill Level + TotalSTR/250\n"
        "**Base Skill Multiplier (Segundo Hit):** 2 + 0.4 * Skill Level + TotalINT/100\n"
        "**Base Skill Constant (Primer Hit):** 200 + 20 * Skill Level\n"
        "**Base Skill Constant (Segundo Hit):** 0\n"
        "**Número de golpes:** 2 hits; el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n"
        "**Alcance del golpe (Primer Hit):** (2.5 + 0.25 * SkillLvl)m; alrededor del lanzador\n"
        "**Alcance del golpe (Segundo Hit):** (4.5 + 0.25 * SkillLvl)m; alrededor de la posición del lanzador al lanzar la habilidad\n\n"
        "**Efecto de la habilidad:** El segundo hit detonará después de 4 segundos\n\n"
        "**Ailment del Segundo Hit:** Dazzled\n"
        "**Chance de Ailment del Segundo Hit:** (10 * Skill Level)%\n"
        "**Duración de Ailment del Segundo Hit:** 10 segundos\n"
        "**Resistencia a Ailment del Segundo Hit:** 30 segundos\n\n"
        "**Efecto del Buff:** Invincibilidad\n"
        "**Duración del Buff:** 3 segundos o hasta que el lanzador toque el suelo\n\n"
        "La Motion Speed de esta habilidad es fija. Por lo tanto, los swift tags y mspd% no afectan la velocidad de esta habilidad\n"
        "El buff a la constante de Triple Thrust's se divide entre 2\n"
        "Esta habilidad es afectada por Whack en ambos hits, sin embargo, solo el primer hit es afectado por los modificadores de Short Range Damage/Long Range Damage"
    ),
)

DRAGON_TOOTH = SkillText(
    title="Dragon Tooth",
    description="**Descripción del juego:** *\"Salta hacia un objetivo y ataca. Después de usar la habilidad, volverás a tu posición original. Tiene alta Ignorancia de Defensa y Critical Rate pero no tiene bonus de poder.\"*",
    details=(
        "**Habilidad Tier 4;** Solo {halberd}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 0.75 * Skill Level\n"
        "**Base Skill Multiplier (Segundo Hit):** 7.5\n"
        "**Base Skill Constant:** 0; constante para cada hit\n"
        "**Número de golpes:** 2 hits; el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe:** Objetivo único, pero tiene un radio de 0.5m + el rango máximo de Auto Attack del arma; alrededor de la posición de aterrizaje del lanzador\n\n"
        "**Efecto de la habilidad:**\n"
        "* Hace que el lanzador salte hacia la posición actual del enemigo y regrese; la velocidad del salto está determinada por Motion Speed y la distancia\n"
        "* Niega Flinch, Tumble y Stun durante la animación de la habilidad\n"
        "* Esta habilidad tiene Critical Rate +65 + (Skill Level) y Physical Pierce +(10 * Skill Level)%\n\n"
        "Si tu punto de aterrizaje (desde el jugador hasta la posición del enemigo) está por encima de (0.5m + el rango de autoataque del arma), esta habilidad no infligirá daño"
    ),
)

DEADLY_SPEAR = SkillText(
    title="Deadly Spear",
    description="**Descripción del juego:** *\"Clava con precisión a un enemigo e inflige daño fatal. Tarda tiempo en activarse, sin embargo, ignora cierta cantidad de defensa y tiene una alta chance de infligir daño crítico.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {ohs} / {halberd}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1.2 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 80 + 3 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n"
        "**Tiempo de carga base:** 1.5 segundos (nivel 1); 1 segundo (niveles 2 a 4); 0.5 segundos (niveles 5 a 7); ninguno (niveles 8 a 10)\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad tiene Critical Rate +(+300% Total Crit Rate boost). Que es 4x tu Critical Rate total.\n"
        "* Esta habilidad tiene Physical Pierce +10% (niveles 1 a 3)/ +15% (niveles 4 a 6)/ +20% (niveles 7 a 9)/ +25% (nivel 10)\n"
        "* El coste de MP de la siguiente habilidad se reduce a la mitad si esta habilidad hace un hit crítico\n\n"
        "**Penalidad OHS:** Skill Multiplier -0.2\n"
        "**Penalidad OHS:** Critical Rate boost de la habilidad -2.5"
    ),
)

PUNISH_RAY = SkillText(
    title="Punish Ray",
    description="**Descripción del juego:** *\"Lanza una magia usando la alabarda como si fuera un bastón. Inflige daño mágico afectado por ATK. La Critical Rate de la siguiente habilidad aumenta.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {ohs} / {halberd}\n"
        "**Coste MP:** 0\n"
        "**Tipo de daño:** Físico/Mágico\n"
        "**Elemento:** Neutral\n\n"
        "**Base Skill Multiplier:** 0.25 + 0.01 * Skill Level² + TotalINT/400\n"
        "**Base Skill Constant:** 0\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Tiempo de Cast Base:** 2 segundos; afectado por Cast Speed\n\n"
        "**Efecto de la habilidad:** Esta habilidad calcula el daño base como si fuera una habilidad física, pero el resto del cálculo de daño como si fuera una habilidad mágica; la habilidad otorga proration mágica\n\n"
        "**Efecto del Buff:** Otorga un boost de Critical Rate para las siguientes tres habilidades;\n"
        "(15 * Skill Level) para la primera,\n"
        "(10 * Skill Level) para la segunda y\n"
        "(5 * Skill Level) para la tercera\n"
        "**Duración del Buff:** Hasta que se use una habilidad\n\n"
        "**Halberd bonus:** Skill Multiplier se duplica\n"
        "**Penalidad OHS:** Critical Rate boost para la primera habilidad se divide entre 1.5\n"
        "**Penalidad OHS:** Critical Rate boost para la segunda habilidad se reduce a la mitad\n"
        "**Penalidad OHS:** Critical Rate boost para la tercera habilidad se reduce a la mitad\n"
        "Esta habilidad no puede usarse como la primera habilidad de un combo"
    ),
)

STRIKE_STAB = SkillText(
    title="Strike Stab",
    description="**Descripción del juego:** *\"Clava a un enemigo con un movimiento rápido. El daño aumenta si el objetivo tiene un ailment. Tiene baja chance de hacer crítico.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {ohs} / {halberd}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1.9 + 0.01 * Skill Level + TotalSTR/500; multiplicador para cada hit\n"
        "**Ailment Bonus Skill Additional Multiplier:** 0.1 * Skill Level\n"
        "**Base Skill Constant:** 100; constante para cada hit\n"
        "**Número de golpes:** 3 hits; el cálculo de daño se realiza una vez y se copia a los otros hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad tiene una penalidad base de Critical Rate de (5 * Skill Level)%;\n"
        "la penalidad se aplica de la siguiente manera:\n"
        "Strike Stab Crit Rate = (25 + CRT/3.4) * (1 - penalidad base de Crit Rate/100) * (1 + Crit Rate%/100) + Flat Crit Rate\n"
        "* Si esta habilidad golpea a un objetivo con un ailment, el Ailment Bonus Skill Multiplier se añade al Base Skill Multiplier\n\n"
        "**Halberd bonus:** Ailment Bonus Skill Multiplier se duplica\n"
        "**Halberd bonus:** Skill Constant +100\n"
        "**Penalidad OHS:** Base Critical Rate se reduce a la mitad, cambiando la fórmula de penalidad a:\n"
        "Strike Stab Crit Rate = (25 + CRT/3.4) * (1 - penalidad base de Crit Rate/100) * (1 + Crit Rate%/100)/2 + Flat Crit Rate"
    ),
)

CHRONOS_DRIVE = SkillText(
    title="Chronos Drive",
    description="**Descripción del juego:** *\"Repite el hecho de que has penetrado un objetivo. Añade un efecto que inflige daño adicional durante unos segundos.\"*",
    details=(
        "**Habilidad Tier 4;** Solo {halberd}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.5 * Skill Level; multiplicador total de todos los hits\n"
        "**Base Skill Constant:** 40 * Skill Level\n"
        "**Número de golpes:** 3 hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n\n"
        "**Efecto de la habilidad:** El objetivo recibe golpes adicionales con el tiempo\n"
        "**Duración del Efecto de la habilidad:** 5 segundos (niveles 1 y 2); 6 segundos (niveles 3 y 4); 7 segundos (niveles 5 y 6); 8 segundos (niveles 7 y 8); 9 segundos (nivel 9); 10 segundos (nivel 10)\n\n"
        "**Chronos Drive Additional Damage Type:** Físico/Mágico\n"
        "**Chronos Drive Additional Skill Multiplier:** 0.4 + 0.01 * Skill Level + TotalINT/500\n"
        "**Chronos Drive Additional Skill Constant:** 250 + 25 * Skill Level\n"
        "**Chronos Drive Additional Hit Count:**\n"
        "Delay entre hits = Delay de autoataque + 1.5 * Animation Time Modifier de Chronos Drive/100\n"
        "Número de golpes = Duración del Efecto de la habilidad/Delay entre hits\n"
        "* Los chequeos de hit/miss, evasion, graze y critical se copian de la habilidad para todos los hits; el resto del cálculo de daño se realiza para cada hit\n"
        "**Chronos Drive Additional Hit** puede recuperar 30 MP por cada 1 hit\n\n"
        "El delay no es afectado por los modificadores de Motion Speed en Chronos Drive\n"
        "Los golpes extra usan proration mágica (lo que significa que el daño se basa en Proration Mágica pero no inflige Proration Mágica), pero el resto del cálculo de daño se realiza como si fueran habilidades físicas\n"
        "Los golpes extra no son afectados por combo tags, Whack ni los modificadores de Short Range Damage/Long Range Damage"
    ),
)

HALBERD_MASTERY = SkillText(
    title="Halberd Mastery",
    description="**Descripción del juego:** *\"Mejora el uso de alabardas. ATK aumenta al equipar una alabarda.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {halberd}\n\n"
        "**Efecto Pasivo:**\n"
        "* Weapon ATK +(3 * Skill Level)%\n"
        "* ATK +1% (niveles 1 y 2)/ +2% (niveles 3 a 7)/ +3% (niveles 8 a 10)"
    ),
)

CRITICAL_SPEAR = SkillText(
    title="Critical Spear",
    description="**Descripción del juego:** *\"Aprende el dominio de las alabardas. Critical Rate aumenta al equipar una alabarda.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {halberd}\n\n"
        "**Efecto Pasivo:**\n"
        "* Critical Rate +0% (nivel 1)/ +1% (niveles 2 y 3)/ +2% (niveles 4 y 5)/ +3% (niveles 6 y 7)/ +4% (niveles 8 y 9)/ 5% (nivel 10) y Critical Rate +1 (niveles 1 y 2)/ +2 (niveles 3 y 4)/ +3 (niveles 5 y 6)/ +4 (niveles 7 y 8)/ +5 (niveles 9 y 10)"
    ),
)

QUICK_AURA = SkillText(
    title="Quick Aura",
    description="**Descripción del juego:** *\"Aumenta tu velocidad con el espíritu de lucha. Activa habilidades consumiendo HP en lugar de MP. Aumenta ASPD durante un cierto período de tiempo.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 0\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto de la habilidad:** Esta habilidad consumirá el 15% de tu MaxHP actual para activarse; si no tienes suficiente HP, te quedará 1 HP pero los efectos del buff se reducirán a los del Skill Level 1\n\n"
        "**Efecto del Buff:** Attack Speed +(2.5 * Skill Level)% y +(50 * Skill Level)\n"
        "**Duración del Buff:** 3 minutos\n\n"
        "**Halberd bonus:** Consumo de MaxHP -5%\n"
        "**Halberd bonus:** Duración del Buff +2 minutos\n"
        "Esta habilidad no puede usarse como la primera habilidad de un combo"
    ),
)

WAR_CRY_OF_STRUGGLE = SkillText(
    title="War Cry of Struggle",
    description="**Descripción del juego:** *\"El rugido de la vida en una situación crítica. Restaura un poco de MP. La cantidad de restauración de MP aumenta cuanto más bajo sea el HP actual.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Tiempo de carga base:** 5 segundos (niveles 1 a 3); 4 segundos (niveles 4 a 6); 3 segundos (niveles 7 a 9); 2 segundos (nivel 10)\n\n"
        "**Efecto de la habilidad:**\n"
        "* Cuando la habilidad se lanza con éxito, restaura 120 MP\n"
        "* Si la habilidad se lanza cuando tu HP está al 85% o menos, aumenta el MP restaurado en (2 * Skill Level) MP\n"
        "* Si la habilidad se lanza cuando tu HP está al 70% o menos, aumenta el MP restaurado en (4 * Skill Level) MP\n"
        "* Si la habilidad se lanza cuando tu HP está al 55% o menos, aumenta el MP restaurado en 20 + (10 * Skill Level) MP\n"
        "* Todos los efectos dependientes del HP se acumulan y se añaden a la cantidad total de MP restaurado\n\n"
        "**Halberd bonus:** Tiempo de carga -1 segundo\n"
        "Esta habilidad no puede usarse en un combo"
    ),
)

GODSPEED_WIELD = SkillText(
    title="Godspeed Wield",
    description="**Descripción del juego:** *\"Consume MaxMP y se puede acumular hasta 3 veces como máximo. Mejora ASPD/Action Speed/Evasion Recharge durante un corto período de tiempo y disminuye enormemente la Physical y Magic Resistance. El efecto termina al recibir daño.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto de la habilidad:** Cada vez que usas la habilidad, añades un stack al buff; el buff puede tener un máximo de 3 stacks\n\n"
        "**Efecto del Buff:**\n"
        "* Attack Speed +(30 * Skill Level * número de stacks)\n"
        "* Motion Speed +(Skill Level * número de stacks)%\n"
        "* Evasion Recharge +(Skill Level * número de stacks)%\n"
        "* Max MP -(100 * número de stacks)\n"
        "* Physical Resistance y Magic Resistance -((100 - 3 * Skill Level) * número de stacks)%\n"
        "**Duración del Buff:** 10 + (2 * Skill Level) segundos\n\n"
        "**Halberd bonus:** Attack Speed del buff +(100 * número de stacks)\n"
        "**Halberd bonus:** La reducción de Physical y Magic Resistance del buff se reduce en (45 * número de stacks)%\n"
        "**Halberd bonus:** Duración del Buff +30 segundos"
    ),
)

BUSTER_LANCE = SkillText(
    title="Buster Lance",
    description="**Descripción del juego:** *\"Ataca lanzando una lanza desde la distancia. Cuanto más lejos estés del objetivo, más débil será. La habilidad cambiará si se cumplen ciertas condiciones y la reducción de poder basada en la distancia también se minimizará.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {halberd}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n"
        "**Base Skill Constant:** 100\n"
        "**Base Skill Multiplier:**\n"
        "5 - Max[0, (distancia - 6)] * (100 - Slvl * 5)% + (TotalSTR + TotalAGI)/200\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "Nota: distancia = rango entre tú y el objetivo al usar esta habilidad.\n"
        "Max es el valor más alto, Ejemplo = Max[0, -4] entonces el resultado es 0\n\n"
        "**Efecto de la habilidad:**\n"
        "* Si usas esta habilidad cuando tienes el Buff de Punish Ray, entonces esta habilidad se transformará en Grand Buster Lance"
    ),
)

GRAND_BUSTER_LANCE = SkillText(
    title="Grand Buster Lance",
    description=(
        "Grand Buster Lance es una habilidad mágica pero usa ATK como daño base. Afectada por concentrate. Los chequeos de Stab, hit, evasion y cálculo de daño se aplican normalmente como si fuera física.\n"
        "**Tipo de daño:** Mágico\n"
        "**Base Skill Constant:** 200\n"
        "**Base Skill Multiplier:**\n"
        "5 + 0.1 * Punish Ray's level - Max[0, (distancia-6)] * (60 - Slvl * 4)% + (TotalSTR + TotalAGI)/200\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "Nota: distancia = rango entre tú y el objetivo al usar esta habilidad.\n\n"
        "**Efecto de la habilidad:**\n"
        "* Grand Buster Lance inflige Proration Mágica. Además, el daño se basa en Proration Mágica.\n"
        "* Cada vez que usas Grand Buster Lance, reiniciará/refrescará el stack de Punish Ray a 3.\n"
        "* Subir de nivel \"Punish Ray\" puede aumentar el multiplicador de Grand Buster.\n\n"
        "**Notas:**\n"
        "* Xenesis5: Stability, Hit, Evasion y el cálculo de daño de [Grand Buster Lance] se basan en características físicas. [Grand Buster Lance] se lanza primero como [Buster Lance], que se trata como una habilidad física. Mientras tanto, [Grand Buster Lance] en sí se trata como una habilidad mágica. Por lo tanto, el lanzador no puede usar [Grand Buster Lance] mientras esté bajo los efectos de [Bleed] o [Silence]. Dado que [Grand Buster Lance] se trata como una habilidad mágica, puede ser afectada por [Concentrate], pero no por [Whack]."
    ),
    details="",
)

DRACONIC_CHARGE = SkillText(
    title="Draconic Charge",
    description="**Descripción del juego:** *\"Desata la furia de un dragón. Se activa cuando está lleno o cuando te mueves. Acumula más furia si sientes peligro al cargar. Ten cuidado de no fallar, ya que el alcance del ataque de carga es de solo 8 metros.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {halberd}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico, el primer hit usa ATK, el segundo hit usa ATK + halberd MATK/2\n\n"
        "> **Base Skill Multiplier (Primer Hit):** (5 + 0.5 * Skill Level) * (100% + Charge%)\n"
        "> **Base Skill Constant (Primer Hit):** 300\n"
        "> **Base Skill Multiplier (Segundo Hit AOE):** (5 + 0.5 * Skill Level) * (100% + Charge%)\n"
        "> **Base Skill Constant (Segundo Hit AOE):** 30 * Skill Level\n"
        "**Número de golpes:** 2 hits en el objetivo principal; 1 hit en todos los demás objetivos (del AOE); el cálculo de daño se realiza para cada hit\n\n"
        "**Alcance máximo de Cast:** Teóricamente infinito (pero necesita un objetivo para lanzar)\n"
        "**Alcance del golpe (Segundo Hit AOE):** frente al lanzador después del dash, con 4m de radio y un ángulo de 90°\n"
        "**Distancia de teletransporte:** MIN((9 + Charge% Value * 0.08);16)m\n"
        "-esta distancia de teletransporte puede considerarse como el rango del primer hit\n\n"
        "**Ailment del Segundo Hit AOE:** Ninguno (con elemento Neutral); Ignite (con elemento Fire); Freeze (con elemento Water); Slow (con elemento Wind); Poison (con elemento Earth); Blind (con elemento Light); Cursed (con elemento Dark)\n"
        "**Chance de Ailment del Segundo Hit AOE:** (Skill lvl ^ 2)%\n"
        "**Duración de Ailment del Segundo Hit AOE:** 10 segundos\n"
        "**Resistencia a Ailment del Segundo Hit AOE:** Ninguna\n\n"
        "**Efecto de la habilidad:**\n"
        "* El Primer Hit tiene atributo Perfect Aim, además tiene un bonus de Physical Pierce basado en la distancia entre tú y el enemigo al hacer dash/lanzamiento = +INT(rango - 1m) * 10% Physical Pierce [sin límite, puedes alcanzar 200% PP para obtener 100% Pierce para el segundo hit solo con el bonus de distancia].\n"
        "Mientras tanto, el Segundo Hit AOE solo tiene Absolute Critical. Sin embargo, si el Segundo Hit AOE es evadido, entonces el daño Amarillo (absolute critical) se convierte en daño Blanco (sin crítico) en lugar de ser evadido. Pero para las fases de evasión absoluta/forzada como Evil Crystal Beast, el Segundo Hit AOE sigue siendo evadido.\n\n"
        "* **El Segundo Hit AOE de esta habilidad es un daño híbrido con propiedades físicas (como proration física, cr, stab, etc.). Este segundo hit usa el Base Damage así: (ATK + halberd MATK/2 + Player Lvl - Enemy Lvl) * (100-pres)% - MDEF.** (a partir del ajuste del 24 de abril de 2025, el daño base ahora usa ⚡{halberdmatk_link} en lugar de MATK normal).\n"
        "* El Segundo Hit usa Pierce de la siguiente manera: MAX(INT(Pierce Físico del Primer Hit%/2); Magic Pierce%) y se refiere a MDEF. Este cálculo usa el Pierce Físico% del Primer Hit con el bonus de rango de ataque, el buff de N Dragon Tooth, Sicarius, etc. incluidos antes de la división. El PP% usado para el cálculo del Segundo Hit puede exceder el 100% (puedes alcanzar 100% de pierce con PP%)."
    ),
)

DRACONIC_CHARGE_EXTRA = (
    "**¡Modo Manual!**\n"
    "> * Al usar esta habilidad manualmente sobre un objetivo, entrarás en Modo de Carga. Cuanto más cargues, más daño infligirás. 20% de Carga cada 1 segundo (esta carga con el tiempo no se ve afectada por Motion Speed%). Esta habilidad dejará de cargar e infligirá daño inmediatamente al mover tu personaje o cuando la carga alcance el 100%. Nota: Solo puedes liberar la carga después de que alcance al menos el 20%.\n"
    "> * Si detectas Enemy AOE durante el Modo de Carga, liberarás automáticamente el 100% de la carga al instante. Nota: ¡Debes cargar antes de que llegue el AOE!\n\n"
    "**¡Modo Combo!**\n"
    "> * Si pones esta habilidad en un combo (no como opener), ganará Charge% dependiendo del slot de combo en el que la coloques. Cada 1 slot de combo después del Combo Opener = +5%. Ejemplo: Opener (puede cargar manualmente hasta 100%) > 2CC(5%) > 3CC(10%) > 4CC(15%) > ... > 10CC(45%) MÁX. CC se refiere a Combo count o slot de combo.\n"
    "> * ps. Fórmula de Charge% del CC = (CC - 1) * 5%\n\n"
    "* Después de liberar el Modo de Carga, te teletransportará a 1m frente al objetivo principal. ¡Atención! Esta habilidad no infligirá daño al objetivo si tu habilidad no alcanzó al objetivo. Debes prestar atención a la distancia y al Charge% o de lo contrario solo el Segundo AOE golpeará, o ninguno.\n"
    "* El daño de esta habilidad es afectado solo por SRD%, incluso si haces dash/teletransporte desde 8m. (Similar a Thunder Release). Y Long Range de shot skills puede afectar esto. Esta habilidad usa e inflige proration física; el segundo hit usa la misma proration que el primer hit."
)

INFINITE_DIMENSION = SkillText(
    title="Infinite Dimension",
    description="**Descripción del juego:** *\"Ataques de lanza repetidos que trascienden el tiempo y el espacio. Realiza repetidamente ataques de amplio alcance alrededor de un objetivo. Chance de infligir [Dazzled]. Si Chronos Drive está activo, se recuperará MP extra.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {halberd}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "> **Base Skill Multiplier:** 4 + BaseSTR/500 + BaseAGI/500; multiplicador para cada tick\n"
        "> **Base Skill Constant:** 20 * Skill Level; constante para cada tick\n"
        "**Número de golpes (Número de Ticks):** 5 ticks; el cálculo de daño se realiza para cada tick\n"
        "**Número de golpes (Golpes por Tick):** 2 hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe:** 6m de radio; alrededor de la posición del objetivo al lanzar\n"
        "**Intervalo de golpe:** 1 tick = 2 hits cada 1 segundo; no afectado por Motion Speed%, swift ni freeze\n\n"
        "**Ailment para cada tick:** Dazzled\n"
        "**Chance Base de Ailment:** (8 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad no inflige proration. Sin embargo, su daño se basa en Proration Física.\n"
        "* Si tu personaje tiene el efecto/buff de CHRONOS DRIVE, entonces esta habilidad puede recuperar tu MP con cada tick por (Total AMPR/10 * Skill Level)\n"
        "* La animación de ataque de esta habilidad terminará inmediatamente tan pronto como el objetivo principal muera.\n"
        "* El daño de esta habilidad no es afectado por SRD/LRD%"
    ),
)

TORNADO_LANCE = SkillText(
    title="Tornado Lance",
    description="**Descripción del juego:** *\"Gana 1 unidad de poder de tornado cuando una habilidad de alabarda golpea. Tu alabarda se vuelve más fuerte a medida que acumulas más poder de tornado. La mitad del tornado se perderá si eres atacado.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {halberd}\n\n"
        "**Efecto Pasivo:**\n"
        "* Cada vez que usas una habilidad de ataque de halberd que no resulta en Miss ni Evasion, otorga 1 stack de tornado lance. El máximo de stacks es 10. Sin embargo, perderás la mitad de los stacks actuales cada vez que recibas daño, ~~incluso si puedes esquivar (el ataque enemigo falla), evasión e invencibilidad~~ Ahora no perderás stacks con iframe/evasion, pero dodge[miss] sigue perdiendo stacks.\n"
        "* Duración del Buff Pasivo: 100 segundos (se puede renovar a 100s después de usar habilidades de ataque de halberd).\n"
        "* Aumenta Critical Damage en +(Skill Level/5) por stack.\n"
        "* Aumenta Dodge/Flee en 10% por stack.\n"
        "* Aumenta la chance de activar Additional Melee/Magic en (2.5 * stack * Skill Level/10)%\n"
        "* [Actualmente necesita confirmación sobre si usa stack o Skill Level, probablemente solo stacks. Al efecto máximo, esta habilidad puede reducir la penalización de Graze Stability desde -50% Final Stability hasta -40% Final Stability, haciendo que tu Graze Damage varíe entre 60% y 100% si tienes 100% Final Stability]\n"
        "* Aumenta tu Graze Threshold en (8 * stack * Skill Level/10)%. Nota: halberd tiene un 20% de Graze Threshold base.\n\n"
        "Si el enemigo está afectado por Dazzled, entonces el Hit Chance se convierte en MAX[(100 - (enemy flee - player accuracy) + MP/10); Base Graze Threshold * 2]. Este Dazzled solo toma el Graze base de halberd sin el aumento de Graze Threshold del buff de Tornado Lance.\n\n"
        "* Aumenta Critical Damage de halberd, la chance de additional attack y el golpe garantizado a medida que se acumula. Cuando el poder de tornado se pierde al ser atacado, la tasa de dodge aumenta según el valor del poder perdido."
    ),
)

ALMIGHTY_WIELD = SkillText(
    title="Almighty Wield",
    description="**Descripción del juego:** *\"Alivia la cantidad de cada resistencia disminuida debido a la habilidad 'Godspeed Wield'. Chance de ganar invencibilidad (basada en AGI) al recibir daño. Este efecto puede activarse (una vez cada 10 segundos). También otorga un efecto pasivo que aumenta el daño físico de las habilidades de Halberd.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {halberd}\n\n"
        "**Efecto Pasivo:**\n"
        "* Chance de activar Invincibilidad al recibir daño si tienes algún stack de Godspeed Wield activo.\n"
        "> * Chance de Invincibilidad: 10 + 2 * Skill Level + BaseAGI/3.5\n"
        "> * Duración de Invincibilidad: 2 segundos\n"
        "> * Cooldown de Invincibilidad: 10 segundos\n"
        "* Reduce la penalidad de Physical/Magic Resistance de Godspeed Wield en (Skill Level/2 * stack)%\n"
        "* Aumenta el daño de las Habilidades Físicas de Halberd en (1 * Skill Level)%\n"
        "> * Habilidades Afectadas: Flash Stab, Cannon Spear, Dragon Tail, Dive Impact, Dragon Tooth, Draconic Charge, Deadly Spear, Strike Stab, Chronos Drive, Infinite Dimension, Buster Lance, Grand Buster Lance, Blitz Spike.\n"
        "> * Este aumento de daño está incluido en el grupo de Skill Damage Modifier como Whack, Long Range, Sword Techniques.\n"
        "* **Solo halberd**, otorgará nuevos atajos de habilidad basados en el nivel de esta habilidad. En el nivel 1, añade \"Almighty Wield III\" que otorga 3 stacks de GSW. En el nivel 5, añade \"Almighty Wield II\" que otorga 2 stacks de GSW. En el nivel 10, añade \"Almighty Wield I\" que otorga 1 stack de GSW. Estos efectos de stack siguen basándose en el nivel de Godspeed Wield como es habitual."
    ),
)

HALBERD_MATK_EXPLANATION = SkillText(
    title="Explicación de Halberd MATK",
    description=(
        "Las tres habilidades de Halberd con temática de Rayo después de la habilidad \"Punish Ray\" en la misma línea, usan una nueva Base MATK para sus hits de daño mágico.\n"
        "> **Base MATK (Halberd MATK):** Player Level + Total Weapon ATK * 62.5% + INT * 4 + AGI * 1\n\n"
        "Los hits de daño mágico de las habilidades de Halberd con temática de Rayo actúan igual que el daño mágico habitual (usan daño crítico mágico, afectados por spell burst, usan estabilidad mágica, afectados por el estado defensivo mágico del Boss).\n\n"
        "*a partir del 24 de abril de 2025, Draconic Charge también usa \"Halberd MATK\" para la parte MATK del daño base híbrido de su segundo hit AOE.\n"
        "*si necesitas una fórmula más precisa para Halberd MATK, entonces usa INT((Player Level + INT*2 + AGI + DEX)*(1+MATK%)) + INT((Total Weapon ATK*62.5% + INT*2 - DEX)*(1+MATK%)). Halberd MATK añade una fórmula nueva/extra sobre el stat de MATK original, por lo que usar esta fórmula sería más preciso."
    ),
    details="",
)

BLITZ_SPIKE = SkillText(
    title="Blitz Spike",
    description="**Descripción del juego:** *\"Una estocada de lanza rápida envuelta en relámpagos. Chance de infligir [Paralysis] al activarse cerca del objetivo. Si está paralizado, el objetivo recibirá daño mágico adicional. Cuando se activa a distancia, se invocarán lanzas de relámpago que atacan automáticamente a los enemigos que se acerquen.\"*",
    details=(
        "**Habilidad Tier 3;** [Activo] Solo {halberd}\n"
        "**Coste MP:** 300\n\n"
        "**[Versión de Corto Alcance]** (rango de cast: 0-7m)\n"
        "**Tipo de daño:** Físico, usa ATK\n"
        "> **Base Skill Multiplier:** 3 + 0.1 * Skill Level + 0.1 * Thor's Hammer Skill Level\n"
        "> **Base Skill Constant:** 300\n"
        "**Número de golpes:** 2 hits; el cálculo de daño se realiza una vez y se divide equitativamente entre los hits\n"
        "El hit es afectado por short range damage; afectado por long range skill; usa e inflige proration mágica.\n\n"
        "**Ailment:** Paralysis\n"
        "**Chance de Ailment:** (5 * Skill Level + INT/10)%\n"
        "**Resistencia a Ailment:** 10 segundos\n\n"
        "**Daño mágico adicional de Paralysis:**\n"
        "**Tipo de daño:** Mágico, usa Halberd MATK\n"
        "> **Base Skill Multiplier:** 1 + 0.3 * Skill Level + 0.1 * Thor's Hammer Skill Level + BaseINT/200\n"
        "> **Base Skill Constant:** TotalINT/2\n"
        "**Número de golpes:** 1 hit\n"
        "Este hit es absolute critical.\n"
        "El hit es afectado por short range damage; afectado por long range skill; usa proration mágica.\n\n"
        "**[Versión de Largo Alcance]** (rango de cast: 8-24m; los proyectiles empiezan a dispararse desde 7m hacia abajo)\n"
        "**Tipo de daño:** Físico, usa ATK\n"
        "* **Base Skill Multiplier:** TotalINT/200\n"
        "* **Base Skill Constant:** TotalINT\n"
        "**Número de golpes = ROUNDUP(Skill Level/3;0)**\n"
        "**Recuperación de MP por proyectil:** 100% del Attack MP Recovery del personaje\n"
        "El hit no es afectado por short/long range damage; no afectado por long range skill; usa e inflige proration normal (cada hit)."
    ),
)

LIGHTNING_HAIL = SkillText(
    title="Lightning Hail",
    description="**Descripción del juego:** *\"Una técnica de lanza que invoca múltiples rayos del cielo. Genera múltiples ataques que infligen daño mágico alrededor del objetivo. Más probable de golpear a objetivos paralizados. Otorga invencibilidad a ti mismo al activarse.\"*",
    details=(
        "**Habilidad Tier 4;** [Activo] solo {halberd}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Mágico, usa Halberd MATK\n\n"
        "> **Base Skill Multiplier:** 0.75 + 0.2 * INT(Skill Level/2) + TotalINT/1000\n"
        "> **Base Skill Constant:** 100 + 10 * Skill Level\n"
        "El cálculo de daño se realiza por separado por hit. Esta es una fórmula para 1 hit.\n"
        "**Número de golpes:** 3 + ROUNDUP(Skill Level/2;0)\n"
        "**Frame de invencibilidad:** 2 segundos (terminará cuando la animación de la habilidad termine)\n"
        "**Alcance máximo de Cast:** 18m\n"
        "Esta habilidad tiene absolute critical.\n\n"
        "Esta habilidad es forzada a ser y es afectada por long range damage; afectada por long range skill; usa e inflige proration mágica; no es afectada por Motion Speed del estado del personaje, pero puede usar el modificador de Motion Speed del combo tag \"swift\"."
    ),
)

THORS_HAMMER = SkillText(
    title="Thor's Hammer",
    description="**Descripción del juego:** *\"Una técnica de lanza que invoca un poderoso rayo. Un ataque mágico con crítico garantizado, pero el daño se dividirá entre los objetivos atrapados en la explosión. Una vez activado, tu Additional Magic, Magic Pierce y Accuracy Rate aumentarán durante un cierto período de tiempo.\"*",
    details=(
        "**Habilidad Tier 5;** [Activo] Solo {halberd}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Mágico, usa Halberd MATK\n\n"
        "> **Base Skill Multiplier:** (10 + 0.5 * Skill Level)/Número de Objetivos\n"
        "> **Base Skill Constant:** 400\n"
        "Si múltiples objetivos son golpeados, el Base Skill Multiplier se dividirá dependiendo del número de objetivo(s) golpeados. El cálculo de daño se sigue haciendo por separado por hit.\n"
        "**Alcance máximo de Cast:** 12m\n"
        "Esta habilidad tiene absolute critical.\n"
        "Esta habilidad no es afectada por short/long range damage; no afectada por long range skill; usa e inflige proration mágica.\n\n"
        "**Daño Mágico Adicional: Lightning Hail's Trail**\n"
        "> **Base Skill Constant:** Base Skill Constant Actual de Lightning Hail\n"
        "> **Base Skill Multiplier:** Base Skill Multiplier Actual de Lightning Hail * posición de Hits\n"
        "El Base Skill Multiplier aumenta según la posición de los hits:\n"
        "-1er hit: multiplicador = Lightning Hail Multiplier * 1\n"
        "-2do hit: multiplicador = Lightning Hail Multiplier * 2\n"
        "-3er hit: multiplicador = Lightning Hail Multiplier * 3\n"
        "...\n"
        "-8vo hit: multiplicador = Lightning Hail Multiplier * 8\n"
        "Estos ataques adicionales son absolute critical.\n"
        "Los hits no son afectados por short/long range damage; no afectados por long range skill; usan proration mágica y no infligen proration.\n\n"
        "**Efecto del Buff:**\n"
        "* Additional Magic: + 10 * Skill Level%\n"
        "* Magic Pierce: + 2 * Skill Level%\n"
        "* Accuracy: + BaseINT * Skill Level/10\n"
        "**Duración del Buff:** 12 segundos * Skill Level (o hasta que seas inmovilizado)\n\n"
        "**Halberd bonus:** Accuracy Rate aumenta según INT. La habilidad \"Lightning Hail\" dejará un rastro de relámpago, y cuando Thor's Hammer se activa, se generará daño mágico adicional."
    ),
)
