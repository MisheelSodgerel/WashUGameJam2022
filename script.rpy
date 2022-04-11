# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#dialogue
define y = Character("Y/N", color="c8c8ff", what_color="c8c8ff")
define p = Character("Paul", color="c8ffc8", what_color="c8ffc8")
define n = Character("Narrator")
define k = Character("Customer", color="FF0000", what_color="FF0000")

#backgrounds
image cafe = im.Scale("cafe.jpeg", 1280, 720)
image office = im.Scale("office.png", 1280, 720)
image phone = im.Scale("phone.jpeg", 1280, 720)
image cafeDate = im.Scale("cafetable.jpeg", 1280, 720)
image streetAfternoon = im.Scale("streetAfternoon.jpeg", 1280, 720)
image homeDesk = im.Scale("homeDesk.jpeg", 1280, 720)
image bedroomNight = im.Scale("bedroom.jpeg", 1280, 720)

#characters
image yn = im.FactorScale("yn.png", .5)
image paul = im.FactorScale("paul_fullbody.png", 1)
image karen = im.FactorScale("karen.png", .5)
image closerKaren = im.FactorScale("karenCloser.png", 1)

#audio
define audio.cafeMusic = "audio/honey.mp3" #https://soundcloud.com/samwiiise/honeyy
define audio.officeSounds = "audio/office.mp3" #https://mixkit.co/free-sound-effects/office/
define audio.battleKaren = "audio/giorno.mp3" #https://soundcloud.com/user-413530259/giorno-giovanna-theme
define audio.calmStreet = "audio/calmStreet.mp3" #https://soundcloud.com/hiroyuki_kondo/calm-street
define audio.calmNight = "audio/calmNight.mp3" #https://soundcloud.com/goliathslayer03/1-hour-of-relaxing-night-time-animal-crossing-music-mix-by-vapidbobcat
define audio.aveMaria = "audio/Schubert-ave-maria.mp3" #https://orangefreesounds.com/schubert-ave-maria/

#sound effects
define audio.phoneVibrate = "audio/phone_vibrate.mp3" #https://freesound.org/people/SmartWentCody/sounds/179012/
define audio.slap = "audio/slap.mp3" #https://www.freesoundeffects.com/free-track/slap-426860/
define audio.dayStart = "audio/fnaf-3-start-sound.mp3" #https://www.myinstants.com/instant/fnaf-3-night-start/

# The game starts here.
label start:

    jump Chapter01
