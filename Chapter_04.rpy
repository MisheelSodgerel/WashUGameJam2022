#office after first timeskip, walking home, the first calm stream
label Chapter04:

    scene office
    play music officeSounds fadein 1.0 volume 0.15
    with fade

    "I can’t believe it’s been 4 months since Paul and I started dating."
    "It almost seems like a dream."
    "He’s so kind, caring, and funny…"

    play sound phoneVibrate

    "Oh!"
    "It’s almost time for his stream to start, better head home!"
    stop music fadeout 1.0
    scene streetAfternoon
    play music calmStreet fadein 1.0 volume 0.15
    with fade

    "I’m so happy he’s started streaming,"
    "He’s putting his charisma to good use and he’s built quite the following since he’s started."
    "I can only see things going uphill from here!"

    stop music fadeout 1.0
    scene homeDesk
    play music calmNight fadein 1.0 volume 0.15
    with fade

    "Nice!"
    "Arrived just in time for his stream!"

    scene black
    with fade

    p "Hey what's up you guys..."

    scene homeDesk
    with fade
    "His jokes are really landing well."
    "I guess everyone understands the struggle of being a barista, or at least working in customer service."

    y "Huh?"

    scene phone
    with fade

    "Looks like someone in the comment section isn’t too happy about his Frappuccino joke…"

    "{color=#dc143c}user2040923853: If you hate ur job so much then quit {/color}"
    "{color=#dc143c}ligma3049549: this is why i'm scared to order from coffe shops lol {/color}"
    "{color=#dc143c}peg_ridder2022: wow all baristas do is just complain about having to do their job. U guys know ur getting paid right?? {/color}"

    "Wow these comments seem to be multiplying."

    "I hope Paul isn't getting too bothered by them. He usually doesn't receive this much criticism"

    menu:
        "Should I: "
        "defend him in the comments":
            jump innocentDefense

        "stay silent":
            jump noDefense

    label innocentDefense:

        y "'hey guys, it's just a joke lol'"

        "I hope that's enough to stop the hate train from gaining momentum"

        "{color=#dc143c}peg_ridder2022: it's not 'just a joke.' imagine compaining about just having to serve coffee while some people actually have bad jobs. (1/2) {/color}"
        "{color=#dc143c}peg_ridder2022: the privilege and ignorance is shocking (2/2){/color}"
        "{color=#dc143c}user2040923853: if someone who wasn't conventionally attractive said this stuff y'all wouldn't find it so funny {/color}"
        "{color=#dc143c}candycrusherrrr: this dude gives me bad vibes {/color?\}"

        scene homeDesk
        with fade

        "Bruh."
        "The internet is crazy."
        "I'm just gonna head to bed. I have a long day of work tomorrow."
        "They're just a bunch of keyboard warriors, so I won't even bother."

        jump bedroomCalmBeforeStorm

    label noDefense:

        scene homeDesk
        with fade

        "I guess these comments will settle themselves."
        "I'm going to bed now, I have a lot of work tomorrow."

        jump bedroomCalmBeforeStorm

    label bedroomCalmBeforeStorm:

        stop music fadeout 1.0
        scene bedroom
        with fade

        "Yeesh, people can be so sensitive."
        "I quickly send an encouraging test to Paul"

        scene phone
        with fade

        y "'Don't listen to the comments from tonight. You're literally the most unproblematic person I know.'"
        y "'Just keep ignoring them and they'll probably lose interest within hours.'"

        scene bedroom
        with fade

        "Well, let's hope tomorrow will be better! I really don't need any stress additional during tax season."
        "I can't afford any distractions this week."

        jump Chapter05
