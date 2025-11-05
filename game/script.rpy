# Character definitions
# 'n' is narration (italic, no name shown)
define n = Character(None, what_italic=True)

# 'p' is protagonist (spoken lines with quotes)
define p = Character('You', what_prefix='"', what_suffix='"')

# Image declarations with scaling to screen size
image bg_city_afternoon = im.Scale("gui/bg_city_afternoon.jpg", config.screen_width, config.screen_height)
image bg_city_street = im.Scale("gui/bg_city_street.jpg", config.screen_width, config.screen_height)

label start:
    scene bg_city_afternoon with fade

    # simulate blinking / opening eyes
    show black with dissolve
    pause 0.5
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

    # menu:
    #     "What do you do?":
    #         "Observe people":
    #             jump scene1_observe
    #         "Look up":
    #             jump scene1_lookup
    #         "Touch chest":
    #             jump scene1_touch

label scene1_observe:
    p "They all look so calm."
    jump scene2

label scene1_lookup:
    p "The sky flickers - maybe it's just the sun."
    jump scene2

label scene1_touch:
    p "Heartbeat steady... almost."
    jump scene2

label scene2:
    scene bg_city_street with fade
    n "You start walking."
    n "Every step echoes louder than expected..."
    return