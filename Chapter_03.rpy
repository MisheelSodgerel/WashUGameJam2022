#lunch date and karen encounter
label Chapter03:

play music cafeMusic fadein 1.0 volume 0.15

scene cafeDate
with fade
show yn at left
show paul at right
with dissolve

p "Yeah I totally agree with you on that!"
p "It’s nice to talk with someone with the same interests and perspectives. It’s a good change from having to interact with customers all day"
p "Don’t get me wrong, I like chatting with them most of the time, but even I get a bit tired of the occasional Karen pitching a fit."
p "But, the customers always right y’know."

y "Haha, I get that. I remember working the IT Phone line during college and having to deal with the not so friendly callers."
y "That experience really made me motivated to get a job where I didn’t have to deal with customers on a daily basis."
y "Now I’m balancing the books from 9 to 5 in my stable job. Really living the dream, ha."

p "Well you did say you’ve always wanted to be a mathmetician. Close enough"

"I laugh. This date is going great, skipping out early for lunch was really worth it."

y "Do you have any dream careers?"

p "What, you don’t think my goal in life is to serve lattes to teens during their lunch breaks?"

"Paul gives me a wink"
"I feel a little flustered"

y "Oh, ha ha, I just think there’s no way someone like you should be cooped up in a cafe."
y "You have great jokes and I honestly enjoy listening to you talk more than those popular streamers my friends keep telling me to watch."

"Paul seemed a bit flushed from my statement."

p "Since you mentioned it, I have always thought about streaming."
p "I was on the cusp of streaming gameplay in high school, but always chickened out before I could even make an account of Twitch."

"Streaming?"
"I could honestly see Paul being a streamer, and a popular streamer at that. He has the charisma, the charm, and the looks to grow a loyal audience."

y "Well I think that-"

"A shrill voice made me abruptly stop speaking."

play music battleKaren fadein 1.0 volume .15

k "Is there ANYONE working here? I’ve been waiting for ages and not a single employee has offered me help at the register."
k "In fact, nobody even greeted me when I entered the store!"
k "My time and money is valuable, I shouldn’t even have to remind anyone of that in order to get basic service."

scene cafe
show karen at center
with dissolve

"A lady was standing impatiently in front of the register and Paul’s coworker was nowhere to be seen."
"As she was looking for an audience to answer to her woes, her gaze landed on Paul who was still in uniform."

hide karen
show closerKaren
with dissolve

k "You! Why aren’t you doing your job? I need a large mocha with two pumps of chocolate syrup, oatmilk, hot but cool enough to drink, in a medium cup. Also with whipped cream and extra drizzle of caramel on top."

menu:
    "I decide to: "
    "get up and confront her":
        jump confrontKarenEnding

    "stay silent":
        jump fearKaren

label fearKaren:

"Paul shoots me an apologetic look while getting up and going to the register."

hide closerKaren
show karen at left
show paul at right
with dissolve

k "I shouldn’t have to even pay for this, given the amount of time I waited and had to force you to do YOUR BASIC JOB"

stop music fadeout 1.0
play music cafeMusic fadein 1.0 volume .15

"Paul quickly apologizes and punches in her order."
"I look down at my phone and realize my lunch break is almost over."
"I glance at Paul making the lady’s order."
"He mouths an apology and I wave it off with what I’m hoping is a reassuring smile."
"As I leave the cafe I decide to quickly shoot him a couple texts"

scene phone
with fade

y "'You should start streaming! I really enjoy your jokes and opinions, and I think others will as well.'"
y "'Maybe you’ll even make enough money from it and you’ll no longer have to deal with people like her anymore.'"

"I impulsively type out one more text"

y "'I believe in you and will support you no matter what!'"

"I felt the heat of embarrassment creep up my neck. Was that too forward?"
"I quickly send the text before I could change my mind. Wow, I’m really being bold today."
"I head back to my office, hoping I won’t arrive too late."

stop music fadeout 1.0
jump timeSkip01

label timeSkip01:

    scene black
    with fade
    "{size=+10}{b} Four Months Later {/b}{/size}"

    jump Chapter04

label confrontKarenEnding:

    hide closerKaren
    show karen at left
    show yn at right
    with dissolve

    y "Hi, Paul is actually on break and-"

    k "Are you an employee?"

    y "No, but-"

    k "Then why are you talking to me?"
    k "Stop sticking your noise where you shouldn't."

    y "Bu-"

    show karen at right
    with dissolve
    play sound slap
    with hpunch
    stop music

    scene black
    with fade
    play music aveMaria fadein 1.0 volume .15
    n "The force of the Karen's slap broke your neck."
    n "Don't underestimate Karens. Especially if they're wearing a 'Don't talk to me 'till I had my coffee' shirt."
    n "Sometimes it's good to not act boldly."
    n "Life can be confusing."
    n "You died."

    "{size=+20}{b} Karen End {/b}{/size}"
    return
