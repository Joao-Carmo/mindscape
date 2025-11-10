# Character definitions
# 'n' is narration (italic, no name shown)
define n = Character(None, what_italic=True)

# 'p' is protagonist (spoken lines with quotes)
define p = Character('You', what_prefix='"', what_suffix='"')

# Image declarations with scaling to screen size
image bg_city_afternoon = im.Scale("gui/bg_city_afternoon.jpg", config.screen_width, config.screen_height)
image bg_city_street = im.Scale("gui/bg_city_street.jpg", config.screen_width, config.screen_height)
image bg_narrow_street = im.Scale("gui/bg_narrow_street.png", config.screen_width, config.screen_height)

###### DISCLAIMER SCREEN ######
label disclaimer:
    scene black with fade

    show text "{color=#b22222}{size=80}{b}DISCLAIMER!{/b}{/size}{/color}\n\n\
    {size=34}{color=#ffffff}This game presents a stylized and exaggerated depiction of a panic attack experience. While some symptoms shown may resemble real ones, it should not be used for self-diagnosis or as a substitute for professional help.\n\n\
    If you are feeling unwell or believe you may be experiencing a panic attack, please reach out for support:\n\
    - You can contact SNS 24 at 808 24 24 24 (national health helpline).\n\
    - In an emergency, call 112.\n\
    - You can also seek help from a mental health professional or visit a local healthcare center.{/color}{/size}" \
    at truecenter
    with dissolve

    $ renpy.pause(10.0)  # duration of the disclaimer screen (you can adjust)
    scene black with fade
    return

###### FIRST SCENE: CITY STREET (LATE AFTERNOON) ######
label start:
    call disclaimer

    scene bg_city_afternoon with fade

    # simulate blinking / opening eyes
    hide black with dissolve
    pause 0.2
    show black with dissolve
    pause 0.2
    hide black with dissolve
    pause 0.2
    show black with dissolve
    pause 0.2
    hide black with dissolve

    n "You open your eyes."
    n "The world feels too bright."
    n "Warm light spills across the cobblestones, people pass by, trams rattle in the distance."
    n "For a moment, everything feels calm - air, sound, light - all perfectly normal."

    p "It's fine. Just another day."

    menu:

        "What do you do?"

        "Observe people around you":

            jump scene1_observe

        "Look up at the sky":

            jump scene1_lookup
        
        "Touch your chest":

            jump scene1_touch

label scene1_observe:
    p "They all look so calm."
    jump scene2

label scene1_lookup:
    p "The sky flickers - maybe it's just the sun."
    jump scene2

label scene1_touch:
    p "Heartbeat steady... almost."
    jump scene2

###### SECOND SCENE: CITY STREET ######
label scene2:
    scene bg_city_street with fade
    n "You start walking."
    n "Every step echoes louder than expected"
    n "A child laughs; the sounds cuts sharply."
    n "The narrow street feels familiar, yet something inside your chest begins to tighten."

    p "Why does it sound... closer?"

    menu:

        "What do you do?"

        "Ignore it, keep walking":

            jump scene2_ignore

        "Focus on your breathing":

            jump scene2_breathe

label scene2_ignore:
    n "You keep walking, trying to ignore the growing discomfort."
    jump scene3

label scene2_breathe:
    n "You try to focus on your breathing, but the tightness in your chest worsens."
    jump scene3

###### THIRD SCENE: SUBTLE DISTORTION ######
label scene3:
    n "You pause by a shopm window."
    n "Your reflection blinks half a second late."
    n "Colors seems too bright. The air wavers slightly, like heat on glass."
    
    p "What's happening to me?"

    menu:
        "What do you do?"

        "Step back":

            jump scene3_help

        "Close eyes":

            jump scene3_quiet

label scene3_help:
    n "You stumble, pulse accelerating."
    jump scene4

label scene3_quiet:
    n "The city noise dulls, replaced by the thudding in your eyes."
    jump scene4

###### FOURTH SCENE: NARROW SIDE STREET ######
label scene4:
    scene bg_narrow_street with fade
    n "The alley closes around you"
    n "Poeple pass by, but their faces blur and stretch."
    n "Street signs blur, letters melting into indecipherable shapes."
    n "Your heartbeat drowns the world."

    p "I cant breathe... Plase stop..."
    return