# Character definitions
# 'n' is narration (italic, no name shown)
define n = Character(None, what_italic=True)

# 'p' is protagonist (spoken lines with quotes)
define p = Character('You', what_prefix='"', what_suffix='"')

# Image declarations with scaling to screen size
image bg_city_afternoon = im.Scale("gui/bg_city_afternoon.jpg", config.screen_width, config.screen_height)
image bg_city_street = im.Scale("gui/bg_city_street.jpg", config.screen_width, config.screen_height)
image bg_narrow_street = im.Scale("gui/bg_narrow_street.png", config.screen_width, config.screen_height)

init python:
    # Dedicated SFX channels so we can stop/fade them independently.
    renpy.music.register_channel('walking', 'sfx', loop=True)
    renpy.music.register_channel('walking_echo', 'sfx', loop=True)
    renpy.music.register_channel('heartbeat', 'sfx', loop=True)

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

    $ renpy.music.set_volume(0.4, delay=0.0)
    play music "audio/music/City_Soundscape.wav" fadein 4.0

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
    $ renpy.music.set_volume(0.2, delay=0.2)
    play sound "audio/sfx/SunShine.wav"
    p "The sky flickers - maybe it's just the sun."
    jump scene2

label scene1_touch:
    $ renpy.music.set_volume(0.1, delay=1.0)
    play sound "audio/sfx/Heartbeat-Scene1.wav" loop
    p "Heartbeat steady... almost."
    jump scene2

###### SECOND SCENE: CITY STREET ######
label scene2:
    
    stop sound fadeout 5.0
    $ renpy.music.set_volume(0.7, delay=5.0)

    scene bg_city_street with Fade(2.0, 0.0, 2.0)
    $ renpy.sound.set_volume(0.5, delay=0.0)
    play walking "audio/sfx/Walking.wav" loop fadein 0.5 volume 0.3
    n "You start walking."
    stop walking fadeout 0.05
    play walking_echo "audio/sfx/Walking_echo.wav" loop volume 0.6
    n "Every step echoes louder than expected"

    stop walking_echo fadeout 0.5
    $ renpy.sound.set_volume(0.0, delay=0.5)
    $ renpy.music.set_volume(0.0, delay=0.5)

    play audio "audio/sfx/ChildLaugh.wav"
    n "A child laughs..."
    n "..."

    $ renpy.music.set_volume(0.6, delay=2.0)
    $ renpy.sound.set_volume(0.5, delay=0.0)
    play sound "audio/sfx/Heartbeat-Scene2.wav" loop fadein 0.5
    n "The narrow street feels familiar, yet something inside your chest begins to tighten."

    $ renpy.music.set_volume(0.4, delay=2.0)
    $ renpy.sound.set_volume(1.0, delay=2.0)
    p "Why does it sound... closer?"

    menu:

        "What do you do?"

        "Ignore it, keep walking":

            jump scene2_ignore

        "Focus on your breathing":

            jump scene2_breathe

label scene2_ignore:
    $ renpy.music.set_volume(0.7, delay=2.0)
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.8, delay=0.0, channel='heartbeat')
    play walking_echo "audio/sfx/Walking_echo.wav" loop fadein 0.5 volume 0.5
    play heartbeat "audio/sfx/Heartbeat-Scene3.wav" loop
    n "You keep walking, trying to ignore the growing discomfort."
    jump scene3

label scene2_breathe:
    $ renpy.music.set_volume(0.4, delay=2.0)
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.8, delay=0.0, channel='heartbeat')
    play sound "audio/sfx/ControlBreath.wav" fadein 0.1 volume 0.5
    play heartbeat "audio/sfx/Heartbeat-Scene3.wav" loop fadein 2.5
    n "You try to focus on your breathing, but the tightness in your chest worsens."
    jump scene3

###### THIRD SCENE: SUBTLE DISTORTION ######
label scene3:

    stop walking_echo fadeout 1.0

    $ renpy.music.set_volume(0.7, delay=2.0)
    $ renpy.music.set_volume(0.4, delay=2.0, channel='heartbeat')

    n "You pause by a shop window."
    n "Your reflection blinks half a second late."
    n "Colors seems too bright. The air wavers slightly, like heat on glass."

    $ renpy.music.set_volume(0.8, delay=2.0, channel='heartbeat')
    
    p "What's happening to me?"

    menu:
        "What do you do?"

        "Step back":

            jump scene3_help

        "Close eyes":

            jump scene3_quiet

label scene3_help:
    stop heartbeat fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=0.0, channel='heartbeat')
    play audio "audio/sfx/Stumble.wav" 
    play heartbeat "audio/sfx/Heartbeat-Scene3_help_ramp.wav" fadein 0.2 
    $ renpy.music.set_volume(0.5, delay=0.2) 
    queue heartbeat "audio/sfx/Heartbeat-Scene3_help.wav" loop
    n "You stumble, pulse accelerating."
    jump scene4

label scene3_quiet:
    stop heartbeat fadeout 2.0
    $ renpy.music.set_volume(1.0, delay=0.0, channel='heartbeat')
    play heartbeat "audio/sfx/Heartbeat-Scene3_quiet.wav" loop fadein 2.0
    $ renpy.music.set_volume(0.1, delay=2.0)
    n "The city noise dulls, replaced by the thudding in your ears."
    jump scene4

###### FOURTH SCENE: NARROW SIDE STREET ######
label scene4:
    stop music fadeout 5.0
    queue music "audio/music/Alleyway_Soundscape.wav" fadein 5.0
    $ renpy.music.set_volume(0.3, delay=0.0)
    stop heartbeat fadeout 10.0
    scene bg_narrow_street with Fade(5.0, 0.0, 5.0)
    $ renpy.sound.set_volume(0.3, delay=0.0)
    play sound "audio/sfx/Heartbeat-Scene3_help.wav" loop fadein 3.0
    n "The alley closes around you"
    $ renpy.sound.set_volume(0.5, delay=2.0)
    n "Poeple pass by, but their faces blur and stretch."
    $ renpy.sound.set_volume(0.7, delay=2.0)
    n "Street signs blur, letters melting into indecipherable shapes."
    $ renpy.music.set_volume(0.1, delay=2.0)
    $ renpy.sound.set_volume(1.0, delay=2.0)
    n "Your heartbeat drowns the world."

    p "I cant breathe... Plase stop..."
    return