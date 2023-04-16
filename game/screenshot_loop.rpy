transform screenshot_natsuki_turned:
    yoffset -60

transform screenshot_natsuki_fs:
    yoffset -60
    xoffset 20

transform screenshot_sayori_turned:
    yoffset -25

transform screenshot_sayori_tap:
    yoffset -40
    xoffset 40

transform screenshot_monika_lean:
    xoffset 100

transform screenshot_yuri_shy:
    xoffset 20

transform warning_image_location:
    yoffset -480

layeredimage warning_image:
    group visible:
        attribute not_vis default null
        
        attribute is_vis:
            "mod_assets/NOT DEFINED WARNING.png"

#TODO: Make transforms for Monika's "lean" pose and Sayori's "tap" pose.  They aren't centered correctly with the screenshot window as-is.  Yuri with "shy" is probably fine, and Natsuki with her "fs" face is probably fine too, but this needs to be verified.

init python:
    import string
    currently_showing = "Nothing"
    
    config.screenshot_crop = (490, 4, 300, 300) #In case you're wondering why screenshots in this build are so small and cropped...
    actually_take_a_screenshot = True
    pose_list = []
    head_list = [] #Because Natsuki.
    
    brow_list = []
    nose_list = []
    mouth_list = []
    eye_list = []
    
    #for num in range(0,10):
    #    brow_list.append("b" + str(num))
    #    nose_list.append("n" + str(num))
    #    mouth_list.append("m" + str(num))
    #    eye_list.append("e" + str(num))
    #for let in range(0,26):
    #    brow_list.append("b" + string.ascii_lowercase[let])
    #    nose_list.append("n" + string.ascii_lowercase[let])
    #    mouth_list.append("m" + string.ascii_lowercase[let])
    #    eye_list.append("e" + string.ascii_lowercase[let])
    #for num in range(0,10):
    #    for let in range(0,26):
    #        brow_list.append("b" + str(num) + string.ascii_lowercase[let])
    #        nose_list.append("n" + str(num) + string.ascii_lowercase[let])
    #        mouth_list.append("m" + str(num) + string.ascii_lowercase[let])
    #        eye_list.append("e" + str(num) + string.ascii_lowercase[let])
    #for let1 in range(0,26):
    #    for let2 in range(0,26):
    #        brow_list.append("b" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
    #        nose_list.append("n" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
    #        mouth_list.append("m" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
    #        eye_list.append("e" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
    #for num1 in range(0,10):
    #    for num2 in range(0,10):
    #        brow_list.append("b" + str(num1) + str(num2))
    #        nose_list.append("n" + str(num1) + str(num2))
    #        mouth_list.append("m" + str(num1) + str(num2))
    #        eye_list.append("e" + str(num1) + str(num2))
    mood_list_main=["neut","angr","anno","cry","curi","dist","doub","flus","happ","laug","lsur","nerv","pani","pout","sad","sedu","shoc","vang","vsur","worr","yand"]
    #The following lists are the specific *known* moods that have been defined for the characters.  Because of how the moods have been defined in the MPT, this loop can potentially create a screenshot of a mood that hasn't actually been formally defined.
    #During the loops, if a special pose that isn't on the relevant list is run into, then it'll throw up a warning image that's really obvious from an images' thumbnail.
    #As more moods/assets are acquired, these lists will fill out.
    mood_list_monika_lean=["neut","happ","anno","angr"]
    mood_list_sayori_tap=["nerv","angr","dist","neut","pout"]
    mood_list_natsuki_fs=["neut","sad","cry"]
    mood_list_yuri_shy=["neut","happ","angr","sad"]
    mood_mouth_list=["cm","om"]
    mood_eye_list=["oe","ce"]
    
    #Testing Yuri eye/eyebrow compatibility.
    yuri_brow_test_list = ["b1a","b1b","b1c","b1f"]
    yuri_eye_test_list = ["e2d","e3a","e3b"]
    
    

label screenshotter:
    scene black
    show warning_image at i11 zorder 10
    show warning_image at warning_image_location
    "This will allow you to automatically generate headshots of every selected character, cycling through the moods listed in this file (screenshot_loop.rpy).  You will need to alter the code there to list any new moods or attributes you want to show."
    "It will also show some information to make it easier to know what's displayed in the image (Or what's supposed to be displayed, anyway.)."
    menu:
        "Do you want to do a normal screenshot set, or a special screenshot set?"
        "Normal":
            pass
        "Special":
            jump screenshotter_special
    
    python:
        brow_list = []
        nose_list = []
        mouth_list = []
        eye_list = []
        
        for num in range(0,10):
            brow_list.append("b" + str(num))
            nose_list.append("n" + str(num))
            mouth_list.append("m" + str(num))
            eye_list.append("e" + str(num))
        for let in range(0,26):
            brow_list.append("b" + string.ascii_lowercase[let])
            nose_list.append("n" + string.ascii_lowercase[let])
            mouth_list.append("m" + string.ascii_lowercase[let])
            eye_list.append("e" + string.ascii_lowercase[let])
        for num in range(0,10):
            for let in range(0,26):
                brow_list.append("b" + str(num) + string.ascii_lowercase[let])
                nose_list.append("n" + str(num) + string.ascii_lowercase[let])
                mouth_list.append("m" + str(num) + string.ascii_lowercase[let])
                eye_list.append("e" + str(num) + string.ascii_lowercase[let])
        for let1 in range(0,26):
            for let2 in range(0,26):
                brow_list.append("b" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
                nose_list.append("n" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
                mouth_list.append("m" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
                eye_list.append("e" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
        for num1 in range(0,10):
            for num2 in range(0,10):
                brow_list.append("b" + str(num1) + str(num2))
                nose_list.append("n" + str(num1) + str(num2))
                mouth_list.append("m" + str(num1) + str(num2))
                eye_list.append("e" + str(num1) + str(num2))
    menu:
        "Who do you want to take pictures of?"
        "Everyone":
            $ char_list = ["sayori", "yuri", "natsuki", "monika"]
        "Just Monika":
            $ char_list = ["monika"]
        "Just Sayori":
            $ char_list = ["sayori"]
        "Just Natsuki":
            $ char_list = ["natsuki"]
        "Just Yuri":
            $ char_list = ["yuri"]
    
    menu:
        "What do you want to take screenshots of?"
        "Moods (Normal Poses)":
            
            "This will create screenshots of every mood for every selected character's face in their default poses - 'forward' for Monika, 'turned' for Sayori and Yuri, and Natsuki's forward face, 'ff'."
            "The next click will start the process; it will cycle through every selected character, so don't worry that it's quickly going through a bunch of graphics.  It's supposed to do that."
            show screen pose_caption()
            window hide
            python:
                
                for character in char_list:
                    for mood in mood_list_main:
                        for eye in mood_eye_list:
                            for mouth in mood_mouth_list:
                                if character == "monika":
                                    currently_showing = character + " forward " + mood + " " + mouth + " " + eye
                                else:
                                    currently_showing = character + " turned " + mood + " " + mouth + " " + eye
                                renpy.show(currently_showing, at_list = [i11])
                                if character == "natsuki":
                                    renpy.show(currently_showing, at_list = [screenshot_natsuki_turned])
                                elif character == "sayori":
                                    renpy.show(currently_showing, at_list =[screenshot_sayori_turned])
                                renpy.pause(0.05)
                                if actually_take_a_screenshot:
                                    renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                                renpy.hide(character)
        "Moods (Special Poses)":
            
            "This will create screenshots of every selected character in their 'special' pose - 'lean' for Monika, 'tap' for Sayori, and 'shy' for Yuri."
            "Natsuki's face isn't controlled by the pose in the same way the other characters' are, so instead it will show her moods for her alternate face, 'fs', on her normal 'turned' pose."
            "The next click will start the process; it will cycle through every selected character, so don't worry that it's quickly going through a bunch of graphics.  It's supposed to do that."
            show screen pose_caption()
            window hide
            python:
                
                for character in char_list:
                    for mood in mood_list_main:
                        for eye in mood_eye_list:
                            for mouth in mood_mouth_list:
                                if character == "monika":
                                    currently_showing = character + " lean " + mood + " " + mouth + " " + eye
                                elif character == "sayori":
                                    currently_showing = character + " tap " + mood + " " + mouth + " " + eye
                                elif character == "natsuki":
                                    currently_showing = character + " turned fs " + mood + " " + mouth + " " + eye
                                elif character == "yuri": #I'd just put an "else" statement here for her, except that'd run into a problem later if/when any other characters are added in.
                                    currently_showing = character + " shy " + mood + " " + mouth + " " + eye
                                renpy.show(currently_showing, at_list = [i11])
                                if renpy.can_show(currently_showing,character):
                                    
                                    if character == "monika":
                                        renpy.show(currently_showing, at_list =[screenshot_monika_lean])
                                    elif character == "sayori":
                                        renpy.show(currently_showing, at_list =[screenshot_sayori_tap])
                                    elif character == "natsuki":
                                        renpy.show(currently_showing, at_list = [screenshot_natsuki_fs])
                                    elif character == "sayori":
                                        renpy.show(currently_showing, at_list =[screenshot_yuri_shy])
                                    #renpy.pause(0.05)
                                    if character == "monika":
                                        if mood in mood_list_monika_lean:
                                            renpy.show("warning_image not_vis")
                                        else:
                                            renpy.show("warning_image is_vis")
                                    elif character == "sayori":
                                        if mood in mood_list_sayori_tap:
                                            renpy.show("warning_image not_vis")
                                        else:
                                            renpy.show("warning_image is_vis")
                                    elif character == "natsuki":
                                        if mood in mood_list_natsuki_fs:
                                            renpy.show("warning_image not_vis")
                                        else:
                                            renpy.show("warning_image is_vis")
                                    elif character == "yuri":
                                        if mood in mood_list_yuri_shy:
                                            renpy.show("warning_image not_vis")
                                        else:
                                            renpy.show("warning_image is_vis")
                                    renpy.pause(0.05)
                                    if actually_take_a_screenshot:
                                        renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                                        renpy.show("warning_image not_vis")
                                else:
                                    pass
                                renpy.hide(character)
        "Individual Subexpressions (Normal Poses)":
            "This will create screenshots of every selected character in their default pose, showing each individual subexpression (mouth, nose, eyes, eyebrows) with an otherwise neutral expression on their face."
            "Note that due to how she's coded and how the screenshot loop is coded, Natsuki will generate a bunch of extra images missing face components."
            "The next click will start the process; it will cycle through every selected character, so don't worry that it's quickly going through a bunch of graphics.  It's supposed to do that."
            show screen pose_caption()
            window hide
            python:
                for character in char_list:
                    for mouth in mouth_list:
                        if character == "monika":
                            currently_showing = character + " forward neut " + mouth
                        else:
                            currently_showing = character + " turned neut " + mouth
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            if character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_turned])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_turned])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)
                    for nose in nose_list:
                        if character == "monika":
                            currently_showing = character + " forward neut " + nose
                        else:
                            currently_showing = character + " turned neut " + nose
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            if character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_turned])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_turned])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)
                    for eye in eye_list:
                        if character == "monika":
                            currently_showing = character + " forward neut " + eye
                        else:
                            currently_showing = character + " turned neut " + eye
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            if character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_turned])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_turned])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)
                    for brow in brow_list:
                        if character == "monika":
                            currently_showing = character + " forward neut " + brow
                        else:
                            currently_showing = character + " turned neut " + brow
                        if brow == "b3a" or brow == "b3b":
                            currently_showing = currently_showing + " e4a"
                        elif brow == "b3c":
                            currently_showing = currently_showing + " e4b"
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            if character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_turned])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_turned])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)
        "Individual Subexpressions (Special Poses)":
            "This will create screenshots of every selected character in their 'special' poses (or face in Natsuki's case), showing each individual subexpression (mouth, nose, eyes, eyebrows) with the default expression otherwise."
            "The next click will start the process; it will cycle through every selected character, so don't worry that it's quickly going through a bunch of graphics.  It's supposed to do that."
            show screen pose_caption()
            window hide
            python:
                for character in char_list:
                    for mouth in mouth_list:
                        if character == "monika":
                            currently_showing = character + " lean happ " + mouth
                        elif character == "sayori":
                            currently_showing = character + " tap nerv " + mouth
                        elif character == "natsuki":
                            currently_showing = character + " turned fs neut " + mouth
                        elif character == "yuri":
                            currently_showing = character + " shy neut " + mouth
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            
                            if character == "monika":
                                renpy.show(currently_showing, at_list =[screenshot_monika_lean])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_tap])
                            elif character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_fs])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_yuri_shy])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)
                    for nose in nose_list:
                        if character == "monika":
                            currently_showing = character + " lean happ " + nose
                        elif character == "sayori":
                            currently_showing = character + " tap nerv " + nose
                        elif character == "natsuki":
                            currently_showing = character + " turned fs neut " + nose
                        elif character == "yuri":
                            currently_showing = character + " shy neut " + nose
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            
                            if character == "monika":
                                renpy.show(currently_showing, at_list =[screenshot_monika_lean])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_tap])
                            elif character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_fs])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_yuri_shy])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)
                    for eye in eye_list:
                        if character == "monika":
                            currently_showing = character + " lean happ " + eye
                        elif character == "sayori":
                            currently_showing = character + " tap nerv " + eye
                        elif character == "natsuki":
                            currently_showing = character + " turned fs neut " + eye
                        elif character == "yuri":
                            currently_showing = character + " shy neut " + eye
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            
                            if character == "monika":
                                renpy.show(currently_showing, at_list =[screenshot_monika_lean])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_tap])
                            elif character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_fs])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_yuri_shy])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)
                    for brow in brow_list:
                        if character == "monika":
                            currently_showing = character + " lean happ " + brow
                        elif character == "sayori":
                            currently_showing = character + " tap nerv " + brow
                        elif character == "natsuki":
                            currently_showing = character + " turned fs neut " + brow
                            if brow == "b2":
                                currently_showing = currently_showing + " e4"
                        elif character == "yuri":
                            currently_showing = character + " shy neut " + brow
                        renpy.show(currently_showing, at_list = [i11])
                        if renpy.can_show(currently_showing,character):
                            
                            if character == "monika":
                                renpy.show(currently_showing, at_list =[screenshot_monika_lean])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_sayori_tap])
                            elif character == "natsuki":
                                renpy.show(currently_showing, at_list = [screenshot_natsuki_fs])
                            elif character == "sayori":
                                renpy.show(currently_showing, at_list =[screenshot_yuri_shy])
                            renpy.pause(0.05)
                            if actually_take_a_screenshot:
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                        else:
                            pass
                        renpy.hide(character)


    "Finished generating headshots; next click will return to the test menu."
    hide screen pose_caption
    jump test_menu


label screenshotter_special:
    menu:
        "Please select a test option."
        "Yuri Eye/Eyebrow compatibility test (Select items)":
            $ char_list = ["yuri"]
            "This will screenshot all combinations of large eyes and specific eyebrows for Yuri, to see what eyebrows work with what large eyes."
            "This is a short list, intentionally looking at only a few combinations of items."
            "Next click will start the process."
            show screen pose_caption()
            window hide
            python:
                for character in char_list:
                    for eye in yuri_eye_test_list:
                        for brow in yuri_brow_test_list:
                            currently_showing = character + " turned " + eye + " " + brow
                            renpy.show(currently_showing, at_list = [i11])
                            if renpy.can_show(currently_showing,character) and actually_take_a_screenshot:
                                renpy.pause(0.05)
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                            else:
                                pass
                            renpy.hide(character)
        "Yuri Eye/Eyebrow compatibility test (All items)":
            python:
                char_list = ["yuri"]
                brow_list = []
                eye_list = []

                for num in range(0,10):
                    for let in range(0,26):
                        brow_list.append("b" + str(num) + string.ascii_lowercase[let])
                        eye_list.append("e" + str(num) + string.ascii_lowercase[let])
                for let1 in range(0,26):
                    for let2 in range(0,26):
                        eye_list.append("e" + string.ascii_lowercase[let1] + string.ascii_lowercase[let2])
            "This will screenshot all combinations of eyes and eyebrows for Yuri, to see what eyebrows work with what eyes."
            "This will test literally every possible combination of eyes and eyebrows, so it will probably take a while."
            "Next click will start the process."
            show screen pose_caption()
            window hide
            python:
                for character in char_list:
                    for eye in eye_list:
                        for brow in brow_list:
                            currently_showing = character + " turned " + eye + " " + brow
                            renpy.show(currently_showing, at_list = [i11])
                            if renpy.can_show(currently_showing,character) and actually_take_a_screenshot:
                                renpy.pause(0.05)
                                renpy.screenshot(currently_showing.replace(" ","_") + ".png")
                            else:
                                pass
                            renpy.hide(character)
        
    "Now returning to main menu."
    hide screen pose_caption
    jump test_menu


screen pose_caption():
    text store.currently_showing xalign 0.5 yalign 0.0