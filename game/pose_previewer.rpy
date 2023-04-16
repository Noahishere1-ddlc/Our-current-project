label pose_previewer:
    image mask_3:
        "images/cg/monika/mask_3.png"
        xtile 3 subpixel True
        block:
            xoffset 1280
            linear 180 xoffset 0
            repeat
    scene black with dissolve_scene_full
    show mask_3
    stop music fadeout 2.0
    play music mend
    python:
        position = [t11]
        position_displayable = "t11"
        character = "yuri "
        posename = "Nothing"
    show screen layeredimagetool_stats()
    jump pose_loop
    return
label pose_loop:
    python:
        #textfilelist=[]
        #import os
        #imagepath = config.basedir + "\\game\\mod_assets\\character_images"
        #for file in os.listdir(imagepath):
        #    if file.endswith(".txt"):
        #        textfilelist.append(file)
        posename = renpy.input("   Enter a command - see commands.txt for details.\nValid commands: 'menu' 'restart' 'clear' 'clear_x' 'xref'")
        if posename.lower() == "menu":
            renpy.jump("test_menu")
        if posename.lower() == "restart":
           renpy.jump("pose_previewer")
        if posename.lower() == "monika" or posename.lower() == "sayori" or posename.lower() == "yuri" or posename.lower() == "natsuki":
            character = posename
            renpy.jump("pose_loop")
        if posename == "t11" or posename == "t21" or posename == "t22" or posename == "t31" or posename == "t32" or posename == "t33" or posename == "t41" or posename == "t42" or posename == "t43" or posename == "t44":
            renpy.call_in_new_context("position_parser")
            renpy.jump("pose_loop")
        if posename.lower() == "clear":
            renpy.hide("sayori")
            renpy.hide("yuri")
            renpy.hide("natsuki")
            renpy.hide("monika")
            renpy.jump("pose_loop")
        if posename.lower() == "clear_s":
            renpy.hide("sayori")
            renpy.jump("pose_loop")
        if posename.lower() == "clear_n":
            renpy.hide("natsuki")
            renpy.jump("pose_loop")
        if posename.lower() == "clear_y":
            renpy.hide("yuri")
            renpy.jump("pose_loop")
        if posename.lower() == "clear_m":
            renpy.hide("monika")
            renpy.jump("pose_loop")
        if posename.lower() == "mref":
            mref()
            renpy.jump("pose_loop")
        if posename.lower() == "sref":
            sref()
            renpy.jump("pose_loop")
        if posename.lower() == "nref":
            nref()
            renpy.jump("pose_loop")
        if posename.lower() == "yref":
            yref()
            renpy.jump("pose_loop")
        else:
            renpy.show(character + " " + posename, at_list = position, zorder = 1)
            renpy.jump("pose_loop")
        #else:
        #    found_pose = False
        #    for x in textfilelist:
        #        datafile = open(imagepath + "\\" + x)
        #        if character.strip() in x:
        #            for line in datafile:
        #                if posename in line:
        #        #    if posename in open(config.basedir + "/game/mod_assets/character_images/" + x).read():
        #        # Note: only do this if you have a lot of RAM ^
        #                    renpy.call_screen("dialog", "Pose located in " + x, ok_action=Return())
        #                    found_pose = True
        #if not found_pose:
        #    renpy.call_screen("dialog", "Pose not found!", ok_action=Return())
    jump pose_loop
    return

label position_parser:
    python:
        position_displayable = posename
        if posename == "t11":
            position = [t11]
        elif posename == "t21":
            position = [t21]
        elif posename == "t22":
            position = [t22]
        elif posename == "t31":
            position = [t31]
        elif posename == "t32":
            position = [t32]
        elif posename == "t33":
            position = [t33]
        elif posename == "t41":
            position = [t41]
        elif posename == "t42":
            position = [t42]
        elif posename == "t43":
            position = [t43]
        elif posename == "t44":
            position = [t44]
    return




















