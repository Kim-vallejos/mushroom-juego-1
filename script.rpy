image splash = "gui/logo.png"

label splashscreen:
    scene black
    with Pause(0.5)

    show splash at truecenter with dis
    $ renpy.pause(0.3, hard=True)
    with Pause(1)

    hide splash with dis
    $ renpy.pause(0.3, hard=True)
    with Pause(0.5)

    show text "{size=40}{color=#ffffff}The game contains screen shaking, mild jumpscares as well as depictions of mind/memory manipulation, blood and death.{/size=50}" with dis
    $ renpy.pause(1, hard=True)
    with Pause(3)

    hide text with dis
    $ renpy.pause(0.3, hard=True)
    with Pause(0.5)

    show text "{size=40}{color=#ffffff}Please read content warnings before proceeding.{p} Player discretion is advised.{/size=50}" with dis
    $ renpy.pause(1, hard=True)
    with Pause(1)

    hide text with dis
    $ renpy.pause(0.3, hard=True)
    with Pause(0.5)

    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dis = { "master" : Dissolve(0.5) }

default protag = "Poppy"
default stranger = "???"
default mushroomman = "Mychael"
default pet = "Molly"
default alma = "Vida"

default veggie = False
default tomato_cheese = False
default tomato_garlic = False

default chat_cook = False
default chat_plumbing = False
default chat_life = False
default help_rabbit = False

default suspicion = 0

define p = Character ("[protag]", what_slow_cps=45, what_slow_abortable=True)
define s = Character ("[stranger]", what_slow_cps=45, what_slow_abortable=True)
define m = Character ("[mushroomman]", what_slow_cps=45, what_slow_abortable=True)
define c = Character ("[pet]",what_slow_cps=45, what_slow_abortable=True)
define v = Character ("[alma]",what_slow_cps=45, what_slow_abortable=True)

transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -30
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform zoom_in:
    ease 0.5 zoom 1.05 xalign 0.5 yalign .7

transform zoom_in2:
    ease 0.5 zoom 1.10 xalign 0.5 yalign .6

transform zoom_in3:
    ease 0.5 zoom 1.03 xalign 0.5 yalign .6

transform zoom_in4:
    ease 0.2 zoom 3 xalign 0.5 yalign .45

transform zoom_in5:
    zoom 3 xalign 0.5 yalign .45

transform zoom_in6:
    ease 1 zoom 1.5 xalign 0.5 yalign .7

transform zoom_in_street:
    ease 4 zoom 1.7 xalign 0.05 yalign 0.4

transform zoom_out:
    pause .15
    easein .175 yoffset -30
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    ease 0.5 zoom 1

transform zoom_out2:
    pause .15
    ease 0.5 zoom 1

transform slow_dissolve:
    on show:
        alpha 0.0
        linear 2.0 alpha 1.0
    on hide:
        linear 3.0 alpha 0.0

transform drop:
    zoom 6 xalign 0.5 yalign 0.2
    ease 0.2 zoom 1 xalign 0.5 yalign .45
    easein .175 yoffset -30
    easeout .175 yoffset 0
    easeout_cubic 1 yoffset 1200

transform slap:
    zoom 6 xalign 0.4 yalign 0.5
    pause.1
    ease 0.2 zoom 1 xalign 0.5 yalign .45
    easein .175 yoffset -30
    easeout .175 yoffset 0

transform shake:
    linear 0.090 xoffset -2
    linear 0.090 xoffset +0
    linear 0.090 yoffset -2
    linear 0.090 yoffset +0
    repeat

image laika happy:
    "images/sprites/laikada/laika happy1.png"
    pause 0.2
    "images/sprites/laikada/laika happy1b.png"
    pause 0.1
    "images/sprites/laikada/laika happy1c.png"
    pause 0.1
    "images/sprites/laikada/laika happy2.png"
    pause 0.2
    "images/sprites/laikada/laika happy2b.png"
    pause 0.1
    "images/sprites/laikada/laika happy2c.png"
    pause 0.1
    repeat

image cg oh he angy:
    "images/cgs/cg oh he angy 01.png"
    pause 0.1
    "images/cgs/cg oh he angy 02.png"
    pause 0.1
    repeat

image yank:
    "images/objects/yank 02.png"
    pause 0.1
    "images/objects/yank 03.png"
    pause 0.1
    "images/objects/yank 04.png"
    pause 0.1
    "images/objects/yank 05.png"
    pause 0.1
    "images/objects/yank 06.png"
    pause 0.1
    "images/objects/yank 07.png"
    pause 0.1
    "images/objects/yank 08.png"
    pause 0.1

# The game starts here.

label start:
    #DAY 1 START

    window show

    stop music fadeout 3.0
    if protag ==  "Poppy":
      $ protag = renpy.input("Cual es tu nombre?", length=25)

    if pet ==  "Molly":
      $ pet = renpy.input("Cual es el nombre de tu gato?", length=25)

    "Y tu gato es..."

    menu:
        "Macho":
            $ pronoun1 = "He"
            $ pronoun2 = "he"
            $ pronoun3 = "Him"
            $ pronoun4 = "him"
            $ pronoun5 = "His"
            $ pronoun6 = "his"
            $ pronoun7 = "mister"
            jump begin

        "Hembra":
            $ pronoun1 = "Ella"
            $ pronoun2 = "ella"
            $ pronoun3 = "Ella"
            $ pronoun4 = "ella"
            $ pronoun5 = "Ella"
            $ pronoun6 = "ella"
            $ pronoun7 = "señora"
            jump begin

    label begin:

    $ suspicion = 0

    "[pet] ha estado desaparecida desde hace un tiempo."
    "%(pronoun1)s Era un gato de interior, pero tenía la tenacidad de un gato salvaje en una misión que intentaba salir cada vez que la puerta estaba abierta."
    "Los catios y el tiempo de juego no fueron suficientes para la pequeña. %(pronoun7)s."
    "Supuse que %(pronoun2)s saldría corriendo si dejaba algo de comida en el porche.{p}Tres días después,{w=.2} todavía no hay gato."
    "He intentado todo lo que se me ocurrió."
    "Preguntando por el vecindario.{w=.2} Poniendo carteles de {b}GATO PERDIDO{/b}."
    "Lamentablemente, nada resultó de mis esfuerzos."
    "No podía buscar a %(pronoun4)s durante el día, ya que el trabajo me mantenía ocupado."
    "Y hay solo unas pocas horas en la noche en las que podía gritar por las calles buscando a %(pronoun4)s."
    "Solo quedaba un lugar en el que podía pensar que %(pronoun2)s podría haberse escapado."
    "El bosque junto a mi casa,{w=.2} justo al otro lado de la calle."
    "Definitivamente he visto a %(pronoun4)s observando a los pájaros y ardillas que corrían junto a los límites desde la ventana delantera,{w=.2} los dientes de %(pronoun6)s chasqueando de emoción."
    "No soy una persona que disfrute estar al aire libre de ninguna manera."
    "De hecho, la idea de entrar ahí me asusta."
    "Pero tenía que encontrarla %(pronoun4)s. O al menos intentarlo."
    "El primer fin de semana que llegó, empaqué algo de agua, las golosinas favoritas de [pet] y una brújula para estar seguro."
    "No estaba seguro ni siquiera de dónde comenzar a buscar a %(pronoun4)s, así que comencé a caminar en línea recta, llamando el nombre de %(pronoun6)s cada pocos pasos."
    "..."
    "Definitivamente no tardé mucho en darme cuenta de que esto era demasiado para mí."

    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
    play sound "audio/sfx/forest-footsteps.ogg" loop
    scene bg woods daytime
    with dis

    p "¿Por qué pensé que esto era una buena idea?"
    "Era difícil orientarme entre los árboles que me rodeaban."
    "No quería admitir que estaba perdido, al menos no todavía."

    stop sound fadeout 2.0

    "Solo podía entrecerrar los ojos hacia mi brújula mientras la aguja giraba lentamente. {w} Estoy bastante seguro de que no están hechas para hacer eso."
    "...¿De verdad traje una brújula rota en mi primera incursión en estos bosques?"
    "Supuse que eso sería justo mi suerte."
    "Lo único que ponía en riesgo mi seguridad era mi propia incompetencia."
    "Sacudí la cabeza apresuradamente.{w} No, no, no, no había tiempo para pensamientos negativos.{w} [pet] estaba ahí fuera en alguna parte, con frío, perdido y hambriento."
    "Tenía que seguir adelante."

    play sound "audio/sfx/forest-footsteps.ogg" loop
    stop music fadeout 2.0
    scene bg woods evening
    with Dissolve (2.0)
    play music "audio/ambience/forest-latenoon.ogg" fadein 2.0 loop

    "...Han pasado horas."
    "Estoy tan, tan perdido."
    "Ni siquiera sé por qué seguí buscando incluso después del momento en que me di cuenta de eso."
    "{i}¿Por qué{/i} pensé que esto era una buena idea!?"
    "El hambre llevaba un rato atormentando mi estómago, ya que me había saltado el desayuno y el almuerzo por completo."
    "El calor y la humedad del sol de la tarde eran insoportables, pero el aire fresco no hacía nada para calmarme."
    "Incluso si intentara regresar a casa, ni siquiera podría ubicar dónde estaba."
    "¿Qué hace la gente en esta situación?"
    "Sabía que era un optimismo infundado, pero seguir caminando era realmente lo único que se me ocurría hacer."
    "Seguramente encontraré algo familiar."
    "Seguí avanzando, cuidando que mis zapatos evitaran cuidadosamente las raíces de los árboles entrelazadas en el suelo del bosque."
    "Pero en mi estado debilitado,{w=.2} sumado a la oscuridad que se acercaba,{w=.2} me encontré tropezando con el terreno accidentado."

    play sound "audio/sfx/kicky.ogg"
    "Mis pies golpearon algo blando que sobresalía del suelo."
    p "¡Ack!" with vpunch
    "Mis manos se extendieron al perder el equilibrio. Mis pies intentaron torpemente encontrar apoyo mientras tambaleaba hacia atrás, agitando los brazos."
    play sound "audio/sfx/poofy.ogg"
    "{i}¡Poof!{/i}" with vpunch
    p "{i}¡Cof cof!{/i} ¿Q-qué...?"

    show bg mushroom ring 01
    with dis

    "Mi zapato había aterrizado justo en el centro de un círculo de hongos, provocando que una nube tenue surgiera del grupo."
    "Metí mi nariz en mi codo para evitar inhalarlo."
    "No podría diferenciar una hoja de árbol de otra para salvar mi vida, pero estoy bastante seguro de que los humanos no deberían inhalar lo que sea que fuera esto."
    "Olía fuertemente a madera podrida y tierra húmeda, incluso cuando la nube se disipó."

    show bg mushroom ring 02
    show sparkle
    with dis

    "Algo brillante captó rápidamente mi atención."
    "Me agaché para recogerlo, jadeando en voz baja."

    play sound "audio/sfx/cat-bell.ogg"
    hide sparkle
    with dis

    show item cat collar
    with dis

    "Era el collar de [pet]."
    "Cubierto de lo que sea que esos hongos hayan soltado."
    "Miré desesperadamente alrededor buscando cualquier señal de %(pronoun4)s."
    p "{size=+5}[pet]{/size}? {size=+10}[pet]{/size}!!"
    p "Psspsspsspsspss!"
    "Tosí al inhalar algo del polvo que aún flotaba en el aire."
    "Realmente debería alejarme de esto."
    "Guardando el collar de [pet], me retiré con cuidado hasta que pude volver a respirar."

    hide item cat collar
    show bg woods evening
    with dis

    "Retrocediendo, aún podía olerlo. Debió haberse pegado a mi cabello y ropa."
    "Una rápida revisión confirmó mis sospechas con un ligero escalofrío. Una capa delgada pero generosa lo cubría todo, desde mis mangas hasta mis jeans."
    "Me apoyé contra un árbol, sacudiendo mi ropa en un intento ingenuo de quitar el polvo y el olor, pero fue inútil."
    "Si acaso, sentía que estaba inhalando más de eso."
    "Lo que antes era un olor húmedo ahora se volvió dulce, y me encontré respirando aún más profundamente, tratando de identificar el aroma."
    "...¿Pepinos?"
    "Olfateaba como pepinos frescos."
    "Una sensación de cosquilleo se deslizó por mis manos y cuello, alfilerazos extendiéndose por mis extremidades mientras un extraño calor llegaba a mi rostro."
    "{color=#8c277a}Empecé{/color} a sentirme mareado y aturdido. {color=#8c277a}Mis{/color} sentidos estaban entumecidos."
    "Debería asustarme."
    "Y, sin embargo..."
    "Una extraña sensación de calma me invadió."
    "{color=#8c277a}Debería{/color} acostarme.{w} De hecho, ahora mismo."
    play sound "audio/sfx/fallen-down.ogg"
    "Mis piernas cedieron debajo de {color=#8c277a}mí{/color}, {color=#8c277a}mi{/color} cuerpo desplomándose de manera torpe." with vpunch

    show bg woods skylight
    with dis

    "{color=#8c277a}Me{/color} quedé ahí tendido,{w} mirando,{w} y mirando,{w} y mirando."
    "Era... agradable aquí."
    "Una calma pacífica."
    "El lugar perfecto para una siesta, incluso."
    "{color=#8c277a}Mis{/color} ojos se sentían pesados mientras {color=#8c277a}me{/color} debatía entre la conciencia y el sueño."
    "Sí. Una siesta suena realmente bien ahora."

    show bg black
    with dis
    stop music fadeout 2.0

    "..."
    "..."
    "..."
    s "Oh..."
    s "Muchas criaturas han pasado por aquí últimamente..."
    s "Lamento que te haya pasado esto, pequeña."
    s "Pudo haber sido cualquiera, pero tuvo que ser a ti..."
    s "..."
    s "¿Hm?"
    s "Espera.{w} ¿Un humano?"
    s "¿Cómo terminaste tan adentro de este lugar?"
    s "...Y aún sigues respirando."
    s "Ah, demonios, no puedo dejarte aquí."
    s "¿Qué debería hacer...?"

    scene bg black
    pause 1

    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop
    scene bg cabin ceiling with hpunch

    "Me desperté de un sobresalto."
    "Hacía calor, pero un calor agradable."
    "Podía sentir el peso de una manta sobre mí mientras intentaba sentarme."
    "…No podía."
    "No podía mover mi cuerpo."
    "Mis dedos se movieron inútilmente a los lados mientras mis ojos se movían desesperados en pánico."
    "Mirando alrededor, podía ver el interior de una cabaña, o al menos el techo de una. No podía ver mucho más allá del borde de mis ojos."
    "¿Dónde estaba? ¿Cómo llegué aquí?"
    "Un sentimiento de desesperación se alzó en {color=#8c277a}mi{/color} pecho."
    "…{color=#8c277a}Tenía{/color} que irme."
    "Ahora mismo."
    "Esto estaba {size=+5}mal. {/size}{size=+10}{color=#73416a}Mal. {/color}{/size}{size=+15}{color=#8c277a}Mal.{/color}{/size}"
    "{color=#8c277a}No{/color} debería estar aquí."
    play sound "audio/sfx/here-comes-the-boy.ogg" fadein 2.0
    "Podía escuchar el crepitar de un fuego cercano, probablemente la fuente del calor que sentí al despertar."
    "También podía escuchar pasos acercándose."

    menu:

        "Fingir que estás dormido.":
            jump ch_asleep

        "Permanecer despierto.":
            jump cont_story_01

    label ch_asleep:

    show bg black
    with dis

    "Cerré los ojos rápidamente, esperando que no se hubieran dado cuenta."
    "Reducí la velocidad de mi respiración, obligando a los músculos de mi rostro a permanecer inmóviles."
    "..."
    "Junto a mí, alguien se rió suavemente."
    s "Ya sé que estás despierto, luciérnaga."
    s "Vamos.{w} No voy a hacerte daño..."

    label cont_story_01:

    show bg cabin ceiling
    show cgwakeup 01
    with dis

    "Parpadeé, esforzándome por mirar a la persona que se acercaba."
    "Mis ojos se abrieron de par en par al observar su apariencia; las protuberancias en su frente llamaron mi atención."
    "¿Sin mencionar la piel verde...?"
    "El extraño no pareció notar mi incomodidad mientras suspiraba aliviado."

    show cgwakeup 02
    with dis

    s "¡Estás despierto!{w} Eso es bueno. Muy, muy bueno."
    s "¿Cómo te sientes?"
    "…Parpadeé."

    show cgwakeup 03
    with dis

    s "¡Oh!{w} P-perdón, ¡se me olvidaba!"
    s "Toma."

    show cgwakeup 04
    with dis

    "La persona sostuvo una taza frente a mis labios; un fuerte y dulce aroma provenía del borde."
    "Una mano suave agarró mi barbilla para abrir mi boca. Ni siquiera podía moverme para resistir."
    s "No te preocupes. Te hará sentir mejor,{w=.2} te lo prometo.{w} ¡Bebe!"
    "Cuando el líquido tocó mi lengua, todo lo que pude sentir fue una vaga sensación de calor."

    show cgwakeup 05
    with dis

    play sound "audio/sfx/dwink.ogg"
    "Mientras seguía bebiendo, el sabor y la textura regresaron; la dulzura de bayas y manzanilla cubría mi paladar. Incluso podía detectar un toque de menta."

    hide cgwakeup 02
    with dis

    "Finalmente levanté la cabeza, con las manos apretadas a mis costados mientras me apoyaba sobre los codos."
    "La persona mantuvo una mano firme en mi barbilla, cuidando no verter demasiado para que no me atragantara."
    "Terminé hasta la última gota, limpiándome la boca con el dorso de la mano."
    "Miré mis dedos, dándome cuenta de que tenía pleno control sobre mi cuerpo nuevamente."

    play music "audio/music/mychael-is-here.ogg" fadein 1.0 loop
    show bg cabin room night
    with dis
    show mychat smile
    with dis
    s "¡Como nueva! Ahora, ¿cómo te sientes?"
    p "M-mejor. Gracias."
    show mychat happy
    with dis
    "El extraño se rió."
    s "¡Oh, me gusta cómo suenas!"
    s "Hace siglos que no hablo con nadie, y mucho menos con una voz tan agradable como la tuya."
    show mychat smile
    with dis
    "Ignoré su extraño cumplido y finalmente miré alrededor de la cabaña con atención."
    "Era una habitación sencilla con muebles de madera escasos pero decorados; adecuada para alguien que viviera solo."
    "Un arco abierto a la derecha conducía a lo que supuse era la cocina."
    "Junto a él, una puerta estaba cerrada.{w} ¿Tal vez el baño?"
    "Observando, noté un tema recurrente de decoraciones tejidas dispersas por todo el lugar. Cualquier superficie disponible estaba cubierta con manteles tejidos con patrones."
    "Un proyecto sin terminar descansaba junto a la mesita de noche donde estaba sentada, un par de agujas de tejer sobresalían de una pila de lana en una pequeña canasta."
    "Por lo que podía decir, parecía el comienzo de una bufanda verde."
    show mychat grab
    with dis
    "El extraño parecía cómodo permaneciendo en silencio, observándome mientras miraba alrededor."
    hide mychat
    show mycb smile
    with dis
    "Se quitó el sombrero y lo lanzó a la cama, despeinándose aún más el cabello."
    "Con el sombrero fuera, sus... características únicas eran imposibles de ignorar."
    p "L-lo siento, pero ¿quién...{w=.2} q-qué eres tú?"
    s "¿Hm?"
    show mycb happy
    with dis
    s "Oh, ¿no me presenté, verdad?"
    show mycb grin
    with dis
    s "¡Hola! Soy Mychael.{w=.2} Con Y."
    "Negué con la cabeza."
    p "No no, quise decir que...{w=.2} um."
    "Mychael me miró, con su oreja izquierda moviéndose ligeramente."
    show mycb smile
    with dis
    p "Tú...{w=.2} luces muy..."
    "Él se rió con un bufido."
    show mycb cheeky
    with dis
    m "¿Feo?{w=.2} ¿Desagradable?"
    p "¡No!{w} Sólo...{w=.2} diferente."
    m "¿Diferente, eh?{w=.2} Sólo estás siendo amable."
    p "¡B-bueno, entonces explícalo tú!"
    show mycb nervous
    with dis
    m "Uhm."
    m "Quiero decir,{w=.2} eso es algo grosero, ¿no crees?"
    "Me detuve por un momento antes de pellizcar el puente de mi nariz, exhalando lentamente."
    p "Yo sólo..."
    p "..."
    p "Lo siento...{w=.2} Ha sido un día muy largo, eso es todo."
    p "Debería estar dándote las gracias."
    m "Si te sirve... es... uh,{w=.2} ¿una c-c-condición de la piel?{w} ¿Así lo llaman ustedes los humanos?"
    "La manera en que lo dijo no sonaba muy convincente."
    p "...{w=.2}¿Y las orejas?"
    m "Um."
    m "Gen{w=.2}-éti-{w=.2}cas{w=.2}...?"
    p "Claro..."
    p "Y supongo que los pequeños..."
    "Hice un gesto vago hacia sus... ¿cuernos?{w=.2} ¿Antenas?"
    p "¿Esas cosas son sólo parte de un cosplay para completar el look?"
    m "¿Eso sería un argumento convincente?"
    "Entrecerré los ojos."
    p "...{w=.2}Tal vez."
    show mycb cheeky
    with dis
    m "Entonces sí. Es...{w=.2} {i}cossss{/i}-play."
    p "Aún no explica todo..."
    show mycb nervous
    with dis
    "Mychael dejó escapar una risa nerviosa."

    play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
    show pink behind mycb
    with dis

    m "Mira, sólo soy un chico viviendo solo en el bosque.{w} No necesitas preocuparte más que por eso, ¿de acuerdo?"
    "Algo en su tono te obligó a no cuestionar más su existencia."
    "Él es sólo un chico.{w} Viviendo en el bosque.{w} Completamente normal."

    stop sound fadeout 3.0
    hide pink behind mycb
    with dis
    show mycb smile
    with dis

    p "C-claro… completamente normal."
    p "Yo soy [protag]."
    show mycb happy
    with dis
    "Mychael sonrió ampliamente."
    m "¡Encantado de conocerte, [protag]!"
    "Jugueteé con las mantas mientras Mychael se acercaba desde el borde de la cama."
    show mycb nervous
    with dis
    m "Y-ya sé que ya pregunté,{w=.2} pero ¿cómo te sientes?"
    m "¿Dolores?{w=.2} ¿Molestias?{w=.2} ¿Náuseas?"
    m "...¿Pensamientos intrusivos?{w=.2} ¿Impulsos raros?{w=.2} ¿Fiebre, tal vez?"
    p "Uh... No creo qu-{nw}"
    show mycb at zoom_in
    "Puso su mano en mi frente antes de que pudiera reaccionar."
    "Sus manos estaban callosas, retirándolas rápidamente mientras daba un murmullo pensativo."
    show mycb surprise at zoom_out2
    m "Pareces estar...{w=.2} lúcida.{w} Eso es una buena señal."
    p "Uh, ¿genial?"
    "Él murmuró distraído, su oreja temblorosa recordándome a un gato perturbado."
    "...gato."
    "{i}¡¡¡Mi gato!!!" with hpunch
    p "¡Oh, rayos!"
    show mycb neutral
    with dis
    p "L-lo siento si esto suena repentino, pero ¿has visto un gato por aquí?{w=.2} %(pronoun5)s nombre es [pet]."
    p "%(pronoun1)s es adorable, más o menos de este tamaño. Tímido, pero %(pronoun2)s podría acercarse a extraños si lo necesita."
    "Saqué mi teléfono para mostrarle fotos de %(pronoun4)s, sólo para darme cuenta de que no estaba en mi bolsillo trasero."
    p "Espera... ¿dónde está?"
    show mycb upset
    with dis
    m "No lo he visto."
    p "¿Eh?"
    m "Tu gato.{w=.2} No lo he visto."
    p "Oh... Ya veo."
    show mycb neutral
    with dis
    "Me desplomé contra las almohadas, frotándome las sienes."
    p "%(pronoun1)s perdió %(pronoun6)s collar también.{w} Incluso si alguien encuentra a %(pronoun4)s, no sabrían de dónde viene."
    p "...{w}Maldita sea."
    "Mychael se quedó en silencio, observándome desde su lado de la cama."
    show mycb surprise
    with dis
    m "¿Viniste hasta aquí por un {i}gato{/i}?"
    p "¿Eh?{w=.2} Por supuesto."
    show mycb upset
    with dis
    m "¿Hasta el punto de agotarte en lo profundo del bosque?{w=.2} ¿Por un gato?"
    m "¿Te das cuenta de lo lejos que te alejaste del pueblo más cercano?"
    m "Te encontré casi inconsciente.{w=.2} En un área donde nadie ha puesto un pie en años."
    m "{cps=10}{b}Por un gato."
    "Sonaba como si estuviera conteniéndose de darme una severa lección, como si no pudiera creer que tuviera tan poco sentido de autopreservación."
    "Mis mejillas se calentaron al darme cuenta de lo imprudente que sonaba."
    p "Y-yo quiero decir."
    p "%(pronoun1)s no es sólo un gato!{w=.2} %(pronoun1)s es...{w=.2} mi familia."
    show mycb neutral
    with dis
    p "Y-yo sé que fue estúpido intentarlo, ¡pero tenía que hacerlo!"
    "Mychael se relajó un poco, con los hombros tensos mientras me miraba desde debajo de su despeinado flequillo."
    m "¿Familia,{w=.2} eh?"
    m "..."
    show mycb smile
    with dis
    "Finalmente inclinó la cabeza hacia mí con una sonrisa."
    m "¿Estás dispuesto a llegar tan lejos por una criatura tan pequeña?"
    m "He conocido a mi buena cuota de campistas perdidos, cazadores y un par de adolescentes fugitivos.{w} ¿Pero alguien buscando a su mascota?"
    show mycb cheeky
    with dis
    m "Eres un poco raro, ¿no?"
    "Me quedé boquiabierto, lo que lo divirtió mucho."
    p "¡Habla por ti mismo!{w} ¿Quién hace cosplay en medio del bosque?" with hpunch
    show mycb happy at bounce
    "Mychael soltó una carcajada profunda que resonó en su pecho."
    m "Touché."
    show mycb smile
    with dis
    m "..."
    m "Creo que...{w=.2} me estás empezando a caer bien, [protag]."
    p "Eh. ¿Igualmente...?"
    show mycb grin
    with dis
    "Su sonrisa se ensanchó, pero había algo extraño en ella.{w} Mostraba demasiados dientes."
    "Parecía como si no hubiera hablado con alguien en mucho tiempo y hubiera olvidado cómo sonreír de la manera adecuada."
    "Me rasqué el cuello, tratando de pensar en algo más que decir."
    p "P-puedo preguntar, ¿cómo llegué aquí?"
    show mycb surprise
    with dis
    m "Oh.{w=.2} Como dije, te encontré en el bosque, no muy lejos de aquí."
    p "Oh, cielos. ¿De verdad?"
    p "Sabía que estaba cansado, pero... No podía haberme..."
    p "Huh. Pisé algo. Algo... {color=#8c277a}importante{/color}."
    "Un cosquilleo familiar recorrió mi piel."
    p "C-casa..."
    p "{color=#8c277a}Necesito ir a {color=#8c277a}casa{/color}."
    "Mychael se tensó mientras agarraba mi hombro."
    m "U-uh. ¡Olvida eso!"

    show mycb nervous at zoom_in
    pause .2
    play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
    show pink behind mycb
    with dis

    m "Te desmayaste por... u-uh... ¡un golpe de calor!"
    "¿Golpe de calor?{w} No… eso no fue lo que pasó."
    p "Y-Yo no… {color=#8c277a}yo{/color} estaba bien hasta que..."
    "Mychael sacudió la cabeza con insistencia, inclinándose hacia mí."
    m "No, no, no, luciérnaga, no estabas bien para nada."
    m "Si no te hubiera encontrado cuando lo hice...{w} bueno, ¿quién sabe qué podría haber pasado?"
    m "Podrías haberte lastimado o haber sido atacada por un animal salvaje."
    m "Hay peligros en estos bosques, ya sabes."
    "No… tenía razón."
    "{color=#ff8da1}Fuiste{/color} tan imprudente."
    "¿Cómo pensaste que podrías hacer esto por {color=#ff8da1}tu{/color} cuenta?{w} Buscando a {color=#ff8da1}tu{/color} gato en medio del bosque."
    "Y entrar sin llevar agua...{w} Desmayarte por un golpe de calor, de todas las cosas."
    "¿Cómo pudiste ser tan tonta?"
    "Sacudí la cabeza, mi cerebro demasiado nublado para analizar mis pensamientos."
    "Él sonaba seguro, así que, ¿por qué deberías dudar de él?"

    stop sound fadeout 3.0
    hide pink behind mycb
    with dis

    p "B-Bueno, si significa algo, me alegra que estuvieras allí."
    "Mychael se relajó, colocando la mano sobre su regazo una vez más."
    show mycb grin at zoom_out2
    "Él me sonrió."
    m "Yo también, [protag]."
    show mycb blush
    with dis
    m "Definitivamente me alegra haberte encontrado a {i}ti{/i}."
    "Sus ojos estaban completamente ocultos detrás de su cabello desordenado, pero no podía evitar sentir lo intensamente que me miraban mientras decía eso."
    "Se me erizó la piel en la nuca."
    p "Eh... claro."
    "Sin distracciones, apenas me di cuenta de lo incómoda que estaba sentada allí."
    "La manta sobre mí comenzaba a picar, justo cuando la necesidad desesperada de regresar a casa comenzó a crecer dentro de {color=#8c277a}mí{/color} nuevamente."
    p "Eh, esto fue… interesante. Pero realmente debería irme ya."
    show mycb surprise at bounce
    m "¡Espera!"
    "Mi anfitrión se levantó de la cama antes de que yo pudiera."
    show mycb nervous
    with dis
    m "Y-Yo quiero decir."
    m "No puedes--{w=.2} No puedo dejar que andes por el bosque a estas horas."
    m "Por favor, q-quédatelo un poco más."
    p "Pero, Mychael, realmente tengo que--{nw}"
    m "¡Ven conmigo!"
    "Él tomó mi mano y me llevó al otro lado de la habitación."

    scene bg cabin kitchen night
    with dis

    "Entramos en la cocina, un fragante aroma a papas cocidas y carne llenaba el aire."
    "Dos platos estaban colocados en una pequeña mesa circular, completos con utensilios y tazas de té."
    show mycb blush
    with dis
    m "N-No esperaba invitados hoy, así que la comida no es nada especial."
    m "Pero…{w=.2} ¿me acompañas a cenar?"

    play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
    show pink behind mycb
    with dis

    "Se veía tan esperanzado, con las orejas caídas."
    "…{color=#ff8da1}Te{/color} sentirías tan mal si {color=#ff8da1}tuvieras{/color} que decirle que no."

    menu:

        "Decir {color=#ff8da1}sí{/color}.":
            jump ch_dinner_yes

        "Decir {color=#8c277a}no{/color}.":
            jump ch_dinner_no


    label ch_dinner_no:

    stop sound fadeout 3.0
    hide pink behind mycb
    with dis
    show dark behind mycb
    with dis
    show mycb nervous
    with dis

    play music "audio/music/mychael-is-here-please.ogg" fadein 1.0 loop
    "{color=#8c277a}Ignoré{/color} la voz suplicante en el fondo de {color=#8c277a}mi{/color} cabeza, fortaleciendo {color=#8c277a}mi{/color} determinación."
    "Curiosamente, en el momento en que tomé la decisión, la estática que nublaba {color=#8c277a}mi{/color} mente desapareció de inmediato, solo siendo reemplazada por la necesidad urgente de regresar a casa."
    "Mychael guardó silencio, su agarre en {color=#8c277a}mi{/color} mano se tensó antes de aflojarse."
    m "Yo... ya veo."
    m "Si… eso es lo que quieres."
    m "Pero… ¿estás realmente segura?"

    menu:

        "Sí. Es lo que {color=#8c277a}debo{/color} hacer.":
            jump ch_dinner_no2

        "Bueno... Supongo que no hace daño quedarme.":
            jump ch_dinner_yes

    label ch_dinner_no2:

        show mycb upset
        with dis
        play music "audio/music/mychael-is-here-please-stay.ogg" fadein 1.0 loop
        show darker behind mycb
        with dis

        "Sus orejas se aplanaron ante mis palabras."
        "Ríe una risa vacía, su boca torciéndose en una mueca torcida."
        m "S-seguro. Seguro que no te molestará sentarte para una comida rápida."
        m "Solo un bocado, incluso."

        play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop
        show pink behind mycb
        with dis

        m "{size=-15}{k=15}Por favor...{/size}"
        "Sus manos se cerraron en puños a sus costados."
        m "..."
        m "¿De verdad tienes que irte?"

    menu:

        "{color=#8c277a}Sí.":
            jump ch_bad_end_01

        "{color=#8c277a}SÍ.":
            jump ch_bad_end_01

        "{color=#8c277a}Sí, claro.":
            jump ch_bad_end_01

        "{color=#8c277a}¡SÍ!":
            jump ch_bad_end_01

        "{color=#ff8da1}En realidad, cenar suena realmente {b}muy{/b} bien ahora.{/color}":
            jump ch_dinner_yes

    label ch_bad_end_01:

        stop music fadeout 2.0
        stop sound fadeout 3.0
        pause 1
        hide pink behind mycb
        with dis
        show mycb upset
        with dis

        play music "audio/music/goodbye.ogg" fadein 2.0 loop
        m "..."
        "Mychael me miró como si buscara algo."
        "Finalmente suspiró en derrota."
        show mycb neutral
        with dis
        m "…Está bien."
        m "Supongo que... no puedo retenerte aquí. No más."
        m "Déjame acompañarte afuera."

        scene bg woods nighttime
        with dis
        play sound "audio/sfx/door-open.ogg"

        "Mychael me guió hacia la puerta trasera, abriéndola mientras se hacía a un lado para dejarme salir."
        "La brisa fría se deslizó por mis brazos. Me giré hacia él por última vez."
        p "Um, gracias de nuevo. Por todo."
        show mycb upset
        with dis
        "Guardó silencio por un momento, mirando más allá de mí hacia los árboles."
        m "De nada. {w=.2} Ten cuidado en tu camino de regreso."
        m "L-lo siento por no poder hacer más por ti..."
        "Ha sido nada más que amable."
        "Es extraño para una despedida, pero {color=#8c277a}yo{/color} estaba demasiado ocupada con pensamientos de volver a casa como para importarme."
        "{color=#8c277a}Miré hacia el bosque, las sombras proyectadas por la luz de la luna causando algo de duda en mí.{/color}"
        p "Um, ¿te importaría darme algunas indicaciones para empezar?"
        "Mychael me miró finalmente, luego al horizonte inclinando su barbilla."
        m "Sigue en esa dirección."
        m "Encontrarás un sendero que te llevará directamente a casa."

        hide mycb
        with dis
        play sound "audio/sfx/door-shut.ogg"
        stop music fadeout 2
        pause 1
        play music "audio/ambience/forest-night.ogg" fadein 1.0 loop

        "{color=#8c277a}Le{/color} saludé mientras cerraba la puerta, el mecanismo se cerró con un clic."
        "{color=#8c277a}Me quedé ahí por un momento, cuestionándome si había tomado la decisión correcta o no.{/color}"
        "Otro pensamiento urgente me obligó a irme."
        "{color=#8c277a}Este no es mi lugar.{/color}"
        "{color=#8c277a}Tengo que irme.{/color}"
        play sound "audio/sfx/forest-footsteps.ogg" loop
        "Ya era demasiado tarde para regresar, así que {color=#8c277a}reuní mi determinación y me alejé.{/color}"
        "..."
        "..."
        "..."
        "{color=#8c277a}Caminé."
        "{color=#8c277a}Y caminé."
        "{color=#8c277a}Los árboles se mezclaron unos con otros después de un rato."
        "{color=#8c277a}Debería haber tenido miedo. O preocupación."
        "{color=#8c277a}Pero se sentía bien."
        "{color=#8c277a}La oscuridad que me rodeaba era demasiado reconfortante como para sentirme en peligro."
        "{color=#8c277a}Me desvié de la dirección que Mychael me había mostrado hace ya tiempo, mis pies llevando mi cuerpo voluntariamente a algún lugar específico."
        "{color=#8c277a}Algún lugar especial."
        "{color=#8c277a}Un destino final."
        "{color=#8c277a}Aquí."
        stop sound fadeout 2.0
        "{color=#8c277a}El parche de hongos en el que había pisado antes."
        "{color=#8c277a}Se suponía que debía estar aquí."
        "{color=#8c277a}Siempre he tenido que estar aquí."
        "{color=#8c277a}Me recosté en la fría y húmeda tierra."
        "{color=#8c277a}Y cerré los ojos."

        show bg black
        with dis

        "..."
        "..."
        "..."

        stop music fadeout 2.0
        pause 1
        show cg badend_01
        with dis
        play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
        m "..."
        m "No hay mucho que pueda hacer si el bosque te ha reclamado, luciérnaga."
        m "..."
        m "…Ojalá te hubiera encontrado antes."
        m "..."
        m "Que descanses bien, [protag]."

        "FINAL 1 - Sueño Tranquilo"

        return

    label ch_dinner_yes:

    play music "audio/music/mychael-is-here.ogg" fadein 1.0 loop
    stop sound fadeout 3.0
    hide dark
    hide darker
    hide pink behind mycb
    with dis

    show mycb surprise
    with dis
    "Mychael's jaw dropped for a second before he quickly recovered."
    show mycb happy
    with dis
    m "I… y-yes yes, of course! Here, here come sit. I’ll serve up the cottage pie in a minute!"
    hide mycb
    show bg table
    with dis
    "I sat as instructed, my stomach rumbling something fierce as the smell was the only thing I could focus on."
    "...Yes, this was definitely the right choice."
    "What was so important that {color=#ff8da1}you{/color} had to leave so soon?"
    "The outside world can wait."
    "{color=#ff8da1}You{/color} could stay here,{w} and enjoy my company."
    m "Oh!{w} Actually..."
    m "I should ask,{w=.2} are you okay with meat for dinner? I could make something else for you if that’s not your preference."

    menu:

        "I don't eat meat.":
            jump ch_dinner_stirfry

        "I'm okay with meat.":
            jump ch_dinner_pie

    label ch_dinner_stirfry:

        m "Good thing I asked!{w=.2} Thanks for letting me know."
        m "Let me pick some veggies from the garden and I’ll make you something."
        "He left out the back door with a basket, coming back inside surprisingly quick with a smile on his face."
        "I expected him to toss something in a bowl and have it done just like that.{w} But apparently he had other plans."
        play sound "audio/sfx/veggie-wash.ogg"
        queue sound "audio/sfx/veggie-chop.ogg"
        "I watched as he washed the veggies thoroughly before chopping them up with an extra sharp knife,{w=.2} setting them aside and pulling out a container from one of the cabinets."
        play sound "audio/sfx/veggie-boil.ogg"
        "He set a pan on the stove and oiled it up,{w=.2} tossing in half of the ingredients and seasoning them with some herbs and spices while a pot boils next to it."
        "The small kitchen quickly filled up with the smell of his cooking."
        "My mouth was already watering in response."
        "I twiddled with a fork on the table, trying to ignore the gnawing feeling in my gut."
        "Luckily I didn’t have to wait long."
        "Before I knew it Mychael had already finished, humming as he strode over to the table and set my food down in front of me."

        play sound "audio/sfx/plate-up.ogg"
        show item stirfry
        with dis

        "I looked down at my dinner and almost gasped."
        "It looked so good!"
        "The rice was fluffy as it peeked out underneath the colorful pile of veggies.{w} I didn’t know a simple dish could look so tantalizing."
        "The serving size was a bit heartier than expected.{w} He must’ve known I was starving."

        hide item stirfry
        with dis
        show myc table smile
        with dis

        "Mychael brought over his own serving of cottage pie as he settled into his seat."
        m "Sorry to make you wait,{w=.2} I tried to keep it simple but filling."
        m "Go ahead!{w=.2} Dig in!"
        "He didn’t have to tell me twice.{w} I jabbed my fork into the dish, scooping up rice with a spoon in my other hand and shoving it into my mouth."
        "Hot!!!" with vpunch
        "Mychael kept a polite expression,{w=.2} the corner of his mouth lifting as I panted with the food still in my mouth."
        "He gave me a few seconds to recover, elbow planted on the table."
        m "Is it good?"
        "I nodded vigorously, even though my buds were burning."
        p "Mmm! Mm!"
        "I couldn't taste anything."
        "He laughed."
        m "It's usually better on the second bite."
        "I slowed down, hand on my mouth as Mychael poked his fork into his pie."
        "I tentatively blew on the plate to make sure it was cool before taking another bite."
        "He was right.{w} The second bite was a lot better."
        "The rice was soft and flavorful, mixing in nicely with the crunch of the vegetables with every chew."
        "I’ve never had greens this fresh, and with how gently he cooked them every single element was finished to perfection."

        jump cont_story01

    label ch_dinner_pie:

        m "Oh, okay! You’ll be having the same dinner as me, then."
        "Mychael pattered about the small kitchen with an almost giddy excitement."
        play sound "audio/sfx/oven-door.ogg"
        "He put on a pair of knitted oven mitts, humming as he stooped down and pulled out a steaming tray of pie from the wood stove."
        "The smell!{w} It filled out the kitchen in an instant as he brought it to the table, my stomach rumbling louder in response."

        show myc table smile
        with dis

        "I'm pretty sure Mychael could hear it,{w=.2} but he just smiled as he served up our portions."
        "He discreetly cut me a bigger piece, which I was grateful for."

        play sound "audio/sfx/plate-up.ogg"
        show item cottagepie
        with dis
        "It looked so good!"
        "The crust was a nice golden color, streaked with crisp lines and garnish. The meat and veggie filling looked absolutely delectable, the savoury sauce leaking onto the plate."
        "My mouth was watering, unsurprising considering the fact I haven't eaten all day."
        hide item stirfry
        with dis
        m "Careful now,{w=.2} it's still hot."
        "It was fair advice, but I didn't wait more than two blows before biting into my first forkful."
        p "Ah!" with vpunch
        "It was...{w=.2} definitely way too hot to eat straight from the oven."
        "Mychael kept a polite expression,{w=.2} the corner of his mouth lifting as I panted with the piece still in my mouth."
        "He gave me a few seconds to recover, elbow planted on the table."
        m "Is it good?"
        "I nodded vigorously, even though my buds were burning."
        p "Mmm! Mm!"
        "I couldn't taste anything."
        "He laughed."
        m "It's usually better on the second bite."
        "I slowed down, hand on my mouth as Mychael poked his fork into his own slice."
        "I tentatively blew on the pie to make sure it was cool before taking another bite."
        "He was right.{w} The second bite was a lot better."
        "The seasoned potato crust was nice and crisp on top, cheesy and creamy in the middle. The savory meat filling was well-cooked and bursting with flavor."
        "Every bite felt like home."

        jump cont_story01

    label cont_story01:

    show myc table smile
    with dis
    "My host watched me enjoy the meal from across the table."
    m "Do you like it?"
    p "Yeah! This tastes amazing, Mychael."
    show myc table blush
    with dis
    "He flushed from the compliment, rubbing the back of his neck."
    m "Heh, I’m glad. I like to think of myself as a decent cook,{w=.2} but I’ve never been able to get anyone else’s opinion on that."
    p "Do you like baking in particular?"
    show myc table smile
    with dis
    m "Hmm, not always.{w} I usually go for simple dishes, with any ingredients available."
    "I nodded amicably, though didn't say much else.{w} I was more focused on scarfing down dinner, which thankfully Mychael didn’t seem to mind."
    "The overall atmosphere was nice and homely,{w=.2} and I could hear Mychael tapping his feet from underneath the table."
    "I guess he was that happy to have someone stay for dinner?{w} It did seem like he lived alone judging from the surroundings in his cabin."
    p "So...{w=.2} I'm kinda curious."
    "He perked up instantly, his focus solely on me."
    show myc table hm
    with dis
    p "What made you wanna live all the way out here?"
    show myc table nervous
    with dis
    m "Oh.{w} Well… when you look like me,{w=.2} it’s kinda easier to just live out of sight from everyone else."
    "A pang of guilt shot through my chest.{w} I was giving him a hard time about how he looked too."
    "He must’ve sensed it clear as day on my face."
    show myc table panic
    with dis
    m "N-not that you’re one of them!{w} You’ve actually been nicer than most."
    m "Though I wonder if..."
    show myc table nervous
    with dis
    "His smile turned strained."
    m "N-nevermind.{w=.2} My point is, it’s better here than anywhere else."
    m "Why don’t you try the tea, firefly?"
    "He seemed uncomfortable now, easing into a different topic."
    "It’s probably best to follow along."
    p "Oh sure."
    "I reached out towards my mug–"

    show myc table panic

    play sound "audio/sfx/tail-whip.ogg" volume 1
    "Only to push it off edge with my clumsy fingers." with hpunch
    p "Wait–!!"
    "I bent over the side to grab it, fully expecting it to fall just out of reach and land on the floor into broken pieces."
    "{w=.2}It never did."

    stop music fadeout 2.0
    show cg tailtime
    with dis
    show myc table hb reveal_01
    with dis
    play music "audio/ambience/tense-ambience.ogg" loop

    "Instead, a long green appendage was twisted around the ceramic mug, securely keeping it in place. Not even a drop had fallen out."
    "My eyes trailed along the length of it until I pinpointed that it came from behind Mychael, the rest of it partially hidden beneath his cardigan."
    p "Mychael…?"
    p "Is that...{w=.2} yours?"
    m "I-I..."
    hide cg tailtime
    with dis
    "Mychael buried his face in his hands,{w=.2} the strange appendage from before lowering to his side, mug in tow."
    m "I’m sorry, [protag]. I think...{w} I think it’s time I was honest."
    show myc table hb reveal_02
    with dis
    "He lifted his head,{w=.2} fingers carding his hair back to reveal his eyes."
    "I froze as two... n-no, {i}multiple{/i} pairs of irises stared right into mine, before darting to the side and avoiding my gaze."
    show myc table hb reveal_03
    with dis
    m "I-I know it's a lot to take in but..."
    show myc table hb reveal_02
    with dis
    m "This is.. who I really am..."
    m "Please... {i}please{/i} don't be scared."


    menu:

        "Freak out.":
            jump runaway

        "Remain calm.":
            jump cont_story02

    label runaway:

        play music "audio/music/freaking-out.ogg" fadein 2.0 loop

        p "M-monster…"
        show myc table hb reveal_05
        with dis
        "I flinched as his eyes thinned into sharp slits."
        m "N-no! No no no no, please don’t be scared–{nw}"
        p "{size=+10}YOU'RE A MONSTER!" with vpunch
        m "[protag]!"

        play sound "audio/sfx/chair-fall.ogg"
        queue sound "audio/sfx/cabin-run.ogg"
        hide myc
        show bg cabin room night
        with dis

        "I kicked back against the chair, letting it clatter to the ground as I scrambled to the living room."
        "He was a freak!"
        "How did I ever let him get close to me!?"
        "I-I had to escape. Now!"

        play sound "audio/sfx/cabin-run.ogg"
        show bg doorclosed
        with dis

        "I ran to the door furthest into the room hoping it was the exit, rattling the doorknob desperately."
        play sound "audio/sfx/doorknob-rattle.ogg"
        "It was locked shut." with vpunch
        m "{size=-10}[protag], please!"

        play sound "audio/sfx/cabin-run.ogg"
        show bg windowclosed
        with dis

        "I abandoned the front door and ran to the window by the bed, my fingernails scraping against the sill."
        "It was sealed tight, the lock barely budging as I tried to twist it with my fingers."
        "Heavy boots slowly came closer behind me."
        show bg doorway
        with dis
        show myc badend approach
        with dis
        "I spun around to see him by the edge of the doorway, hands up in a careful stance."
        m "[protag], calm down.{w} I’m begging you, just let me explain."
        p "S-stay away from me!"
        "My eyes landed on the basket on the bedside table, the needles glinting against the firelight."

        menu:

            "Take them.":
                jump runaway_wneedles

            "Leave them.":
                jump runaway_noneedles

        label runaway_wneedles:

            "I grasped both needles and pulled them from the yarn, the basket dropping to the floor in my haste." with hpunch
            show myc badend scared
            with dis
            "Holding them to my chest, I stepped back as Mychael came closer,{w=.2} eyes wild as he realized what I held."
            m "H-hey… hey…{w=.2} hey… look at me, [protag]..."
            play sound "audio/sfx/hypno-static.ogg" fadein 1.0 loop
            show myc badend plead
            with dis
            show pink behind myc
            with dis
            m "You don’t wanna do this.{w=.2} You’re gonna hurt yourself."
            m "Let go of those things."

            menu:

                "Attack him.":

                    "He was right. If {color=#ff8da1}you{/color} weren’t careful, {color=#ff8da1}you{/color} could--{nw}"

                    stop sound
                    stop music
                    play sound "audio/sfx/stab.ogg"
                    hide pink behind myc
                    show myc badend stab
                    "Aiming blindly, I lunged forward." with vpunch
                    "He probably wasn’t expecting it,{w=.2} because he hardly moved as I stabbed them straight through his chest."

                    show myc badend stabb
                    with dis
                    pause 1
                    show myc badend stabbb
                    with dis
                    pause 1
                    hide myc
                    with dis
                    play sound "audio/sfx/mychael-is-dead.ogg"

                    "A choked sound made past his lips before he collapsed,{w=.2} his disgusting pair of eyes dazedly searching the room for me." with vpunch

                    play music "audio/music/goodbye.ogg" fadein 2.0 loop

                    show cg badend_02a
                    with dis

                    m "[protag]...?"
                    m "I...{w=.2} I can’t see you..."
                    "I backed away, my breath lodged in my throat."
                    m "Th-that’s okay...{w=.2} I-I know you... you can hear me..."
                    m "..."
                    m "Ah...{w=.2} th-this hurts so much…"

                    show cg badend_02b
                    with dis

                    "He wheezed out a pained laugh."
                    m "You know...{w=.2} I-I was...{w=.2} so alone."
                    m "When you came along...{w=.2} I was so happy..."
                    m "Just to talk to someone...{w=.2} to have dinner with someone..."
                    m "You even liked my cooking!"
                    m "Agh..."

                    show cg badend_02a
                    with dis

                    m "..."
                    m "I really thought...{w=.2} you would be different."
                    m "Did you really hate...{w=.2} the way I looked that much...?"

                    show cg badend_02b
                    with dis

                    "He laughed bitterly once more, spitting out some blood."
                    m "Why do I...{w=.2} keep lying to myself?"
                    m "This has always been my fate...{w=.2} since the beginning..."
                    m "A-at least...{w=.2} I got one wish..."
                    m "I-I’m not dying alone..."

                    show cg badend_02a
                    with dis

                    m "..."
                    m "[protag]...?"
                    m "Are you there...?"
                    m "..."
                    m "P-please..."
                    m "I'm... getting c-cold..."
                    m "T-tell me you're there..."
                    "I didn’t realize I had tears streaming down my face."
                    "He sounded so pathetic."
                    "I stared down at my hands.{w} The hands that hurt Mychael."
                    "Had I made a mistake…?"
                    "A sputtered cough snapped my attention back to him." with vpunch
                    m "...{w=.2}Ah. {w}{cps=15}I think{w=.2} this is goodbye, [protag]."
                    m "{cps=15}It was...{w=.2}nice...{w=.2} to meet... y..."

                    show cg badend_02c
                    with dis

                    "He cast one last breath, the sound rattling across the empty cabin as his eyes glassed over completely."
                    "I sunk to my knees, hands still shaking."

                    scene bg black
                    with dis

                    "What...{w=.2} what have I done...?"

                    "Ending 2 - You Monster."

                    return

                "Listen to him.":

                    show pink behind mycb
                    with dis
                    "He was right. If {color=#ff8da1}you{/color} weren’t careful, {color=#ff8da1}you{/color} could hurt yourself."
                    play sound "audio/sfx/needles-gone.ogg"
                    "{color=#ff8da1}Your{/color} hold on the needles slipped,{w=.2} {color=#ff8da1}your{/color} ears picking up the sound of them clattering to the floor."
                    hide pink behind mycb
                    with dis
                    jump runaway_noneedles
                    stop sound fadeout 2.0

        label runaway_noneedles:

            "Defenseless,{w=.2} I faced Mychael as he stepped closer."
            "I couldn’t stop staring at those eyes."
            "They looked wide with panic."
            show myc badend plead
            with dis
            m "Okay...{w=.2} listen to me."
            m "Everything’s gonna be alright."
            p "S-stay away from me, you freak." with vpunch
            show myc badend hurt
            with dis
            m "W-why...?{w=.2} Do you hate me that much?"
            show myc badend plead
            with dis
            m "C-can't we just start over...?"
            "I shook my head, backing away from him."
            p "Just let me leave!!"
            p "I-I don’t want to be anywhere near you..."
            show myc badend still
            with dis
            "Mychael stopped advancing, hands fisting at his sides."
            m "O-okay...{w} that’s okay...{w=.2} I’ll let you go..."
            m "Just..."

            hide myc
            play sound "audio/sfx/grab.ogg"
            show cg badend_03a with vpunch

            "I screamed as his arms wrapped around me, all I could do was twist in his hold."
            "I could feel something tightening around my legs, his grip on my chin forcing me to look at his face."
            show cg badend_03b
            with dis
            p "{size=+5}L-let go of me!{w} Let me go, Mycha–{nw}"

            show cg badend_03c with vpunch
            stop music
            play sound "audio/sfx/hypno-static.ogg" volume 2 loop
            show pink
            with dis
            "Static."
            "All I could hear was static."
            "..."
            "My body went against my will as I slackened against him, limp as a ragdoll as his eyes bored straight into mine."
            "Mychael’s smile was manic."
            m "That’s it, firefly...{w=.2} I’ve caught you now..."
            m "You’ll be fine...{w=.2} everything will be fine..."
            "..."
            "{color=#ff8da1}Of course.{w} Of course everything’s fine."
            "{color=#ff8da1}What did you have to worry about anyways? It was just your dear sweet friend, Mychael."
            "{color=#ff8da1}Trustworthy Mychael."
            "{color=#ff8da1}Safe and sound Mychael."
            "{color=#ff8da1}He was all that you needed."
            m "That's right."
            m "Settle in, firefly."
            m "I’ll take good care of you."
            m "I promise."

            stop sound fadeout 3.0
            play music "audio/music/goodbye.ogg" fadein 2.0 loop
            show cg badend_03d
            with dis

            m "..."
            m "I can’t have the real you..."
            m "But I’ll willingly play pretend if it means I get to keep you."

            scene bg black
            with dis

            "..."
            "{color=#ff8da1}Your name is [protag].{w} You live in the woods with your best friend, Mychael."
            "{color=#ff8da1}You love Mychael."
            "{color=#ff8da1}And he loves you."
            "{color=#ff8da1}You’ve never had a job."
            "{color=#ff8da1}You’ve never had a cat."
            "{color=#ff8da1}You’ve never left these woods."
            "{color=#ff8da1}You’ve never had a home anywhere else."
            "{color=#ff8da1}You already are home."
            "{color=#ff8da1}..."
            m "Hey, firefly.{w} You wanna help with dinner today?"
            m "..."
            m "Haha...{w} of course you do."
            m "..."
            m "Come on."

            "Ending 3 - Playing Pretend."

            return

    label cont_story02:

    stop music fadeout 2.0

    "I swallowed audibly, willing myself to not look away."
    "He seemed to be holding his breath as I gripped the edge of the table."
    "It felt unsettling every time he blinked those eyes in succession,{w=.2} even when he wasn’t looking at me."
    "Was it real?"
    "{i}It had to be.{/i}{w} Everything about him suddenly made so much more sense."
    "The isolation.{w} The avoidant behaviour."
    "He looked...{w=.2} freaky, yes."
    "But...{w=.2} he also looked sad."
    p "I..."
    "I swallowed thickly."
    p "I-I'm not scared."
    show myc table hb reveal_04
    with dis
    "Mychael’s many pupils blew wide, dilating like an excited wildcat."
    "It sent a shiver up my spine."
    p "O-okay, maybe just a little bit scared."

    play music "audio/music/mychael-is-here.ogg" fadein 1.0 loop
    show myc table hb panic
    with dis

    m "Ah! S-Sorry."
    show myc table hb hiding at bounce
    "He hastily grabbed an empty plate and hid behind it,{w=.2} shoulders scrunched up despite his stature."
    m "Would it help if I just... hide it?"
    m "I-I could fix my hair like before...{w=.2} if that's what you prefer."
    "His voice was muffled behind the ceramic barrier between us."
    "It was...{w=.2} kind of endearing."
    "I slowly reached out to touch his hand, the slight brush of my fingertips making him jump in place."
    show myc at bounce
    p "Mychael?"
    m "...Yeah?"
    p "Can you put that down?"
    m "..."
    show myc table hb sideglance
    with dis
    "He slowly lowered the plate.{w} His eyes were still darted to the side, avoiding me."
    p "C-can you look at me?"
    m "..."

    show myc table hb blush_01
    with dis
    pause 0.5
    show myc table blush_02
    with dis
    pause 1
    show myc table hb blush_03
    with dis
    pause 1
    show myc table hb blush_04
    with dis

    m "D-don't look at me like that..."
    p "S-sorry! I just...{w=.2} can't stop looking..."
    "This was so awkward.{w} His hands were shaking."
    "I looked down at the mug still floating next to him,{w=.2} hanging on for dear life."
    "I reached over and plucked it straight out of his grasp."
    show myc table hb surprise
    with dis
    m "!!!"
    show item gingertea
    with dis
    "I tentatively took a sip, noticing how Mychael was watching me over the rim of the mug."
    "The taste was mildly spicy,{w=.2} with an almost earthy bite to it.{w} I recognized it instantly as ginger tea."
    hide item gingertea
    with dis
    p "...It’s almost room temperature.{w=.2} But it’s still pretty good."
    m "Huh?"
    p "You wanted me to try the tea,{w=.2} right?"
    p "I-I like it!{w=.2} So... thank you."
    show myc table hb nervous
    with dis
    m "O-oh.{w} I'm glad."
    "Mychael relaxed back into his seat, following my lead as I picked up my fork once more."
    "The silence didn't last long as Mychael fidgeted."
    m "A-are you really...{w=.2} okay with this?{w} With me?"
    "I gave him a once over, really taking in his features."
    p "It's...{w=.2} very different than what I'm used to."
    p "But I think I can learn to like it."
    show myc table hb blush_01b
    with dis
    "Is that weird to say?"
    p "I-I mean,{w=.2} y-you're not bad to look at."
    p "It's actually kind of... um..."
    "Dammit dammit dammit what do I say!?"

    menu:
        "Pretty.":

            show myc table hb surprise
            with dis
            m "Y-you think I'm... p-pretty?"
            p "Y-yeah."
            m "..."
            m "..."
            m "..."
            m "{i}Oh."
            jump after_compliment

        "Cool.":

            show myc table hb surprise
            with dis
            p "It's like something out of science fiction!"
            m "Is... that a good thing?"
            p "Yeah!"
            m "O-oh..."
            jump after_compliment

        "Hot.":

            m "H-hot...?" with vpunch
            show myc table hb surprise
            with dis
            m "...You're not referring to temperature, are you?"
            p "No, I am not."
            m "Oh..."
            "He looked confused but seemed embarassed anyway."
            jump after_compliment

    label after_compliment:
    show myc table hb blush_02b
    with dis

    p "My point is!{w} Your appearance shouldn't matter."
    p "You've been nothing but kind to me so far."
    p "I'd be the worst kind of person to judge someone based on how they look."
    p "I haven't known you that long...{w=.2} but you seem like a good person."
    p "You're fine, Mychael."
    "I smiled at him."
    p "We're fine."
    m "I... I see."
    show myc table hb nervoussmile
    with dis
    "He fidgeted some more before nodding, smiling a bit."
    m "Th-thanks, [protag]."
    show myc table hb happy
    with dis
    m "I'll cherish this moment forever."
    "He beamed at me as he enthusiastically went back to eating his food."

    hide myc
    show bg cabin kitchen night
    with dis

    "That was...{w=.2} something."
    "We continued with a bit of small talk, mostly stories about [pet] or snippets from my personal life."
    "Mychael hung on to every word I said, not bothering to elaborate much about himself despite my burning curiosity."
    "I could tell he was extremely insecure about his appearance, so it's probably best I keep my questions to myself for tonight."
    "We cleared up the kitchen in relative silence, Mychael storing away the rest of the pie as I washed the dishes by the sink."
    stop music fadeout 3.0
    "Being out here in this remote cabin,{w=.2} I wondered how he had running water."
    "Maybe I’ll ask him later."

    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop

    scene bg cabin room night
    with dis
    show myc smile
    with dis

    p "So...{w=.2} thanks for dinner."
    show myc happy
    with dis
    m "Thanks for the company."
    show myc smile
    with dis
    m "Oh! And please,{w=.2} take the bed tonight.{w=.2}"
    p "B-but–"
    show myc scold
    with dis
    m "Ah ah!{w=.2} You’re my guest and I’m the host.{w} Take the bed, okay?"
    p "...A-alright.{w=.2} I’ll be out of your hair first thing in the morning!"
    show myc neutral
    with dis
    pause 1
    show myc upset
    with dis
    "Mychael got quiet, staring at the floorboards."
    "With his hair out of the way, I could finally read his expressions."
    "He did seem...{w=.2} upset?"
    p "Is...{w=.2} that okay?{w} I-I do need your help though, I'm pretty sure I'm just gonna get lost again on my own."
    "His tail flicked behind him."
    m "...Yeah,{w=.2} I’ll bring you home tomorrow morning."
    "I heaved a sigh of relief."
    p "Thanks, Mychael.{w} I’ll see you in the morning."
    m "Yeah..."
    show myc shy
    with dis
    m "Um...{w=.2} g-goodnight, [protag]."
    p "Goodnight,{w=.2} Mychael."
    "He seemed really happy being able to say that."
    "I plopped myself down onto Mychael’s bed, getting comfy beneath the blanket."
    hide myc
    with dis
    "Mychael was gathering some blankets of his own to make a makeshift bed on the floor in front of the fire.{w} He had an impressive collection of knitted items, a comfortable nest forming in the center of the room."
    "My eyes trailed after his tail, now out in the open as it flicked and swayed."
    "Kinda like a cat..."
    "..."
    "I miss [pet]..."
    "Now with a full stomach, dozing off came easy.{w} I didn’t even realize how tired I was."
    "I listened to the gentle crackling of the fire...{w=.2} my vision darkening..."

    show bg black
    with Dissolve (1)
    show bg cabin room nightt
    with Dissolve (1)
    show bg black
    with Dissolve (1)
    show bg cabin room nighttt
    with Dissolve (1)
    show bg black
    with Dissolve (2)
    show cg goodnight yn
    with Dissolve (1)
    m "Goodnight,{w=.2} [protag]."

    stop music fadeout 2.0

    scene bg black
    with dis
    jump day_two

label day_two:
    #DAY 2 START

    "..."
    "..."
    "...?"
    "A soft humming invaded my dreams, stirring me awake."

    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop
    play sound "audio/sfx/knitting.ogg" volume 0.7 loop

    show bg cabin room day
    with Dissolve (1)
    show bg black
    with Dissolve (1)
    show bg cabin room day
    with Dissolve (2)

    "I blinked my eyes open to unfamiliar surroundings,{w=.2} swaddled in a blanket that clearly wasn’t mine."
    p "Wh-where...?"
    p "...{w}Oh."

    show cg morning mychael 01
    with dis
    "I spotted the familiar figure of my host seated on a stool in front of the fire,{w=.2} hands deftly working on the green scarf bundled in his lap."
    "His back was towards me, but I caught glimpses of his fingers as the needles softly clicked between the yarn."
    "He looked incredibly adept at using them, the rhythmic movements almost hypnotic as the fibers wound together into an intricate pattern."
    play sound "audio/sfx/bed-wakeup.ogg" volume 0.7
    "I slowly stirred into a sitting position, rubbing at my eyes."
    show cg morning mychael 02
    with dis
    "The movement quickly caught his attention, ear flicking in my direction before his eyes trained onto me."
    "Just like last night, his pupils blew up as we made eye contact."
    "His expression lit up the instant he saw me."

    hide cg morning mychael 02
    with dis
    show myc happy
    with dis

    m "[protag], hey! I’m glad you’re finally awake."
    show myc nervous
    with dis
    m "You looked so tired...{w=.2} I-I didn’t want to disturb you until you've gotten enough rest."
    p "Hmn...{w} Good morning, Mychael."
    show myc surprise
    with dis
    pause 1
    show myc shy
    with dis
    m "Good morning, [protag]..."
    m "Did you sleep well?"
    p "Grgh..."
    "I was still too groggy to answer his question, a yawn slipping out as I stretched."
    show myc amused
    with dis
    "He smiled kindly, a soft chuckle under his breath."
    m "Like a baby, then?"
    show myc smile
    with dis
    "He pointed over his shoulder to the door beside the fireplace, tilting his head towards it."
    show myc happy too
    with dis
    m "You can freshen up in the bathroom if you’d like,{w=.2} while I start on making us some food."
    m "I’d have eaten breakfast by now but I’d want you to join me while the food is still hot."
    m "How do eggs and toast sound?"

    menu:
        "Sounds delicious.":

            show myc happy
            with dis
            m "Great!{w} I’ll see you in the kitchen then."
            jump cont_story_03

        "Do you have something else?":

            label veggie:

                $ veggie = True

                show myc surprise
                with dis
                m "Oh! I could make some fresh salad, if that’s what you’d prefer?"
                p "I’d love that.{w} Thank you."
                show myc nervous
                with dis
                m "Of course..."
                jump cont_story_03

    label cont_story_03:

    show myc smile
    with dis

    "He tucked away his knitting materials and set it aside."
    show myc happy too
    with dis
    m "Oh, I also have a surprise for you after breakfast!"
    show myc nervous
    with dis
    m "It’s... it’s not the most exciting surprise but..."
    show myc nervous2
    with dis
    m "Um.{w=.2} Just join me when you’re ready."
    hide myc
    with dis

    play sound "audio/sfx/kitchen-cabinets.ogg" volume 0.5 fadeout 2.0
    "He ducked into the kitchen without another glance."
    "I could hear his boots thud about the floorboards, cabinets opening and closing in succession in the kitchen."
    "I suppose that’s my cue."
    play sound "audio/sfx/bed-wakeup.ogg" volume 0.7 fadein 1.0
    "I rolled out of bed, leaving the warmth of Mychael’s blankets and trotting over to the door Mychael pointed out."

    stop music fadeout 1.0
    play sound  "audio/sfx/door-open.ogg" volume 0.5
    play music "audio/music/freshen-up-firefly.ogg" fadein 1.0 loop
    show bg cabin bathroom
    with dis

    "Stepping inside, I didn’t know what I was expecting when he said he had a bathroom, but it was surprisingly spacious!"
    "Everything looked like it was carved and polished out of wood."
    "He seemed to have everything you’d find in a modern bathroom;{w=.2} a sink with a cabinet, a shower and a tub, and even a toilet."
    "Curious, I crept over to the toilet in particular, inspecting it."
    "There wasn't a tank like you'd expect where the water would be stored, instead there was a compartment to the side full of sawdust and a scoop."
    "I expected it to have at least a bit of a smell, but it was surprisingly odorless."
    "There was even a roll of toilet paper on the side."
    "It was no flushing system but... it was hygienic.{w} Mychael must have done his research."
    "Walking over to the sink, I stared at the faucet before hesitantly twisting it."
    play sound "audio/sfx/sink.ogg"
    "I jumped when I heard the rush of water pouring in, swirling in the basin before disappearing to who knows where."
    "Wow."
    "..."
    "Why am I impressed by a damn functioning bathroom sink."
    "I helped with the dishes last night, I already knew Mychael had plumbing."
    stop music fadeout 3.0
    "Shaking my head, I finished freshening up and headed to the kitchen."

    show bg cabin kitchen day
    with dis
    play music "audio/music/curiosity.ogg" fadein 1.0 loop
    show myc smile
    with dis

    "Mychael looked up as I entered, a steaming kettle in his hand with two empty mugs on the counter."
    "It might've been the lighting, but he was taller than I remembered..."
    "Glancing to the table I could see he already finished plating up our food."
    p "Oh wow.{w} You work fast."
    show myc proud
    with dis
    "Mychael looked proud of himself."
    m "Can’t have my guest stay on an empty stomach!"
    show myc happy too
    with dis
    m "Go on! Have a seat.{w} I’ll join you in a moment."
    "I returned his smile and sat down, stomach grumbling as I looked at our plates."

    hide myc
    show bg table
    with dis
    pause .2

    if veggie:

        show item veggies
        with dis
        "Just as promised, Mychael had prepared a delightful bowl of salad."
        "Fresh lettuce, cherry tomatoes, minced carrots and onions.{w} I could see bits of homemade croutons added into the mix, too."
        "A drizzle of dressing weaved through the colorful ensemble,{w=.2} enticing me to take a bite."
        "It was quick and simple, but I could tell he put a lot of effort into it.{w} I couldn’t wait to dig in."

    else:

        show item eggies
        with dis
        "Once again Mychael was generous with the serving sizes."
        "Fat slices of bread were toasted perfectly with crisp buttered sides,{w=.2} bright red tomato slices and crisp salad peeking underneath the fluffy eggs."
        "It looked amazingly tantalizing, the smell of savory herbs wafting into my nose."
        "My mouth watered."
        jump cont_story_04

    label cont_story_04:

    hide item
    with dis
    play sound "audio/sfx/plate-up.ogg"
    show myc table smile2
    with dis

    "Mychael set down a steaming mug beside me before settling into his own seat."
    "Peeking above the rim I could see small flowers floating about, tinting the water yellow;{w=.2} it faintly smelled of apples."
    "I recognized the yellow dried pellets on tea packaging I’ve seen before."
    p "Oh! Chamomile?"
    "He nodded."
    show myc table sidesmile
    with dis
    m "I hope you like it..."
    p "I’m sure I will."
    show myc table smile2
    with dis
    "His smile widened, his tail swaying at the tip by his feet."
    "He seemed more relaxed showing his natural features this morning."
    "Any trace of panic and hesitation from last night were gone, replaced by a look of contentment."
    show myc table munch
    with dis
    "Mychael bit into his toast and I followed suit."
    "The food was as delicious as I expected."

    if veggie:

        "One forkful of the salad had me sighing in delight, the taste and textures mingling on my tongue.{w} I could tell these were fresh, and nothing beats fresh ingredients straight out of a garden."
        jump cont_story_05

    else:

        "The chunk of toast I bit into was heavenly, the butter sweet on my tongue.{w} The tomato and salad provided a nice crisp balance."
        "And the eggs!{w} Something about simple home-cooked food is just the best."
        jump cont_story_05

    label cont_story_05:

    "Mychael was happy to eat in silence, occasionally looking up at me as I enjoyed my food."
    "He’d smile when our eyes met, his bottom pair narrowing into a happy squint."
    "I wonder if he’d be open to some questions."
    p "Hey..."
    show myc table munchhm
    with dis
    m "Mm?"
    p "Do you mind if I ask..."

    label menu_chat_choices:

        menu:

            "How did you learn to cook?" if not chat_cook:
                jump chitchat_cook

            "How do you have plumbing in your house?" if not chat_plumbing:
                jump chitchat_plumbing

            "What's it like living in the woods?" if not chat_life:
                jump chitchat_life


    label chitchat_cook:

        $ chat_cook = True

        show myc table munchhm
        with dis
        p "Cottage pie is a pretty complicated recipe..."
        p "I just wonder if anyone taught you how to cook?"
        show myc table amused
        with dis
        m "I'd be lucky if someone could teach me how to make boiled eggs, firefly."
        m "But it was trial and error mostly.{w} My earlier endeavours were...{w=.2} uh..."
        show myc table laugh
        with dis
        m "{size=-5}{b}...pretty much inedible."
        show myc table amused
        with dis
        m "I picked up a thing or two about cooking though,{w=.2} so your tastebuds aren't gonna fall victim to any nasty creations like in my early days at least."
        show myc table hb nervoussmile
        with dis
        m "Um... speaking of...{w=.2} did you enjoy dinner last night?"
        p "Of course I did!"
        p "You're a really good cook, Mychael."
        show myc table surprise
        with dis
        m "I'm...{w=.2} glad."
        show myc table hb nervoussmile
        with dis
        m "It probably wasn’t obvious, but... I'm really happy I got to cook for you."
        m "I don't get guests often in case you couldn't tell..."
        p "I should ask you to cook for me everyday then!"
        show myc table happy
        with dis
        "He grinned at my joke, looking pleased."
        m "I'd be happy to."
        "I chuckled as I took another bite."
        p "So what's your favorite thing to cook?"
        "He lit up at the question."
        m "Fried mushrooms!"
        p "Fried mushrooms?"
        show myc table smile2
        with dis
        m "Yeah!{w} There's plenty to find and it's easy to make."
        p "Huh...{w=.2} I do remember finding a patch of mushrooms yesterday."
        show myc table hb surprise
        with dis
        p "They smelled pretty funky though."
        m "{size=-10}You... remember that?"
        p "Hm?{w=.2} What was that?"
        show myc table hb nervous
        with dis
        m "Nothing."
        m "A-anyways, mushrooms were the only thing I had for a while,{w=.2} before figuring out I could eat other stuff like roots and veggies."
        p "Do you forage all your ingredients?"
        show myc table smile2
        with dis
        m "Mostly!{w} The times I figured out how to catch fish and hunt game were the best of my life, I'll tell you that."
        m "My first taste of meat?"
        show myc at bounce
        "He did an awkward version of a chef's kiss,{w=.2} as if mimicking something he saw on television once."
        m "Maummer mee-ya."
        "...{w=.2}was he trying to say {i}mamma mia{/i}?"
        "He continued before I could even dwell on it for a second longer."
        show myc table amused
        with dis
        m "But...{w=.2} nothing beats what you humans are able to make."
        m "You guys go nuts with ingredients."
        m "Rice was a challenge!"
        m "It's a precious ingredient since I have to actually get some from a store,{w=.2} but once I figured out how to make it nice and fluffy I consider it a special treat."
        "I did a double take."
        p "You...{w=.2} go to the store?"
        show myc table hb surprise
        with dis
        m "Yeah?{w} Where else would I get it?"
        p "I-I thought you... you would grow it yourself...{size=-3} or something..."
        show myc table laugh at bounce
        "He laughed as I flushed in embarrassment."
        m "It's flattering you think I'm even capable of something that impressive but no..."
        m "There’s only so much the forest can provide."
        p "But... what about money?{w} We're talking about human currency, right?{w=.2} Otherwise how would you even..."
        p "Do you actually have a job?"
        "A thought occured to me."
        p "{size=-5}O-or did you steal it...?"
        show myc table amused
        with dis
        "He almost looked offended."
        m "Do you take me for a criminal?"
        p "N-no!{w} But that would mean... then h-how..?"
        show myc table wink
        with dis
        "Mychael bit into his toast, his two eyes winking in mischief."
        m "I have my ways, firefly."
        "What's that supposed to mean!?"
        show myc table munch
        with dis

        if chat_cook and chat_plumbing and chat_life:
            jump cont_story_06
        else:
            jump menu_chat_choices

    label chitchat_plumbing:

        $ chat_plumbing = True

        p "I know it's a silly question... but I can't stop thinking about it."
        show myc table hb surprise
        with dis
        m "Oh!"
        m "You were wondering about that?"
        "The embarrassed look on my face was probably enough of an answer."
        show myc table amused
        with dis
        m "Aw."
        show myc table smile2
        with dis
        m "Well,{w=.2} it's nothing fascinating.{w} It's just rainwater I've got stored above the cabin."
        p "Just...{w=.2} rainwater?"
        "He nodded."
        "I detected a hint of pride as he continued."
        m "It's actually a recent installment, believe it or not."
        show myc table sidesmile
        with dis
        m "Granted the project took a while. Gathering materials,{w=.2} figuring out the tools,{w=.2} finding the right instruction manuals..."
        m "Plus I had to figure out where to store the water tank."
        show myc table smile2
        with dis
        m "And don't worry, I installed a filtration system, so it's safe for us to use!{w} I check in every few weeks to make sure nothing's contaminated."
        "That sounded daunting.{w} Especially considering he lived all the way out here in the woods."
        p "You did all that on your own?"
        show myc table sidesmile
        with dis
        m "I kinda had to."
        show myc table smile2
        with dis
        m "A-anyway, it took a whole lot of calibrating and adjusting,{w=.2} but it really worked out!"
        show myc table sidesmile
        with dis
        m "And now that I think about it, {w=.2} I’m glad you get to be comfortable here during your stay too."
        show myc table smile2
        with dis
        m "Does that answer your question?"

        menu:

            "Yeah.":
                if chat_cook and chat_plumbing and chat_life:
                    jump cont_story_06
                else:
                    jump menu_chat_choices


            "Where'd you learn how to do all that?":

                show myc table hb nervous
                with dis
                m "I... had to figure out a lot of things on my own."
                "There was a faint hint of exhaustion in his eyes."
                show myc table smile2
                with dis
                m "But to answer your question,{w=.2} I go to libraries a lot.{w} It’s where I learned about a majority of things."
                "The fact that he even ventured into buildings at all already surprised me."
                m "And if I’m {i}real{/i} lucky they have all these neat DIYs and workshop manuals archived for anyone to browse through."
                m "It took a while to figure everything out...{size=-5}{w} a really long time actually...{/size}{w=.2} but hey, {w=.2} I had nothing but time."
                show myc table happy
                with dis
                m "And it paid off!"
                m "I'm considering upgrading the toilet next,{w=.2} but for now the composting setup works fine."
                show myc table wink
                with dis
                m "Learned about that in an old camping guide."
                show myc table smile2
                with dis
                "He paused to take a breath, as if he hadn't talked this much in a while."
                m "Uh, I-I’m rambling but...{w=.2} that’s how I did it."
                m "Is there anything else you wanna ask?"

                menu:

                    "No, I'm good.":
                        if chat_cook and chat_plumbing and chat_life:
                            jump cont_story_06
                        else:
                            jump menu_chat_choices


                    "Wait, you've been to libraries?":

                        show myc table happy at bounce
                        "His ears perked up, posture straightening."
                        m "Oh, yeah!{w} I can’t tell you enough how much books have helped me."
                        m "I’ve made it this far only because I quickly figured out how to read.{p}Well, figured out that I {i}can{/i} read."
                        p "Do you visit often?"
                        show myc table smile2
                        with dis
                        m "In my early days?{w=.2} Any chance I could get."
                        m "Nowadays I stick to my side of the forest, though."
                        show myc table amused
                        with dis
                        m "Gotta make sure people don't wander too far off than they're meant to..."
                        "I paused in my chewing at the teasing lilt in his voice."
                        p "H-hey!" with vpunch
                        show myc table laugh
                        with dis
                        m "I'm joking."
                        m "Anyways..."
                        show myc table sidesmile
                        with dis
                        m "If you’re wondering what I do about...{w=.2} {i}this{/i}..."
                        "He gestured towards his face."
                        m "I just... have to make sure everything’s covered..."
                        show myc table smile2
                        with dis
                        m "You'd be surprised how little people pay attention to me when I bundle up just right."
                        p "Do people not give you trouble?"
                        "He shrugged nonchalantly."
                        m "Small town libraries are usually so empty from my experience.{w} And people just mind their own business there."
                        p "Huh, I guess that's true."
                        p "I can’t remember the last time I visited a library..."
                        "I guess libraries would be Mychael's equivalent to the world wide web."
                        "I should introduce him to the internet sometime."
                        "..."
                        "Actually maybe not."
                        "Not without parental controls."
                        "Finally satisfied, I nodded and went back to eating my food."
                        show myc table munch
                        with dis

                        if chat_cook and chat_plumbing and chat_life:
                            jump cont_story_06
                        else:
                            jump menu_chat_choices


    label chitchat_life:

        $ chat_life = True

        p "I still can't believe how cozy you've managed to make it, considering the whole...{w=.2}  middle of nowhere thing."
        show myc table hb surprise
        with dis
        m "It wasn't like this when I found it."
        p "No?"
        show myc table sidesmile
        with dis
        m "It was a major...{w=.2} uh..."
        m "Fix-her-up-her?"
        "So the cabin was abandoned..."
        p "I never would've guessed!"
        show myc table smile2
        with dis
        m "Yeah, I'm really happy I get to live somewhere...{w=.2} permanent, for once."
        m "It's not much but it's home."
        p "What's it like?"
        m "Peaceful.{w=.3} Quiet.{w=.3} I do like it a lot."
        m "The forest provides me with everything I need."
        show myc table stare
        with dis
        pause 0.5
        show myc table hb nervous
        with dis
        m "A-and nobody bothers me for the way I look out here."
        "His ears twitched slightly."
        m "Sometimes you just happen to end up where it's most convenient for you...{w=.2} and everyone else."
        "The way he avoided my eyes as he said that gave me the impression there's something more to it."
        "Like his home wasn't just out of convenience...{w=.2} but a fear of something else."
        "Rejection, perhaps?"
        "Or something worse?"
        show myc table smile2
        with dis
        m "A-anyways, {w=.2} I don’t really have anything else to say about it, unless there’s something specific you wanna ask."
        "He doesn’t think about his answer much before beaming at me."
        show myc table happy
        with dis
        m "What about you?{w} I know you’ve told me a little bit about yourself, but... what’s it like being you?"
        "I scoffed, waving a hand."
        p "Please... I’m the least interesting person in this room, trust me."
        show myc table smile2 at zoom_in3
        "His eyes were shining in earnest as he leaned forward."
        m "Tell me anyway."
        p "Oh! W-well..."
        "I told him about my life, at least the parts I was comfortable with sharing."
        "Just like last night his eyes didn’t leave my face, occasionally darting about my features in interest."
        "The direct ogling was making me nervous{w=.2} but I suppose I was doing the exact same thing when it was his turn to talk."
        "Eventually I came to the topic of my job and the woes of living in modern capitalism."
        p "I am a bit jealous...{w=.2} you have the whole cottage-core aesthetic practically perfect."
        show myc table hb surprise at zoom_out2
        "His face morphed into a confused pout."
        m "Cottage-core...?"
        "I explained it to him in my own words."
        m "Oh!"
        m "You're saying... you wanna live the way I do?{w=.2} Out in the woods?"
        "I nodded without hesitation."
        show myc table hb nervoussmile
        with dis
        m "I mean...{w=.2} I-I wouldn't mind showing you the ropes..."
        "His tone seemed strangely lilted."
        p "What do you mean?"
        show myc table stare
        with dis
        m "...{w}Nevermind."
        show myc table hb nervous
        with dis
        m "Anyways..."
        m "I don't get what the appeal is but...{w=.2} it's not easy either, you know."
        m "The forest provides but it’s up to me to make use of it."
        m "Starting out was..."
        show myc table dark
        with dis
        "A dark look crossed over his face then, as if reliving a bitter memory."
        m "..."
        m "...{i}rough{/i}."
        show myc table stare
        with dis
        m "..."
        show myc table wink
        with dis
        m "But I’m built for survival."
        "I feel like asking him to elaborate would make things...{w=.2} awkward."
        "I decided to veer the topic into a different direction."
        p "Doesn’t it get lonely?"
        show myc table hb surprise
        with dis
        m "Hm...{w=.2} sometimes...{w} But I’m used to it."
        "He smiled, his eyes lighting up."
        show myc table happy
        with dis
        m "Besides, I have you at the moment, don't I?"
        show myc table smile2
        with dis
        m "I never thought I'd enjoy having someone around."
        m "...You must be really special."

        if chat_cook and chat_plumbing and chat_life:
            jump cont_story_06
        else:
            jump menu_chat_choices

    label cont_story_06:

    show myc table munch
    with dis
    "I'm starting to know a lot more about Mychael."
    "He didn't directly say it, but it felt like he was lonelier than he was letting on."
    "Not to mention how he managed to make a home for himself...{w=.2} all on his own."
    "I had to wonder if he had anyone at all."
    show myc table stare
    with dis
    p "Do you have any family around?"
    m "...Family?"
    "His expression turned solemn for a moment before he looked sheepish."
    show myc table amused
    with dis
    m "Remind me how that works again...?"
    m "I-I get the concept,{w=.2} based on some books I've read."
    m "I don't have what you call 'parents' if that's what you're asking."
    "My mouth dropped open in shock."
    p "No parents?"
    show myc table munch
    with dis
    "He shrugged and took another bite of toast."
    m "Not that I recall."
    p "Then how did you—{nw}"
    show myc table hb surprise at bounce
    m "What’s that like?{w=.2} Living with so many people like you in such close proximity?"
    p "Huh?"
    m "That's how it works, right? You and other humans living in one house..."
    m "And you have this...{w=.2} uh,{w=.2} 'denna' thing that makes you... 'relate' to the rest."
    m "That's what makes a family, right?"
    "Was he talking about {i}DNA{/i}?"
    "His definition threw me off, {w=.2} but I had to answer somehow."
    p "N-not just that.{w} Family is..."

    menu:

        "People you’re related to, like your mom and your dad and your siblings and relatives.":

            "He nodded at my explanation.{w} I couldn't help thinking that he looked somewhat relieved."
            show myc table smile2
            with dis
            m "If that's the case...{w=.2} I definitely don't have family around."
            m "As far as relations go, I'm the only one of me there is and ever will be."
            "He sounded determined about that fact."
            p "So you're not...{w=.2} I assume you're not a family person then?"
            show myc table amused
            with dis
            "He looked amused at my question."
            m "Definitely not."
            "I found that surprising;{w=.2} he seemed like the type, but I guess I couldn't just assume that."
            show myc table stare
            with dis
            m "Although..."
            "He twiddled with his mug, his brows furrowed as he stared at it."
            show myc table sidesmile
            with dis
            m "It does sound nice... knowing you have that undeniable bond with someone."
            m "Something to link you with others, just underneath the surface."
            m "That kind of relationship... that makes it unique and precious, wouldn't it?"
            show myc table shysmile
            with dis
            "He looked at me then, his eyes almost full of longing."
            m "But some things just... aren't meant for me."
            p "What do you mean?"
            show myc table stare
            with dis
            pause 0.5
            show myc table sidesmile
            with dis
            "He smiled, shrugging."
            m "Nothing you have to worry about, firefly."
            "What a strange man..."

            jump cont_story_07

        "People that you love and care about, who love and care about you too.":

            show myc table stare
            with dis
            "He seemed intrigued."
            m "Is that so?"
            m "That... {w=.2} does sound nice."
            show myc table hb nervous
            with dis

            m "I-is there... anyone that {i}you{/I} love and care about?"

            menu:

                "Of course, I do. I have a family.":

                    p "Heck, I'd even call my cat family!"
                    show myc table stare
                    with dis
                    m "Ah... right.{w} Obviously."
                    jump after_family

                "Yeah. I love my friends.":

                    show myc table surprise
                    with dis
                    m "Your friends can be considered family too?"
                    p "Yeah! I don't see why we have to be related to be family."
                    p "I even consider my cat family."
                    m "Oh."
                    show myc table stare
                    with dis
                    jump after_family

            label after_family:

            m "And this is the same for all families?"
            "I bit my lip, pondering the question."
            p "It would be...{w=.2} naive to think that."
            p "A lot of families do love and take care of one another, but not everything's perfect."
            p "Sometimes that love can be misplaced... o-or taken advantage of... or even abused."
            "Mychael looked thoughtful."
            m "So it starts with love...?"
            m "I've read some stories about that.{w} Love, I mean."
            show myc table sidesmile
            with dis
            m "Though certain feelings just don't make sense to me."
            show myc table amused
            with dis
            m "A-at least from a reader's perspective."
            p "I guess you'd have to experience it for yourself to understand?"
            show myc table stare
            with dis
            "He stared at me unblinking for a moment."
            show myc table hb nervoussmile
            with dis
            m "Yeah... you might be right."
            show myc table smile2
            with dis
            m "I never considered that."
            show myc table laugh
            with dis
            m "Then again who would bother loving a monster like me, huh?"
            p "Wha...{w} y-you're not a monster..."
            m "I look like one, don't I?"
            p "That's besides the point..."
            show myc table amused
            with dis
            m "You're not denying it though."
            p "I'm just saying--{nw}"
            m "It's okay.{w} You don't have to lie to me."
            m "So...{w=.2} family?"
            p "Right..."

            jump cont_story_07

        "Actually, I guess they {i}are{/i} just people you live in close proximity to, whether by choice or not.":

            show myc table dark
            with dis
            "Mychael's ears flattened instantly, followed with a look of discomfort on his face."
            m "I see."
            m "All the more reason I don't need family then."
            m "I don't understand how you humans can be around each other so much."
            m "If it was me in that situation... I don't even wanna think about it."
            "I was taken aback by that."
            p "Do you... hate being around humans?"
            show myc table panic2 at bounce
            "He straightened in his seat."
            m "N-no! That's not what I meant!"
            m "How do I explain this..."
            "He waved at the air while his tail flicked aggressively."
            m "I... can be around humans... {w=.2}{i}because{/i} we're so different."
            m "Your presence near me doesn't affect me at all."
            m "But um,{w=.2} say... you're like me."
            "He gestured wildly at himself."
            m "As in, {i}like me{/i}, like me."
            m "I-I might get...{w=.2} a bit dangerous."
            "I couldn't ever imagine associating Mychael with the word 'dangerous' but he seemed dead serious."
            p "What are you saying?"
            p "Like... if I had horns and a tail like you?"
            show myc table sidesmile
            with dis
            "He laughed under his breath, but it sounded forced."
            m "Exactly that, actually."
            p "Are you saying...{w=.2} there’s more like you out there?"
            show myc table dark
            with dis
            m "..."
            "He didn't seem like he wanted to talk about it anymore, so I cleared my throat and changed the topic."

            jump cont_story_07

    label cont_story_07:

    show myc table stare
    with dis
    p "To be fair, everyone’s definition of family could be different."
    p "What about you?{w} What's your definition of family?"
    show myc table hb surprise
    with dis
    "Mychael looked surprised I asked him that question."
    show myc table sidesmile
    with dis
    m "I... don't know..."
    m "I've never had one,{w=.2} a-and I think your answer just confused me more."
    p "Well, if you ever figure it out, let me know."
    "Mychael stared at the remaining crumbs on his plate before he nodded, avoiding my gaze."
    m "Sure."
    m "..."
    stop music fadeout 5.0
    "We both fell quiet, the lull in conversation blanketing us in a comfortable silence."
    "All this family talk...{w=.2} it reminded me of the reason why I'm out here in the first place."
    "To look for my beloved cat, a sight I might never be able to see again."
    play music "audio/music/missing-kitty.ogg" fadein 3.0 loop
    "I couldn't help the sinking feeling in my chest, the growing pit in my stomach."
    p "I wish...{w=.2} I wish I was able to find [pet]."
    show myc table hb surprise
    with dis
    p "You would've loved %(pronoun4)s."
    "Mychael opened his mouth to say something, but changed his mind."
    show myc table hb nervous
    with dis
    "My voice warbled as a lump formed in my throat."
    p "S-sorry..."
    p "I just miss %(pronoun4)s so much."
    p "I keep thinking if I just went looking for %(pronoun4)s sooner... maybe I would've been able to find %(pronoun4)s by now."
    "He was quick to speak up."
    show myc table surprise
    with dis
    m "You did your best, firefly."
    m "No one else could've gone to the lengths that you did."
    m "You almost risked getting yourself--"
    show myc table stare
    with dis
    pause 0.5
    show myc table hb nervous
    with dis
    pause 1
    show myc table sidesmile
    with dis
    m "I'm sure... wherever %(pronoun2)s is...{w=.2} %(pronoun2)s's...{w=.2} doing okay."
    p "You really think so?"
    show myc table hb nervous
    with dis
    m "I...{w=.2} I know so."
    "His voice was laced with a confident assurance, despite the worried look on his face."
    "I nodded with a quiet sniff."
    p "I hope so..."
    p "%(pronoun1)s's just... important to me, is all."
    show myc table stare
    with dis
    "Mychael looked like he wanted to reach across the table for me, but sighed instead."
    stop music fadeout 5.0
    show myc table hb nervous
    with dis
    m "Actually..."
    m "I'm sorry, [protag]."
    m "I-I should tell you..."
    m "..."
    play music "audio/music/curiosity.ogg" fadein 1.0 loop
    m "U-um."
    show myc table amused
    with dis
    m "M-maybe I do have family, now that I think about it.{w} That was the surprise I mentioned before."
    p "Wait,{w=.2} really?"
    "He nodded."
    show myc table smile2
    with dis
    m "Are you done?{w} I could take you to go meet them right now."
    "I looked down at my plate.{w} During the conversation I didn't even realize I'd finished the meal."
    p "Yeah. I'm done."
    play sound "audio/sfx/stack-plates.ogg"
    hide myc
    with dis
    "His movements were quick, stacking our empty plates and mugs and setting them in the sink."
    "He grasped my hand before I could say another word,{w=.2} pulling me up and heading outside with me in tow."

    play sound "audio/sfx/door-open.ogg"
    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
    show bg woods daytime
    with dis

    "As the door swung open I could only see forest ahead,{w=.2} before he tugged me along as he rounded the side of the cabin."
    show bg garden
    with dis
    play sound "audio/sfx/garden-footsteps.ogg" loop

    "Almost immediately my peripherals were assaulted with greens on both sides."
    "I figured he was the type to grow his own vegetables,{w=.2} but to see it in person as confirmation was a whole different thing."
    "With Mychael leading the way, I only had a moment to take in the surrounding garden."
    "He had marked the different plots with messy drawings on small wooden signs jutting out of the dirt."
    "Carrots, lettuce, potatoes;{w=.2} trellises of tomatoes and beans."
    "I wouldn't have been able to differentiate one plant to another without the signs."
    "Even the chamomile from our tea just now grew abundant close by, the small buds swaying gently."
    play sound "audio/sfx/bump.ogg" volume 0.3
    "I bumped into Mychael as he suddenly stopped,{w=.2} the man looking over his shoulder to beam at me." with hpunch
    "We reached what looked like a fenced-off area, with a bit of netting stretching all around."
    stop music fadeout 3.0
    "He stepped aside,{w=.2} watching me as my eyes widened."

    show cg hiya ladies
    with dis
    hide bg garden
    play sound "audio/sfx/chickadees.ogg" volume 0.5 loop
    play music "audio/music/ladies.ogg" fadein 2.0 loop
    "Chickens!"
    "Three fat happy little hens strutted about like they owned the place."
    "As he entered through the gate, the hens swarmed over in an instant at Mychael’s feet, circling him and pecking at his boots."
    m "Ladies,{w=.2} meet [protag]!{w} [protag],{w=.2} these are Mawar, Sansuyu and Primrose."
    m "Or as I like to call them,{w=.2} Marmar, Sunny and Rosie."

    show bg coop
    show mycrose happy at bounce
    hide cg hiya ladies
    with dis
    "He ducked to pick one up, fluffing up her feathers as he smiled."
    show mycrose smile
    with dis
    "He gently scratched the hen's little head which I assumed was Rosie."
    "She practically melted at his pampering, eyes sliding shut."
    "The other two flapped their wings in a huff and went about their business once more."
    stop sound fadeout 2.0
    "Mychael leaned closer, beckoning me to pet Rosie."
    "She was so soft!"
    show mycrose smile2
    with dis
    m "Rosie’s the oldest.{w} She doesn’t lay eggs anymore, but I couldn’t bring myself to...{w=.5} um..."
    show mycrose nervous
    with dis
    m "You know."
    show mycrose smile
    with dis
    m "So I brought her some friends!{w} Marmar came first, Sunny’s a more recent addition."
    show mycrose happy
    with dis
    m "What do you think?{w=.2} Do we make a good family?"
    "I laughed and nodded, watching as Rosie nuzzled into Mychael’s chest."
    p "I didn't expect chickens of all things..."
    show mycrose smile2
    with dis
    m "Were you... expecting something else?"
    p "I was expecting it to be some{i}-one{/i} else."

    show mycrose solemn
    with dis
    m "Oh..."
    show mycrose amused
    with dis
    m "Heh, no..."
    m "When you look like me... people generally don't stick around."
    "There's that negative self talk again."
    p "You don't even look that bad..."
    show mycrose solemn
    with dis
    "His eyes flicked to mine, a look of pleasant surprise crossing his face."
    m "You really think so?"
    p "Yeah?"
    show mycrose amused
    with dis
    m "You can't be {i}that{/i} naive, firefly."
    p "I mean it!" with vpunch
    show mycrose amused2
    with dis
    "He let out a polite scoff as he scratched Rosie's head absently."
    m "You {i}genuinely{/i} believe people wouldn't run away at the sight of me?"
    p "Well... {i}I{/i} didn't."
    "His smile turned smug, the corner of his lips lifting just a bit."
    m "Of course you didn't."
    show mycrose cheeky
    with dis
    m "Because you {i}couldn't."
    "...Shoot.{w} He wasn't wrong."
    "I was pretty much paralyzed in his bed when we first met."
    p "B-but I still don't think you look that bad!"
    m "Is that so?{w} Describe me then."
    p "...{w=.2}What?"
    show mycrose amused2
    with dis
    m "You heard me.{w} Look at me{w=.2} and describe what you see."
    "For a second I thought he was being condescending but...{w=.2} looking at his eyes, all I could see was a bit of playfulness."
    p "Uh."
    "He looked at me expectantly, eyes shining."
    p "You're... {w}tall?"
    m "Go on..."
    p "You have blonde hair."
    "He gave an amused squint, his left ear twitching."
    m "What else?"
    p "..."
    p "You have green skin...{w=.2}{size=-5} and a tail..."
    "He chuckled, though there was no malice in it."
    m "But that's not all, is it?"
    "He definitely expected me to say it straight."
    p "Oh fine!" with hpunch
    p "So you don't look human."
    p "So what?"
    stop music fadeout 3.0
    show mycrose amused
    with dis
    "He hummed absently."
    m "As I was saying, animals generally don't care if you look like a monster."
    "My heart twisted at his words."
    "His passive nonchalance somehow makes it even worse."
    p "Mychael...{w} you're not a mo--{nw}"
    play music "audio/music/ladies.ogg" fadein 2.0 loop
    "A tug at my shoelace caught my attention." with vpunch

    show mycrose solemn
    with dis
    show cg sunny
    with dis

    "A light brown hen stood at my feet, her beady eyes shining.{w} Sunny flapped her wings almost expectantly."
    m "Aw...{w=.5} I think she likes you!"
    m "Go ahead! Pick her up,{w=.2} gently,{w=.2} like how I did with Rosie."
    "I hesitated, but slowly lowered myself to cup Sunny by her wings."
    hide cg sunny
    show mycrose smile2
    with dis
    "Lifting her up, she was quick to nestle herself until she was comfortably tucked under my arms."
    "I could feel her wings wiggling as she nuzzled into my side."
    "So...{w=.2} cute..."
    show mycrose soft
    with dis
    "Mychael’s gaze softened as I cooed at the chicken, mimicking her small clucks."
    m "S-so um...{w=.2} did it help?"
    m "Cheering you up, I mean."
    "Oh.{w} So that’s what this was."
    "A fuzzy feeling bloomed in my chest as he looked at me, chicken in his arms and concern on his face."
    p "A little bit.{w=.2} Yeah."
    show mycrose cheeky
    with dis
    m "Only a little?"
    "I snickered, rolling my eyes."
    p "Okay, mister.{w=.2} A lot."
    show mycrose happy at bounce
    m "That's more like it!"
    "His proud grin was infectious.{w} I couldn’t help smiling back."
    hide mycrose
    with dis
    "We spent a bit more time with the hens, petting them until they were satisfied."
    "Mychael even showed me the spot where they liked to have their dust baths,{w=.2} little chicken-shaped holes scattered about in the dry soil underneath the coop."
    "Once the gals had enough of us, we refilled their water container before leaving."
    "He left them some treats, procuring them straight out of his pockets before shutting the gate."
    hide mycrose
    show bg garden
    with dis
    "The girls’ excited chatter over the food faded as we made our way back inside his cabin."

    play sound "audio/sfx/door-shut.ogg"
    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop
    show bg cabin room day
    with dis
    "I sat by his bed as he crouched down by the fireplace."
    "From the window I could see the sun outside was getting higher,{w=.2} it might be close to afternoon now."
    p "Hey, Mychael?"
    show myc neutral
    with dis
    m "Mm?"
    "He looked up at me from where he was stoking the fire."
    "I rubbed my arms, unsure where to place my gaze."
    p "I think... it's a good time for me to go now?"
    p "I didn't..."
    "My expression fell, but I caught myself quickly."
    "He'd done his best to cheer me up; it'll be inconsiderate towards him to leave in a bad mood."
    p "I-I might have to accept that I'll never see [pet] again."
    p "I think it's better if I focus on moving on..."
    show myc upset
    with dis
    "He was quiet for a moment, hands in his pockets."
    m "I-if you say so..."
    show myc nervous
    with dis
    m "But... you don’t have to leave just yet."
    m "We’ve still got plenty of daylight left, a-and... there’s some places I wanna show you."
    show myc nervous2
    with dis
    m "Won’t you come with me?"
    "I had to decide..."

    $ _window_hide()
    show item fake choices
    pause 0.5
    play sound "audio/sfx/you-dont-have-a-choice.ogg"
    show item fake choices 02
    with dis
    pause 0.8
    hide item fake

    show myc desperate at zoom_in
    m "I-I promise I’ll take you home right after!" with vpunch
    show myc at zoom_in
    "He took another step towards me."
    show myc at zoom_in2
    m "Please, firefly?"
    "I didn’t want to say it, but he looked desperate."
    p "Okay, okay!{w} I’ll go with you!"
    show myc elated at zoom_out
    "The joy on his face was shining bright as a billboard."
    m "Great!{w} Let me get our stuff."
    hide myc with dis
    "He disappeared into the kitchen, returning with my backpack in one hand and a satchel in the other."
    "He passed it to me as he walked by towards the front door."
    "Huh, I almost forgot I had this."
    play sound "audio/sfx/backpack-backpack.ogg" volume 0.5
    "Rifling through my bag, I found cat treats, [pet]'s collar, a broken compass and--!"
    show item phone
    with dis
    "My phone!"
    "...The battery was dead, though."
    "Still, that's one less thing to worry about."
    hide item
    with dis
    "I checked through my bag once more, finding an empty water bottle."
    "I frowned, distinctly remembering I forgot to pack water for my trip."
    "Or at least... Mychael told me I did."
    "Didn't I...?"
    m "You ready?"
    show mycjackie cb
    with dis
    "I looked up at Mychael, startling when I spotted the large crossbow in his hands."
    show mycjackie cb whoops
    with dis
    "He followed my gaze and shrugged, albeit with a nervous smile,{w=.2} like he’d been caught doing something he shouldn’t be."
    show mycjackie amused
    with dis
    "He quickly strapped the weapon to his back and out of sight."
    m "Don't worry, I'm not gonna use it unless necessary."
    p "I would hope not!" with hpunch
    "He chuckled at my indignant tone."
    m "You think I'm gonna let you out into the woods without guaranteeing your safety?"
    m "I made a promise to get you home, so this is just an extra precaution."
    p "You don't think it's a bit...{w=.2} much?"
    m "Better safe than sorry, firefly."
    "He did have a point.{w} If anyone knew these woods and the kind of danger it held, it'd be Mychael."
    "I glanced over him again, noticing he'd changed his oversized cardigan for something more outdoor appropriate."
    show mycjackie blush
    with dis
    "His eyes tracked mine, his shoulders stiffening as a tint spread across his face."
    show mycjackie at bounce
    m "S-so!{w} Shall we?"
    play sound  "audio/sfx/door-open.ogg" volume 0.5
    "He opened the door and waved me out."
    hide mycjackie
    show bg woods daytime
    with dis
    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop

    "I stepped outside to glance around his front yard."
    "The landscape wasn't anything special, it was actually left quite plain, just thick with trees and foliage."
    "Only paths of dirt and flattened grass clued me in the routes Mychael would use as he comes and goes, webbing in all directions trailing to the front door."
    "Come to think of it,{w=.2} anyone passing through would be able to spot Mychael's house if they squinted through the trees carefully enough."
    "...I guess he was right that nobody's walked through this area in years."
    play sound "audio/sfx/door-shut.ogg"
    "I heard a lock turn before Mychael joined me by my side."
    "He smiled wide before tipping his head in a direction, making sure I was behind him before he started walking."
    "I was hesitant, but followed suit."
    play sound "audio/sfx/forest-footsteps.ogg" loop

    show bg woods trail 01
    with dis

    "It was quiet as we traveled, save for the sounds of nature calling out around us."
    "The weather was bright and warm, the sun casting pretty rays through the gaps in the trees."
    "I had to admit,{w=.2} enjoyable at it was,{w=.2} the birdcalls and rustling of leaves as we walked somewhat brought bad memories."
    "Yesterday was miserable.{w} I was lost, tired and hungry."
    "There was a chance I wasn't gonna make it out alive."
    "I watched Mychael's back as he lead the way, the man barely paying any mind to his surroundings."
    "His ear would occasionally flick back in my direction, but overall he seemed confident on where to go."
    "Having Mychael as my guide home was definitely a great assurance.{w} It made me even more grateful he'd found me when he did."
    "I sighed and shook off the negative feelings, keeping pace while appreciating the fresh air."
    "I stepped up next to my companion, willing my voice to speak after plenty of silence."
    p "...This is actually kinda nice."
    m "Hm?"
    p "Um, a good old nature walk."
    "I coughed into my fist, feeling embarrassed."
    p "I don't go outside as often as I should..."
    "Mychael smiled kindly."
    m "I'm glad I get to bring you then."
    p "Yeah...{w=.2} feels different when you know where you're going."
    stop sound fadeout 5.0
    p "..."
    p "A-actually, where {i}are{/i} we going?"
    "He sensed my nervousness and laughed."
    m "Don't worry.{w} We're almost there."
    "I looked up and saw it before he even pointed it out."

    show bg woods trail 02
    with dis
    "A clearing in the distance, the trees growing strangely sparse in that area."
    "I held my breath as I noticed the grass slowly started to dot with flowers, delicate blooms swaying here and there in the breeze."
    "As we got closer, Mychael watched me as my mouth dropped open, a knowing twinkle in his eyes."
    "It was... breathtaking."

    show bg meadow
    with dis
    play music "audio/ambience/meadow-ambience.ogg" fadein 1.0 loop

    "A secluded little meadow of flowers, lit up by beams of light making the scenery resemble a page from a forgotten fairy tale."
    "Butterflies flitted about in pairs, their wings flickering and complementing the surreal yet enchanting ambience of the whole place."
    "Mychael let me gawk some more before walking ahead, turning to face me before sitting down to relax on the grass."
    "He slipped off his satchel and laid it on the grass by his side along with his crossbow."
    "I blinked out of my stupor and approached him, spinning around to drink everything in before plopping myself down next to him."
    m "So?{w=.2} What do you think?"
    m "Pretty, isn’t it?"

    show bg meadowpov
    show mycmeadow smile
    with dis
    "I nodded dumbly before finally glancing to face him, the man's gaze on me softening as our eyes met."
    "A butterfly approached us rapidly, making me flinch on instinct."
    show mycmeadow oh
    with dis
    pause 1
    show mycmeadow butterflysmile
    with dis
    "It landed on his finger as he held it out, its wings flapping gently."
    "He smiled at the dainty creature, a fond look in his eyes before he held it out towards me."
    show mycmeadow butterflyask
    with dis

    m "Do you like butterflies, [protag]?"

    menu:

        "I love butterflies.":
            p "I do!{w} I think they’re so pretty."
            p "This is...{w=.2} this is amazing, Mychael."
            show mycmeadow butterflyblush
            with dis
            "His usual prideful smirk was absent, replaced instead with a shy smile."
            m "...I'm glad you like it."
            jump cont_story_08

        "I think they're okay.":
            show mycmeadow butterflysmile2
            with dis
            "Mychael nodded, rotating his finger to watch the creature flutter its wings."
            m "I think they’re fascinating."
            m "Their...{w=.2} um..."
            m "M-meta...{w=.2} metaphormor...{w=.2} ph-phormosis...?"
            p "Metamorphosis?"
            show mycmeadow butterflygrin
            with dis
            "He beamed, nodding excitedly."
            m "Methasphmorphorsis!"
            "My cheeks puffed in holding back a laugh.{w} Mychael knew he fumbled but grinned anyway."
            m "That word you said."
            show mycmeadow butterflysmile
            with dis
            m "It's... amazing.{w} To have that ability of being reborn... into a different creature."
            m "The chance to look different.{w} The chance to look...{w=.2} beautiful..."
            "I scanned his face thoughtfully before pulling my knees up to my chest."
            p "...It kind of is."
            jump cont_story_08

        "I’m... scared of them, actually.":
            show mycmeadow butterflyohno
            with dis
            "Mychael’s eyes widened, a look of guilt flashing across his face."
            "He slowly lowered his hand, the butterfly (menace) still perched on his fingertip."
            m "Oh no... this place has to be your worst nightmare!"
            m "I-I’m sorry... we can leave right now if you want to...?"
            "I inhaled a breath before shaking my head."
            p "I... I still wanna be here."
            p "It’s okay, Mychael."
            "I eyed the insect crawling on his finger, wings gently flapping.{w} I leaned over to Mychael slowly."
            p "{size=-5}P-promise you’ll keep them off me though?{/size}"
            show mycmeadow butterflyoh
            with dis
            pause 1
            show mycmeadow butterflygrush
            with dis
            "Mychael looked at me with a playful grin."
            m "I won’t let a single wing tip even brush you, firefly."
            "He sounded so determined I had to snort with laughter, forgetting my fears in an instant."
            jump cont_story_08

    label cont_story_08:

    hide mycmeadow
    show bg meadow
    with dis

    "The sun was at its peak now, the air getting warmer as minutes passed."
    "The leafy canopy over us provided enough cover for us to not overheat."
    play sound "audio/sfx/pluck.ogg"
    "Mychael picked a flower with his other hand and placed it in my palm, his tail looping loosely around us both as my cheeks darkened."
    play sound "audio/sfx/mychael-purr-as-a-treat.ogg" fadein 3.0 volume 0.4 loop
    "He closed his eyes and leaned back further, the butterly still resting on his hand."
    "My ears caught a soft rumbling before I realized it was coming from his direction."
    "I almost wanted to ask but...{w=.2} I didn't want to ruin the moment."
    "My gaze dropped as I twirled the flower in my hand, holding the stem delicately."
    "The gesture felt... platonic{w=.2}{i} but also{/i} romantic...?"
    "I wonder if Mychael was even interested in relationships..."
    "He'd been alone most of his life.{w} He'd probably get tired of my presence sooner or later."
    "Before I could contemplate further the butterfly on Mychael's finger took off, my gaze trailing after it as it left the sunlight and flew away into the woods."
    "Which reminds me..."
    p "Mychael?"

    show mycmeadow comfort
    show bg meadowpov
    with dis
    m "Hm?"
    p "...Don't get me wrong.{w} This place is stunning."
    p "But is it...{w=.2} okay if we go now?"
    stop sound fadeout 2.0
    show mycmeadow what
    with dis
    "He straightened from his relaxed slouch."
    m "Wh-why?{w} We just got here."
    "I chewed on my lip, hesitating."
    p "I-I love it here, I do."
    p "But I wanna go home, Mychael."
    show mycmeadow serious
    with dis
    "Mychael studied my face."
    m "[protag]..."
    show mycmeadow serious2
    with dis
    m "{size=-5}...Do you want to leave me that badly?"
    p "Wha–no!" with vpunch
    p "I just..."
    p "I-I need time to recover from losing... [pet]..."
    show mycmeadow serious
    with dis
    p "I know it's silly and dramatic but... knowing %(pronoun2)s won't be there when I get home..."
    "I trailed off, another shot of guilt and regret filling my chest."
    p "I just need... to get it done with..."
    show mycmeadow oh2
    with dis
    pause 1
    show mycmeadow comfort
    with dis
    "I feel a hand rubbing my back."
    "Mychael nodded slowly, looking me in the eyes.{w} His smile was gentle."
    m "That's okay.{w} I understand..."

    show pink behind mycmeadow
    with dis
    play sound "audio/sfx/hypno-static.ogg" fadein 3.0 loop

    m "But maybe this place can help with that."
    m "It's a nice spot to nap in, isn't it?"
    m "I picked it out just for you."
    m "Why don't you go ahead and lie down?"
    "His words made {color=#ff8da1}you{/color} sway, a sudden bout of sleepiness weighing heavy over {color=#ff8da1}your{/color} eyelids."
    "He was right.{w} It {i}is{/i} a nice spot to nap in."
    "Why were {color=#ff8da1}you{/color} in such a hurry?"
    "{color=#ff8da1}You{/color} yawned, laying back to stretch on the grass."
    "The warmth from the ground seeped through {color=#ff8da1}your{/color} clothes, lulling {color=#ff8da1}you{/color} into a sense of comfort and safety."
    "There {color=#ff8da1}you{/color} go.{w} Just... just spend some time with me."
    "{color=#ff8da1}Just a bit more."
    "{color=#ff8da1}{size=-5}{k=5}Please..."

    hide pink behind mycmeadow
    with dis
    stop sound fadeout 3.0

    show mycmeadow serious
    with dis
    m "..."
    show mycmeadow oh
    with dis
    pause 1
    show mycmeadow grin
    with dis
    m "O-oh!{w} Here’s something else I could show you."
    "He reached into his satchel..."
    play sound "audio/sfx/satchel-rustle.ogg"
    hide mycmeadow
    with dis
    pause 0.5
    show mycmeadow kalimba
    with dis
    "...and pulled out a wooden box."
    m "It’s called a kalimba."
    "I blinked slowly, clarity coming back as I shook my head to pay attention."
    "The box fit neatly in his hands,{w=.2} Mychael holding it as if he were typing on a phone."
    "I could see it had a hole in the middle with thin strips of metal arranged in a triangular shape over it."
    p "Wh-what does it do?"
    "A proud smirk spread across his face."
    m "I’ll show you."
    play sound "audio/music/kalimba-time.ogg" volume 0.5 loop
    show mycmeadow kalimbaplay
    with dis
    "He began to pluck at the metallic prongs, a gentle ringing sound resonating with every flick of his thumbs."
    "I couldn’t recognize the song...{w=.2} he might’ve made it up himself."

    hide mycmeadow
    show bg black
    with dis

    "I closed my eyes, enjoying the tune."
    "Mychael gave a soft chuckle as he kept playing."
    m "Relax and listen as long as you'd like, firefly."
    "{cps=.2}........"
    stop sound fadeout 5.0
    "A few minutes passed by with Mychael plucking away at the instrument, the two of us sunbathing like two cats on a Sunday afternoon."
    "I must’ve dozed as the next thing I knew I felt a nudge on my shoulder."
    m "Comfy?"
    p "Mnghrrm."
    "He chuckled low when I refused to open my eyes."
    m "{size=-5}I mean if you’d rather stay..."
    show bg meadowpov
    show mycmeadow shook
    "My eyes shot open, my whole body jerking to sit up." with vpunch
    "Mychael glanced at me, kalimba in his lap and half a forget-me-not chain in his hands."
    m "Wh-what?"
    "I shook my head, slapping at my cheeks."
    p "I can't believe I fell asleep!"
    p "I-I just... I still need to--{nw}"
    show mycmeadow serious
    with dis
    m "It's alright."
    "He cut me off. His sigh was heavy."
    show mycmeadow serious2
    with dis
    m "I-I was hoping{cps=5}...{/cps} n-nevermind."
    show mycmeadow sadsmile
    with dis
    "He patted my shoulder, though his smile didn't reach his eyes."
    m "Thanks... for being here with me."
    show mycmeadow comfort
    with dis
    m "Maybe we can do this again sometime."
    show mycmeadow sadsmile
    with dis
    m "{size=-10}If... I ever see you again..."
    m "..."
    show mycmeadow grin
    with dis
    m "Let’s get you home."

    hide mycmeadow
    show bg meadow
    with dis

    "He rolled over to his feet and stood up, brushing off dirt and fixing his satchel."
    m "Come on."

    show bg woods trail 01
    with dis

    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
    play sound "audio/sfx/forest-footsteps.ogg" loop
    "We gathered our things and set off into the unknown once more."
    "Well, unknown to me at least.{w} Mychael seemed to have a map of this place ingrained in his brain."
    m "You seem a bit sleepy still, so let’s freshen up okay?"

    play music "audio/ambience/river-ambience.ogg" volume 0.5 loop
    show bg river
    with dis

    "We walked a bit further away from the clearing, coming across a river."
    "Compared to the rest of the path we walked, the area was shaded considerably with the thick canopy of leaves over us."
    stop sound fadeout 2.0
    "The flowing water looked inviting as I kneeled down by the bank, Mychael idling close by."
    play sound "audio/sfx/river-dip.ogg"
    "I dipped my hands in, eager to wash my face.{w} The water was refreshing and cooled my heated skin in the afternoon sun."
    show mycjackie shy
    with dis
    "I pulled my hands back to see Mychael peeking over my shoulder into my reflection, smiling with a faraway look on his face."
    show mycjackie blush at bounce
    "He startled as our gazes met, irises darting away to look at himself instead."
    "Immediately his expression changed."
    show mycjackie angry
    with dis
    "His ears flattened, a grimace twisting his features as his lips curled back."
    "I'd never seen such contempt in his eyes as I did then,{w=.2} staring at his own visage."
    hide mycjackie
    with dis
    "He stepped away, retreating underneath the cover of a tree to lean against it with crossed arms."
    "He doesn't notice me watching."
    "I patted my hands dry on my shirt and approached him."
    show mycjackie smile
    with dis
    m "You ready?"
    p "Yeah."
    "I stopped him before he could turn to leave."
    show mycjackie confused
    with dis
    "He looked at me with a questioning look, tipping his head."
    "I hesitated.{w} I wasn't the type to speak my mind directly."
    "Most of the time I'd keep things to myself and let things go by."
    "But nobody should look at themselves and have that sort of reaction."
    p "Hey...{w=.2} you know you're not...{w=.2} um."
    "I might as well be frank."
    p "You're not a monster, Mychael."
    show mycjackie surprise at bounce
    "He looked taken aback."
    m "Wh-what makes you say that?"
    p "I saw how you were looking at yourself.{w} How you talk about yourself."
    p "N-none of it is true."
    p "I keep telling you... you're more than just your appearance."
    "I don't know what compelled me to do it, but I did it anyway."
    show mycjackie at zoom_in2
    show bg at zoom_in
    "I reached for his hands and held them between us."
    show mycjackie blush at bounce
    "His eyes widened at the contact."
    p "All it took was a day with you,{w=.2} and truthfully I think you're the most amazing person I've ever met!"
    "He made a choked noise."
    m "I-I... I..."
    p "I'm just some old nobody compared to you!"
    m "Th-that's not–"
    stop music fadeout 3.0
    p "Shut up and listen!" with vpunch
    "He promptly shut his mouth with an audible click of his teeth."
    play music "audio/music/listen-here.ogg" fadein 3.0 volume 0.5 loop
    p "From where I stand, you saved my life!"
    p "You've taken care of me better than I could ever ask for from a stranger."
    p "That already proves to me you're not the monster you think you are!"
    p "You're charming.{w=.2} You're smart.{w=.2} You're {i}sweet."
    p "You're a million more wonderful things but you are {i}not {w=.2}a {w=.2}monster."
    "I take a second to compose myself, lowering my voice."
    p "You may look different, Mychael."
    p "But guess what?"
    "His multiple eyes stared into mine, ears flattening as if fearing the worst."
    p "That makes you all the more {i}beautiful{/i} to me."
    show mycjackie dokidoki1
    with dis
    "His breath hitched."
    "I could feel his hands squeezing mine,{w=.2} fingers trembling."
    stop music fadeout 3.0
    "It was like he forgot how to breathe."
    "..."
    play music "audio/ambience/river-ambience.ogg" fadein 3.0 volume 0.5 loop
    "..."
    "..."
    "...I realized my hands were getting sweaty."
    show mycjackie dokidoki1 at zoom_out2
    show bg at zoom_out2
    "I pulled away hastily, scratching at my neck and avoiding his gaze." with hpunch
    "I could feel the blood rush to my face.{w} I could dunk my whole head in the river and it'd probably let off steam."
    p "{size=+10}S-sorry that came out of nowhere!!" with vpunch
    p "It just didn't feel right if I didn't say anything..."
    p "I hope you... understand..."
    "An awkward silence passed between the two of us."
    p "Um.{w} A-anyways..."
    show mycjackie dokidoki2
    with dis
    "I caught him mumbling under his breath."
    m "{size=-20}{k=5}...I can't let you leave."
    p "Wh-what?"
    m "I-I said, you can't leave."
    m "I mean, n-not without your cat, right?"
    "I frowned."
    p "I've already tried, Mychael.{w} Like you said, it was stupid for me to just wander off in the woods as if I'd find %(pronoun4)s through dumb luck."
    "He paused, his fists clenching."
    m "But I haven't."
    p "Huh?"
    m "I haven't tried."
    m "I know these woods better than anyone.{w} I can try looking for %(pronoun4)s."
    show mycjackie uh oh
    with dis
    stop music fadeout 3.0
    m "B-but that means... that means {b}{cps=25}you can't leave yet."
    p "Mychael, I appreciate the offer but I don't think I should stick around any longer."

    play music "audio/sfx/hypno-static-daytwo-electric-boogaloo.ogg" fadein 3.0 loop
    show pink behind mycjackie
    with dis

    p "I have a job, a-and responsibilities and..."
    p "A-and..."
    show mycjackie uh oh2
    show pinker behind mycjackie
    with dis
    "{b}{color=#ff8da1}You hissed in pain, a sudden migraine overcoming your senses."
    "{sc=2}{b}{color=#ff8da1}You felt sick,{w=.2} your stomach wringing itself into knots.{/sc}"
    "{sc=2}{b}{color=#ff8da1}It felt like the world was warping around you as your legs{p=.1}wobbled.{/sc}"
    "{sc=2}{b}{color=#ff8da1}Your body buckled over as you resisted the urge to vomit.{/sc}"

    play sound  "audio/sfx/caught-you.ogg"
    show mycjackie at zoom_in4
    pause .2
    hide mycjackie
    play sound "audio/sfx/fallen-down.ogg" volume 2
    show bg fallen down
    show cg fallen down behind pink
    show pinker behind cg

    "{sc=3}{b}{color=#ff8da1}Mychael caught you as you slumped gracelessly to the ground,{p=.1}your head resting on his shoulder as he cradled you close.{/sc}" with vpunch
    m "{atl=0.3,drop_text~#~ 1.5, bounce_text~3}Hey... hey, you don't look so good.{/atl}"
    "{sc=3}{b}{color=#ff8da1}Your vision doubled as he spoke, his speech oozing together{p=.1}words into an indecipherable mess.{/sc}"
    m "{atl=0.3,drop_text~#~ 1.5, bounce_text~3}Are you okay? You need me to carry you home?{/atl}"

    menu:

        "{sc=2}{b}{color=#ff8da1}Yes, please.{/sc}":
            jump day_two_over

        "{sc=4}{b}{color=#ff8da1}Yes, please!{/sc}":
            jump day_two_over

        "{sc=6}{b}{color=#ff8da1}YEs PleAsE.{/sc}":
            jump day_two_over

        "{sc=8}{b}{color=#ff8da1}YES PLEASE.{/sc}":
            jump day_two_over

    label day_two_over:

    m "{atl=0.3,drop_text~#~ 1.5, bounce_text~3}Okay... no problem!{/atl}"
    m "{atl=0.3,drop_text~#~ 1.5, bounce_text~3}Just... just hang in there.{/atl}"
    m "{atl=0.3,drop_text~#~ 1.5, bounce_text~3}Hang on to {sc=3}{k=5}{b}me.{/atl}{/sc}"
    stop sound fadeout 3.0
    stop music fadeout 3.0

    scene bg black
    with Dissolve (1)
    pause 2

    play sound "audio/sfx/forest-footsteps.ogg" loop
    "..."
    "..."
    m "{size=-15}I'm sorry..."
    m "{size=-15}I'm so sorry..."
    m "{size=-10}You don't deserve this..."
    play sound  "audio/sfx/door-open.ogg" volume 0.5
    m "{size=-5}If I could just..."
    play sound "audio/sfx/here-comes-the-boy.ogg" fadein 2.0
    m "{size=-5}Just one more day with you..."
    m "I'd be the happiest man alive."
    m "Here we are."
    play sound "audio/sfx/bed-tuckin.ogg"
    m "Let's get you tucked in."
    m "Um."
    m "I should give you some clothes."
    m "Especially since you'll be staying another night."
    m "..."
    m "You're okay with that, aren't you?"

    scene bg black
    with dis
    jump day_three

label day_three:

    #DAY 3 START

    "..."
    "..."
    "..."
    p "Eugh..."

    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop
    show bg cabin room nighttt
    with dis

    "I blinked groggily awake to the gentle sounds of a crackling fire..."
    "The itchy texture of worn bedsheets...{w=.3} the weight of a heavy knit blanket."
    "I could recall once or twice having felt these very sensations to the point I’d consider them familiar and comforting..."
    "And yet..."
    show bg black
    with dis
    pause 1
    show cg wakeywakey
    play sound "audio/sfx/mychael-purr-as-a-treat.ogg" volume 0.4 loop
    "Nothing could prepare me for the bright yellow eyes peering into mine."
    hide cg
    show bg cabin room night
    show myc smack at drop
    play sound "audio/sfx/mychael-bonk.ogg"
    p "{size=+15}Wagh!!" with vpunch
    "My knuckles hit him square in the face as Mychael yelped, nose scrunching as the taller man stumbled backwards into a stool."
    hide myc
    play sound "audio/sfx/mychael-is-dead.ogg" volume 0.7
    "He landed on his rear with the grace of a clumsy toddler on the floor." with vpunch
    "I sat up in a panic and immediately grimaced,{w=.2} landing back on the bed with an unceremonious flop." with vpunch
    "It hit me in one fell swoop how my whole body was {i}aching."
    "Every single one of my limbs felt like they'd gone through a wringer and came out the other side all crinkled and wrong."
    "I groaned aloud, leaning my head back on the pillow."
    show myc rubnose
    with dis
    "Mychael shifted back onto his feet, rubbing his nose."
    m "[protag]!"
    "His voice was an awkward croak before he cleared his throat."
    show myc desperate
    with dis
    m "I-I’m glad you’re awake!{w} How’re you...{w=.2} feeling?"
    p "{cps=15}...{w=.2}Terrible."
    show myc upset
    with dis
    "He visibly flinched."
    m "I-I’m sorry to hear that..."
    show myc shy at zoom_in
    "He stepped closer to the bed, leaning over warily in case my hand dramatically whips out again in self-defense."
    "With my hands settled on my lap, he deemed it safe enough to sit beside me."
    p "What... {w=.2}what happened, Mychael?"
    show myc surprise at zoom_out
    m "U-uh.{w} You don't remember?"
    "I shook my head, wincing a bit as my head pounded."
    p "Not at all."
    show myc nervous3
    with dis
    "Mychael hesitated."
    m "Y-you uh,{w=.2} tripped!{w} And hit your head!"
    m "I...{w=.2} had to carry you home...{w=.2}?"
    "His words almost slurred together as he fidgeted."
    p "My...{w=.3} head?"
    show myc nervous4
    "I slowly lifted my hand to feel for bumps or bruises but he hastily snatched my wrist." with vpunch
    m "D-don't worry about that!"
    show myc desperate
    with dis
    m "Here, have this.{w} It'll help."
    "Mychael gave me a familiar-looking drink as he quickly pressed a cup into my hands."
    "Sitting up with some effort to take a sip, I couldn't help the small sense of deja vu."
    "The amount of times I woke up in his bed dazed and disoriented is almost uncomfortable now."
    "At least the drink was helping, just like he promised.{w} My body felt lighter as I finished."
    show myc nervous3
    with dis
    "Mychael took the cup from me and set it aside before wringing his hands together with a nervousness I haven’t seen in a while."
    m "So...{w=.3} um...{w=.3} I-I'm sorry this happened."
    m "I didn't mean for you to get hurt."
    "I sighed and waved aside his worry with an embarassed grumble."
    p "Wouldn't be the first time I tripped, if you could believe it.{w} It's not your fault..."
    show myc nervous
    with dis
    "He gave a soft chuckle, but it sounded guilty."
    m "I-I suppose you're right...{w=.2} it's just..."
    show myc shame
    with dis
    "His face looked like he had a million thoughts running through his head."
    m "I promised...{w=.2} didn't I?"
    m "I said I was gonna look out for you."
    m "I said I was gonna keep you {i}safe."
    m "Instead I..."
    m "I made you hurt."
    show myc shame2
    with dis
    "His voice cracked."
    m "I'm...{w=.3} I-I'm so sorry, [protag]..."
    "The sudden change in demeanor was startling to say the least."
    show myc surprise
    with dis
    p "Y-you couldn't have predicted it was gonna happen!"
    p "A-and I'm fine!{w=.2} See?"
    show myc nervous
    with dis
    m "Oh, firefly..."
    m "I-I guess you're right..."
    "His expression carried a lingering doubt but he quickly masked it with a small smile, his eyes dim."
    show myc nervous2
    with dis
    m "In that case, you’ll...{w=.2} be staying?"
    "The way he said it almost sounded like a decision that’s already been made."
    "Or a plea."
    p "What...{w=.2} do you mean?"
    show myc nervous
    with dis
    "His eyes darted aside."
    stop music fadeout 5
    m "You agreed to let me find [pet], remember?"
    p "D-did I say that?"
    show myc nervous2
    with dis
    m "Yeah!{w} So um,{w=.2} you’ll be staying a while longer...{w=.2} right?"
    "He didn’t even let me get a word in."
    play music "audio/music/creep.ogg" fadein 1.0 volume 0.7 loop
    "In fact, a feeling of uncertainty washed over me, as if we’ve had this conversation before."
    p "I-I don't think I should–{nw}"
    show myc desperate at zoom_in
    m "Besides!{w} What's the rush?"
    m "It's already late and you're in no condition to travel anyway..."
    "I blinked before glancing out the window."
    hide myc
    show bg windowclosed
    with dis
    "Pitch black darkness greeted me as I realized he was right."
    "Yet another uncanny feeling spread through my chest, shivers crawling down my spine."
    "I don’t know why,{w=.2} but something about this whole situation felt...{w=.2} {i}wrong."
    show bg cabin room night
    show myc desperate
    with dis
    p "I-I feel like I'm forgetting something else."
    show myc nervous3
    with dis
    "Mychael had a nervous look on his face."
    m "Maybe you hit your head harder than you thought?"
    "His words didn't sound confident."
    p "How long was I out?"
    m "A couple hours, I think?{w} You uh, really took a...{w=.2} {i}hit."
    p "It was {i}that{/i} bad?"
    "My brows creased as I tried to recall today’s events."
    p "But I don't remember tripping..."
    play sound "audio/sfx/hypno-static.ogg" fadein 5.0 loop
    show pink behind myc at slow_dissolve
    p "There was a river."
    show myc nervous4
    with dis
    p "I-I remember {i}you{/i}."
    p "And then... a-and then..."
    m "Your memory must be fuzzy... and for good reason!"
    m "After all, it’s been a rough few days–{nw}"
    stop music
    hide pink
    play sound "audio/sfx/hongy.ogg"
    show myc surprise
    "My stomach rumbled suddenly, echoing in the quiet room." with hpunch
    "There was a heavy silence right after."
    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop
    show myc amused
    with dis
    "Mychael was polite enough to hide his chuckle under a palm as I flushed."
    "He seemed relieved."
    m "Well...{w=.2} lucky for you I’ve got dinner on the way!{w} It should be ready soon."
    m "You’re okay with soup, right?"
    p "S-soup...{w=.2} soup sounds alright."
    "My stomach growled once more, the pain of an empty gut making me wince a bit."
    show myc surprise
    with dis
    "My host noticed immediately."
    m "Oh...{w=.2} maybe we should get you some food sooner than later."
    m "Do you feel okay enough to get up?"
    "I nodded with a grumble, swinging my legs over the side of the bed before noticing something was on my lap."
    p "Wait, what’s this?"
    play sound "audio/sfx/yay-clothes.ogg"
    show item myclothes
    with dis
    "I unbundled the pile of thick fabric, realizing it was an oversized sweater with a pair of baggy sweatpants."
    "...a mushroom pattern?{w} That's oddly cute."
    "The material felt worn, but comfortable.{w} A towel laid right next to them."
    p "Is this for me?"
    hide item
    show myc nervous
    with dis
    m "O-oh.{w} I figured since you'll be staying another night... you'd want some fresh clothes."
    m "They might be a few sizes bigger.{w} Or a lot?"
    m "S-sorry."
    show myc shy
    with dis
    "He'd gotten shy for some reason."
    "On the other hand, I didn't have to take a whiff at myself to know that I probably reek."
    "I nodded again, giving him a small but grateful smile."
    p "They're fine, Mychael.{w} Thank you."
    "Yet another thing I had to owe him.{w} I couldn't help feeling like I'm taking advantage of his kindness now."
    show myc proud
    with dis
    m "So uh... you know where the bathroom is."
    m "Take your time cleaning up!{w} I’ll be in the kitchen if you need anything..."
    m "..."
    show myc shy
    with dis
    m "I'm really happy you're here..."
    "He stood there for a good few seconds, fidgeting with his hands as if he wanted to say more before finally heading to the kitchen."
    hide myc
    with dis
    play sound "audio/sfx/kitchen-cabinets.ogg" volume 0.5 fadeout 2.0
    "I watched his back retreat before hoisting myself up and heading to the bathroom."

    play sound  "audio/sfx/door-open.ogg" volume 0.5
    play music "audio/ambience/forest-night.ogg" fadein 1.0 loop
    show bg cabin bathroom night
    with dis
    "Now that I was alone, I had a moment to gather my thoughts."
    "The nagging feeling was back,{w=.2} a prickling feeling across my skin raising goosebumps as if to tell me I shouldn’t be here."
    "I just couldn't place my finger on what..."

    menu:

        "I should be careful...":
         $ suspicion += 1
         jump cautious_decision

        "I was probably just being paranoid...":
         jump carefree_decision

    label cautious_decision:

        stop music fadeout 3.0
        pause 1
        play music "audio/music/sus-sus.ogg" fadein 1.0 volume 0.7 loop

        "I just couldn’t shake the feeling that Mychael was hiding something."
        "He’d been a gracious host so far, but that didn’t make him the most trustworthy either."
        "There’s definitely something I’m missing..."
        "My mind was wandering even as I undressed and stepped under the shower."
        play sound "audio/sfx/showertime.ogg" volume 0.7
        "The icy chill of the water did nothing to distract me from my nerves,{w=.2} if anything it elevated it." with vpunch
        "I was a shivering mess by the time I was done cleaning myself with whatever soap he had lying around."
        "Once I dried myself, I inspected his clothes inside and out to see if there’s anything off with them."
        "They smelled like wet grass and burnt wood."
        "Considering his lifestyle it made sense for his clothes to have that sort of scent stuck to them, I supposed."
        play sound  "audio/sfx/bed-tuckin.ogg" volume 0.5
        "Putting them on, it just reminded me how big and tall Mychael was, {w=.2} compared to me at least."
        "I fidgeted and fiddled with the sleeves and waistband until I could somewhat move comfortably."
        "There’s no mirror in his bathroom, so I had to assume I looked like a walking potato sack."
        "Better than nothing."
        play sound  "audio/sfx/door-open.ogg" volume 0.5
        show bg cabin room night
        with dis
        "Gathering my courage, I shook out my hands and straightened myself before exiting towards the kitchen."
        "A savory scent filled my nose.{w} Mychael did mention dinner was almost done."
        show bg let him cook
        show myc cook neutral
        with dis
        "As I entered, I saw Mychael by the stove, idly stirring something crimson in a pot and humming quietly to himself."
        show myc cook smile
        with dis
        "His content smile widened as he saw me,{w=.2} his ears flicking."
        "I tried not to look uneasy as he looked me up and down."
        m "Uh, how do they fit?"
        p "They’re...{w=.2} alright."
        p "Much too big for me."
        show myc cook neutral
        with dis
        "He nodded, turning back to the pot."
        m "I can see that!"
        p "...Right."
        show myc cook upset
        with dis
        "His smile faltered as he picked up on the wariness in my tone."
        m "...Is everything alright?"
        "His eyes held a sense of worry,{w=.2} his shoulders tensing."
        show myc cook nervous
        with dis
        m "I-I can get you something else to wear if you'd like?"
        p "There’s no need."
        "He paused, hand gripping onto the ladle tightly as he continued to hesitate."
        m "[protag]..."
        "There’s another pause before his brows furrowed."
        show myc cook upset2
        with dis
        m "I'm not an idiot..."
        m "You don’t trust me, do you?"
        show myc cook upset
        with dis
        "I flinched.{w} Mychael looked hurt as he sighed."
        m "So I’m right..."
        "His ears flicked by the sides of his head as he turned back towards the stove."
        show myc cook upset2
        with dis
        m "C-can I just...{w=.2} know why?"
        "His eyes were sad as he stared at the pot, as if he’d been in this situation before."
        m "I thought I did everything right..."
        "Truthfully, I didn’t expect such a direct confrontation."
        "There’s a lump in my throat as my fists clenched at my sides."
        p "I-I..."
        p "It’s just..."
        play sound "audio/sfx/kettle-whistle.ogg" volume 0.7 fadein 1.0
        "The kettle started whistling, but he was clearly ignoring it."
        "I swallowed down my growing anxiety and decided to be upfront."
        p "I-I just didn’t expect to be here again."
        show myc cook angry
        with dis
        "It felt like the wrong thing to say when Mychael’s frown deepened."
        m "So you never wanted to be here."
        p "I-I didn’t mean it like that!"
        show myc cook angry2
        with dis
        m "Then how else could you possibly mean it?"
        show myc cook upset2
        with dis
        "Another deep sigh slipped out of him as he reached to lift the kettle off the stove, mumbling to himself."
        m "{size=-15}I was hoping you’d be different...{w=.2} what was I thinking?"
        p "Wh-what’d you say?"
        m "...{w=.2}nothing."
        p "Mychael...{w=.2} I'm..."
        "His forlorn expression made my words feel thick on my tongue, forcing me to reluctantly swallow them back down."
        "Any trace of suspicion I had faded and was replaced by a feeling of guilt."
        p "I-I’m sorry."
        p "I just thought I’d be home by now."
        show pink behind myc at slow_dissolve
        play sound "audio/sfx/hypno-static.ogg" fadein 2.0 loop
        m "I know.{w} I’m sorry, too."
        show myc cook upset
        with dis
        "He lifted his gaze towards me, eyes full of regret."
        m "..."
        show myc cook upset2
        with dis
        m "..."
        hide pink at slow_dissolve
        stop sound fadeout 5.0
        m "..."
        show myc cook upset
        with dis
        m "But... is it really so bad, [protag]?"
        m "I know being lost in the woods with a mon–{w=.2} man you don’t know can be..."
        show myc cook upset2
        with dis
        m "...{w}Scary."
        show myc cook upset
        with dis
        m "But I promise you you're safe."
        m "The last thing I'd {i}ever{/i} want you to be is scared..."
        "He trailed off."
        m "So just-{w=.2} trust me, okay?"
        m "Can you do that?{w} Please?"
        "I swallowed and gave him a nod."
        "My gut still roiled with suspicion, every fiber of my being wary of him to a certain extent."
        show myc cook tepid
        with dis
        "He seemed satisfied though, eager to move on past the tension."
        m "Thank you."
        "His mouth quivered at the edges, all four of his eyes squinting with the slightest bit of hope."
        m "{size=-10}Please... let it be different for once..."
        jump cont_story_09

    label carefree_decision:

        stop music fadeout 3.0
        pause 1
        play music "audio/music/freshen-up-firefly.ogg" fadein 1.0 loop

        "Then again,{w=.2} it's been a while since I've showered, so I could chalk it up to dirt accumulating on me and making me itch in places I didn't want to think about."
        play sound "audio/sfx/showertime.ogg" volume 0.7
        "After undressing, I folded my clothes so I could place them in my backpack later before turning on the shower."
        "The water was ice cold!" with vpunch
        "My teeth chattered as I cleaned myself as fast as I could, using some scentless soap by the side of the tub."
        "Dressing myself again I wrung out my hair as best as I could before drying it with the towel."
        play sound  "audio/sfx/bed-tuckin.ogg" volume 0.5
        "Putting on the clothes Mychael provided, I felt like I had shrunk in size."
        "I adjusted the sleeves and waistband to my liking with some struggling,{w=.2} just so my hands and feet could poke out of the holes comfortably."
        "I couldn’t help noticing his clothes smelled like freshly cut grass{w=.3} ...with a smoky hint of a woodsy bonfire?"
        "The scent reminded me of camping in summer."
        "Persistent doubt aside,{w=.2} I definitely felt way better compared to when I woke up."
        play sound  "audio/sfx/door-open.ogg" volume 0.5
        show bg cabin room night
        with dis
        "Stepping out, I could smell something good coming from the kitchen."
        "A gentle humming greeted me as I came through the doorway."
        show bg let him cook
        show myc cook neutral
        with dis
        "Mychael was idly stirring a pot by the stove, looking up at me as I entered the kitchen."
        "Whatever he had in that pot made my stomach grumble yet again."
        show myc cook smile
        with dis
        "His ears flicked as he registered the clothes I was wearing."
        m "Uh, how do they fit?"
        "I shrugged."
        p "They're definitely bigger on me."
        show myc cook neutral
        with dis
        "He nodded, turning back to the pot."
        m "I can see that!"
        m "I-I wasn't sure what you normally wear so I went with whatever I had that was..."
        "He struggled to pick a word."
        show myc cook nervous
        with dis
        m "...Coziest?"
        "I gave a hum of agreement,{w=.2} fiddling with the hem of my (his) sweater."

        menu:

            "Flirt.":
                jump flirt_clothes

            "Goof around.":
                jump silly_clothes

    label silly_clothes:

        stop music fadeout 5.0
        pause 1
        play music "audio/music/silly-silly.ogg" fadein 1.0 loop

        "I fisted the sweater by the sides, flapping it back and forth."
        "It really was so ridiculously baggy on me I had to spout whatever nonsense that came to my mind before my brain could filter it."
        p "Look at all this free yarn real estate!"
        show myc cook upset2
        with dis
        "Mychael did a whole body freeze, his hand stilling as the pot bubbled merrily."
        show myc cook upset
        with dis
        m "Free real what?"
        p "Free yarn real estate."
        m "..."
        show myc cook confused
        with dis
        m "Is that...{w=.2}{i} supposed{/i} to make sense?"
        m "Because it feels like another one of those things you say just to mess with me."
        p "I don't need to explain myself."
        show myc cook squint
        with dis
        "He narrowed his eyes."
        m "Explain."
        p "I genuinely can't."
        show myc cook glare
        with dis
        m "Then why say it in the first place!"
        "By the look on my face it was clear I was just messing with him."
        p "Mychael, Mychael, Mychael..."
        p "Why does anyone say anything at all?"
        p "Perhaps it was a spur of the moment..."
        p "To express themselves with declarations of spontaneous whimsy!"
        show myc cook squint
        with dis
        "His expression flickered between confusion, doubt and maybe even a smidge of grief."
        m "Do you make it a habit to talk nonsense all the time?"
        p "Only sometimes."
        show myc cook sigh
        with dis
        "He turned his focus back on stirring, sighing heavily."
        m "I should've left you in the dirt."
        show myc cook sigh2
        with dis
        "I gasped."
        p "Was that a threat?"
        show myc cook amused
        with dis
        m "No."
        p "That was a threat!"
        show myc cook laugh
        with dis
        m "It was- {i}snrk-{/i} it was not!"
        p "Jail for Mychael!"
        p "{b}Jail for one thousand years!"
        show myc cook amused
        with dis
        "His ears flattened against his head in amusement, the tip of his tail flicking in playful irritation."
        m "I deserve jail for speaking my truth?!"
        p "Yes!{w=.2} Absolutely!"
        show myc cook laugh
        with dis
        "He laughed again."
        show myc cook amused
        with dis
        m "You're ridiculous, you know that?"
        p "Hey, not my fault you can't keep up!"
        p "I am what I am."
        m "A {b}greighkhen{/b} is what you are."
        "I blinked."
        "It sounded like he gargled a bag of marbles pronouncing...{w=.2} whatever the hell it was he said."
        p "A {i}what{/i}?"
        show myc cook smug
        with dis
        "His eyes squinted, a triumphant grin mirroring mine just a few seconds ago gracing his face."
        m "Doesn't feel good, does it?"
        "I scoffed, folding my arms as I leaned against the counter."
        p "Whatever.{w} I can totally say {b}greagh-reargh-can{/b}."
        show myc cook laugh
        with dis
        "He burst into laughter."
        m "That is {i}not{/i} how you say it."
        p "{b}Greghieghken?"
        m "That's even worse!"
        "Refusing to back down, my hand shot out to poke his side."
        show myc cook flustered at bounce
        "Surprisingly he yelped, his hand nearly letting go of the ladle." with vpunch
        m "Wh-what was that?"
        "Wait a second..."
        "Has he never been...?"
        show myc cook uhm at bounce
        "I gave another curious poke,{w=.2} to which he swatted away my hand with a panicked look on his face." with vpunch
        m "Stop that!?"
        p "Are you...{w=.2} ticklish?"
        m "...wh-what does that mean?"
        m "What'd you just do?"
        "Oh."
        "{i}Oh."
        "{b}{k=10}Oh, this is {i}wonderful{/i} news."
        play sound "audio/sfx/kettle-whistle.ogg" volume 0.7 fadein 1.0
        "Before I could even consider a strategic frontal assault, the kettle started to whistle."
        "Mychael turned towards it, clueless as to what would have ensued otherwise."
        "Someday, Mychael...{w} someday..."
        jump cont_story_09

    label flirt_clothes:

        stop music fadeout 5.0
        pause 1
        play music "audio/music/flirty-flirty.ogg" fadein 1.0 loop
        "...{w=.2}Was I really about to do this?"
        "{k=5}{b}I guess I was."
        "With the confidence of a courting peacock with nothing to lose, I leaned against the doorway,{w=.2} making sure to prop my hip in just the right angle against the edge."
        p "I think I look good in your clothes."
        p "Maybe I should wear them more often?"
        "With how baggy the clothes were on me, I probably looked closer to a sentient sack of potatoes than a human being."
        show myc cook smile
        with dis
        "Mychael must have sensed something was different with my tone, {w=.2}as he gave a confused chuckle with his tail noticeably swishing side to side."
        m "Uh...{w=.2} I-I guess you could."
        m "Though I'm pretty sure most of them won't fit right..."
        "Undeterred, I continued on."
        p "I could help find something more... comfortable?"
        "I send the smoothest wink I could muster."
        show winkwonk
        with dis
        pause 0.4
        hide winkwonk
        with dis
        "{i}Wink."
        "Nailed it."
        show myc cook tepid
        with dis
        "He seemed to consider my offer."
        m "Hmm... I thought I found the right outfit,{w=.2} but you can look through the closet for something you like now that you're awake."
        show myc cook confused
        with dis
        m "Um."
        m "Do you have something in your eye?"
        p "I..."
        "I straightened subtly."
        p "I'm just trying something, I guess..."
        m "Trying what?"
        p "N-nevermind..."
        p "Uh...{w} what's cooking, good-looking?"
        show myc cook flustered
        "Against all odds his cheeks actually began to color, his hand stirring the pot faltering for a brief second." with hpunch
        m "Wh-what?"
        "Wait, this might actually work."
        "I bolstered my efforts, leaning forward with another smile."
        p "You heard me."
        m "You said..."
        "He hesitated to repeat it."
        show myc cook nervous
        with dis
        m "Well..."
        m "M-maybe you should get your eyes checked..."
        p "..."
        "Yeah, this was a terrible idea."
        "I cleared my throat awkwardly."
        p "Thank you for the clothes..."
        "He must've sensed something wrong again as he quickly tried to salvage whatever the hell was going on."
        m "F-for what it's worth... you look...{w=.2} um."
        show myc cook uhm
        with dis
        m "You look very...{w=.2} {size=-5} {b}ktchreikrichein{/b}...?"
        "Whatever it was he said sounded like several strange clicks of the tongue."
        "But with vowels?{w} Somehow?"
        p "...what?"
        "He huffed, tail waving side to side like a metronome."
        m "It means..."
        "He trailed off."
        m "I guess in your language it would mean..."
        m "Um."
        show myc cook uhh
        with dis
        m "{size=-10}...........{w=.2}cute?"
        "My smile faltered as he fidgeted."
        show myc cook uhm
        with dis
        "We stared at each other."
        "I might actually have a chance!?" with vpunch
        "The color on his face was closer to a blueberry the longer I looked at him."
        "There was an awful awkward tension before I broke it with a nervous laugh."
        p "Cute?"
        show myc cook whimper
        with dis
        "In fact, I could swear I heard him whimper in panic."
        "The situation was so absurd I had to laugh harder."
        p "Was that so hard to say?"
        "He sputtered."
        show myc cook uhm
        with dis
        m "I didn't think you'd be comfortable with me saying it..."
        p "Why not?"
        m "Well...{w=.2} you know..."
        p "What do I know?"
        show myc cook uhh
        with dis
        "My grin was teasing and he picked up on that quickly,{w=.2} his nervousness dissipating as he gave a sharp huff."
        "His hand stirred the pot faster."
        m "S-so I called you cute!{w} It’s not a big deal!"
        p "Then why’s your face so blue like it is?"
        "He made another choking noise, eyes darting about."
        m "It’s...{w=.2} i-it’s just the heat from the stove!"
        show myc cook uhm
        with dis
        m "I’m cooking my best here..."
        "I snickered at his terrible excuse."
        p "You’re a bad liar."
        m "But it’s true!"
        p "Stovetops don’t do that!"
        show myc cook glareb
        with dis
        m "Mine does!"
        show myc cook uhm
        with dis
        pause 1
        show myc cook laugh
        with dis
        play sound "audio/sfx/kettle-whistle.ogg" volume 0.7 fadein 1.0
        "A glaring contest ensued before we ended up bursting into a fit of giggles, my face warming from the silly banter."
        "The kettle started whistling then,{w=.2} cutting our moment short."
        "He seemed disappointed by the shift in the atmosphere, but quickly moved to pick it up."
        jump cont_story_09


    label cont_story_09:

    if suspicion == 1:

        stop music fadeout 3.0
        queue music "audio/ambience/forest-night.ogg" fadein 1.0 loop

        show bg cabin kitchen night
        show myc desperate
        with dis


    else:

        stop music fadeout 3.0
        queue music "audio/music/dinnertime.ogg" fadein 1.0 loop

        show bg cabin kitchen night
        show myc proud
        with dis

    m "...Why don't you take a seat, firefly?"
    show myc smile
    with dis
    m "I'll be right with you."
    stop sound fadeout 2.0
    "He was already turning his back towards me to start preparing the tea.{w} I slowly approached him."
    p "Hey...{w} Let me help this time."
    show myc surprise
    with dis

    if suspicion == 1:

        stop music fadeout 2.0
        pause 1
        play music "audio/music/dinnertime.ogg" fadein 2.0 loop


    "Mychael startled, surprised to see me beside him."
    m "O-oh.{w=.2} Sure!"
    show myc nervous
    with dis
    m "Could you get some bowls ready?{w} We're having tomato soup."
    m "Oh, do you want some grilled cheese with yours or would you prefer garlic bread?"

    menu:

        "Grilled cheese, please.":
            $ tomato_cheese = True
            jump cont_story_10

        "Garlic bread, please.":
            $ tomato_garlic = True
            jump cont_story_10

        "Just the soup, please.":
            jump cont_story_10


    label cont_story_10:

    show myc proud
    with dis
    m "Got it!"
    hide myc
    with dis
    "I brushed past him, feeling his tail linger by my ankle as I grabbed the bowls and spoons from the bottom shelf."
    "He started preparing the sides,{w=.2} the smell of toasted bread filling the kitchen and mingling with the soup's.{w} I took over preparing the tea."
    "Finally I ladled the soup from the pot into a larger bowl just as Mychael finished flipping the last piece."
    play sound "audio/sfx/plate-up.ogg"

    show bg table
    show myc table hb nervoussmile
    with dis

    if tomato_cheese:

        show item tomatocheese
        with dis

    elif tomato_garlic:

        show item tomatogarlic
        with dis

    else:

        show item tomatoonly
        with dis


    "We settled in for a nice hot dinner."

    if tomato_cheese:

        "Regardless of how I felt about tomato soup, Mychael's turned out rich and creamy with an amazing balance of sour and sweet."
        "Dipping in the bite-sized grilled cheese sandwiches made it taste like pure savoury comfort, crisp and gooey."
        "Even if I've never had it as a kid, it still made me feel nostalgic somehow."

    elif tomato_garlic:

        "Regardless of how I felt about tomato soup, Mychael's turned out rich and creamy with an amazing balance of sour and sweet."
        "The fragrant garlic bread added the perfect texture to the meal, practically melting in my mouth with every bite."
        "The simple combination of bread slices,{w=.2} toasted with a buttery garlic spread,{w=.2} dipped in fancy ketchup had no business being this {b}{i}good."

    else:

        "Regardless of how I felt about tomato soup, Mychael's turned out rich and creamy with an amazing balance of sour and sweet."
        "I'd decided to have it simple tonight, opting out of any sides Mychael offered."
        "Personally I think it let me enjoy the soup on its own even better, the richness of the flavor lingering on my tongue with every sip."

    hide item
    with dis
    "There’s still a feeling of stilted awkwardness, but the food helped ease us both into a warmer lighthearted conversation."
    "I didn't realize how hungry I was until I refilled my bowl, Mychael watching me with his chin propped in his hand."
    "His own bowl sat empty;{w=.2} apparently he'd already had his fill."
    show myc table shysmile
    with dis
    m "Is... {w=.2} tomato soup your favorite?"
    "His question was innocent, though his eyes were observing me carefully as I shrugged."
    p "I think I’d love anything you cook."
    show myc table hb surprise
    with dis
    "He stilled, taking a second to process what I said."
    show myc table laugh
    with dis
    m "O-oh!{w} Well, thank you."
    show myc table hb surprise
    with dis
    p "No, thank {i}you."
    p "Usually I get take-out or microwave dinners.{w} Nothing beats home-cooked food."
    show myc table stare
    with dis
    m "...{w}What’s a microwave?"
    "I snickered and tried to explain it the best I can."
    show myc table confused
    with dis
    m "A metal box that heats up food?{w} That sounds like... what's the word in those fantasy books,{w=.2} m-magic?"
    m "Am I using that word right?"
    "I laughed lightly."
    p "Sometimes science is just like that."
    "We talked about other kitchen appliances off the top of my head, slowly branching out to other human inventions.{w} He seemed even more interested."
    show myc table sidesmile
    with dis
    m "I-I never understood how... uh..."
    p "Technology."
    show myc table laugh
    with dis
    m "{i}Technology{/i} worked."
    show myc table stare
    with dis
    "I pulled out my phone and let him fiddle with it,{w=.2} though with the battery dead there’s not much I could show."
    show myc table pout
    with dis
    "He was clearly disappointed."
    m "It’s...{w=.2} about as useful as a brick."
    p "For now!{w} Otherwise I’d have a whole network of information in my hands."
    show myc table hb surprise
    with dis
    "His eyes lit up."
    m "L-like a library? And you can access it at any time as long as the bat-{w=.2}bat-{i}eerie{/i} is alive?"
    p "And as long as I have an Internet connection."
    show myc table laugh
    with dis
    m "Right!{w} In-ter-net!"
    show myc table amused
    with dis
    m "I didn’t know you could do that!"
    show myc table sidesmile
    with dis
    m "I just see people staring at them all the time... {w=.2}it seemed boring."
    show myc table smile2
    with dis
    "He looked at my phone again, a look of wonder on his face."
    m "Having a whole library in your hands..."
    show myc table happy
    with dis
    m "Everyone must be really smart, then."
    p "W-well..."
    show myc table hb surprise
    with dis
    p "Not everyone uses it like a library... more like...{w=.2} a messaging hub?{w} Or uh, a source of...{w=.2} content consumption?"
    show myc table smile2
    with dis
    "His ear flicked as he stared at me with a blank smile."
    m "Connnn-sumption?"
    m "You can eat it?"
    "...yeah, he has no clue what I’m talking about."
    "{i}How do I explain to him the very concept of Web 2.0?"
    "I cleared my throat, deciding that I simply won’t."
    show myc table hb surprise
    with dis
    p "Maybe I can show you what I mean someday."
    show myc table shysmile
    with dis
    "His eyes brightened, seeming to like that idea a lot."
    m "You...{w=.2} mean that?{w} I-I can have some?"
    p "Yeah!{w} I think it’s about time you start getting a little more modern around here, no offense."
    p "Imagine what you could do with a generator."
    show myc table happy
    with dis
    "His smile widened just a tad, though there’s still a cluelessness to his face that was just a little endearing."
    m "Gen-ee-raider?"
    "I laughed and reached across to pat his hand,{w=.2} a gesture that made his smile wobble."
    show myc table hb nervoussmile
    with dis
    p "Like I said.{w} I’ll show you someday."
    show myc table hb blush_02b
    with dis
    "A loud thwack sounded against the floorboards, followed by rhythmic thudding." with vpunch
    "Leaning over I could see the tip of his tail was wagging back and forth, the tip of it slapping against the floor almost comically."
    "Mychael looked flustered as he laughed softly, pulling his hand back to rub his neck."
    show myc table panic2
    with dis
    m "Sorry..."
    "He looked like he had more to say but exhaled heavily, gathering himself before tilting his chin towards my empty bowl."
    show myc table laugh
    with dis
    m "Are you done?"
    hide myc
    with dis
    play sound "audio/sfx/stack-plates.ogg"
    "I nodded as he stood and collected our dirty dishes, heading towards the sink to wash them."
    "I followed close behind carrying the mugs."

    play music "audio/ambience/cabin-fireplace.ogg" fadein 1.0 loop
    show bg cabin room night
    with dis
    "We made quick work of the dishes, heading back to the living room to relax."
    "Mychael headed to his basket of knitting materials, his movements routine."
    "I wasn't sure what to do with myself."

    if suspicion == 1:

        "Now that food was no longer a distraction, {w=.2}I felt uneasy again, glancing around the room and staring at the window."
        "Mychael was eyeing me as he grabbed the stool and dragged it to the center of the room."
        show myc neutral
        with dis
        m "Is there something outside?"
        "His question sounded innocent, but it had a sense of wariness to it."
        "I shook my head quickly."
        p "N-nothing, I was just-"
        "Something catches my eye from under the bed, glinting like a knife."
        show cg under the bed
        with dis
        "Tilting my head lower, I could see it was a tin container the size of a shoebox."
        p "What’s that?"
        "Mychael looked up."
        m "Hm?"
        p "Under your bed."
        "A panicked look came across his face."
        m "Th-that thing?"
        m "Just some...{w=.2} emergency supplies."
        m "Y-yeah.{w=.2} Nothing too special."
        "I had an inkling he was being dishonest again, {w=.2}but I figured I’d leave it for another day."
        p "I see..."
        hide cg
        show myc nervous
        with dis

    else:

        "I looked over at Mychael as he pulled out the stool from the corner of the room towards the front of the fireplace."
        "His ear flicked in my direction before he returned my glance."
        show myc amused
        with dis
        m "Do you knit?"

        menu:

            "Yes, actually.":
                show myc happy
                with dis
                "His eyes lit up."
                m "It's relaxing, isn't it?"
                jump box_under_bed

            "A little.":
                show myc smile
                with dis
                "His smile softened."
                m "A little is enough sometimes."
                jump box_under_bed

            "Not at all.":
                show myc proud
                with dis
                "He gave a soft chuckle."
                m "Maybe you'll like it if you tried?"
                jump box_under_bed

        label box_under_bed:
            p "Can I see what you're working on?"
            show myc surprise
            with dis
            "He looked surprised, not expecting my interest."
            show myc nervous
            with dis
            m "Sure. It's just something to work on in my down time..."
            m "Halfway through I started to realize that maybe it's not really my color."
            show myc surprise
            with dis
            "He lifted it up for me to see, only for my foot to kick the basket and sending a ball of yarn rolling towards the bed."
            p "Ah, sorry!"
            "I quickly followed after it, only to halt as I spotted something under the bed."
            "It was glinting off the bright firelight within the room."
            show cg under the bed2
            with dis
            "Approaching the bed and tilting my head lower, I could see it was a tin container the size of a shoebox."
            p "What’s that?"
            "Mychael looked up."
            m "Hm?"
            p "Under your bed... is it something important?"
            "A hesitant look came across his face."
            m "Oh..."
            m "Just some...{w=.2} emergency supplies."
            m "Nothing too special."
            "I had an inkling it was something more, {w=.2}but I figured I'd let him keep his privacy without prying anymore."
            p "I see..."
            hide cg
            show myc nervous
            with dis

    "Mychael watched me for a moment or two before clearing his throat."
    m "H-hey, firefly?"
    p "Hm?"
    show myc shy
    with dis
    m "I've been meaning to ask...{w} do you remember what you said? At the river?"
    "The river?"
    "Oh.{w} Where I tripped..."
    "I pursed my lips in thought."
    p "Not really.{w} Everything feels fuzzy to me..."
    show myc upset
    with dis
    "He seemed disappointed."
    m "Oh...{w} Not even a little?"
    "I shook my head."
    p "Why? Did I say something stupid?"
    show myc shy
    with dis
    m "Just...{w=.2} some things.{w} It made me happy."
    "Oh god, I think I {i}did{/i} say something stupid."
    "Before I could ask about it he’d already gestured towards the bed."
    show myc desperate
    with dis
    m "Well... you should get some sleep, firefly."
    m "Wanna wake up nice and early to find [pet], right?"
    "The idea of looking for my cat once more made me wilt."
    p "You really think we’ll find %(pronoun4)s?"
    show myc nervous4
    with dis
    "Mychael looked on edge, pocketing his hands."
    m "It doesn’t hurt to try."
    p "But it does hurt to hope..."
    "His face twitched."
    show myc nervous
    with dis
    m "W-well...{w=.2} um..."
    "His ears flattened as he thought of something to say, clearly struggling."
    "He finally opened his mouth to respond, his words slow and careful."
    m "I-I’m here for you..."
    p "..."
    p "Thank you, Mychael."
    show myc nervous2
    with dis
    "He nodded, a strange mixture of polite happiness and hidden anxiety playing across his face."
    "He’s probably not used to another person sticking around this long...{w=.2} let alone someone going through a loss he could care less about."
    "Maybe I’ve been enough of a burden to him."
    p "Actually...{w=.2} c-can you just send me home?"
    show myc surprise
    with dis
    "His brows raised, his posture straightening in surprise."
    m "A-are you sure?"
    m "But what about [pet]? D-don’t you wanna see if we can find %(pronoun4)s?"
    p "I’m sure."
    show myc shame2
    with dis
    "A look of apprehension crossed his face."
    m "B-but it’s so soon!{w} [pet] could be out there, we can still try to–{nw}"
    p "Mychael, {i}please."
    p "I... I-I can’t think about %(pronoun4)s right now..."
    p "I just wanna go home."
    "He fidgeted with the sleeves of his cardigan."
    show myc shame
    with dis
    m "But..."
    m "I-I..."
    show myc shame3
    with dis
    "He looked like he had so much more to say, but whatever turmoil going on in his head was quickly swept behind a reassuring smile."
    show myc desperate
    with dis
    m "..."
    m "Okay."
    m "Get some sleep, firefly."
    m "You’ve been through a lot."
    "He went to collect his blankets again, already arranging them into a nest like the night before."
    "The words left my mouth before I could think twice."

    if suspicion == 1:

        p "I can trust you, right?"
        show myc surprise
        with dis
        "A flicker of surprise crossed Mychael's face."
        m "O-of course you can trust me!"
        "He didn't say anything else, as if that one line should be enough to convince me."
        "And honestly it was too late to start an interrogation that's only gonna end up in me feeling guilty for upsetting him."
        hide myc
        with dis
        "I got under the covers, facing the wall with my back towards him."
        "I could hear him setting up his nest behind me, before finally quieting down with a satisfied hum."
        "I closed my eyes."

    else:

        p "Do you wanna use the bed tonight?"
        show myc surprise
        with dis
        "He stopped in his tracks."
        m "Oh.{w} No, I don’t mind the floor."
        p "I-I meant... we’d be sharing...{w=.2} the bed..."
        "Hearing it out loud just made me wanna slap myself across the face."
        show myc proud
        with dis
        "Mychael blinked at me before laughing lightly."
        m "My bed’s too small for two people, don’t you think?"
        m "I don’t think it’d be comfortable for either of us."
        show myc smile
        with dis
        "He eyed the bedframe before looking back at me."
        m "I’ll be alright."
        hide myc
        with dis
        "With that he crouched on the floor and started setting up his bed,{w=.2} his tail swaying languidly."
        "I laid down and faced the wall, the sharp sting of embarrassment in my chest refusing to go away."
        "Why did I ask that!!"
        "That was so stupid!!"
        "Maybe I needed a sense of comfort..."
        "Or maybe I just needed him?"
        "Whichever it was, at least he took it at face value.{w} I wasn’t sure what I’d even do if he said yes."
        "I groaned internally and shut my eyes, willing myself to go to sleep."

    label cont_story_11:

    play sound "audio/sfx/knitting.ogg" volume 0.7 loop


    show bg black
    with Dissolve (1)
    show bg cabin room nightt
    with Dissolve (1)
    show bg black
    with Dissolve (1)
    show bg cabin room nighttt
    with Dissolve (1)
    show bg black
    with Dissolve (2)

    stop music fadeout 5.0

    "The last thing I heard was the gentle crackling of the fireplace,  accompanied by Mychael’s knitting needles clicking away in the dark."

    stop sound fadeout 1

    "..."
    "..."
    "..."

    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop volume 0.1
    "Before I knew it, I could hear birds chirping outside the window."
    "The first thing I noticed was the fire must’ve been out, considering I couldn’t hear the familiar pop and snap that came with the room’s ambience."
    "The second thing I realized was the hand gently shaking my shoulder awake."
    m "Wake up, sleepyhead..."
    p "Ghhrgnmm..."
    "I stirred, yawning as I sat up in bed."

    show bg cabin room day nf
    show myc grin
    with dis
    "Mychael beamed, hand still on my shoulder."
    m "There you are.{w} Had a good sleep?"
    "I mumbled incoherently."
    "His smile widened into a grin as I blinked myself out of my woozy state."
    "If I didn’t know any better he seemed to enjoy waking me up in the morning just to see my disgruntled expressions."
    m "Breakfast is ready.{w} Wash up and meet me in the kitchen, alright?"
    p "Mghhnn... give me a second."
    show myc proud
    with dis
    "He took that as my assent, humming his response."
    show myc cheeky
    with dis
    "Suddenly his hand reached up to ruffle my hair, messing up my bedhead further." with vpunch
    p "Hey!"
    hide myc
    with dis
    "He merely laughed at my indignant squawk before reminding me once more to get up, his steps already thudding towards the kitchen."
    "Recovering after a moment, I stared at the wall and pondered my situation for a second as I made my way to the bathroom."
    play sound  "audio/sfx/door-open.ogg" volume 0.5
    show bg cabin bathroom
    with dis
    "This was the third day since I’ve left my house..."
    "I’m missing work, missing my cat, and missing my sense of direction."
    "I gotta get back to my life."
    "{b}Today."
    "Quietly reminding myself of my goal, I padded to the bathroom, freshened up and joined him in the kitchen."
    show bg table
    show myc table shysmile
    with dis
    "Mychael was already seated, cutting into some pancakes."
    "His smile was bright as I entered the kitchen, his tail flicking closer to my seat as I sat down."
    show item pancakes
    with dis
    "A similar stack of mouth-watering pancakes was placed across him, waiting for me to dig in."
    "Though I couldn't bring myself to muster up an appetite with so many thoughts filling up my head."
    hide item
    with dis
    show bg table
    "He seemed to notice the look on my face, laughing nervously."
    show myc table amused
    with dis
    m "You look serious.{w} Something on your mind, firefly?"
    "I picked up my fork, twiddling with it."
    p "I’m just... worried about getting home."
    show myc table hb surprise
    with dis
    "Mychael faltered as he lifted a piece to his mouth."
    show myc table dark
    with dis
    m "...oh.{w} You’re still thinking about that?"
    "He seemed annoyed, which was a first."
    p "Of course!{w} I’ve been gone for {i}three days{/i}!"
    p "People probably think I’ve gone missing!"
    show myc table dark
    with dis
    "His gaze lowered, almost grumbling."
    m "Is that so bad?"

    stop music fadeout 5.0

    p "I— {i}what?{/i}{w} Yeah, it’s {i}bad."
    p "Why do you sound like you don’t even care?"
    show myc table angry
    with dis
    play music "audio/ambience/tense-ambience.ogg" loop
    "Mychael frowned, looking up at me now."
    m "Why do you sound like you’re desperate to leave?"
    p "{i}What?"
    show myc table dark
    with dis
    m "It’s all you ever think about!"
    m "Are you not...{w=.2} happy here?"
    m "Is it not enough?"
    "I sighed, rubbing my fingers over my eyes."
    p "Mychael, we’ve gone over this."
    show myc table angry
    with dis
    p "I’ve said it once and I’ll say it again."
    p "You’ve done so much for me already."
    p "But I can’t keep pretending everything’s okay here.{w} I want to go home."
    p "I {i}need{/i} to go home."
    show myc table dark
    with dis
    "He sucked in a deep breath, grunting something indecipherable under his breath."
    m "I just... I only wanted to..."
    "He seemed to be battling himself before he finally sighed."
    show myc table regret
    with dis
    m "..."
    stop music fadeout 3.0
    show myc table regret2
    with dis
    m "..."

    m "...I’m sorry."
    m "You’re right.{w} Of course, you’re right."

    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop volume 0.1

    "His tone seemed genuine, even if the hurt in his eyes was clear as day."
    m "I’ll send you back today."
    "I narrowed my eyes."
    show myc table panic2
    with dis
    m "I mean it this time!{w=.2} I promise!"
    "He held his hand over his chest."
    m "I swear on my heart."

    menu:

        "Trust him.":
            "I mean, how could I not trust him?"
            "He was my last hope."
            jump cont_story_12

        "Don't trust him.":
            $ suspicion += 1
            "My eyes narrowed just a tad."
            "Could I really trust his word?"
            "Did I have another choice?"
            p "Will you tell me what happened yesterday at the river?"
            show myc table panic2
            with dis
            m "Th-the river?"
            m "I already told you what happened at the river..."
            "His voice sounded strained at the end."
            p "So...{w=.2} that's it, then?{w} You're just gonna send me home?"
            "He nodded."
            jump cont_story_12

    label cont_story_12:

    p "...okay."
    "I paused for a moment before adding quickly."
    p "Thank you."
    show myc table sad munch
    with dis
    "He nodded and went back to eating, watching me expectantly as he took a timid bite."
    show myc table hb nervous
    with dis
    "It was a moment before he swallowed and spoke again."
    show myc table sad
    with dis
    m "C-can you promise me something?"
    "His voice was quiet and for a lack of a better word,{w=.2} vulnerable."
    p "...what is it?"
    m "Promise me..."
    "His mouth hung open for a second or two before he laughed."
    show myc table wink
    with dis
    m "Promise you weren’t lying when you said you liked my cooking?"
    "I snorted."
    p "Are you kidding?{w} Do I look like the kind of person to lie?"
    p "I’m offended, Mychael!"
    "He laughed again, light and airy.{w} But if I dared to look closer, I could tell it was fake."
    "He probably didn’t want to make our last moments tense and awkward.{w} The least I could do was meet him halfway."

    scene bg black
    with Dissolve (1)

    "..."
    show bg woods daytime
    with dis
    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
    play sound "audio/sfx/forest-footsteps.ogg" loop
    "Before long we found ourselves walking down another path from Mychael’s."
    "The route was different today, probably because he didn’t have any detours in mind."
    "We walked in silence for a while; the only thing accompanying us were the sounds of nature and our footsteps."
    "I couldn’t tell what Mychael was thinking."
    "I knew he wasn’t the talkative type unless spoken to, but right now he seemed eerily quiet."
    "His back was tense,{w=.2} eyes looking nowhere but forward."
    "My voice was itching to say something{w=.2}, anything."
    stop sound fadeout 3.0
    "But it felt like the both of us had some thoughts to digest, despite it being easier to just say it out loud."
    "Still, the silence was getting unbearable."
    play sound "audio/sfx/twig-SNAP.ogg" volume 3
    p "S-so... um..."
    "We both halted in our steps at the sound of rustling, Mychael’s ear perking in a direction."
    p "Wh-what was that?"
    stop music fadeout 1.0
    play sound "audio/sfx/crossbow-load.ogg" volume 2
    "His hands were already raising to hold his crossbow, deftly cocking it with an experienced pull of the string until a solid click was heard."
    m "{size=-10}Stay quiet.{w} Stay close."
    play music "audio/music/creep.ogg" fadein 1.0 loop
    "I swallowed, my heart picking up speed."
    play sound "audio/sfx/bushes-rustle.ogg"
    hide mycjackie
    with dis
    "He started stalking low towards the source of the noise, his boots barely making a sound compared to my clumsy footsteps."
    "The rustling continued, sounding like a scuffle was occurring between the bushes."
    "Closer...{w}{i} closer..."
    "Until my ears picked up an unfamiliar high-pitched sound."
    "It sounded like a tiny infant screaming."
    "As morbid as that was, Mychael actually relaxed as he recognized it."
    "His steps hastened silently towards the source, crossbow lowering until we came across what exactly it was that caused the disturbance."
    show cg rabbit
    with dis
    stop music fadeout 2.0
    "...a rabbit."

    play music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
    "Its small delicate foot snagged in an old rusted trap."
    "Its little body trembled as it breathed fast and shallow, no doubt scared out of its mind."
    hide cg
    show mycjackie cb relieved
    with dis
    "Mychael regarded it empathically before unloading his crossbow,{w=.2} disturbed by the caught rabbit but at the same time relieved at the absence of a threat."
    m "Just a rabbit..."
    show mycjackie neutral
    with dis
    "Sweeping his crossbow behind his back and out of sight,{w=.2} he looked at it for another moment,{w=.2} before looking up towards me."
    m "...Let’s keep going then."
    "My mouth dropped in shock."
    p "And leave that poor thing behind?"
    show mycjackie confused
    with dis
    "He raised a brow,{w=.2} confused at my bewilderment."
    m "...yes?"
    p "B-but it’s going to die!"
    "His face twisted into confusion."
    show mycjackie confused2
    with dis
    m "That’s... generally what happens to prey animals, yes."
    "He was so nonchalant about it I had to keep my emotions in check."
    p "W-we can’t do that!"
    p "Look at it!"
    show mycjackie annoyed
    with dis
    "His expression was understanding, if a little annoyed."
    m "I am.{w} Someone left a trap.{w} A rabbit gets caught in it.{w} That’s how it works."
    show mycjackie annoyed2
    with dis
    m "What do you want me to do?"
    p "S-set it free?{w} Obviously?"
    show mycjackie bothered
    with dis
    "He was frowning now."
    m "I can't.{w} If someone is nearby they'll be suspicious how their catch got free."
    p "Does that matter? Animals escape traps all the time!{w} The poor thing is suffering!"
    show mycjackie annoyed2
    with dis
    m "[protag], I know you’re smarter than this.{w} If it doesn’t die today, it’ll die tomorrow."
    m "To a trap.{w=.2} To a fox.{w=.2} To a hunter."
    m "It probably won’t even survive long with its injured foot if we set it free."
    m "You’re prolonging the inevitable."
    p "Can't you put it out of its misery then?"
    show mycjackie confused
    with dis
    "He hesitated."
    m "Do you really want me to do that?"
    p "...{w}no."
    p "B-but even then!{w} We don’t even know if anyone’s coming back for it. The thing looks so old!"
    show mycjackie sigh
    with dis
    "He sighed impatiently, looking stubborn in his decision."
    show mycjackie annoyed2
    with dis
    m "That’s the point of a trap.{w} It’s to keep things right where they are until you come back."
    "The way he said it just rubbed me the wrong way..."

    menu:

        "He's being realistic.":
            "In a way, his logic made sense, but still..."
            jump cont_story_13

        "He's being sadistic.":
            $ suspicion += 1
            "What kind of cold-hearted person says that?"
            jump cont_story_13

    label cont_story_13:

    "I could hardly believe how needlessly callous he was being."
    "For someone so sweet with his hens he was so indifferent about the poor rabbit shaking at our feet."
    "I looked down at it once more, my heart breaking as it started to squeak."
    p "Mychael..."

    menu:

        "I-I guess you're right.":
            m "...okay."
            m "Follow me."
            show bg woods trail 01
            hide mycjackie
            with dis
            "Who was I to say what was right and wrong?"
            "Maybe he had a point."
            "It was just one small rabbit in the grand scheme of things."
            "We should just let it be."
            "Mychael led us back to where we came, the struggling, squeaking noises of the rabbit eventually drowned out by the sounds of the forest around us."
            "Left alone to its fate."
            "Guilt spread through my chest like an icky mold, but I quickly stifled it."
            "It’s just nature."
            "Let it be."
            "{i}Let it be."
            jump cont_story_15

        "Please..?":
            $ help_rabbit = True
            jump cont_story_14

    label cont_story_14:

    "My heart was torn as the rabbit helplessly kicked its feet, its cries weakening."
    "For a moment I imagined [pet] being caught in a trap just like this one,{w=.2} left to starve and die when someone could’ve been there to help %(pronoun4)s."
    p "N-no...{w} We can’t leave it like this."
    p "{i}Please{/i}, Mychael...?"
    show mycjackie annoyedb
    with dis
    "His harsh gaze started to soften at my plea."
    m "...does it matter that much to you, firefly?"
    "I nodded quickly without hesitation."
    p "Please!{w} It’ll be the last time I’ll ever ask for anything!"
    show mycjackie sigh
    with dis
    "He paused for another moment before shaking his head with a defeated sigh."
    m "{size=-10}Somehow I doubt it’s the last time."
    "There was a smile in his voice, though."
    show mycjackie annoyedb
    with dis
    m "But alright.{w} I’ll do it for you."
    m "Stand back.{w=.2} I have to pry it open."
    hide mycjackie
    with dis
    play sound "audio/sfx/knife-out.ogg" volume 0.7
    "My gratitude was clear on my face as he pulled out a deadly-looking hunting knife from his pocket, kneeling down next to the rabbit."
    "The terrified creature started to writhe all over again at the sign of a looming threat, Mychael grunting as he held it down firmly with one hand."
    "It started to fall still under his hold, relaxing completely with its foot hanging limp."
    "Huh.{w} He sure had a way with animals."
    show bg woods daytime
    with dis
    "I backed away to give him space, not wanting to distract him."
    "As he was working to free the rabbit, I looked around to take in my surroundings."
    "The trees felt somewhat familiar, a flash of a memory playing in my mind."
    play sound "audio/sfx/bushes-rustle.ogg" volume 0.7
    "Casting one last glance towards Mychael’s back, I wandered a bit further away,{w=.2} making sure to stay within earshot."
    "It took a few steps before I came across a familiar sight."
    show bg mushroom ring 03
    with dis
    p "Oh!"
    "It was the circle of mushrooms from the other day."
    "I recalled that [pet] was definitely here..."
    stop music fadeout 3.0
    "I hesitated at the edge of it, a sourceless sense of fear suddenly coursing through me as I stared at it."
    "...Had it grown bigger?"
    show darker at slow_dissolve
    play sound "audio/sfx/hypno-static-daytwo-electric-boogaloo.ogg" fadein 3.0 loop
    "The longer {color=#8c277a}I{/color} stood there the more the fear dissipated, {w=.2}{color=#8c277a}my{/color} limbs tingling pleasantly and urging {color=#8c277a}me{/color} forward."
    "Before I realized it {color=#8c277a}my{/color} foot was already lifting to approach it."
    "{color=#8c277a}Closer...{w}{i} closer..."
    show bg mushroom ring 04
    with dis
    "Staring at it,{w=.2} a fuzzy haze creeped over my mind.{w} My face was warm."
    "I found myself smiling at the oddly comforting familiarity."
    "Like recalling a fond memory, like greeting an old friend..."
    show yank 01
    with dis
    "{color=#8c277a}I{/color} knelt down to inspect the growth, reaching out to brush {color=#8c277a}my{/color} hand on one of the mushroom caps."
    play sound "audio/sfx/grab.ogg"
    queue music "audio/ambience/forest-morning.ogg" fadein 1.0 loop
    show yank with vpunch
    hide darker with dis
    "When someone yanked my wrist back."
    p "Wha—-"
    m "{b}Don’t."
    p "...Huh?"
    m "{b}Don’t.{w=.3} Touch.{w=.3} Those."
    show cg oh he angy
    hide yank
    with dis
    "I looked up to see Mychael looming over me, gaze sharp and irises shaped like thin slivers."
    m "{sc=2}...you have a terrible habit of wandering off, don’t you?{/sc=2}"
    "I gulped."
    p "I-I just..."
    p "H-how is the rabbit? Is it safe?"
    "His eyes narrowed as I flailed to change the subject."
    m "...it’s free like you asked.{w} Don’t touch those."
    "Mychael squeezed my wrist before letting go."
    hide cg
    show bg woods daytime
    with dis
    "I rubbed my wrist. It didn’t hurt but his grip had intent."
    p "Wh-why? What’s wrong with them?"
    show mycjackie bothered
    with dis
    m "...{w}Nothing."
    m "Just don’t touch them."
    p "{color=#8c277a}I-I{/color} just... thought it looked pretty, that's all."
    show mycjackie annoyed2
    with dis
    play sound "audio/sfx/you-dont-have-a-choice.ogg"
    show pink behind mycjackie
    with dis
    "{sc=2}Did {color=#ff8da1}you{/color}, though?{/sc}"
    "I shook my head, feeling disoriented as my mind flickered between thoughts rapidly like a broken radio station."
    show mycjackie angry
    hide pink
    with dis
    play sound "audio/sfx/fingersnaps.ogg"
    "Mychael snapped his fingers for my attention."
    m "Look at me, firefly."
    "His voice was snippy and irritated."
    p "U-uh..."
    "I blinked rapidly to ground myself, scratching my head as I tried to gather my thoughts."
    m "Talk to me.{w=.2} Say anything."
    p "Some...{w=.2} people think they’re magic."
    "Yeah... that’s a pretty common belief with mushroom rings, isn’t it?{w} I hung onto that thought."
    m "Keep going."
    p "L-like,{w=.2} related to fae-folk, you know?{w} It’s why they’re called fairy rings, o-or a fairy circle."
    show mycjackie annoyed2
    with dis
    "Mychael squinted before easing, his demeanor just a little less tense compared to before."
    p "They do look like they could summon a portal at any moment and whisk you away..."
    "I looked over at Mychael,{w=.2} expecting him to look amused."
    show mycjackie disgust
    with dis
    "Instead he was glaring down at the ground,{w=.2} as if the mushrooms were the most vile thing he’d ever seen."
    m "No.{w} {sc=2}It’s more of an invasive species than anything else.{/sc=2}"
    "I followed his gaze towards the harmless circle of fungus."
    p "They are?"
    p "Should we...{w=.2} do something about it?"
    show mycjackie surprise at bounce
    "He blinked as if coming out of a daze."
    m "Uh, n-no. No."
    m "Sorry, {w=.2}just uh... a thought that slipped out."
    show mycjackie bothered
    with dis
    "He pinched his nosebridge, his normally soft voice a tired grumble."
    m "Normally I'd leave them alone to do their business but having you here..."
    m "A-anyways, just don't touch it, okay?"
    "He was being far too uptight about something as trivial as a circle of mushrooms."
    p "It feels like there's more to it than that..."
    show mycjackie annoyed
    with dis
    "His sigh was exasperated."
    m "They just...{w=.2}{sc=2}grew in my part of the forest{/sc=2}, is all."
    m "They make me{cps=10}...{/cps} {w=.2}{i}{sc=2}uncomfortable.{/sc=2}"
    "It definitely felt like Mychael wanted to use a stronger word than ‘uncomfortable’, a barely concealed growl between his teeth."
    p "Why? I thought you liked mushrooms."
    show mycjackie angry
    with dis
    "Mychael’s ears flattened."
    show mycjackie annoyed
    with dis
    m "Not these ones..."
    m "They're not even real mushrooms..."
    p "They're...{w=.2} not?"
    m "No."
    "He seemed to hesitate before blurting."
    show mycjackie annoyed2
    with dis
    m "They just happen to {i}mimic{/i} mushrooms."
    "Oh.{w} I've never heard of something like that."
    "Though there are some pretty wild foliage out there that could copy the look of nearby plants..."
    p "Does it have a name?"
    "His brows scrunched in confusion."
    m "What? Them?"
    p "Yeah.{w} You know,{w=.2} as in the species?"
    show mycjackie annoyed
    with dis
    m "Oh."
    m "Uh...{w=.2} I’m not entirely sure."
    m "I can recognize them by sight though so just..."
    m "S-stick with me when we’re out in the woods, okay?"
    show mycjackie sigh
    with dis
    m "I {cps=15}{i}really{/i}{/cps} don’t want you anywhere near them."
    p "Alright... if you say so."
    p "I just don’t get how they can be invasive, is all."
    show mycjackie angry
    with dis
    m "{size=-10}...I consider it invasive when they come on {i}my{/i} property."
    "Is he really getting this angry over cute mushrooms?"
    p "I'm gonna be honest, you're acting really weird about it, Mychael."
    show mycjackie disgust
    with dis
    "He was getting more agitated the longer we stood there, hands clenching into tight fists."
    m "[protag], I know I ask a lot from you but {i}please{/i} let's just leave them alone, okay?"
    p "Wh-why?{w} There's something you're not telling me here–{nw}"
    play sound "audio/sfx/kicky.ogg" volume 10
    show mycjackie shout
    m "{size=+15}{b}Look, can we just–!" with vpunch
    show mycjackie shout2
    with dis
    "I flinched, backing away from him as his voice rang through the trees."
    "A silence passed between us before he took a deep breath."
    show mycjackie scared
    with dis
    m "I'm sorry.{w=.3} I'm sorry."
    m "Please can we step away from here?"
    "He held out his hand.{w} His fingers were trembling."

    menu:

        "Take his hand.":
            show mycjackie blush at bounce
            "I closed my hand around his, noting the way his tail flicked so hard it thumped against his leg."
            "His fingers were calloused against my own, twitching at the unfamiliar sensation."
            "I stepped up beside him, looking at him expectantly."
            m "O-oh."
            show mycjackie dokidoki1
            with dis
            m "I-I...{w} I didn’t think you’d take it."
            "Now it was my turn to get flustered."
            p "Y-you offered!"
            m "I know I did!"
            m "I thought I scared you, so I figured..."
            "We waited for the other to say something, our faces growing heated as seconds passed."
            show mycjackie shy
            with dis
            "He finally laughed, exclaiming something strange and garbled before squeezing my hand."
            m "[protag]... you’re really something special.{w} I hope you realize that."
            "He gave my hand another tight squeeze, snapping me out of my daydream."
            m "Let’s get you home, firefly."
            hide mycjackie
            with dis
            jump cont_story_15

        "Decline.":
            "I shake my head."
            show mycjackie sad
            with dis
            "He looked dejected, but nevertheless accepted it with a gentle nod of his head."
            m "I-I’m really sorry for scaring you, firefly."
            m "Are you...{w=.2} okay?"
            p "...I'm fine.{w} But don't ever yell at me like that ever again."
            show mycjackie scared
            with dis
            "His ears drooped, expression full of regret."
            m "I’m sorry."
            m "I-I’m sorry..."
            p "..."
            m "Let’s get you home?"
            p "..."
            p "Let’s get me home."
            hide mycjackie
            with dis
            jump cont_story_15

        "Call him out." if suspicion == 3:
            jump pleasedontpleasedontpleasedont

    label pleasedontpleasedontpleasedont:

        stop music fadeout 3.0

        p "No.{w} Enough is enough."
        p "You keep dodging my questions.{w} You keep deciding things on your own."
        p "You won’t even tell me what the hell is wrong with these stupid mushrooms!"
        p "Are you ever gonna tell me the truth or am I stuck in this loop of doubting every single word you say?"
        show mycjackie shock
        with dis
        play music "audio/music/forgiveme-forgetme.ogg" fadein 3.0
        "His hand dropped like an anchor."
        m "Y-you don’t trust me?"
        p "How can I!" with vpunch
        p "What happened yesterday, Mychael!?" with vpunch
        "I stared up at him, my glare sending him into a panic."
        show mycjackie scared
        with dis
        m "D-do you really wanna know?"
        "My eyes narrowed."
        "He flinched."
        show mycjackie regret
        with dis
        m "I-I..."
        m "I-I made you...{w=.2} sick."
        p "...Sick?"
        "He swallowed, taking a deep breath."
        m "I’m able to...{w=.2} {i}suggest{/i} things. {w}M-make people listen."
        m "I-I can make you forget fear.{w} Mess with the thoughts inside your head."
        p "What are you talking about?"
        show mycjackie regret2
        with dis
        m "[protag]..."
        play music "audio/sfx/hypno-static-daytwo-electric-boogaloo.ogg" fadein 3.0 loop
        show pink behind mycjackie
        with dis
        "{color=#ff8da1}I hope you don’t hate me for this."
        "{b}{color=#ff8da1}I{/color}{/} cried out as a pressure started pushing against {b}my{/b} eyes." with vpunch
        show pinker
        with dis
        "A painful aching pressure filled {b}{color=#ff8da1}my{/color}{/b} head,{w=.2} {b}my{/b} hands flying to clutch at {b}my{/b} ears." with vpunch
        p "Wh-what-?" with hpunch
        show mycjackie regret
        with dis
        "{b}My{/b} head felt tight and full to bursting, crushed under a weight {b}{color=#ff8da1}I{/color}{/b} couldn't comprehend." with vpunch
        "It was like {b}{color=#ff8da1}I{/color}{/b}’d painfully grown a second skull and none of {b}{color=#ff8da1}my{/color}{/b} thoughts fit in {b}my{/b} own brain, pushing pushing pushing {color=#ff8da1}outwards." with vpunch
        "{color=#ff8da1}Relax..."
        "{b}{size=+5}{k=5}{sc=2}{color=#ff8da1}It won’t hurt if you relax.{/sc}"
        p "Mychael–!"
        "{b}{color=#ff8da1}I{/color}{/} inhaled sharply, feeling the unbearable droning headache growing into a painful spike.{w} Were {b}{color=#ff8da1}my{/color}{/b} ears bleeding or am {b}I{/b} imagining it?" with vpunch
        "{sc=2}{color=#ff8da1}Usually I have to be subtle otherwise your psyche will try to fight back.{/sc}"
        "{sc=2}{color=#ff8da1}Like it is right now.{/sc}"
        p "{size=+10}{b}Stop it!" with vpunch
        show mycjackie regret2
        with dis
        hide pink
        hide pinker
        with dis
        stop music fadeout 1.0
        "The feeling faded instantly.{w} It was only then I realized I was crying, my cheeks wet with tears and nose stuffed with snot."
        p "Wh-why did you do that?"
        m "I-I was trying to help you understand..."
        p "{size=+10}{b}By trying to kill me!?" with vpunch
        play music "audio/music/forgiveme-forgetme.ogg" fadein 3.0
        show mycjackie panic
        with dis
        m "N-no!"
        m "That wouldn't have killed you!"
        m "I-I made sure of it!"
        p "{i}Made sure of it...?"
        p "What does that even mean!?"
        m "I-I don't-{w=.2} I didn't know what to do!{w} That was all I've ever known!"
        p "You...{w=.2} you tricked me?"
        p "{size=+5}You hurt me!?"
        p "{b}{size=+8}And you {i}dare{/i} ask me to trust you!?" with vpunch
        m "I’d never hurt you like that,{w=.2} ever!"
        m "I-I can promise you you weren't hurt,{w=.2} it was all in your head!"
        "I balked at the audacity."
        p "{b}{i}{size=+10}And you think that makes it okay!?" with vpunch
        show mycjackie regret
        with dis
        "He froze, expression growing pained."
        m "N-no, it doesn’t..."

        menu:

            "You're a monster.":
                jump meanie_01

            "You're a freak.":
                jump meanie_01

            "You're disgusting.":
                jump meanie_01

        label meanie_01:

        show mycjackie hurt
        "His eyes widened with hurt." with vpunch
        m "N-no, [protag]...{w=.2} d-don’t say that, not after everything you've said..."

        menu:

            "I was wrong.":
                jump meanie_02

            "I was lying.":
                jump meanie_02

            "I was an idiot.":
                jump meanie_02

        label meanie_02:

        m "Y-you don’t mean that..."
        show mycjackie panic
        m "You don’t mean that!" with vpunch

        menu:

            "Leave me alone.":
                jump forget_me

            "Stay away.":
                jump forget_me

            "I hate you.":
                jump forget_me

        label forget_me:

        show mycjackie badend cry with vpunch
        m "{size=+5}No!{w} No, please!!"
        m "Don’t look at me like that!"
        m "You’re different!! I know you are!{w=.3} We can start over,{w=.3} I promise,{w=.3} we can be friends-{nw}"
        p "Friends!?{w} Are you serious!?"
        p "Forget it! Friends don't hurt each other playing twisted mind games!"
        show mycjackie badend cry2 at shake
        with dis
        m "N-no...{w=.2} Nono, {b}please{/b}. Please forgive me."
        m "{b}Please please please{/b} let me have this.{w=.3} Please forgive me."
        "His breathing grew erratic, gasping for air."
        m "{b}Please!{w=.2} PleASE!{w=.2} PLEASE!!"
        m "{sc=2}I can’t lose you like this!{w} I can’t!!{/sc}"
        show mycjackie badend tense at reset
        with dis
        "I take a step back from him, the movement causing his entire body to tense up."
        play sound "audio/sfx/grab.ogg" volume 0.3
        show mycjackie badend grab at zoom_in3
        show bg at zoom_in2
        "He suddenly lunged for me, grabbing my shoulders tight." with vpunch
        show mycjackie badend slap at slap
        show bg at zoom_out2
        play sound "audio/sfx/get-off-me.ogg"
        "Somehow I was ready for it, shoving him back and slapping him across the face." with hpunch
        show mycjackie badend slap2
        with dis
        "He stood there in shock,{w=.2} tears spilling over his cheeks from the force."
        m "{size=-5}You{cps=15}...{/cps}{w=.2} you really do hate me..."
        m "{size=-5}Oh..."
        m "{size=-5}That... hurts so much, [protag]."
        show mycjackie badend slap3 at shake
        with dis
        m "..."
        m "{sc=2}I'm sorry.{/sc}"
        stop music

        scene bg black
        play sound "audio/sfx/fallen-down.ogg"
        "Everything goes dark."
        "..."
        "..."
        "..."
        s "...[protag]?"
        s "[protag]!"
        p "Mngh..."
        play music "audio/ambience/street-ambience.ogg" fadein 1.0 volume 0.7
        play sound "audio/sfx/sniff-snorf.ogg" volume 1.5
        show cg boopersnoot 01 at zoom_in5
        p "AGH!" with vpunch
        play sound "audio/sfx/bork-bork.ogg" volume 3
        show cg at zoom_in
        "I shot into a sitting position, a wet lick trailing up my cheek as the golden retriever barked."
        s "Laika, down!"
        p "L-Laika?"
        "I recognized that voice..."
        show cg boopersnoot 02
        with dis
        "A tall figure loomed into view, their long hair tied back into a messy ponytail."
        "My eyes widened as I recognized a familiar face."
        p "Vida?{w} You’re back?"
        hide cg
        show bg street
        show laika happy at right
        show vida surprise at left
        with dis
        show vida nervous smile
        with dis
        "My neighbor gave me a timid smile, fidgeting with the frisbee in their hands."
        v "For my semester break, yeah!"
        show vida worried
        with dis
        v "Where have you been, [protag]?{w=2.} I came by during the weekend but you weren’t home and you weren’t answering your phone either!"
        show vida sad
        with dis
        v "We were on our way to the park when we found you..."
        show vida confused
        with dis
        "I glanced around, realizing I was sitting by the sidewalk.{w} A few feet away was the edge of the woods right beside our neighborhood."
        "Vida reached down and started picking twigs and leaves out of my hair,{w=.2} completely unprompted."
        show vida worried
        with dis
        v "Did you go camping...?"
        p "I...{w=.2} I-I don’t remember."
        "I stood on my feet, brushing off my clothes and fixing the bag over my shoulder."
        show vida sad
        with dis
        v "Oh, that’s worrying...{w=.2} are you sure you’re alright?"
        p "I think so..."
        "A shudder ran through me, my head glancing towards the trees."
        "I saw a flash of yellow disappear into the bushes."
        "...maybe a bird?{w} A butterfly, perhaps?"
        play sound "audio/sfx/bork-bork.ogg" volume 3
        show laika at bounce
        "Laika must've seen it too, as the dog started barking."
        show vida surprise
        with dis
        "Whatever it was, it was already out of sight."
        p "I-I think I need to go home..."
        hide vida
        hide laika
        with dis
        pause 1
        show bg at zoom_in_street
        play sound "audio/sfx/concrete-run.ogg"
        "Vida was about to say more before I sidestepped them, leaving them confused as I hastily made my way to my street."
        show bg home at reset
        with dis
        stop music
        play sound "audio/sfx/door-open.ogg"
        "Reaching my home I threw the door open and stumbled inside."
        "All of my senses felt out of tune, like my brain was still catching up with my body."
        "My bag dropped with a muffled thud to the ground, its contents a mystery as I wandered to the kitchen for a drink."
        "Why did everything feel so fuzzy?"
        "It’s like I was trimmed out of a stray photograph and pasted onto the scrapbook of a page where the memory didn’t belong..."
        "Why?"
        "Why?"
        "Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why?""{cps=300}{b}Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why? Why?"
        "{i}{b}Why did everything feel so wrong?"
        "I downed my drink.{w} And another."
        "My tongue was numb.{w} It didn’t feel like I tasted anything or if my thirst was real at all."
        "Maybe I needed a nap...?"
        play sound "audio/sfx/knocky.ogg"
        "I was about to shuffle off to my bedroom when there was a knock at my door."
        play sound "audio/sfx/door-open.ogg"
        play music "audio/ambience/street-ambience.ogg" fadein 1.0 volume 0.7
        "Confused, I hurried to open it expecting Vida back from their walk."
        "...nobody."
        show cg lost n found 01
        with dis
        "Glancing down at my feet, there was a circle of blue flowers placed next to a strange wooden box."
        "It looked like an instrument."
        "Did someone mistake my house for another?"
        show cg lost n found 02
        with dis
        "Picking up the items, my hands brush over the wood and thumbed the delicate petals."
        "What a strange thing to leave at someone’s doorstep..."
        "Even if it was a prank, why leave these items specifically?"
        hide cg
        show bg forestfromhome2:
            xoffset 0
        with dis
        "I looked out towards the forest, a pang of something nostalgic striking hard in my chest."
        "I’ve never set foot in those woods,{w=.2} never had a reason to."
        "And yet...{w=.2} I couldn’t help feeling like I’ve lost something.{w} Something important."

        show bg black
        with dis
        pause 1

        "But if it was important...{w=2.} surely I’d remember it?"
        "..."
        "..."
        "..."
        "ENDING 4: Forget-Me-Not."

        return

    label cont_story_15:

    show bg woods trail 01
    hide myc
    with dis

    play sound "audio/sfx/forest-footsteps.ogg" loop
    "Mychael took the lead, his footing sure and confident."
    "He must’ve noticed my unsteady gait beside him, as he subtly veered towards a clearer path I could easily follow."
    "I didn’t verbalize it,{w=.2} but I was definitely grateful for that."
    "As much as the forest was growing on me, getting my feet caught in roots and twigs every few steps gets tiring after a while."
    "Our steps fell into rhythm next to each other."
    "I peeked at Mychael every once in a while, trying to gauge his mood after what happened."
    "Even after spending so much time with him, he was so difficult to read."
    "How can someone both wear their heart on their sleeve yet keep it stitched tight, never letting anyone come too close?"
    "I knew he had secrets he wanted to keep close to his chest,{w=.2} but I wished he’d just open up to me a little."
    "The silence that hung in the air was making my skin prickle."
    p "Wh-what’s your favorite animal?"
    stop music fadeout 3.0
    "I was so caught up in my thoughts I didn’t even realize I blurted the first thing that came to mind."
    show mycjackie confused
    with dis
    "Mychael regarded me curiously, ear flicking."
    stop sound fadeout 5.0
    play music "audio/music/goofing-around.ogg" fadein 1.0 loop
    m "My favorite animal?"
    "He pursed his lips in thought before his ears perked."
    show mycjackie amused
    with dis
    m "Jellyfish."
    "I did a double take."
    "It was one thing for him to have an answer so readily but the choice was something else."
    p "A jelly...?"
    p "Why jellyfish?"
    p "I thought it’d be...{w=.2} I don’t know,{w=.2} a bird or something."
    show mycjackie smile
    with dis
    "He shrugged."
    m "They're pretty to look at.{w=.2} At least... from pictures I've seen."
    m "Plus I kinda relate to them."
    "He said that without zero hesitation."
    p "H-how exactly do you relate to jellyfish...?"
    show mycjackie surprise
    with dis
    "His expression faltered, as if deciding on the right way he could explain his answer."
    show mycjackie nervous
    with dis
    m "Let’s just say... I have something in common."
    p "...with a {i}{b}jellyfish{/i}."
    show mycjackie grin
    with dis
    m "Well, {i}one{/i} jellyfish."
    p "In what way?{w} That they're pretty to look at?"
    show mycjackie blush at bounce
    "A strangled noise slipped past his throat."
    m "N-no!"
    m "..."
    m "You wouldn't get it."
    p "Try me."
    m "{cps=5}. . .{/cps}{w} no."
    "I groaned like a dying whale in exasperation, shoulders slumped like I had a back problem.{w} He’s not gonna elaborate any more, is he?"
    "He probably spotted the vein growing on my forehead as he snickered."
    show mycjackie amused
    with dis
    m "Relax, firefly.{w} You’re gonna faint on the spot if you think any harder."

    if help_rabbit:

        p "If you’re allowed to get upset about mushrooms, I’m allowed to get upset about jellyfish."

    else:

        p "Yeah, well, it'd be your fault."

    show mycjackie surprise
    with dis
    "His smile dropped for a second before his cheeky grin returned."
    show mycjackie grin
    with dis
    m "Touch."
    p "...touch?{w} Touch what?"
    show mycjackie happy
    with dis
    m "Y’know, touch!"
    "I stared at him, his happy grin shifting into a confused frown."
    show mycjackie amused
    with dis
    m "Y’know, touch! When um... it’s like saying you’re right."
    p "{cps=25} You mean {i}touché{/i}?"
    "He smiled innocently."
    m "Yeah!"
    "{sc=2}This man will be the death of me.{/sc}"
    "He laughed at my screwed up grimace, waving a hand hastily."
    m "What about you?{w} What’s your favorite animal?"

    menu:

        "Cats.":
            show mycjackie amused2
            with dis
            "He snorted, a fond smile on his lips."
            m "You know what?{w=.2} I don’t even know why I bothered asking."
            m "Of course it’s cats."
            p "What’s that supposed to mean!"
            show mycjackie amused
            with dis
            "He gave me a look."
            m "You know what I mean."
            p "...{w}yeah.{w=.2} I know what you mean."
            show mycjackie happy
            with dis
            "He pretty much giggled in response."
            jump cont_story_16

        "Your chickens.":
            show mycjackie surprise
            with dis
            "He looked taken aback, clearly not expecting that answer."
            m "Really?"
            p "Yeah!{w} Who wouldn’t fall in love with the little darlings?"
            show mycjackie shy
            with dis
            "He seemed pleased with that answer, his already wide smile softening further."
            m "You’re right."
            m "{i}...who wouldn’t fall in love with a little darling?"
            jump cont_story_16

    label cont_story_16:

    hide mycjackie
    with dis
    show bg woods daytime
    stop music fadeout 3.0
    "We continued with idle chatter after that."
    "I didn’t even know how much time had passed as the trees slowly thinned out, the sounds of nature muffling as the canopy started to grow scarce."
    play sound "audio/sfx/vroom-vroom.ogg" volume 0.7
    "Suddenly, I heard the soft yet familiar rumble of a car in the distance."
    "I almost didn't pick up on it, fully immersed in whatever Mychael was rambling about."
    "Something-something about the life cycle of a {i}Topsy-turvy door-knee{/i} or whatever it was he called it."
    p "Oh!"
    "Had we really walked that far already?"
    play sound "audio/sfx/grassy-run.ogg"
    "I left Mychael’s side and rushed forward."
    "He made a sound of surprise but followed suit."
    play music "audio/ambience/street-ambience.ogg" fadein 1.0 volume 0.7
    "I neared the edge of the forest just as another car drove past."
    show bg street
    with dis
    "I recognized my street instantly."
    play sound "audio/sfx/concrete-run.ogg"
    "Breaking into a light jog, I almost miss Mychael calling for my name as I run down the road."
    "There!"
    "My house was visible from where I stood by the street."
    "I was breathing heavily by the time Mychael approached my side, the man barely making a sound as I took in the sight."
    p "Oh, I missed this..."
    "I turned to thank Mychael,{w=.2} only to startle when a bundled stranger took his place."
    show mycjackie bundled
    p "Ah!" with vpunch
    m "Sorry.{w} People about."
    "I couldn’t see anyone around,{w=.2} but I guess he was right to be safe."
    "I guess this was his version of a disguise..."
    "If I were to pass him on the street I don't think I would've bothered to look twice."

    if suspicion >= 2:

        "I shuffled my feet, feeling awkward now about my previous apprehension."
        "I might've had my doubts about him,{w=.2} but maybe I was wrong after all."
        "He did get me home, despite everything."

    p "I-I mean, I’d wanna say thank you to your face but I’ll settle for this, I guess."
    show mycjackie bundledh
    with dis
    "His chuckle was muffled underneath the scarf."
    show mycjackie sd cheeky
    with dis
    "He pulled it down so he could speak properly."
    m "Did I scare you?"
    p "I-I got distracted!"
    show mycjackie sd amused
    with dis
    "Mychael’s eyes squinted from where I could see them."
    m "And I wonder how you don't get lost every twenty steps..."
    p "Hey!"
    "He laughed at my offended tone."
    m "You better not go back in there, got it?"
    m "I'm not always gonna be around to find you."
    p "Who says I need you around to find me?"
    show mycjackie sd scold
    with dis
    "Almost instantly his eyes hardened under his sunglasses."
    m "I'm serious."
    m "Don’t go wandering in these woods again."
    m "Or I might have to start taking drastic measures just to make sure you stay put right where you are."
    "I sputtered indignantly."
    p "I’ll wander where I please!"
    m "Sure..."
    show mycjackie sd neutral
    with dis
    "He looked over my shoulder towards my house."
    m "So that’s where you live, huh?"
    m "Looks cozy."
    "I wasn’t sure if he was being genuine considering he lived in the wooden back ends of the middle of nowhere."
    "Suddenly, I perked up with a thought."

    if suspicion >= 2:

        "A small part of me couldn't help insisting it was a bad idea,{w=.2} but I was too curious not to ask."

    p "Do you wanna come by?"
    show mycjackie sd surprise at bounce
    "His eyes darted towards me, shock evident on his face."
    m "M-me?{w=.2} To your home?"
    "I nodded."
    "He froze completely.{w} For a second I thought he stopped breathing."
    show mycjackie sd blush
    with dis
    m "I-I...{w}{cps=25} I’d love to–{nw}"
    play sound "audio/sfx/bork-bork.ogg" volume 2
    show mycjackie sd angry at bounce
    pause 1.2
    play sound  "audio/sfx/caught-you.ogg" volume 0.7
    show bg at zoom_in2
    show mycjackie sd angry at zoom_in4
    pause 0.2
    hide mycjackie
    "Sudden barking and a shout startled us both, my body jerking forward as his arm yanked me close." with hpunch
    "I heard a soft rustle as his sunglasses fell to the grass from the sudden motion,{w=.2} his hastily worn beanie shaken off his head."
    "Looking up it was just my neighbor calling out to their dog."
    p "Oh!{w} Looks like Vida’s back from college..."
    "I paused, feeling his grip tighten.{w} I looked down at his hand on my shoulder before glancing up at him."
    p "Uh... Mychael..."
    show mycjackie surprise
    with dis
    "He snapped back to the present, his hand releasing me quickly."
    show bg at zoom_out2
    m "S-sorry."
    show mycjackie confused2
    with dis
    "He looked towards my neighbor and their dog for another moment before turning back to me."
    m "Um. I don’t think it’s a good idea for me to go with you..."
    m "I don’t wanna be seen..."

    if suspicion >= 2:

        "Even though I didn't fully trust him,{w=.2} I still felt disappointed at his rejection."

    "I deflated just a little."
    p "B-but you have your disguise, don’t you?"
    show mycjackie nervous2
    with dis
    "He shook his head insistently."
    m "I can’t risk it."
    m "It’s better this way."
    "He spoke with a finality that was starting to become familiar."
    "If he wasn’t willing, fine.{w} At least I was."
    "Before he could pick up his accessories I gently grabbed his wrist."

    if suspicion >= 2:

        "Though I couldn't help feeling like he had one too many secrets to keep,{w=.2} it wouldn't hurt to get to know him more and figure them out."

    p "Then can I come visit you instead?"
    show mycjackie surprise
    with dis
    stop music fadeout 3.0
    m "...what?"
    "I huffed impatiently."
    play music "audio/music/happy-end.ogg" fadein 2.0 loop
    p "If you won’t come to mine,{w=.2} then I’ll go to yours."
    "Once again he was rendered speechless."
    m "Wh-why would you {i}ever{/i} wanna see me again?"
    "At this point I was starting to look and sound peeved."
    "For all his good traits, the constant need to build his walls higher around me was starting to get annoying."
    "I folded my arms, looking stern."
    show mycjackie blush
    with dis
    "His eyes widened as if in preparation, ears flattening like a cat in the middle of a scolding."
    p "Mychael.{w} Can you just accept the fact that {i}maybe{/i} I enjoy your company and wouldn’t mind more?"
    m "I’m sorry, I just..."
    m "Nobody’s ever..."
    show mycjackie nervous2
    with dis
    m "But you wanted to go home so badly?"
    "{b}Oh, this man is hopeless..."
    p "{i}Yes.{/i} Of course I do!{w} But that doesn’t mean I’m gonna forget about you completely!"
    p "Besides, I promised I’d show you what phones could do, didn’t I?"
    "...dismissing the fact that there’s probably not much I can show when there’s no data in the woods."
    "I’m sure he’d be enthralled by whatever dinky mobile game I had installed at the time."
    "The point was I just wanted to see him again."
    show mycjackie blush
    with dis
    m "So that means... I-I get to see you again?"
    "I picked up on the eager tone in his voice, realizing he wished for the same sentiment."
    p "Y-yeah.{w} I want to."
    "His voice warbled for a second."
    show mycjackie dokidoki1
    with dis
    m "F-firefly..."
    "He cleared his throat, laughing to himself."
    m "[protag]..."
    m "You can’t imagine how much that means to me."
    m "...a lot.{w} It means a lot.{w=2.} More than you know."
    "I nodded, a giddy smile creeping onto my own face."
    p "How’s next weekend?"
    show mycjackie blush
    with dis
    "He tilted his head."
    m "That’s... seven sundowns from now?"
    p "Five."
    show mycjackie shy
    with dis
    "His smile widened, eyes squinting in absolute delight."
    m "Okay."
    m "I’ll meet you here then."
    "I smiled at him, figuring this was goodbye."

    if suspicion >= 2:
        "I wasn't my best self in the last few hours spent with Mychael...{w=.2} being closed off the moment he held back information."
        "But maybe a simple gesture could make up for it."

    menu:

        "Hug him.":
            show mycjackie dokidoki1 at zoom_in6
            show bg at zoom_in6
            play sound "audio/sfx/congrats-you-hugged-mychael.ogg"
            pause 1
            hide mycjackie
            show cg hug the lad 01
            with dis
            "I didn’t think twice, arms spread and wrapped around him before he could react."
            "Mychael froze from head to toe,{w=.2} inhaling sharply as his shoulders tensed."
            "For a second I thought I triggered a fight-or-flight-or-freeze response."
            play sound "audio/sfx/mychael-purr-as-a-treat.ogg" fadein 4.0 volume 0.8 loop
            show cg hug the lad 02
            with dis
            "It took a few seconds before he shifted to reciprocate,{w=.2} lightly placing his hands on the small of my back in a loose hold, fingertips splayed awkwardly along my spine."
            "He seemed to gain confidence as he wrapped his arms around me properly,{w=.2} a shaky sigh leaving his body as he relaxed."
            "A faint rhythmic rumble emitted from his chest, my eyes widening at the strange feeling."
            "Was he...{w=.2} purring?"
            "I knew I'd heard that sound before but he was definitely purring!"
            stop music fadeout 3.0
            show cg at zoom_in2
            "I didn’t have time to dwell on it for long."
            stop sound fadeout 2.0
            show hug 01 with dis
            "His grip was getting tighter."
            show hug 02 with dis
            "{i}Tighter."
            show hug 03 with dis
            play sound "audio/sfx/bed-tuckin.ogg"
            "{i}{k=5}{cps=10}Tighter."
            play sound  "audio/sfx/honk-honk.ogg"
            "I was about to sputter out a gentle protest-{w=.5}{nw}"
            hide cg
            hide hug
            show mycjackie dokidoki1 at zoom_out2
            show bg street at zoom_out2
            with dis
            "-when another car passing by made him jump and release me."
            "I had to step away to catch my breath after the squeeze."
            play music "audio/music/happy-end.ogg" fadein 2.0 loop
            "His arms dropped to his sides with a blank stare in my direction."
            m "{size=-5}O-oh..."
            "Out of the corner of my eye I could see his hands clenching tightly as if holding himself back."
            "I looked  up at him, expecting him to say something first."
            "Instead he just stared at me like I grew a third eye."
            "I quickly cleared my throat, cheeks starting to burn."
            p "Um.{w=.3} A-anyways!"
            jump cont_story_17

        "Thank him.":
            show mycjackie surprise
            with dis
            pause 1
            show mycjackie shy
            with dis
            m "You’re welcome, firefly."
            "His voice was filled with a warm, soft reverence."
            "I didn’t think much of it before, but now I was really curious."
            p "Why do you call me that?"
            show mycjackie surprise
            with dis
            m "Huh?"
            p "Firefly.{w=.2} You’ve been calling me that since we met."
            p "Why?"
            show mycjackie nervous
            with dis
            m "Oh.{w=2.} Um..."
            "He fidgeted with the strap of his satchel as if embarrassed."
            m "I guess you just... reminded me of one."
            "I snorted, folding my arms in mock offense."
            p "You're comparing me to a fly now?"
            show mycjackie amused
            with dis
            m "...beetle, actually."
            p "Still a bug!"
            show mycjackie amused2
            with dis
            "He sighed, rolling his eyes."
            m "I'm not done."
            p "Right,{w=.2} sorry."
            p "Go on."
            show mycjackie nervous
            with dis
            "He rubbed the tips of his fingers on the strap again, slowly speaking."
            m "When I first found you, I thought our time together would be short."
            m "Something that might fade as quickly as it appeared."
            show mycjackie nervous2
            with dis
            m "And if I wasn’t careful, you could slip away so easily."
            m "...Fireflies are so delicate, after all."
            show mycjackie solemn
            with dis
            m "But then...{w=.2} you stayed."
            m "And not just stayed, you...{w=.2} you {i}lit up{/i} everything around me."
            m "Something I didn't even realize I needed..."
            m "Your light was warm.{w=.2} Soft.{w=.2} Mesmerizing."
            m "...{w=.2}{i}safe."
            stop music fadeout 3.0
            show mycjackie solemnb
            with dis
            m "I... wish I could keep you in my hands forever."
            m "..."
            show mycjackie stare
            with dis
            m "{b}{size=-10}But you wouldn’t like that."
            m "{b}{k=5}..."
            m "{b}Would you?"
            "He stared at me with such intensity, I really did start to feel like a bug under a microscope."
            "My face grew warm, a shudder running up my spine."
            play music "audio/music/happy-end.ogg" fadein 2.0 loop
            p "Um!{w=.2} Wow!{w=.2} Uh!"
            p "Cool story!"
            p "A-anyways!"
            jump cont_story_17

    label cont_story_17:

    show mycjackie blush at bounce
    play sound "audio/sfx/punchy.ogg" volume 1.3
    "I gave him one last light punch to the shoulder." with hpunch
    "It felt like punching a sack of grains."
    p "I’ll see you next weekend!"
    m "A-ah..."
    hide mycjackie
    with dis
    pause 0.7
    show bg at zoom_in_street
    play sound "audio/sfx/concrete-run.ogg"
    "Ignoring the heat on my face, I looked both ways before jogging across the street."
    "My neighbor in their yard looked up as I approached, their eyes lighting up in recognition."
    v "[protag]!?"
    show vida surprise at left
    show laika happy at right
    with dis
    "Their hands fidgeted with the frisbee in their hand as they approached, their ever loyal Laika following close behind."
    show vida at bounce
    v "I was wondering where you’ve been!"
    v "I dropped by to give you some cake over the weekend but...{w=.2} b-but you weren’t home!{w=.3} A-and you didn’t answer your phone!{w=.3} And-and your packages were piling up at the door! A-and–!"
    "I held my hands up in a placating gesture."
    p "Vida!{w=.2} Vida, I’m fine!"
    show laika hop at bounce
    "At our feet, Laika was dutifully pawing at their elbow to calm them down."
    "Their mouth stopped mid-way through another sentence, blinking rapidly."
    v "Ah!"
    show vida nervous smile
    with dis
    v "Sorry..."
    show laika happy
    with dis
    "They reached down to pat Laika’s head, significantly calmer as they asked me again."
    show vida worried
    with dis
    v "Where were you?{w=.2} Where have you been?"
    p "I was... uh..."
    p "Visiting a friend.{w} For a digital detox?"
    p "Off-the-grid and all that..."
    show vida confused
    with dis
    "They blinked slowly, nodding."
    v "Oh... that sounds... {i}exciting..."
    "By the tone of their voice they didn’t mean that at all."
    show vida smile
    with dis
    v "Oh, what about [pet]?{w=.2} Did you manage to find %(pronoun4)s?"
    "My mood instantly dropped."
    p "Um.{w=.2} N-no."
    p "It’s why I went away in the first place, you could say..."
    "It took a a few seconds for Vida to understand what I meant."
    show vida realize
    with dis
    v "O-oh!"
    show vida sad
    with dis
    v "I’m sorry..."
    p "It’s fine."
    show vida realize
    with dis
    "They straightened, a flash of empathy on their face before they smiled."
    show vida nervous smile
    with dis
    v "W-well, Laika and I are around for the semester break if you need anything..."
    show vida smile
    with dis
    v "We should do a movie night!{w} Maybe that'll lift your spirits!"
    show vida happy at bounce
    v "I found this really good one I think you'd like! I did some research and I feel like it's right up your alley!"
    v "Laika and I could take a quick drive to the store so just let us know when you're up for it!{w} I could get your favorite snacks and stuff!"
    show laika at bounce
    play sound "audio/sfx/bork-bork.ogg"
    "Laika gave a happy bark at the familiar word."
    show laika happy
    with dis
    "A fond smile quirked at my lips."
    p "Thank you, Vida.{w} I’ll bring the orange soda."
    show vida smile2 at bounce
    "Their expression lit up happily."
    v "Take care!"
    hide vida
    hide laika
    with dis
    "I bid them both goodbye to walk up my driveway."
    "Once I got to my door I had an urge to turn around one last time."
    show bg forestfromhome at reset
    with dis
    "I was surprised to see Mychael still standing by the forest’s edge, shadowed by the trees."
    "Our eyes made contact, his own a fierce piercing yellow shining against the shade."
    "I gave him a big wave.{w} It took a moment, but he waved back."
    "Smiling to myself, I unlocked the front door and let myself inside."

    play sound "audio/sfx/door-shut.ogg"
    show bg home
    with dis
    "...it was surreal standing in my doorway again."
    "I felt like Alice who just woke up at the end of the book, feeling like I’d dreamed of Wonderland."
    "I tossed my keys and my backpack by the hall carelessly before plugging my phone into the charger."
    "I dreaded playing catch up with the people who might’ve tried to reach me during my absence."
    "Work.{w=.2} Family.{w=.2} Friends."
    play sound "audio/sfx/bed-tuckin.ogg"
    "I groaned aloud, flopping onto the living room couch."
    "Ah well..."
    "At least I had this weekend to look forward to."

    scene bg black
    with Dissolve (1)

    "That’s all from Day 3 of Mushroom Oasis [[DEMO]!"
    "More updates coming in the future!"
    "Tell me what you think of the game! Any support/feedback is highly appreciated!"
    "Thank you for playing! <3"

    return
