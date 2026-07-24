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

ENHANCED_AUTO_ATTACK = SkillText(
    title="Autoataque Mejorado",
    description=(
        "* Al usar Main Katana (no Sub-Katana), obtienes pasivamente la habilidad de hacer un dash después de un autoataque (todo lo que necesitas es autoataque y moverte al mismo tiempo). Lo llamamos 'Enhanced auto-attack buff'.\n"
        "Este buff duplica el daño total de tu autoataque (se acumula multiplicativamente con otros modificadores de autoataque como Kairiki, Nukiuchi, Berserk, etc.), otorga un 50% de bonus de AMPR y también otorga Absolute Critical en el enhanced auto-attack. Este buff termina después de usar un autoataque.\n\n"
        "* Además, puedes hacer un dash después de usar una habilidad y también obtener el Enhanced auto-attack buff. Estas habilidades son Pulse Blade, Hasso Happa, Bouncing Blade, Shadowless Slash. Bow+katana puede realizar esto, pero no puede obtener el Enhanced auto-attack buff."
    ),
    details="",
)

ISSEN = SkillText(
    title="Issen",
    description="**Descripción del juego:** *\"Abre a un enemigo a una velocidad cegadora. Alto Critical Rate en el segundo hit.\"*",
    details=(
        "**Habilidad Tier 1;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 0.5\n"
        "**Base Skill Multiplier (Segundo Hit):** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant (Primer Hit):** 0\n"
        "**Base Skill Constant (Segundo Hit):** 50 + 5 * Skill Level\n"
        "**Número de golpes:** 2 hits; el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* El segundo hit tiene un boost de Critical Rate de 200%;\n"
        "el boost se aplica de la siguiente manera:\n"
        "Issen Segundo Hit Critical Rate = Critical Rate total * 3"
    ),
)

PULSE_BLADE = SkillText(
    title="Pulse Blade",
    description="**Descripción del juego:** *\"Haz un corte aéreo a un enemigo desde la distancia. El daño disminuye cuanto más te alejas del objetivo. Puedes moverte al envainar la katana.\"*",
    details=(
        "**Habilidad Tier 1;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 0.5\n"
        "**Base Skill Multiplier (Segundo Hit):** 0.5 + Skill Level * 0.05\n"
        "**Base Skill Multiplier (Tercer Hit):** 0.5 + Skill Level * 0.1\n"
        "**Base Skill Constant:** 30 + Skill Level; constante para cada hit\n"
        "**Número de golpes:** 3 hits; los cálculos de crítico se realizan una vez y se copian a los otros hits; el resto del cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** 12m\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* Esta habilidad tiene una penalidad de DEF (o podría ser pierce físico negativo) basada en el nivel de la habilidad y la distancia entre el lanzador y el mob;\n"
        "la penalidad se aplica de la siguiente manera\n"
        "Distance Penalty = distancia al mob - Katana Max Auto Attack Range; este valor no puede ser menor a 0\n"
        "Target's Pulse Blade DEF = DEF del objetivo * (1 + Distance Penalty * (11 - Skill Level)/100)\n"
        "* Si esta habilidad se usa fuera de un combo o como la última habilidad de un combo, y no estás afectado por el ailment Slow o el ailment Stop, puedes hacer dash en cualquier dirección usando el \"trackball\" de movimiento durante la animación de envainado de la habilidad"
    ),
)

TRIPLE_THRUST = SkillText(
    title="Triple Thrust",
    description="**Descripción del juego:** *\"Acércate rápidamente y clava a un objetivo. Muévete detrás de un objetivo al atacar. Aumenta un poco el daño de la siguiente habilidad.\"*",
    details=(
        "**Habilidad Tier 2;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1.5 + 0.2 * Skill Level + TotalAGI/500; multiplicador total de todos los hits\n"
        "**Base Skill Constant:** 0; constante total de todos los hits\n"
        "**Número de golpes:** 3 hits; el cálculo de daño se realiza una vez y se divide equitativamente entre los hits\n"
        "**Alcance máximo de Cast:** 12m\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* Esta habilidad te moverá al otro lado de tu objetivo\n\n"
        "**Efecto del Buff:** Aumenta Skill Constant de la siguiente habilidad de ataque;\n"
        "el aumento se calcula de la siguiente manera:\n"
        "Triple Thrust Skill Constant Increase = Player Level/(11 - Skill Level)\n"
        "**Duración del Buff:** Hasta que se use una habilidad de ataque o cualquier habilidad\n\n"
        "Algunas habilidades tienen interacciones específicas con el buff de Triple Thrust's"
    ),
)

HASSO_HAPPA = SkillText(
    title="Hasso Happa",
    description="**Descripción del juego:** *\"Abre a todos los enemigos en un cierto espacio. Inflige daño a los enemigos a tu alrededor sin Miss. Puedes moverte al envainar la katana.\"*",
    details=(
        "**Habilidad Tier 3;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primer Hit):** 2.2 (nivel 1); 2.3 (nivel 2); 2.4 (nivel 3); 2.5 (nivel 4); 2.6 (nivel 5); 2.7 (nivel 6); 2.8 (nivel 7); 2.9 (nivel 8); 3 (nivel 9); 6 (nivel 10)\n"
        "**Base Skill Multiplier (Otros Hits):** 2.2 (nivel 1); 2.3 (nivel 2); 2.4 (nivel 3); 2.5 (nivel 4); 2.6 (nivel 5); 2.7 (nivel 6); 2.8 (nivel 7); 2.9 (nivel 8); 3 (niveles 9 y 10); multiplicador para cada hit\n"
        "**Base Skill Constant:** 130 + 2 * Skill Level\n"
        "**Número de golpes del Primer Hit:** 1 hit (niveles 1 a 10)\n"
        "**Número de golpes de Otros Hits:** 0 hit (niveles 1 a 3); 1 hit (niveles 4 a 6); 2 hits (niveles 7 a 10); el cálculo de daño se realiza para cada hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n"
        "**Alcance del golpe (Todos los Hits):** 2m (niveles 1 y 2); 3m (niveles 3 a 6); 4m (niveles 7 a 10); alrededor del lanzador\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* Esta habilidad tiene el atributo Perfect Aim\n"
        "* Si esta habilidad se usa fuera de un combo o como la última habilidad de un combo, y no estás afectado por el ailment Slow o el ailment Stop, puedes hacer dash en cualquier dirección usando el \"trackball\" de movimiento durante la animación de envainado de la habilidad\n"
        "* **[Solo Main Katana]** Si usas esta habilidad después de Kasumisetsu Getsuka, entonces usarás una versión mejorada, Sakura Ranman, que añade un multiplicador extra ~~(+1 + 0.5 + 0.5)~~ (+1 +1 +1) a cada hit correspondiente en comparación con el multiplicador original de Hasso. Además, otorga +300 MP de recuperación por cada hit exitoso de Sakura Ranman [límite de 600 MP].\n\n"
        "Nota sobre Sakura Ranman: Dado que Kasumisetsu Getsuka otorga 1 stack de Sakura. Así que para activar Sakura Ranman, solo necesitas tener ese 1 stack de Sakura y usar Hasso Happa en cualquier momento.\n\n"
        "El buff a la constante de Triple Thrust's se divide por el Número de golpes\n"
        "El daño de esta habilidad ~~no es afectado~~ **es afectado** por Whack, pero es afectado por los modificadores de Short Range Damage independientemente de la distancia"
    ),
)

TENRYU_RANSEI = SkillText(
    title="Tenryu Ransei",
    description="**Descripción del juego:** *\"Abre consecutivamente con furia. El poder aumenta durante un tiempo cada vez que usas la habilidad (4 veces como máximo). Se aplica un ataque especial a Madagachi/Zantei Settetsu al cumplir ciertas condiciones y la duración del buff aumenta.\"*",
    details=(
        "**Habilidad Tier 4;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1.5 + 0.25 * Skill Level; multiplicador total de todos los hits\n"
        "**Base Skill Constant:** 10 * Skill Level; constante total de todos los hits\n"
        "**Número de golpes:** 4 hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* La habilidad tiene un modificador de Motion Speed de (125 - 15 * número de stacks[máx 3 stacks])%;\n"
        "* Si tu última acción fue Tenryu Ransei, entonces usar Tenryu Ransei de nuevo no infligirá proration. Nota: Autoataque se considera una acción, por lo que hacer Tenryu luego auto luego Tenryu luego auto repetidamente, tampoco aumenta el daño de proration de Tenryu.\n\n"
        "**Efecto del Buff:**\n"
        "* Cada vez que se usa la habilidad, ganas un stack; puedes tener un máximo de 4 stacks\n"
        "* El Coste MP de esta habilidad se vuelve 100\n"
        "* No puedes renovar la duración del buff usando esta habilidad\n"
        "* Si atacas con éxito con **\"Madagachi\" o \"Kasumisetsu Getsuka\"** O haces un parry exitoso con **Zantei Settetsu** mientras el buff está activo, el buff de Tenryu Ransei se extiende, pero pierdes todos los stacks; puedes renovar la duración del buff con Madagachi o Zantei Settetsu o Kasumisetsu Getsuka; si la duración del buff expira justo después de hacerlo, el buff se reactiva; el reinicio de stacks se aplica después de Tenryu Ransei: Zannou/Zanyu\n"
        "* Tenryu Ransei: Zannou con Zantei Settetsu no puede infligir Armor Break\n"
        "* Attack Accuracy de Tenryu Ransei +(1 + número de stacks) * 10; este efecto solo se activa si tienes al menos 1 stack; solo toma en cuenta un máximo de 3 stacks\n"
        "* Base Skill Multiplier * (1 + número de stacks); solo toma en cuenta un máximo de 3 stacks\n"
        "* Mientras no tengas el ailment Paralysis, tu delay de autoataque se establece a 0; esto no incluye los delays de Fear ni de tocar una parte\n"
        "**Efecto del Buff:** 10 segundos (con Tenryu Ransei); 30 segundos (con Madagachi y Zantei Settetsu); 10 + número de stacks del buff de Tenryu Ransei * 10 segundos (con Kasumisetsu Getsuka)"
    ),
)

GARYOU_TENSEI = SkillText(
    title="Garyou Tensei",
    description="**Descripción del juego:** *\"El corte definitivo. El poder aumenta cada vez que usas ciertas habilidades de Mononofu (10 veces como máximo). El poder aumenta contra objetivos infligidos con [Armor Break]. La Critical Rate es extremadamente baja.\"*",
    details=(
        "**Habilidad Tier 4;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** MAX[0.2 * Skill Level; (0.2 * Skill Level + número de stacks/10) * número de stacks]\n"
        "**Base Skill Constant:** 100\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad tiene Critical Rate -(110 - 10 * Skill Level)\n"
        "* Al usarla, esta habilidad eliminará el buff de Kairiki Ranshin. A cambio, Kairiki puede otorgar 100 de flat crit rate y 100% de physical pierce a esta habilidad\n"
        "* Si el objetivo tiene el ailment Armor Break, Skill Constant se multiplica por 10\n"
        "* Después de usar esta habilidad, otorgará buffs que pueden reducir el daño recibido en (5% x número de stacks). Y su duración = (número de stacks) segundos\n"
        "* NO es Unsheathe Attack\n"
        "* Si usas esta habilidad nivel 10 y tienes 10/10 stacks completos durante la animación de Shadowless Slash, esta habilidad se convertirá en [Divine Slash](https://discord.com/channels/565365471805833216/567994630679953408/967839971316748368)\n\n"
        "**Efecto del Buff:**\n"
        "* Cada vez que se usa una habilidad de ataque del Mononofu Skill Tree o cada vez que haces un autoataque mejorado (ataque después de dash) con Main Katana, esta habilidad gana un stack; puedes tener un máximo de 10 stacks\n"
        "**Efecto del Buff:** Hasta que lances Garyou Tensei\n\n"
        "**Efecto Pasivo:**\n"
        "* Cada stack de Garyou aumenta +2% el daño de todas las habilidades de Mononofu (incluye Garyou Tensei y Divine Slash) independientemente del nivel de Garyou. Sin embargo, el buff de daño pasivo siempre se fija en +20% independientemente del stack de Garyou actual **si tienes el buff de reducción de daño de Garyou presente/activo** (esto sucede después de usar Garyou/Divine. Y su duración depende del stack de Garyou, que es +1s por stack)."
    ),
)

POMMEL_STRIKE = SkillText(
    title="Pommel Strike",
    description="**Descripción del juego:** *\"Golpea a un enemigo con el pomo. Chance de infligir [Paralysis]. Chance de infligir [Stun] si el objetivo está paralizado.\"*",
    details=(
        "**Habilidad Tier 1;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Físico\n"
        "**Elemento:** Neutral\n\n"
        "**Base Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "**Base Skill Constant:** 100 + 10 * Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n\n"
        "**Efecto de la habilidad:** Si el objetivo ya tiene el ailment Paralysis, infligirá el ailment Stun en su lugar\n\n"
        "**Ailment Primario:** Paralysis\n"
        "**Chance de Ailment Primario:** 50% + (5 * Skill Level)%\n"
        "**Duración de Ailment Primario:** 10 segundos\n"
        "**Resistencia a Ailment Primario:** Ninguna\n\n"
        "**Ailment Secundario:** Stun\n"
        "**Chance de Ailment Secundario:** (5 * Skill Level)%\n"
        "**Duración de Ailment Secundario:** 5 segundos\n"
        "**Resistencia a Ailment Secundario:** 25 segundos (Easy, Normal, Hard y Nightmare); 30 segundos (Ultimate)\n\n"
        "Mind's Eye detendrá la habilidad si el objetivo tiene el ailment Paralysis"
    ),
)

MAGADACHI = SkillText(
    title="Magadachi",
    description="**Descripción del juego:** *\"Parry el ataque de un enemigo y reduce el daño solo una vez. Anula los ailments, recupera un poco de MP y permanece con al menos 1 HP al recibir daño fatal con cierta cantidad de HP. Solo inflige daño si no haces parry.\"*",
    details=(
        "**Habilidad Tier 2;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 2 + 0.3 * Skill Level\n"
        "**Base Skill Constant:** 100 + 10 * Skill Level\n"
        "***Tenryu Ransei: Zannou*** Skill Multiplier: 13 + Floor(Base Skill Multiplier of Tenryu * 100 * número de stacks en el buff de Tenryu Ransei/2)/100\n"
        "***Tenryu Ransei: Zannou*** Skill Constant: 300\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n\n"
        "**Efecto de la habilidad:**\n"
        "* Si el buff no se elimina antes de que termine la animación de levantar la katana, la habilidad simplemente infligirá daño; si el buff se elimina antes de que termine la animación de levantar la katana, la animación de la habilidad cambia y no infliges daño\n"
        "* Si ocurre el primer escenario del efecto anterior mientras el buff de Tenryu Ransei está activo, el ataque normal se reemplaza por Tenryu Ransei: Zannou; se considera como un Unsheathe Attack, otorga invencibilidad durante 2 segundos O hasta 0.5 segundos después de que termine la animación y tiene el atributo Perfect Aim\n\n"
        "**Efecto del Buff:**\n"
        "* Reduce el daño Físico y el daño Fraccional recibido en 90%; reduce el daño Mágico recibido en 45%\n"
        "* Si el daño recibido aún te mataría mientras estás al 20% de tu MaxHP o más, sobrevivirás con 1 HP\n"
        "* Niega cualquier ailment asociado con el hit de daño reducido\n"
        "* Recupera 100 + (10 * Skill Level) MP si el buff se elimina por recibir daño. Sin embargo, si esta habilidad se usa en un combo, entonces -100 MP de recuperación\n"
        "**Duración del Buff:** Hasta que termine la animación de levantar la katana O hasta que recibas un hit de daño\n\n"
        "Esta habilidad no hará proration al hacer un parry exitoso.\n"
        "El boost de Skill Constant de Triple Thrust's se aplica al ataque normal, pero no a Tenryu Ransei: Zannou."
    ),
)

ZANTEI_SETTETSU = SkillText(
    title="Zantei Settetsu",
    description="**Descripción del juego:** *\"Abre a un enemigo con furia absorbiendo su ataque. Anula el daño una vez y hace un ataque adicional. Chance de infligir [Armor Break] con él.\"*",
    details=(
        "**Habilidad Tier 3;** Solo Main/Sub {katana}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 1 + 0.2 * Skill Level; multiplicador total de todos los hits\n"
        "**Base Skill Multiplier (Counter):** 5 + 1 * Skill Level\n"
        "**Base Skill Constant:** 10 * Skill Level; constante total de todos los hits\n"
        "**Base Skill Constant (Counter):** 30 * Skill Level\n"
        "**Tenryu Ransei: Zannou Skill Multiplier:** 13 + Floor(Base Skill Multiplier of Tenryu * 100 * número de stacks en el buff de Tenryu Ransei/2)/100\n"
        "**Tenryu Ransei: Zannou Skill Constant:** 300\n"
        "**Número de golpes:** 4 hits; el cálculo de daño se realiza una vez y se divide equitativamente entre los hits\n"
        "**Número de golpes del Counter:** 1 hit; el cálculo de crítico se copia de los 4 hits anteriores; el resto del cálculo de daño se realiza independientemente de los 4 hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* Si el buff se elimina antes de que termine la animación de corte, la animación de envainado de la habilidad se reemplaza por un ataque adicional\n"
        "* Si ocurre el efecto anterior mientras el buff de Tenryu Ransei está activo, el contraataque se reemplaza por Tenryu Ransei: Zannou; se considera como un Unsheathe Attack, otorga invencibilidad durante 2 segundos O hasta 0.5 segundos después de que termine la animación y tiene el atributo Perfect Aim. Pero no puede infligir Armor Break.\n\n"
        "**Efecto del Buff:**\n"
        "* Reduce el daño recibido a 0 (aún cuenta como recibir daño)\n"
        "* Niega cualquier Flinch, Tumble, Stun o Knockback asociado con el hit anulado\n"
        "**Duración del Buff:** Hasta que termine la animación de corte O hasta que recibas un hit de daño\n\n"
        "**Ailment del Counter:** Armor Break\n"
        "**Chance de Ailment del Counter:** 50% + (5 * Skill Level)%\n"
        "**Duración de Ailment del Counter:** 5 segundos\n"
        "**Resistencia a Ailment del Counter:** Ninguna\n\n"
        "El boost de Skill Constant de Triple Thrust's se aplica a los primeros 4 hits, pero no al hit del counter ni a Tenryu Ransei: Zannou"
    ),
)

BUSHIDO = SkillText(
    title="Bushido",
    description="**Descripción del juego:** *\"Aprende a ser un Mononofu. HP, MP y Accuracy aumentan un poco. ATK aumenta al equipar una Katana.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}/Solo Main {katana} (según el efecto)\n\n"
        "**Efecto Pasivo:**\n"
        "* Max HP +(10 * Skill Level); Max MP +(10 * Skill Level); Accuracy +(Skill Level)\n"
        "* Weapon ATK +(3 * Skill Level)%; ATK +1% (niveles 1 y 2)/ +2% (niveles 3 a 7)/ +3% (niveles 8 a 10); estos efectos solo se aplican si estás usando una Katana en el slot de arma principal"
    ),
)

TWO_HANDED = SkillText(
    title="Two-Handed",
    description="**Descripción del juego:** *\"Empuña el arma con ambas manos. Varios stats mejoran si el Sub-Weapon está vacío. El Critical Damage con una Katana aumenta enormemente.\"*",
    details=(
        "**Habilidad Tier 1;** Sin Restricciones {all}/Solo Main {katana} (según el efecto)\n\n"
        "**Efecto Pasivo:**\n"
        "* Weapon ATK +(Skill Level)%; Accuracy +(Skill Level)%; Critical Rate +(Skill Level); Stability +(Skill Level)%; estos efectos solo se aplican si no tienes equipo en el slot de arma secundaria\n"
        "* Si estás usando una Katana en el slot de arma principal, no tienes equipo en el slot de arma secundaria [excepto Ninjutsu scroll con la habilidad pasiva ninjutsu \"Ninja Spirit\"], y usas un autoataque o habilidad que hace crítico, tu ATK total aumenta en (5 * Skill Level)% para ese ataque;\n"
        "el aumento se calcula de la siguiente manera:\n"
        "Two-Handed Crit ATK = Total ATK * (1 + 0.05 * Skill Level)\n\n"
        "**Penalidad si no es Main Katana:** El bonus de Critical Rate se reduce a la mitad\n"
        "**Penalidad si no es Main Katana:** El bonus de Stability se reduce a la mitad\n"
        "NO CREAS en la descripción de esta habilidad cuando dice \"Critical Damage\"; es muy engañoso"
    ),
)

MEIKYO_SHISHUI = SkillText(
    title="Meikyo Shishui",
    description="**Descripción del juego:** *\"Agudiza tu enfoque. La Critical Rate aumenta enormemente por un corto tiempo y el Critical Damage, DEF y MDEF disminuyen. El efecto termina cuando usas otra habilidad.\"*",
    details=(
        "**Habilidad Tier 2;** Sin Restricciones {all}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto del Buff:**\n"
        "* Critical Rate +20 + (2 * Skill Level)\n"
        "* DEF -(100 * (11 - Skill Level)); MDEF -(100 * (11 * Skill Level))\n"
        "* Critical Damage -(15 - Skill Level)%\n"
        "**Duración del Buff:** 10 segundos + (2 * Skill Level) segundos O hasta que uses una habilidad\n"
        "La siguiente habilidad después de esta puede obtener este efecto de bonus de crit rate y penalidad de crit dmg\n\n"
        "**Katana Main/Sub bonus:** Critical Rate +25\n"
        "**Katana Main/Sub bonus:** La reducción de Critical Damage% se anula\n"
        "**Katana Main/Sub bonus:** La duración del Buff se duplica\n"
        "Si usas Decoy después de esta habilidad, entonces el señuelo puede disfrutar del bonus de crit rate todo el tiempo hasta que termine."
    ),
)

SHUKUCHI = SkillText(
    title="Shukuchi",
    description="**Descripción del juego:** *\"Una técnica para moverse rápido. Muévete rápidamente dentro del rango al hacer ataques normales. Aumenta la capacidad del siguiente ataque normal. No disponible durante [Slow/Stop].\"*",
    details=(
        "**Habilidad Tier 3;** Sin Restricciones {all}\n"
        "**Coste MP:** 0\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Alcance máximo de Cast:** Teóricamente infinito (limitado a 24m por el límite de targeting de autoataque; se vuelve infinito para habilidades si el objetivo fue golpeado al menos una vez)\n\n"
        "**Efecto Pasivo/de la habilidad:**\n"
        "* Cuando usas un autoataque o una habilidad de ataque de Mononofu mientras estás fuera de rango y no estás afectado por el ailment Slow o el ailment Stop, te moverás hacia el objetivo en una animación de dash, obtendrás un buff y la acción usada se encola para ser utilizada al final del dash\n"
        "* Si un autoataque se encola y se usa al final del dash, se convierte en un Unsheathe Attack\n\n"
        "**Efecto del Buff:**\n"
        "* Aumenta el Skill Multiplier del siguiente autoataque en (0.05 * Skill Level)\n"
        "* Attack MP Recovery +0 (nivel 1)/ +1 (nivel 2)/ +2 (nivel 3)/ +4 (nivel 4)/ +6 (nivel 5)/ +9 (nivel 6)/ +12 (nivel 7)/ +16 (nivel 8)/ +20 (nivel 9)/ +25 (nivel 10)\n"
        "**Duración del Buff:** Hasta que se use una habilidad o un autoataque sea \"lanzado\"\n\n"
        "**Katana Main bonus:** El Attack MP Recovery del buff se duplica\n"
        "Si Rampage está activo, el Skill Multiplier de los Primeros 10 Auto Attacks se incrementa por el boost de Skill Multiplier de forma aditiva, pero no los Skill Multipliers del Final Blow\n"
        "El boost de Skill Multiplier del autoataque solo se aplica a la mano principal de Dual Swords\n"
        "El dash puede cancelarse moviéndose; si lo cancelas, perderás el buff y el siguiente autoataque que hagas no será un Unsheathe Attack\n"
        "Si el autoataque se cancela antes de que pueda golpear, el buff se elimina"
    ),
)

KAIRIKI_RANSHIN = SkillText(
    title="Kairiki Ranshin",
    description="**Descripción del juego:** *\"Libera el poder demoníaco interior. Aumenta ATK/Attack MP Recovery/Poder de Ataque Normal. Mejora Defense Pierce/Critical Rate de Garyou Tensei. Inflige [Ignition] en ti mismo al activarse.\"*",
    details=(
        "**Habilidad Tier 4;** Sin Restricciones {all}\n"
        "**Coste MP:** 200\n"
        "**Tipo de daño:** Ninguno\n\n"
        "**Efecto de la habilidad:** Lánzate Ignite durante 5 segundos (nivel 1)/ 6 segundos (niveles 2 y 3)/ 7 segundos (niveles 4 y 5)/ 8 segundos (niveles 6 y 7)/ 9 segundos (niveles 8 y 9)/ 10 segundos (nivel 10) sin Tiempo de Resistencia\n\n"
        "**Efecto del Buff:**\n"
        "* ATK +(10 * Skill Level)\n"
        "* Attack MP Recovery +6 (nivel 1)/ +7 (nivel 2)/ +8 (nivel 3)/ +9 (nivel 4)/ +10 (nivel 5)/ +16 (nivel 6)/ +17 (nivel 7)/ +18 (nivel 8)/ +19 (nivel 9)/ +25 (nivel 10)\n"
        "* Aumenta el Skill Multiplier de tus autoataques en (0.05 * Skill Level)\n"
        "* Critical Rate de Garyou Tensei +(10 * Skill Level)\n"
        "* Physical Pierce de Garyou Tensei +(10 * Skill Level)%\n"
        "**Duración del Buff:** 5 segundos (nivel 1)/ 6 segundos (niveles 2 y 3)/ 7 segundos (niveles 4 y 5)/ 8 segundos (niveles 6 y 7)/ 9 segundos (niveles 8 y 9)/ 10 segundos (nivel 10) O hasta que uses Garyou Tensei\n\n"
        "**Katana Main/Sub bonus:** Boost de Skill Multiplier de autoataque +0.5\n"
        "**Katana Main/Sub bonus:** La duración del Buff se triplica\n"
        "Si Rampage está activo, el Skill Multiplier de los Primeros 10 Auto Attacks se incrementa por el boost de Skill Multiplier de forma aditiva, pero no los Skill Multipliers del Final Blow\n"
        "El boost de Skill Multiplier del autoataque solo se aplica a la mano principal de Dual Swords"
    ),
)

BOUNCING_BLADE = SkillText(
    title="Bouncing Blade",
    description="**Descripción del juego:** *\"Una técnica de defensa usando la vaina. Se realiza un contraataque solo 1 vez si te lastimas mientras sostienes la vaina. Si tiene éxito, se restaurará algo de HP. El coste de MP de la siguiente habilidad se reduce y la precisión aumenta.\"*",
    details=(
        "**Habilidad Tier 3;** Solo Main {katana}\n"
        "**Coste MP:** 100\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 2 + 0.2 * Skill Level\n"
        "**Base Skill Constant:** 100 * 10 Skill Level\n"
        "**Número de golpes:** 1 hit\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack de katana\n\n"
        "**Efecto de la habilidad:**\n"
        "* Si recibes daño una vez durante la animación de esta habilidad, entonces esta habilidad infligirá daño a cambio y ganarás stack de Garyou por (+ stack actual de Garyou que tengas + 2).\n"
        "Ej: usarla cuando tienes 4 stacks de Garyou, luego haces un parry exitoso, ganarás 4 + 2 = 6 stacks.\n"
        "* Si no recibes daño, entonces esta habilidad no inflige daño ni inflige proration. Inmune a Flinch, Tumble y Stun durante la recepción de daño\n\n"
        "**Efecto del Buff:**\n"
        "* Al recibir daño con esta habilidad, recuperará tu HP basado en cuánto daño se recibió. Recupera HP +(Skill Lvl * 10)% del daño recibido\n"
        "* Después de recibir daño exitosamente con esta habilidad, el coste de MP de la siguiente habilidad se reducirá a la mitad. Además, otorga Accuracy en (Base Accuracy * Total Weapon Atk * (0.05 + 0.02 * Skill Lvl)%)"
    ),
)

KASUMISETSU_GETSUKA = SkillText(
    title="Kasumisetsu Getsuka",
    description="**Descripción del juego:** *\"Ataca al objetivo con una serie de cortes y reduce ligeramente el daño recibido mientras está activo. Realiza un ataque especial si Tenryu Ransei está activo, y el número de veces que se usa determina la duración del aumento de poder.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {katana}\n"
        "**Coste MP:** 500\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier (Primeros 4 Hits):** 7.5 + 0.75 * Skill Level\n"
        "**Base Skill Constant (Primeros 4 Hits):** 500\n"
        "**Número de golpes de los Primeros 4 Hits:** 4 hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits\n"
        "**Base Skill Multiplier (Último Hit):** 1 + TotalDEX/250\n"
        "**Base Skill Constant (Último Hit):** 200\n"
        "**Tenryu Ransei Zanyu Multiplier:** (1.5 + 0.25 * Skill Level de Tenryu) * Tenryu stk + TotalDEX/(50 * (5 - Tenryu stk))\n"
        "**Tenryu Ransei Zanyu Constant:** 200\n"
        "**Número de golpes del Último Hit/Zanyu:** 1 hit; los chequeos de hit/miss/graze/evasion/critical/guard no se copian de los primeros 4 hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* Si tienes el buff de <:Tenryuransei:971373861801168916>Tenryu Ransei, entonces al usar esta habilidad, su último hit se convierte en Tenryu Ransei: Zanyu, que puede infligir más daño y la duración del buff de Tenryu Ransei será mayor cuantos más stacks de Tenryu tengas. Su duración = 10 + (número de stacks del buff de Tenryu Ransei * 10) segundos [Penalidad Bowtana = -10 segundos de duración].\n"
        "* Usar esta habilidad consumirá 3 stacks de Tenryu, incluso si no tienes suficientes stacks de Tenryu, aún puedes usarla sin penalidad. Sin embargo, si haces un parry exitoso con esta habilidad, entonces consumirás 2 stacks de Tenryu en lugar de 3 stacks de Tenryu.\n"
        "* Sin embargo, usar esta habilidad con el buff de Tenryu no otorga invencibilidad ni Perfect Aim a diferencia de Tenryu Ransei Zannou Magadachi y Zantei Settetsu. Pero tranquilo, puedes usar esta habilidad directamente sin condiciones de parry.\n"
        "* Tiene una ligera reducción de daño Físico/Mágico durante la animación de esta habilidad = (Skill Level * 9 - (MAX[0 ; Skill Level * 9 - 50]/2))%\n"
        "* **Solo Main Katana**, el Último Hit de esta habilidad y Zanyu tienen +(BaseSTR/5) de Critical Rate. Y también, tienen +(BaseDEX/5) de Physical Pierce%\n"
        "* Eres inmune a los ailments FTS y Knockback durante la animación de esta habilidad (incluso ailment absoluto)\n"
        "* **[Solo Main Katana]** Usar <:hassohappa:971373861629198346>[Hasso Happa](https://discord.com/channels/565365471805833216/567994630679953408/967803898951782410) después de esta habilidad, realizará una nueva acción \"[Sakura Ranman](https://discord.com/channels/565365471805833216/567994630679953408/967803898951782410)\"\n\n"
        "Bowtana usando esta habilidad, su rango de cast es por defecto el rango máximo de autoataque del arco.\n"
        "Si usas esta habilidad cuando no tienes un stack de Tenryu, entonces esta habilidad no renovará el buff de Tenryu Ransei."
    ),
)

SHADOWLESS_SLASH = SkillText(
    title="Shadowless Slash",
    description="**Descripción del juego:** *\"Abre rápidamente al enemigo. Es tan rápido que ni siquiera el enemigo sabe cuándo la katana sale de su vaina. Ataca con alta precisión y otorga 2 de los buffs de Garyou Tensei. Puedes moverte al envainar la katana.\"*",
    details=(
        "**Habilidad Tier 5;** Solo {katana}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Base Skill Multiplier:** 4 + 0.5 * Skill Level + BaseDEX/200 + BaseAGI/200; multiplicador de todos los hits\n"
        "**Base Skill Constant:** 300\n"
        "**Número de golpes:** 5 hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits\n"
        "**Alcance máximo de Cast:** Por defecto el rango máximo de Auto Attack del arma\n\n"
        "**Efecto de la habilidad:**\n"
        "* Esta habilidad es tratada como un Unsheathe Attack\n"
        "* Esta habilidad ~~no es afectada~~ es afectada por SRD% independientemente de la distancia\n"
        "* Esta habilidad otorga +2 stacks de Garyou en total.\n"
        "* La Accuracy de esta habilidad aumenta en 200 * Skill Level\n"
        "* Además, obtienes la habilidad de hacer un dash después de usar esta habilidad. Obtienes el Enhanced auto-attack buff después de hacer el dash exitosamente (Bowtana no puede obtener este buff mejorado).\n"
        "* **Solo Main Katana**: Si tienes stack de Garyou 10/10 y tu Garyou adquirido está al nivel máximo, entonces usar Garyou durante la animación de Shadowless se convertirá en Divine Slash que inflige un daño tremendo, y es afectado por unsheathe y SRD%. Puedes poner una habilidad entre ellas y aún así activar Divine Slash, pero debes activar Divine Slash durante la animación de golpe de Shadowless.\n"
        "* Divine Slash tiene perfect aim e Invincibilidad sobre ti mismo durante 2s\n"
        "* Divine Slash tiene (10 * Kairiki lvl) de Critical Rate y (10 * Kairiki lvl) de Physical Pierce%.\n"
        "* Al realizar este Divine Slash, obtendrás automáticamente el buff de Kairiki Ranshin (su efecto sigue el nivel de Kairiki Ranshin)\n"
        "* Divine Slash solo resulta en Evasion durante fases de evasión absoluta/forzada como Evil Crystal Beast.\n\n"
        "**Divine Slash Multiplier:** 30 + BaseWATK/100\n"
        "**Divine Slash Constant:** 500 (sin Armor Break) o 1000 (con Armor Break)\n"
        "**Número de golpes:** 1\n"
        "Nota: BaseWATK no incluye refine, watk% de equipo/etc. BaseWATK de Dauntless podría estar incluido.\n\n"
        "**Efecto del Buff:** Unsheathe Attack +TRUNC((Total STR + Total DEX)/51)%\n"
        "**Duración del Buff:** después de que Divine Slash aterrice; 10 segundos\n\n"
        "**Información de Proration:**\n"
        "* Shadowless Slash usa proration física en el momento del cast, aunque el daño aparezca después.\n"
        "* Shadowless Slash inflige proration física al final de la habilidad.\n"
        "* Si Shadowless Slash se vuelve a lanzar antes de que aparezca el registro de daño, la proration se cancela.\n"
        "* Los cálculos de Divine Slash se realizan tan pronto como aparece el texto, no en el momento de aterrizar.\n"
        "* Por lo tanto, Shadowless -> Divine Slash deja -2 de proration física, pero Shadowless y Divine Slash en sí mismos no se verán afectados por eso.\n\n"
        "Bowtana usando esta habilidad, su rango de cast es por defecto el rango máximo de autoataque del arco.\n"
        "Usando el combo \"Shadowless->Garyou\", el daño de proration de Divine Slash es el mismo que la proration de Shadowless."
    ),
)

NUKIUCHI_SENNOSEN = SkillText(
    title="Nukiuchi Sennosen",
    description="**Descripción del juego:** *\"Una técnica de desenvaine que es como un milagro. Cuando no atacas durante un cierto período de tiempo, el ataque normal con Shukuchi se potenciará enormemente. Cuanto menos HP tengas, más poderoso es.\"*",
    details=(
        "**Habilidad Tier 5;** Solo Main {katana}\n\n"
        "**Efecto Pasivo:**\n"
        "* Un efecto de brillo en la katana aparecerá después de cargarla durante (12 - Skill Level) segundos sin hacer ataques en absoluto, de lo contrario el tiempo de carga se reiniciará. Este efecto de brillo dura hasta que uses un autoataque o habilidades de ataque. Además, hacer un dash de katana también puede reducir el tiempo de carga del brillo en 1 segundo. Así que en el Nivel 10, después de hacer un dash de katana, obtendrás este efecto pasivo instantáneamente.\n"
        "* Efecto de brillo: Reemplaza el Skill Multiplier total de tu Shukuchi Auto Attack por (400% del Multiplier del autoataque). Y su constante aumenta a medida que tu HP disminuye = (1000 * (100% - HP actual%)). Este Multiplier de Nukiuchi Auto Attack puede acumularse aditivamente con Kairiki, Berserk, etc. Mientras tanto, el Enhanced katana auto attack simplemente duplica el daño total del autoataque de Nukiuchi.\n"
        "* Además, este efecto de brillo puede convertir Pulse Blade en Swift Pulse Blade. Esto multiplica el daño de Pulse Blade por 5x en comparación con el normal. El daño de Pulse no cambia con diferentes HP. **Ten en cuenta que Swift Pulse Blade no inflige proration.**"
    ),
)

DAUNTLESS = SkillText(
    title="Dauntless",
    description="**Descripción del juego:** *\"Una fuerte determinación para enfrentarse al enemigo. Dauntless se acumula automáticamente cuando luchas contra un enemigo poderoso. Otorga varios buffs por cada 10 puntos de Dauntless acumulados. Los efectos terminan cuando el enemigo es derrotado.\"*",
    details=(
        "**Habilidad Tier 5;** Solo Main {katana}\n\n"
        "**Efecto Pasivo:**\n"
        "* Este efecto de Dauntless comienza a ganar stacks una vez que te enfrentas a un miniboss o Boss. Cada (12 - Skill Level) segundos añade 1 punto/stack de Dauntless. Máximo 100 stacks. Matar a un minijefe costará -10% de los stacks actuales de Dauntless que tengas y si no hay ningún miniboss o Boss presente, entonces 1 stack disminuirá cada 2 segundos.\n"
        "* Hacer un parry exitoso otorgará 2 stacks de Dauntless. (Habilidades de parry: Magadachi, Zantei Settetsu, Bouncing Blade)\n"
        "* Las siguientes habilidades a continuación, todos los efectos siguen siendo los mismos independientemente del Skill Level:\n"
        "* Cuando Dauntless alcanza 10 stacks:\n"
        "* Aumenta Accuracy = +(Stack/10 * 10)\n"
        "* Cuando Dauntless alcanza 20 stacks:\n"
        "* Flat Watk aumentado en +(Stack/10 * 5)\n"
        "* Cuando Dauntless alcanza 30 stacks:\n"
        "* Unsheathe% aumentado en +(Stack/10)%\n"
        "* Cuando Dauntless alcanza 40 stacks:\n"
        "* Motion Speed% aumentado en 12.5%\n"
        "* Cuando Dauntless alcanza 50 stacks: Otorga 2 efectos de buff\n"
        "* - Ganas pasivamente la habilidad de reducir cualquier daño recibido a 0 una sola vez durante la animación de deslizamiento de katana (igual que el iframe de zantei, que puede evitar que gsw/aura desaparezcan al recibir daño).\n"
        "* - Reduce el consumo de Kasumisetsu Getsuka en stacks de Tenryu en 1 stack.\n"
        "* - Aumenta el Base Skill Multiplier de Tenryu Ransei en +1.\n"
        "* Cuando Dauntless alcanza 60 stacks:\n"
        "* Flat BaseWATK aumentado en (Stack/10 * 5)\n"
        "* Cuando Dauntless alcanza 70 stacks:\n"
        "* Aumenta Unsheathe% nuevamente en +(Stack/10)%\n"
        "* Cuando Dauntless alcanza 80 stacks:\n"
        "* Motion Speed% aumentado nuevamente en 12.5%\n"
        "* Cuando Dauntless alcanza 90 stacks:\n"
        "* Reduce a la mitad el coste de MP de todas las habilidades de Mononofu\n"
        "* Cuando Dauntless alcanza 100 stacks:\n"
        "* Weapon Refine Value +1 (+15 también conocido como +S refine se convierte en +16)"
    ),
)

AUSPICIOUS_WIND = SkillText(
    title="Auspicious Wind",
    description="**Descripción del juego:** *\"Se activa por probabilidad cuando tu ataque resulta en Miss (Evasion; 1 stack por registro de daño) o cuando logras Evasion con [Evasion]. Durante 30 segundos, el poder de ataque de corto alcance/Critical Damage/Accuracy aumenta ligeramente, acumulándose hasta un máximo de 3 stacks. El efecto aumenta según el nivel del Skill Tree de Mononofu (se sube de nivel desde la library).\"*",
    details=(
        "**Habilidad Tier 2;** [Pasivo] {katana}\n\n"
        "**Efecto Pasivo:**\n"
        "* Chance de ganar stack: 10% * Skill Level\n"
        "* Duración: 30s; se extiende/renueva a 30s al ganar un stack. No se puede extender después de tener stacks completos.\n"
        "* Stack máximo: 3\n"
        "* Accuracy: + 10 * Skill Tree Level * stack\n"
        "* Short Range Damage: + 1% * Skill Tree Level * stack\n"
        "* Critical Damage: + Skill Tree Level * stack"
    ),
)

GUST = SkillText(
    title="Gust",
    description="**Descripción del juego:** *\"Adopta una postura de doble katana. Elimina y convierte el poder de Unsheathe en ATK y Weapon ATK. Reactivar Gust mientras está activo producirá un efecto diferente según la entrada de tecla. El efecto termina cuando te mueves mientras envainas tu katana (animación de deslizamiento de katana).\"*",
    details=(
        "**Habilidad Tier 3;** [Activo] {katana}\n"
        "**Coste MP:** 300\n"
        "**Tipo de daño:** Físico\n\n"
        "**Efecto de Activación:**\n"
        "* Elimina y convierte el stat de Unsheathe en:\n"
        "* ATK% = 0.1 * Skill Level * Unsheathe%\n"
        "* Basic Weapon Attack = 0.1 * Skill Level * Unsheathe%\n"
        "* Flat ATK = 0.1 * Skill Level * Flat Unsheathe\n"
        "* Basic Weapon Attack es el ATK mostrado en tu arma en el juego.\n"
        "* Activa Gust Stack 1/3 2/3 3/3.\n"
        "* Saca otra katana. Cambia la animación, el poder y el efecto del autoataque:\n"
        "**Auto Attack 1** (2 hits) [Gust Stack 1/3 → 2/3]\n"
        "* **Auto Attack Skill Multiplier:** 1 + 0.05 * Skill Level\n"
        "* **Auto Attack Skill Constant:** 0\n"
        "**Auto Attack 2** (2 hits) [Gust Stack 2/3 → 3/3]\n"
        "* **Auto Attack Skill Multiplier:** 2 + 0.1 * Skill Level\n"
        "* **Auto Attack Skill Constant:** 100\n"
        "**Auto Attack 3** (3 hits) [Gust Stack 3/3 → 1/3]\n"
        "* **Auto Attack Skill Multiplier:** 6 + 0.3 * Skill Level\n"
        "* **Auto Attack Skill Constant:** 200\n"
        "* Todo el cálculo de daño de autoataque se realiza una vez y luego se distribuye equitativamente entre los hits.\n\n"
        "* Activa ataques de temporada al re-lanzar + entrada de tecla (referencia de dirección = tú hacia el mob):\n"
        "**Still Wind** [Gust + sin dirección]\n"
        "Parry todos los ataques de monstruos durante la animación. Al hacer un parry exitoso, infligirás 1 hit adicional con Still Wind:\n"
        "* **Base Skill Multiplier (Still Wind Counter):** 5 + 0.5 * Skill Level\n"
        "* **Base Skill Constant (Still Wind Counter):** 300\n"
        "* Alcance máximo de Cast: 20m\n"
        "* Todos los ataques de monstruos durante la animación de esta habilidad te infligen 0 de daño. Aún puedes recibir ailments e inmovilización al hacer parry usando este Still Wind, y tus buffs \"intactos\" (ej: Brave Aura, Godspeed Wield) también desaparecerán.\n"
        "* Esta habilidad es afectada por short range damage; afectada por long range skill; usa e inflige proration física.\n"
        "* Mientras usas \"Still Wind\", si usas una entrada de dirección, activarás la habilidad de viento direccional por 0 mp. Al hacerlo, Still Wind Counter usa proration física y no inflige proration, y la habilidad de viento direccional usa e inflige proration normal.\n"
        "**Easterly Wind** [Gust + ←] 🌸\n"
        "* **Base Skill Multiplier:** 5 + 0.3 * Skill Level + Gust Stack\n"
        "* **Base Skill Constant:** 300\n"
        "* Alcance máximo de Cast: 20m; pero solo golpea desde 5m o menos, de lo contrario será Miss.\n"
        "* El movimiento de esta habilidad es tratado como [Evasion].\n"
        "* Esta habilidad es afectada por short range damage; afectada por long range skill; usa e inflige proration normal.\n"
        "**Southerly Wind** [Gust + ↓] ☀️\n"
        "* **Base Skill Multiplier:** 3.5 + 0.2 * Skill Level + Gust Stack * 1.5\n"
        "* **Base Skill Constant:** 300\n"
        "* Condición de desbloqueo: aprender \"Kairiki Ranshin\".\n"
        "* Alcance máximo de Cast: 20m. Al usar esta habilidad, tu personaje se mueve hacia atrás 4m, luego lanza un ataque AOE lineal de exactamente 16m de rango.\n"
        "* Esta habilidad es forzada a ser afectada por short range damage; afectada por long range skill; usa e inflige proration normal.\n"
        "**Northerly Wind** [Gust + ↑] 🍁\n"
        "* **Base Skill Multiplier:** 8.5 + 0.2 * Skill Level - 1.5 * Gust Stack\n"
        "* **Base Skill Constant:** 300\n"
        "* Condición de desbloqueo: aprender \"Shukuchi\".\n"
        "* Número de golpes: 2 Hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits.\n"
        "* Alcance máximo de Cast: 20m. Al usar esta habilidad, tu personaje se teletransporta a 0m frente al enemigo.\n"
        "* Esta habilidad usa physical pierce * 4 de tu physical pierce% total.\n"
        "* Esta habilidad es forzada a ser afectada por short range damage; afectada por long range skill; usa e inflige proration normal.\n"
        "**Westerly Wind** [Gust + →] ❄️\n"
        "* **Base Skill Multiplier:** 2.5 + 0.6 * Skill Level + 0.5 * Gust Stack\n"
        "* **Base Skill Constant:** 300\n"
        "* Número de golpes: 2 Hits; el cálculo de daño se realiza una vez y se distribuye equitativamente entre los hits.\n"
        "* Alcance máximo de Cast: 20m; pero solo golpea desde 5m o menos, de lo contrario será Miss.\n"
        "* Esta habilidad tiene el atributo perfect aim.\n"
        "* Esta habilidad es afectada por short range damage; afectada por long range skill; usa e inflige proration normal.\n\n"
        "* Mientras gust está activo, no puedes usar \"Divine Slash\".\n\n"
        "**Katana bonus:** Still wind, Northerly Wind, Easterly Wind, Westerly Wind y Southerly Wind pueden activarse con entrada de tecla sin terminar el efecto de Meikyo Shisui. Después de asumir la postura \"Still Wind\", aún puedes hacer la transición a la habilidad correspondiente con una entrada de tecla. (El MP solo se consume al activar Still Wind)."
    ),
)

FOUR_SEASONS = SkillText(
    title="🍁 ❄️ Four Seasons ☀️ 🌸",
    description=(
        "Esta es una interacción de los Ataques de Temporada de la habilidad Gust.\n\n"
        "**Condición de Activación:** Realizar exitosamente ⬅️ Easterly Wind > ⬇️ Southerly Wind > ⬆️ Northerly Wind > ➡️ Westerly Wind > Efecto de Brillo de Nukiuchi Sennosen, y luego re-lanzar la habilidad \"Gust\". La activación de las Habilidades de Gust Direccional/Estacional tiene que ser en el orden correcto y no debe repetirse antes de lanzar \"Four Seasons\". Ser inmovilizado también hace que \"Four Seasons\" falle; aunque, puedes lanzar cualquier otra habilidad o caminar antes de continuar con cada ritual.\n\n"
        "**Base Skill Multiplier:**\n"
        "* 1er Ataque (2 hits): 20.5 + 0.2 * Skill Level - 1.5 * Gust Stack\n"
        "* 2do Ataque (2 hits): 17 + 0.6 * Skill Level + 0.5 * Gust Stack\n"
        "* 3er Ataque (1 hit): 17 + 0.2 * Skill Level + 1.5 * Gust Stack\n"
        "* 4to Ataque (1 hit): 20.5 + 0.3 * Skill Level + Gust Stack\n"
        "**Base Skill Constant:** 300\n"
        "* Para el 1er y 2do ataque, el cálculo de daño se realiza una vez y se distribuye equitativamente entre los 2 hits.\n"
        "* Four Seasons tiene el atributo perfect aim, 100% de physical pierce, y siempre el elemento más fuerte contra el enemigo.\n"
        "* Toda la animación de Four Seasons anulará todo el daño recibido, pero reduce el daño de su siguiente ataque: 2do Ataque -50% de daño, 3er Ataque -40% de daño, 4to Ataque -25% de daño. Aún puedes recibir ailments e inmovilización durante la animación de esta habilidad y tus buffs \"intactos\" (ej: Brave Aura, Godspeed Wield) también desaparecerán.\n"
        "* Four Seasons no se activará al luchar contra monstruos pequeños (que no sean Boss/miniboss).\n\n"
        "**Alcance máximo de Cast:** 20m\n\n"
        "Four Seasons es afectado por short/long range damage; afectado por long range skill; usa proration normal e inflige proration física."
    ),
    details="",
)

ZEPHYR_RUSH = SkillText(
    title="Zephyr Rush",
    description="**Descripción del juego:** *\"Escapa del peligro como una brisa repentina (solo mientras estás en estado Gust). Obtienes invencibilidad mientras estás en el aire, luego desciendes y realizas un corte después de un tiempo o al usar una entrada de tecla. El poder aumenta según la duración de la invencibilidad, pero será un MISS si no hay ningún objetivo en el punto de aterrizaje.\"*",
    details=(
        "**Habilidad Tier 4;** [Activo] {katana}\n"
        "**Coste MP:** 400\n"
        "**Tipo de daño:** Físico\n\n"
        "* **Base Skill Multiplier:** 0.6 * Skill Level + Invincibility Duration Bonus\n"
        "**Invincibility Duration Bonus:**\n"
        "* 1-2s (icono muestra 4-3s): 3 de multiplicador\n"
        "* 3s (icono muestra 2s): 6 de multiplicador\n"
        "* 4s (icono muestra 1s): 9 de multiplicador\n"
        "* 5s-descend (icono muestra 0s o descenso automático): 12 de multiplicador\n"
        "* **Base Skill Constant:** 100\n\n"
        "**Frame de invencibilidad:** 5 segundos (cancelar usando entrada de tecla)\n"
        "**Alcance máximo de Cast:** infinito\n\n"
        "Esta habilidad es afectada por short range damage; afectada por long range skill; usa e inflige proration física."
    ),
)

SUPER_GUST = SkillText(
    title="Super Gust",
    description="**Descripción del juego:** *\"Mejora la técnica de doble empuñadura a través del entrenamiento diario. Aumenta el poder del ataque normal de 'Gust' (los 3 estados) y todas las habilidades a las que cambia.\"*",
    details=(
        "**Habilidad Tier 5;** [Pasivo] {katana}\n\n"
        "**Efecto Pasivo:**\n"
        "Aumenta el Base Skill Multiplier de los derivados de \"Gust\" en:\n"
        "* Auto Attack 1: +0.05 * Skill Level\n"
        "* Auto Attack 2: +0.1 * Skill Level\n"
        "* Auto Attack 3: +0.3 * Skill Level\n"
        "* Still Wind: +0.5 * Skill Level\n"
        "* Easterly Wind: +0.45 * Skill Level\n"
        "* Southerly Wind: +0.35 * Skill Level\n"
        "* Northerly Wind: +0.3 * Skill Level\n"
        "* Westerly Wind: +0.45 * Skill Level\n\n"
        "**Four Seasons:**\n"
        "* 1er Ataque: +0.3 * Skill Level\n"
        "* 2do Ataque: +0.45 * Skill Level\n"
        "* 3er Ataque: +0.35 * Skill Level\n"
        "* 4to Ataque: +0.45 * Skill Level"
    ),
)
