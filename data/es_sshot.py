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

POWER_SHOT = SkillText(
    title="Power Shot",
    description="**Descripción del juego:** *\"Dispara al objetivo con mayor potencia. El tiempo de carga se reduce al subir de nivel. Chance de infligir [Tumble] al objetivo. La Critical Rate aumenta en objetivos ralentizados.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Esta habilidad tiene una reducción innata de Motion Speed de (155 - 10.5 * Skill Level)%; la reducción se aplica de la siguiente manera:\n\n"
        "Power Shot Animation Time Modifier = Animation Time Modifier * (1 + Motion Speed penalty/100)\n\n"
        "*  Esta habilidad obtiene Critical Rate +(5 * Skill Level) si tu objetivo tiene Slow Ailments.\n\n"
        "**Ailment:** Tumble\n"
        "**Chance de Ailment:** 20% + (3 * Skill Level)%\n"
        "**Duración de Ailment:** 3 segundos\n"
        "**Resistencia a Ailment:** 3 segundos (Easy y Normal); 6 segundos (Hard); 12 segundos (Nightmare); 18 segundos (Ultimate)\n\n"
        "**Bow bonus:** Tumble chance +40%\n"
        "**Bowgun bonus:** Motion Speed penalty -50%\n"
        "**Penalidad Bowgun:** Tumble chance -40%\n\n"
        "**Base Skill Multiplier:** 1.25 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 50 + 8 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 16m"
    ),
)

BULLSEYE = SkillText(
    title="Bullseye",
    description="**Descripción del juego:** *\"Dispara consecutivamente a un punto. El daño infligido aumenta con cada ataque.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Esta habilidad tiene Physical Pierce +(4 * Skill Level)% en el segundo hit\n"
        "*  Physical Pierce +(8 * Skill Level)% en el tercer hit\n\n"
        "**Alcance máximo de Cast:** 12m\n\n"
        "**Bow bonus:** Skill Multiplier +0.25\n"
        "**Bowgun bonus:** Physical Pierce del segundo hit +10%; Physical Pierce del tercer hit +20%\n\n"
        "**Base Skill Multiplier:** 0.25 + 0.05 * Skill Level; multiplicador para cada hit\n"
        "**Base Skill Constant:** 30 + 4 * Skill Level; constante para cada hit\n"
        "**Número de golpes:** 3 hits; Dodge, Evasion, Guard, Anticipate, Guard Break y los cálculos críticos se realizan en el primer hit, luego se copian para los otros hits; el resto del cálculo de daño se realiza para cada hit"
    ),
)

MOEBA_SHOT = SkillText(
    title="Moeba Shot",
    description="**Descripción del juego:** *\"Disparo con líquido pegajoso. Ataque de elemento Water. Elemento Dual con Arrow. Chance de infligir [Slow Down] al objetivo.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n"
        "**Elemento:** Water; tiene atributo Elemento Dual (obtiene elemento extra de Arrow sub)\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Si el enemigo recibe Slow ailments con esta habilidad, el multiplicador y la constante aumentarán solo para ese hit\n"
        "*  Bonus Base Skill Multiplier +(0.5 + baseDex/100)\n\n"
        "**Ailment:** Slow\n"
        "**Chance de Ailment:** 50% + (2 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Bow bonus:** Slow chance +30%\n"
        "**Bowgun bonus:** Skill Multiplier +0.5\n"
        "**Penalidad Bowgun:** Slow chance -30%\n\n"
        "**Base Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 50 + 5 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 14m"
    ),
)

SHOT_MASTERY = SkillText(
    title="Shot Mastery",
    description="**Descripción del juego:** *\"Mejora en el uso de Bows y Bowguns. El ATK de los Bows y Bowguns aumenta.\"*",
    details=(
        "**Habilidad Tier 1;** Solo {bow} / {bowgun}\n"
        "**Efecto Pasivo:**\n"
        "*  Weapon ATK +(3 * Skill Level)%\n"
        "*  ATK +1% (niveles 1 y 2) / +2% (niveles 3 a 7) / +3% (niveles 8 a 10)"
    ),
)

SNEAK_ATTACK = SkillText(
    title="Sneak Attack",
    description="**Descripción del juego:** *\"Escóndete y desvía el Aggro. Ciertos ataques no reciben Aggro después de esta habilidad.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto del Buff:**\n"
        "*  Durante los siguientes (Skill Level) autoataques y habilidades de ataque, no obtendrás aggro\n"
        "**Duración del Buff:** (Skill Level) autoataques y/o habilidades de ataque\n\n"
        "**Bow bonus:** Coste MP -200\n"
        "**Bowgun bonus:** Coste MP -200\n\n"
        "Las habilidades de apoyo y las habilidades sin ataque (incluyendo Sneak Attack) seguirán generando aggro, pero no disminuirán el contador de ataques/habilidades de ataque."
    ),
)

ARROW_RAIN = SkillText(
    title="Arrow Rain",
    description="**Descripción del juego:** *\"Dispara muchas flechas al cielo. Las flechas caen a intervalos e infligen daño.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Esta habilidad no se ve afectada por las estadísticas de Whack, Long Range y Short Range Damage/Long Range Damage\n"
        "*  El buff de Triple Thrust's Skill Constant se divide por el Hit Count\n\n"
        "**Bow bonus:** Alcance del golpe +2m\n"
        "**Bow bonus:** El Hit Count se duplica\n"
        "**Bowgun bonus:** Skill Multiplier +0.7\n\n"
        "**Base Skill Multiplier:** 1 + Floor(Skill Level / 2) * 0.06; multiplicador para cada hit\n"
        "**Base Skill Constant:** 50 + Floor((Skill Level + 1)/2) * 10; constante para cada hit\n"
        "**Número de golpes:** 1 hit (niveles 1 y 2); 2 hits (niveles 3 a 5); 3 hits (niveles 6 a 8); 4 hits (niveles 9 y 10){{el cálculo de daño se realiza para cada hit}}\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe(Radio):** alrededor de la posición del objetivo cuando se lanza la habilidad, 1.5m (niveles 1 a 3); 2m (niveles 4 a 6); 2.5m (niveles 7 a 9); 3m (nivel 10)"
    ),
)

PARALYSIS_SHOT = SkillText(
    title="Paralysis Shot",
    description="**Descripción del juego:** *\"Dispara al objetivo con un veneno paralizante. Ataque de elemento Wind. Elemento Dual con Arrow. Chance de infligir [Paralysis] al objetivo. Aumenta tu Stability durante un tiempo.\"*",
    details=(
        "**Habilidad Tier 2;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n"
        "**Elemento:** Wind; tiene atributo Elemento Dual (obtiene elemento extra de Arrow sub)\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Si el enemigo recibe Paralysis ailments con esta habilidad, el multiplicador y la constante aumentarán solo para ese hit\n"
        "*  Bonus Base Skill Multiplier +(1 + baseDex/100)\n\n"
        "**Efecto del Buff:**\n"
        "*  Aumenta la Stability en +(Skill Level)%\n"
        "**Duración del Buff:** 10 segundos\n\n"
        "**Ailment:** Paralysis\n"
        "**Chance de Ailment:** 50% + (2 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Bow bonus:** Skill Multiplier +1\n"
        "**Bow bonus:** Paralysis Rate +20%\n"
        "**Bowgun bonus:** Skill Multiplier +1.5\n"
        "**Penalidad Bowgun:** Paralysis Rate -20%\n"
        "**Arrow bonus:** Paralysis Rate +20%\n\n"
        "**Base Skill Multiplier:** 1.1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 100 + 20 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 14m"
    ),
)

LONG_RANGE = SkillText(
    title="Long Range",
    description="**Descripción del juego:** *\"Te vuelves bueno atacando desde la distancia. El daño infligido desde 8 metros o más aumenta.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Efecto Pasivo:**\n"
        "*  Aumenta el daño de todas las habilidades que tengan un Alcance máximo de Cast de 8m o más en (Skill Level)%\n"
        "Algunas habilidades no se ven afectadas"
    ),
)

SNIPE = SkillText(
    title="Snipe",
    description="**Descripción del juego:** *\"Apuntar a un punto débil. El tiempo de carga disminuye al subir de nivel. Chance de infligir [Armor Break]. 100% de chance de golpear objetivos con Blind.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Esta habilidad obtiene el atributo Perfect Aim cuando el objetivo tiene el ailment Blind\n"
        "*  Esta habilidad tiene una penalización total de Critical Rate de (25 - floor(Skill Level/2))%; la penalización se aplica de la siguiente manera:\n"
        "Snipe Critical Rate = Total Critical Rate * (1 - Critical Rate penalty/100)\n\n"
        "**Ailment:** Armor Break\n"
        "**Chance de Ailment:** 50% + (2 * Skill Level)%\n"
        "**Duración de Ailment:** 5 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Bow bonus:** Skill Multiplier +2\n"
        "**Bow bonus:** Armor Break chance +30%\n"
        "**Bow bonus:** La penalización de Total Critical Rate se convierte en (10 - Skill Level)%\n"
        "**Bowgun bonus:** Skill Multiplier +3\n"
        "**Bowgun bonus:** Tiempo de carga -0.5 segundos\n"
        "**Bowgun bonus:** La estabilidad de esta habilidad aumenta en +20%\n"
        "**Penalidad Bowgun:** Armor Break chance -60%\n\n"
        "**Base Skill Multiplier:** 7 + 0.1 * Skill Level\n"
        "**Base Skill Constant:** 300 + 10 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 16m\n"
        "**Tiempo de carga:** 5 segundos (niveles 1 y 2); 4 segundos (niveles 3 y 4); 3 segundos (niveles 5 a 7); 2 segundos (niveles 8 y 9); 1 segundo (nivel 10)"
    ),
)

SMOKE_DUST = SkillText(
    title="Smoke Dust",
    description="**Descripción del juego:** *\"Un ataque con una pantalla de humo. Ataque de elemento Dark. Elemento Dual con Arrow. Chance de infligir [Blind] al objetivo. Aumenta accuracy durante un tiempo.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Físico\n"
        "**Elemento:** Dark; tiene atributo Elemento Dual (obtiene elemento extra de Arrow sub)\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Si el enemigo recibe Blind ailments con esta habilidad, el multiplicador y la constante aumentarán solo para ese hit\n"
        "*  Bonus Base Skill Multiplier +(2 + baseDex/100)\n\n"
        "**Efecto del Buff:**\n"
        "*  Aumenta Accuracy en +(Skill Level²/2 + 5 * Skill Level)\n"
        "**Duración del Buff:** 10 segundos\n\n"
        "**Ailment:** Blind\n"
        "**Chance de Ailment:** 50% + (2 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Bow bonus:** Skill Multiplier +2\n"
        "**Bow bonus:** Blind Rate +20%\n"
        "**Bowgun bonus:** Skill Multiplier +2.5\n"
        "**Penalidad Bowgun:** Blind Rate -20%\n"
        "**Arrow bonus:** Blind Rate +20%\n\n"
        "**Base Skill Multiplier:** 1.2 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 200 + 30 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 14m"
    ),
)

QUICK_DRAW = SkillText(
    title="Quick Draw",
    description="**Descripción del juego:** *\"Prepárate rápidamente para el próximo movimiento. Chance de recuperar un poco de MP al tener éxito atacando con una habilidad.\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Efecto Pasivo:**\n"
        "*  Cada vez que se usa una habilidad de ataque que consume MP, tienes un (3 * Skill Level)% de chance de recuperar 100 MP\n\n"
        "Las habilidades de apoyo, las habilidades sin ataque y las habilidades de ataque que no consumen MP no activarán esta habilidad. Esto incluye los efectos de combo tags y modificadores de Coste MP."
    ),
)

FATAL_SHOT = SkillText(
    title="Fatal Shot",
    description="**Descripción del juego:** *\"Una habilidad de disparo que perfora una armadura fuerte. Es un ataque único con un alto Critical Rate, pero bajo accuracy. Si golpea al objetivo correctamente, el tap time para romper la parte del monstruo se extiende.\"*",
    details=(
        "**Habilidad Tier 3;** Solo {bow} / {bowgun}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Fatal Shot Critical Rate: +25 + 5 * Skill Level\n"
        "*  Fatal Shot Skill Accuracy: -100% + 2% * Skill Level\n"
        "*  Esta habilidad puede extender el tap break time: Floor (skill level/2), {{Si el ataque de esta habilidad resulta en Miss/Evasion/Graze, no extiende el break time}}\n\n"
        "**Base Skill Multiplier:** 5 + 0.1 * Skill Level + TotalSTR/200 + TotalDEX/200\n"
        "**Base Skill Constant:** 200\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 14m"
    ),
)

CROSS_FIRE = SkillText(
    title="Cross Fire",
    description="**Descripción del juego:** *\"Habilidad de Carga (5 niveles). Ataca hacia un objetivo e inflige daño en línea recta. El poder aumenta al aumentar el nivel de carga y agrega un ataque adicional. Agrega otro ataque al cumplir ciertas condiciones.\"*",
    details=(
        "**Habilidad Tier 4;** Solo {bow} / {bowgun}\n"
        "**Coste MP:** 400 (buff cast) / 0 (attack cast)\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Si usas el attack cast sin cargas, fallará (y tu avatar se verá confundido)\n"
        "*  Esta habilidad agrega un hit adicional si hay un señuelo de Decoy Shot activo\n"
        "*  Si el attack cast tiene el mismo Combo Tag que el buff cast, el Combo Tag del attack cast se ignora\n"
        "*  El Combo Multiplier se transfiere desde el buff cast; esto considera si el Combo Tag del attack cast se ignora; el total de Combo Multiplier se calcula así:\n"
        "CrossFire Total Combo Multiplier = Attack Cast Combo Multiplier + Buff Cast Combo Multiplier - 100\n"
        "¡Recuerda! De todos los combo tags, solo Bloodsucker(lifesteal) y Mind's eye(siempre Graze/no Miss) no pueden aplicarse en el buff(Charge) cast, pero Bloodsucker after-effect(Spirit = boost dmg), Smite, Save y el resto pueden aplicarse en el buff cast.\n\n"
        "**Efecto del Buff:**\n"
        "*  El próximo cast de Cross Fire cuesta 0 MP\n"
        "*  Obtiene cargas con el tiempo, empezando en 0 cargas\n"
        "*  Límite máximo de carga: 2 (niveles 1 a 3); 3 (niveles 4 a 6); 4 (niveles 7 a 9); 5 (nivel 10)\n"
        "*  Tiempo por carga: 1 segundo (primera carga); 2 segundos (segunda carga); 5 segundos (tercera carga); 10 segundos (cuarta carga); 17 segundos (quinta carga) [la carga actual debe completarse antes de pasar a la siguiente]\n"
        "*  Si recibes un hit, la habilidad dejará de cargar; si recibes un hit sin cargas, el buff se elimina\n"
        "**Duración del Buff:** Hasta que lances Cross Fire (attack cast) de nuevo O hasta que recibas un hit si no tienes cargas\n"
        "Nota: La animación de carga de esta habilidad no se ve afectada por la motion speed del estado del personaje, pero puede usar el modificador de motion speed del combo tag \"swift\".\n\n"
        "**Bow bonus:** Golpe Principal Skill Multiplier +((baseDex/500 + 0.5) * número de cargas)\n"
        "**Bow bonus:** Radio del Golpe Principal +1m\n"
        "**Bowgun bonus:** Golpes Adicionales Skill Multiplier +1\n"
        "**Bowgun bonus:** Golpes Adicionales Physical Pierce +(baseDex/10)%\n\n"
        "Solo el Golpe Principal y los Decoy Hits se ven afectados por Whack, Long Range y Short Range Damage/Long Range Damage stats. Mientras que los Golpes Adicionales solo se ven afectados por Whack\n\n"
        "**Golpe Principal Skill Multiplier:** (4 + 0.5 * Skill Level) * número de cargas\n"
        "**Golpes Adicionales Skill Multiplier:** 2; Skill Multiplier para cada hit\n"
        "**Decoy Hit Skill Multiplier:** (0.8 + 0.1 * Skill Level) * número de cargas\n"
        "**Golpe Principal Skill Constant:** 300 + 10 * Skill Level\n"
        "**Golpes Adicionales Skill Constant:** 300 + 10 * Skill Level; constante para cada hit\n"
        "**Decoy Hit Skill Constant:** 60 + 2 * Skill Level\n"
        "**Número de golpes:** 1 hit (Golpe Principal y Decoy Hit); número de cargas - 1 (Golpes Adicionales); el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** Buff cast-Ilimitado; Attack cast-12m\n"
        "**Alcance del golpe:** 100m de largo y 1m de radio; desde la posición del lanzador (Golpe Principal)/ objetivo principal (Golpes Adicionales)/ 100m de largo y 1m de radio; desde la posición del señuelo (Decoy Hit)"
    ),
)

ARM_BREAK = SkillText(
    title="Arm Break",
    description="**Descripción del juego:** *\"Ataca el brazo de un objetivo y reduce su poder de ataque. El elemento base es Neutral y tiene Elemento Dual(Arrow). Chance de infligir [Lethargy].\"*",
    details=(
        "**Habilidad Tier 4;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 700\n"
        "**Tipo de daño:** Físico\n"
        "**Elemento:** Neutral; tiene atributo Elemento Dual (obtiene elemento extra de Arrow sub)\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Si el enemigo recibe Lethargy ailments con esta habilidad, el multiplicador y la constante aumentarán solo para ese hit\n"
        "*  Bonus Base Skill Multiplier +(1.3 + baseDex/100)\n\n"
        "**Ailment:** Lethargy\n"
        "**Chance de Ailment:** 50% + (2 * Skill Level)%\n"
        "**Duración de Ailment:** 10 segundos\n"
        "**Resistencia a Ailment:** Ninguna\n\n"
        "**Bowgun bonus:** Skill Multiplier +3\n"
        "**Bow bonus:** Lethargy Rate +20%\n"
        "**Bowgun bonus:** Skill Multiplier +3.5\n"
        "**Penalidad Bowgun:** Lethargy Rate -20%\n"
        "**Arrow bonus:** Lethargy Rate +20%\n\n"
        "**Base Skill Multiplier:** 3 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 300 + 40 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 14m"
    ),
)

DECOY_SHOT = SkillText(
    title="Decoy Shot",
    description="**Descripción del juego:** *\"Genera un clon y hazlo atacar. El clon ataca a los enemigos que atacan dentro del rango. El ataque del clon es un ataque normal pero no tiene proration.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 400\n"
        "**Alcance máximo de Cast:** Teóricamente infinito (limitado a 100m)\n"
        "**Tiempo de Cast base:** 1 segundo; afectado por Cast Speed\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Coloca un decoy que ataca automáticamente mientras el objetivo principal esté dentro de su rango; se aplica Attack MP Recovery y Aggro completos, pero el decoy no hace proration\n"
        "*  El decoy ataca según tu Attack Speed, pero tiene un retraso mínimo de autoataque de 0.001 segundos\n"
        "*  Duración: 10 + (Skill Level x Skill Level / 2) segundos. En Nivel 10 = 60 segundos\n\n"
        "**Decoy Auto Damage Type:** Neutral\n"
        "**Decoy Auto Element:** Neutral\n"
        "**Decoy Auto Multiplier:** 0.2 + 0.08 * Skill Level\n"
        "**Decoy Hit Count:** 1 hit\n"
        "**Decoy Hit Range:** Por defecto al Autoataque Max Range del arma\n\n"
        "Nota: Esta habilidad no se ve afectada por la motion speed del estado del personaje, pero puede usar el modificador de motion speed del combo tag \"swift\".\n\n"
        "**Penalidad No Bow/Bowgun:** Si un decoy recibe hit de un AoE, su retraso de auto-atk aumenta en 1 segundo (por cada hit) para el próximo auto-atk. Retraso máximo de 3 segundos (3 hits de AoE)\n"
        "*  El Decoy Auto Multiplier no se ve afectado por efectos que aumentan el daño de autoataques\n"
        "*  El decoy se ve afectado por los efectos de Combo Tag cuando lanzas Decoy Shot en un combo\n"
        "*  Dual Swords se beneficia de su Attack MP Recovery duplicado en el decoy, pero el daño solo escala con el ATK de la mano principal\n"
        "*  El decoy solo atacará al mob/boss que estés atacando\n"
        "*  La habilidad y el decoy evitan el efecto de Sneak Attack\n"
        "*  Power Wave NO afecta el rango del decoy\n"
        "*  El decoy se verá afectado por todos los cambios de estadísticas (como Attack MP Recovery, Critical Rate, etc.) incluso mientras está activo, pero la habilidad debe ser relanzada para que el decoy se vea afectado por cambios en Attack Speed\n"
        "*  Cada vez que tu decoy ataque cuando tengas Poison ailments, Poison seguirá activándose/reducirá tu HP\n"
        "*  El ataque del decoy no puede infligir Proration neutral\n"
        "*  Este decoy puede sincronizarse con Cloning de \"Scroll Skills\"\n\n"
        "**Bug Note:** (no abuses, o corres el riesgo de ser Baneado; Phantom's Library no se hace responsable)\n"
        "*  Esta habilidad tiene un bug de AMPR. Cada vez que el decoy ataca a un objetivo, da +100% de base AMPR en el próximo autoataque del jugador (el decoy puede disfrutar este efecto todo el tiempo sin gastar este efecto hasta que hagas autoataque). Pero la condición de este bug AMPR es extraña, a veces funciona y a veces no (Sí, ocurre cuando cambias de personaje y cambias de arma; y reloguear reinicia esos [a veces funciona y a veces no] = lo cual es como usar el sistema). ¿Extraño verdad? Usar el sistema = bug. (En realidad, espero que no sea un bug, pero es imposible por esa extraña condición/sistema).\n"
        "*  Este bug de AMPR siempre ocurre incluso si no lo pretendes (solo ignóralo y continúa sin usar el sistema [solo finge = no saber ese bug] o reporta ese bug de AMPR [risa malvada])."
    ),
)

HUNTING_BUDDY = SkillText(
    title="Hunting Buddy",
    description="**Descripción del juego:** *\"Invoca a tu compañero para que luche a tu lado. Ataca cada pocos segundos, causando proration de ataque normal. El efecto que mejora el próximo ataque de tu compañero se acumulará cuando golpees al objetivo con una Shot Skill; 1 ataque normal con Twin Storm (2 stacks de Twin Storm) te dará 1 stack de Hunting Buddy.\"*",
    details=(
        "**T4; [Activo]** Solo {bow} / {bowgun}\n"
        "**Coste MP:** 100 invocación; 0 cancelar invocación\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Hunting Buddy ataca al objetivo y volverá a ti antes de atacar más, por lo tanto, mantenerse lejos del objetivo o huir extenderá el intervalo de ataque\n"
        "*  Esta habilidad se ve afectada por short range damage; afectada por awaken element; no afectada por whack; usa proration física e inflige proration normal\n\n"
        "**Base Skill Multiplier:** 1 + TotalDEX/1000 + Stack Multi Bonus\n"
        "**Stack Multiplier Bonus:** 0.1 * Skill Level * Stack (máx. 25 stacks)\n"
        "Cualquier habilidad que potencie el multiplicador de los autoataques (ej. Kairiki Ranshin, Berserk) y registlets (ej. Power Wave Modifier, Mana Thrash) se suman al multiplicador de habilidad base. Los stacks no tienen ningún icono; el cálculo de daño del stack se realiza detrás de escena y los stacks se reinician a 0 cada vez que el perro ataca.\n"
        "**Base Skill Constant:** 100\n\n"
        "**Bow/Bowgun Bonus:** A menos que todo tu equipo sea eliminado, tu compañero usará First Aid antes de irse cuando seas noqueado. First Aid Level = Hunting Buddy Skill Level."
    ),
)

PIERCING_SHOT = SkillText(
    title="Piercing Shot",
    description="**Descripción del juego:** *\"Una flecha que perfora incluso la defensa más fuerte. Apunta y ataca en línea recta con una Habilidad de Carga (5 Niveles). Puedes moverte y ajustar la dirección con Evasion. Cada hit (excepto Graze) mejora su rendimiento y recupera ligeramente MP.\"*",
    details=(
        "**T5; [Activo]** {bow} / {bowgun}\n"
        "**Coste MP:** 600\n"
        "**Tipo de daño:** Físico\n\n"
        "**Carga:**\n"
        "*  Tiempo de carga: 1.5 segundos/carga; 7.5s para carga máxima. Reduce el tiempo de carga a objetivos dormidos/interrumpidos (0.5 segundos/carga; 2.5s para carga máxima)\n"
        "*  Dentro de un combo, la carga se fija a una carga\n"
        "*  La habilidad Quick Loader funciona solo para carga manual\n\n"
        "**Evasion Bypass Chance:** MIN(100;(25%*stack))\n"
        "**Guard Bypass Chance:** 100%\n"
        "*  El bypass de Evasion/Guard tiene un mecanismo similar a anticipate/Guard break pero sin el aviso emergente\n\n"
        "Esta habilidad se ve afectada por short/long range damage; afectada por Long Range Skill; usa e inflige proration física\n\n"
        "!Bug: Esta habilidad tiene un bug visual donde tus hits amarillos de Graze se convierten en críticos falsos sin Graze (aún usando estabilidad de Graze, sin constante extra y sin bonus de MP recovery)\n\n"
        "**Bowgun Bonus:** Obtienes invencibilidad durante 1.5 segundos cuando comienzas o reanudas la carga. * Activar una habilidad o moverse con Evasion eliminará esta invencibilidad. Moverse con Evasion ya no elimina la invencibilidad según la actualización del 24 de abril de 2025.\n"
        "* Esta invencibilidad se elimina cuando se activa una habilidad.\n\n"
        "**Base Skill Multiplier (cada Hit):** 10 + 0.25 * Skill Level + BaseDEX/200\n"
        "**Base Skill Constant (cada Hit):** 600 + (bonus si no es \"Graze\", depende del arreglo de hit count)\n"
        "**bonus skill constant:**\n"
        "* 1er hit: boss def * 0.25\n"
        "* 2do hit: boss def * 0.5\n"
        "* 3er hit: boss def * 0.75\n"
        "* 4to hit: boss def\n"
        "* 5to hit: boss def\n"
        "**Número de golpes:** 5 hits; 1 hit/carga\n"
        "**Alcance máximo de Cast:** 24m\n"
        "**Alcance máximo del golpe:** 45m; AoE lineal\n"
        "**MP recovery:** Attack MP Recovery * 1.5 * número de hits sin Graze al objetivo principal"
    ),
)

VANQUISHER = SkillText(
    title="Vanquisher",
    description="**Descripción del juego:** *\"Asesta un golpe poderoso a un área pequeña. El poder se dispersa si hay múltiples objetivos en el área. Cuanto más cerca estés del objetivo, más se ignoran el Guard y la Evasion.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {bow} / {bowgun}\n"
        "**Coste MP:** 1200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Cuando tengas el debuff Ignite, usar esto eliminará el debuff Ignite inmediatamente. También puede evitar la dispersión de poder a múltiples objetivos dentro del área. Y también otorga el atributo Perfect Aim\n"
        "*  El daño de esta habilidad se ve afectado ya sea por SRD% o LRD% según cuál de ellos sea mayor\n"
        "*  Si estás usando un Bowgun y tienes 5 o más stacks de \"Twin Storm\" disponibles; al lanzar \"Vanquisher\", consumes 5 stacks de \"Twin Storm\" para duplicar el daño de \"Vanquisher\" y recuperas 600 MP\n"
        "*  El bypass de Evasion/Guard tiene un mecanismo similar a anticipate/Guard break pero sin el aviso emergente\n\n"
        "**Bow/Bowgun bonus:** Si tienes el debuff Ignite, activar esta habilidad lo eliminará, garantizará hits y evitará que el poder se disperse\n"
        "**Bowgun bonus:** Si tienes 5 o más \"Overheat stacks\" de Twin Storm, se consumirán 5 stacks para potenciar Vanquisher\n"
        "**MD Bonus:** Reemplaza \"BaseDEX/100\" en Skill Multiplier por \"BaseINT/100\"; todo lo demás permanece igual\n"
        "**Dagger bonus:** Cambia de un AoE a un ataque de un solo objetivo\n\n"
        "**Base Skill Multiplier:** 5 + Skill Level + BaseDEX/100\n"
        "**Base Skill Constant:** 1200\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 8m\n"
        "**Alcance del golpe:** 8m con 0.5m de radio de daño\n"
        "**Evasion/Guard bypass chance:** MIN(100;(20% * (8 - range)))"
    ),
)

TWIN_STORM = SkillText(
    title="Twin Storm",
    description="**Descripción del juego:** *\"Mejora enormemente el ataque normal y también aumenta la velocidad de movimiento. Se acumulan Overheat stacks cada vez que un ataque normal golpea, y el estado de la habilidad se puede eliminar al reactivar la habilidad.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {bowgun}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto del Buff:**\n"
        "*  1.5x tu velocidad de movimiento mientras el buff esté activo; esto es anulado por el ailment Stop y se acumula con el ailment Slow\n"
        "*  El Total AMPR se duplica durante este buff de stack\n"
        "*  Bonus de Attack Speed: +100 * Skill Level\n"
        "*  Final Damage Modifier para Shot/Hunter Skills (incluyendo Twin Storm): +TRUNC(Stack/25) * 10%\n"
        "*  Bleed, Freeze y Stun a tu personaje disminuirán los stacks de Twin Storm en 15; Bleed desactiva Twin Storm; Freeze desactiva la ganancia de stacks de Twin Storm\n\n"
        "**Auto Attacks Skill Multiplier:** +0.9 * Skill Level + MIN(4;TRUNC((Stack-1)/15)) * (0.2 * Skill Level) [nota: igual que Rampage, este multiplicador funciona de forma aditiva con otros Auto Attacks Skill Multiplier como Kairiki, etc.]\n"
        "**Auto Attacks Skill Constant:** +0\n"
        "**Auto Attacks Hit Count:** 2 hits; el cálculo de daño se realiza una vez, luego se divide entre los hits\n"
        "**Twin Storm Stability Decrease:** -MAX(0;ROUNDDOWN((Stack-31);-1))% o -10% cada 10 stacks a partir del 41.\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Reemplaza los autoataques del usuario por autoataques de Twin Storm\n"
        "*  Autoataques necesarios para aumentar un stack: MAX(1;MIN(4;TRUNC((Current Stack-1)/15))) o\n"
        "0-30 stk = 1 autoataque\n"
        "31-45 stk = 2 autoataques\n"
        "46-60 stk = 3 autoataques\n"
        "61-98 stk = 4 autoataques\n\n"
        "**Bowgun Bonus:** Buff de \"Overheat stack\". El poder de los ataques normales, Shot Skills y Hunter Skills aumenta a medida que se acumulan Overheat stacks. La Stability disminuye si se acumulan demasiados Overheat stacks\n"
        "**Magic Device Bonus:** Realiza ataques normales con MATK si MATK es mayor que ATK (aún usa cálculo físico). Aumenta Auto Attacks Skill Constant por BaseINT/2 independientemente de si ATK o MATK es mayor\n\n"
        "**Dagger Bonus:** Siempre aplica el poder del ataque de rango cercano o el ataque de rango largo, el que sea mayor\n"
        "Power Wave no se desactiva durante este buff de Twin Storm. (Afecta el rango máximo del autoataque y el modificador de daño del autoataque)\n"
        "Esta habilidad no se puede poner en un combo"
    ),
)

QUICK_LOADER = SkillText(
    title="Quick Loader",
    description="**Descripción del juego:** *\"Activa Cross Fire y aumenta su carga en 1 nivel si no está completamente cargado. Esta habilidad no se sobrescribe.\"*",
    details=(
        "**T5;** Solo {bow} / {bowgun}\n"
        "**Coste MP:** 400\n\n"
        "**Efecto del Buff:**\n"
        "*  Al usarlo, obtienes 3 cargas de Quick Loader. Puedes usar esta habilidad de nuevo pero no sobrescribirá este buff (debes esperar a que termine el buff para obtenerlo de nuevo)\n"
        "*  Penalidad Bowgun: -1 carga de Quick Loader al usarlo\n"
        "*  Cuando uses Cross Fire que no esté completamente cargado, automáticamente usarás 1 carga de Quick Loader para +1 carga de CF\n"
"*  Si ya has aprendido Sneak Attack, usar esta habilidad te otorga automáticamente su buff basado en el nivel de dicha habilidad. Sin embargo, su nivel activado no puede exceder el nivel de esta habilidad\n"
"*  Usar Quick Loader nuevamente mientras su buff sigue activo agrega +(5% * Skill Level) de motion speed a la siguiente habilidad y recupera (MP Consumido por Quick Loader/2) MP\n"
        "*  Esta habilidad tiene motion máximo por defecto\n\n"
        "**Duración del Buff:** (120 - 6 * Skill Level) segundos\n"
        "Nota: La motion speed de esta habilidad siempre está establecida en +50%."
    ),
)

RETROGRADE_SHOT = SkillText(
    title="Retrograde Shot",
    description="**Descripción del juego:** *\"Una técnica de disparar a los enemigos mientras te mueves hacia atrás. Ataca en un rango lineal y el objetivo con más HP que reciba un golpe será marcado.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {bow}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Esta habilidad tiene 50% de Physical Pierce% en el hit adicional\n"
        "*  Normalmente, usar esta habilidad te hará retroceder 5m desde el objetivo. Pero si usas esta habilidad mientras te mueves hacia adelante al mismo tiempo, te quedarás ahí en lugar de retroceder\n"
        "*  Tiene la habilidad de reducir cualquier daño recibido a 0 una sola vez durante la animación de la habilidad (similar al iframe de zantei, no detiene la carga de CF cuando recibes un golpe durante este tiempo, pero no puede evitar que GSW/Aura desaparezcan al recibir un hit). Nota: Aún puedes reducir el daño recibido a 0 incluso sin retroceder\n"
        "*  Usar esta habilidad también puede dar un efecto de marca al objetivo, este efecto de marca dura (10 + 2 * Skill Level) segundos. Sin embargo, si esta habilidad golpea a múltiples enemigos, solo da 1 efecto de marca al enemigo con más HP\n"
        "*  El objetivo marcado verá su dodge/flee reducido en [(TotalDEX+TotalSTR)*0.04]% y recibe más Daño Adicional cada vez que recibe hit de algun Shot/Hunter skills\n"
        "*  Este Daño Adicional se ve afectado por srd/lrd%, pero no por Long Range de Shot Skills y combo tags de daño. Este Daño Adicional se basa en proration física\n"
        "*  Esta habilidad no se ve afectada por motion speed; si el dash se cancela (manteniendo hacia adelante), se vuelve 14 frames más lenta\n\n"
        "**Efecto de la marca:**\n"
        "*  Reduce la tasa de dodge del objetivo marcado\n"
        "*  La marca también es visible para los miembros del equipo\n"
        "*  Inflige daño adicional cuando el objetivo marcado recibe un hit de algun Shot/Hunter Skill y el poder continúa aumentando hasta un cierto número de veces.\n"
        "[nota: solo el lanzador puede activarlo con su propia habilidad]\n\n"
        "**Daño Adicional al objetivo marcado por hit con Shot/Hunter skills:**\n"
        "**Multiplicador para cada hit:** 1\n"
        "**Constante para cada hit:** 0\n"
        "Por cada hit adicional, el multiplicador del siguiente hit adicional aumenta en (TotalDEX * Skill Level/100)%. Este efecto puede obtener hasta (Floor(Skill Level/4) + 3) veces\n\n"
        "Para resumir, este multiplicador adicional aumenta cada vez que se activa un hit adicional:\n"
        "[1er adicional: 1], [luego 2do adicional: 1 + dex bonus], [luego 3er adicional: 1 + 2x dex bonus], etc.\n\n"
        "**Base Skill Multiplier:** 5 + 0.5 * Skill Level + BaseDex/100\n"
        "**Base Skill Constant:** 300\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** 12m\n"
        "**Alcance del golpe:** 100m con 2.5m de radio de daño"
    ),
)

PARABOLA_CANNON = SkillText(
    title="Parabola Cannon",
    description="**Descripción del juego:** *\"Ataca disparando un proyectil en una trayectoria parabólica. Es un ataque AoE, y cuanto más lejos está el proyectil del objetivo, más rápido viaja. Baja chance de infligir [Silence].\"*",
    details=(
        "**Habilidad Tier 5;** Solo {bow} / {bowgun} / {arrow}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Ailment:** Silence\n"
        "**Chance de Ailment (Golpe Principal):** 2% * Skill Level\n"
        "**Chance de Ailment (trampa):** 10% * Skill Level\n"
        "**Resistencia a Ailment:** 5s\n\n"
        "**Efecto de la habilidad:**\n"
        "*  Si eres Bow o Bowgun, tras el impacto del Golpe Principal, colocará una trampa de seguimiento. Esta trampa explotará al encontrar cualquier enemigo en un radio de 1m. Sin embargo, la trampa desaparecerá si recibe un golpe AoE (incluso si está en el aire). Esta trampa durará 1 minuto.\n"
        "*  Esta habilidad es siempre un ataque homing incluso cuando la usas desde 24m (incluso sin el buff de Retrograde Shot).\n"
        "*  El daño de esta habilidad solo es afectado por LRD%, sin importar la distancia entre tú y el objetivo, siempre usa LRD%.\n\n"
        "**Bow/Bowgun Bonus:** Mantén presionada una tecla de movimientopara rodar hacia esa dirección cuando se activa la habilidad. Cuando golpea o alcanza al objetivo, se convierte en una trampa y se activa 1 segundo después. La trampa aumentará enormemente la chance de infligir [Silence]. Como Bow/Bowgun, si usas esta habilidad cuando hay una trampa anterior presente, esa trampa anterior desaparecerá.\n\n"
        "**Base Skill Multiplier (Golpe Principal):** 7.5 + 0.25 * Skill Level + TotalDEX/100\n"
        "**Base Skill Constant (Golpe Principal):** 40 * Skill Level\n"
        "**Número de golpes:** 1 Hit AoE\n"
        "**Alcance máximo de Cast:** 24m\n"
        "**Alcance del golpe:** (0.5 * Skill Level)m de radio\n\n"
        "**Base Skill Multiplier (trampa):** 10 + 0.25 * Skill Level + BaseDEX/100\n"
        "**Base Skill Constant (trampa):** 400\n"
        "**Número de golpes:** 1 Hit AoE"
    ),
)

SPREAD_SHOT = SkillText(
    title="Spread Shot",
    description="**Descripción del juego:** *\"Ataca usando 5 flechas hábilmente controladas. Chance de infligir un ailment (elemento del arma) al objetivo. Cada hit en el mismo objetivo mejora ligeramente su rendimiento. También puedes cambiar la dirección de las flechas disparadas usando las teclas direccionales.\"*",
    details=(
        "**Habilidad Tier 5; [Activo]** Solo {bow} / {bowgun}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n\n"
        "**Ailment:** Ninguno (con elemento Neutral); Ignite (con elemento Fire); Freeze (con elemento Water); Dazzled (con elemento Wind); Poison (con elemento Earth); Weaken (con elemento Light); Curse (con elemento Dark)\n"
        "**Chance de Ailment:** 1.2 * Skill Level% (cuando múltiples hits se registran en el objetivo, la chance de ailment se acumula; por lo tanto, será 100% cuando 5 hits se registren al usar Bow en nivel de habilidad 9-10)\n"
        "**Resistencia a Ailment:** 10 segundos\n"
        "*  La habilidad Element Starter puede hacer que inflijas 2 ailments al usar un Bow/Arrow de elemento diferente; los registlets de Element Talent funcionan y hacen que inflijas solo el ailment relacionado con el elemento del registlet\n\n"
        "Esta habilidad no se ve afectada por short/long range damage; no afectada por Long Range Skill; usa e inflige proration física\n\n"
        "**Bow Bonus:** La chance de infligir un ailment se duplica. Los hits adicionales de \"Retrograde Shot\" pueden ocurrir hasta 4 veces\n"
        "**Bowgun Bonus:** El poder se duplica (Base Skill Multiplier * 2) cuando se activa usando una tecla direccional (izquierda/derecha)\n\n"
        "**Ignore Defense:** (30 + 5 * Skill Level)% (multiplicado por separado de \"Armor Break\" y \"Physical Pierce\")\n"
        "**Alcance máximo de Cast:** 12m; AoE\n\n"
        "**Número de golpes:** 2 o 5 (depende del uso de teclas direccionales al lanzar)\n"
        "* Sin dirección: 5 Hits en forma de abanico\n"
        "* Frente/Atrás: [Bow] 5 Hits lineales dispuestos en fila. [Bowgun] 5 Hits lineales tipo gatling\n"
        "* Izquierda/Derecha: 1er Hit > tu personaje realiza [Evasion] rodeando 90° al objetivo > 2do Hit\n\n"
        "**Base Skill Multiplier (cada Hit):** 2 + 0.1 * Skill Level\n"
        "**Base Skill Constant (cada Hit):** 200"
    ),
)

ELEMENT_STARTER = SkillText(
    title="Element Starter",
    description="**Descripción del juego:** *\"El elemento del Bow o Bowgun se activará al mismo tiempo que la flecha. *No válido para habilidades de Elemento Dual. Obtiene una pequeña barrera de recuperación cada vez que infliges daño a objetivos con el elemento al que eres débil.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {bow} / {bowgun}\n\n"
        "**Efecto Pasivo:**\n"
        "*  Permite que las habilidades que no son de Elemento Dual tengan [\"Arma Principal Ele\" y \"Arrow Ele\"/\"Katana Ele\" (si Samurai Archery está en Nivel 10)] como Elemento Dual al mismo tiempo en lugar de solo Arrow Ele o Arma Principal Ele (si no tienen Arrow Ele). Sin embargo, si las habilidades que no son de Elemento Dual tienen un elemento fijo, entonces el elemento fijo reemplazará Arrow/Katana Ele, haciéndolo como [\"Arma Principal Ele\" y \"Ele Fijo\"] como Elemento Dual al mismo tiempo\n"
        "*  Gana +1 stack cada vez que infliges un elemento más fuerte contra el objetivo. Puedes almacenar hasta 99 stacks. Su stack se usará para HP Recovery cada vez que seas atacado. HP Recovery = Floor(Skill Level * tu MaxHP/1000) * stack"
    ),
)

SAMURAI_ARCHERY = SkillText(
    title="Samurai Archery",
    description="**Descripción del juego:** *\"Aumenta ligeramente el ATK y la estabilidad si un Bow y una Katana están equipados al mismo tiempo. Si se realiza un ataque normal con la Katana, accuracy de la siguiente habilidad usada aumenta.\"*",
    details=(
        "**Habilidad Tier 5;** Solo Sub Katana\n\n"
        "**Efecto Pasivo:**\n"
        "*  WATK aumenta en (BaseWATK de Katana * 0.1 * Skill Level), pero solo hasta un máximo de (BaseWATK de Bow * baseStability de Bow * 0.1 * Skill Level)\n"
        "*  La estabilidad aumenta en (BaseStability de Katana/4) independientemente del nivel\n"
        "*  Cuando usas con éxito un ataque normal con una Katana, Incrementa Accuracy en (Skill Level * stack)%. Este buff de accuracy dura hasta la siguiente habilidad usada. El stack máximo es 10."
    ),
)
