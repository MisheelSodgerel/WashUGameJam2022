#First scene in cafe, y/n gives phone number
label Chapter01:

play music cafeMusic fadein 1.0 volume 0.15

scene cafe
with fade
show yn at center
with dissolve

"Wow, it's nice being back in my small town."
"I can’t believe graduate school is over!"
"All that studying has paid off and now I have my own place and buying my own coffee."
"This coffee shop is my favorite. I came here so often during high school."
"There’s a new face working here and I think he’s rather charismatic…"
"He always remembers my order and never spells my name wrong."
"Does he like me?..."

hide yn
show yn at left
show paul at right
with dissolve

p "Hey, y/n! How's it going at your new job? Accounting, right?"

"He's so thoughtful and considerate."

y "It's going great! How about you?"

p "Well, could be better but I can’t complain about the awesome customers that come in once in a while."

"Could he be talking about me?"
"I feel my face grow hot."

y "Haha, well I’m glad there’s something about this job you like."

p "Totally. What would you like to order?"

hide paul
hide yn
with dissolve

show yn at center
with dissolve

menu:
    "I give my order, but before I take my usual seat I: "

    "do the most impulsive thing I’ve ever done in my life.":
        jump cafeCrazy

    "wait for drink and leave.":
        jump cafeEnd

label cafeCrazy:

"I quickly grab a napkin while his back was turned. After scribbling my number on it, I placed it on the register and tried to act natural walking to my usual table."
"Wow, I’m starting off the new chapter of my life boldly!"
". . ."
"Well, at least bolder than I was before."
"I hope he texts me!"

stop music fadeout 1.0

jump Chapter02

label cafeEnd:

    stop music fadeout 1.0
    scene black
    with fade
    play music aveMaria fadein 1.0 volume .15

    n "You go back to your accounting office and never find the love of your life."
    n "As you lay on your deathbed at age 95, you wonder:"
    n "Would my life had been different if I acted out of my comfort zone and formed a deeper connection with Paul?"
    n "Unfortunately, you passed away before you could think of an answer."

    "{size=+20}{b} Coward End {/b}{/size}"
    return
