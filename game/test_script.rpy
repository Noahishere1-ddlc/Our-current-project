#This file is here specifically for the "test" command in the main pose testing loop.
#Replace this with whatever you'd like if you want to test something out without having to specifically exit out of the tool.

label test_menu:
    
    hide screen layeredimagetool_stats
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    
    menu:
        "Pose Previewer":
            jump pose_previewer
        "Looping black background":
            jump black_background_loop
        "Mood Headshot Generator":
            jump screenshotter
        "See an example script play out!":
            jump example_layeredimage_script
        "Test your script!":
            jump test_poses
    
    jump test_menu_borked

label test_menu_borked:
    #in case a menu fucks up:
    "Something done got borked, returning to the main test menu"
    jump test_menu



#Intentionally looping menu.
default bbl_monika = False
default bbl_sayori = False
default bbl_natsuki = False
default bbl_yuri = False
default test_poses_is_looping = False



label black_background_loop:
    scene black
    "This is an intentional looping black background.  To restart, you'll have to quit out to the main menu or restart the game."
    "Every advance of the screen will cycle through any on-screen characters' opened and closed mouths and eyes for their current mood."
    "This is here as a quick way to check whether a mood you've defined works properly or not.  You'll need to use the developer console (Press 'shift+o' on windows) to change characters' moods for the loop."
    
    label black_background_loop_2:
        
        if not test_poses_is_looping:
            menu:
                "Who do you want to show on screen?" #Later on, implement the natsuki dad sprite.
                "Monika":
                    $bbl_monika = True
                    show monika forward at t11
                "Sayori":
                    $bbl_sayori = True
                    show sayori turned at t11
                "Natsuki":
                    $bbl_natsuki = True
                    show natsuki turned at t11
                "Yuri":
                    $bbl_yuri = True
                    show yuri turned at t11
                "2 characters":
                    menu:
                        "Which two characters do you want to show on screen?"
                        "Monika and Sayori":
                            $bbl_monika = True
                            show monika forward at t21
                            $bbl_sayori = True
                            show sayori turned at t22
                        "Monika and Natsuki":
                            $bbl_monika = True
                            show monika forward at t21
                            $bbl_natsuki = True
                            show natsuki turned at t22
                        "Monika and Yuri":
                            $bbl_monika = True
                            show monika forward at t21
                            $bbl_yuri = True
                            show yuri turned at t22
                        "Sayori and Natsuki":
                            $bbl_sayori = True
                            show sayori turned at t21
                            $bbl_natsuki = True
                            show natsuki turned at t22
                        "Sayori and Yuri":
                            $bbl_sayori = True
                            show sayori turned at t21
                            $bbl_yuri = True
                            show yuri turned at t22
                        "Natsuki and Yuri":
                            $bbl_natsuki = True
                            show natsuki turned at t21
                            $bbl_yuri = True
                            show yuri turned at t22
                        
                        
                "3 characters":
                    menu:
                        "Which 3 characters do you want to show on screen?"
                        "Monika, Sayori, and Natsuki":
                            $bbl_monika = True
                            show monika forward at t31
                            $bbl_sayori = True
                            show sayori turned at t32
                            $bbl_natsuki = True
                            show natsuki turned at t33
                        "Monika, Sayori, and Yuri":
                            $bbl_monika = True
                            show monika forward at t31
                            $bbl_sayori = True
                            show sayori turned at t32
                            $bbl_yuri = True
                            show yuri turned at t33
                        "Monika, Natsuki, and Yuri":
                            $bbl_monika = True
                            show monika forward at t31
                            $bbl_natsuki = True
                            show natsuki turned at t32
                            $bbl_yuri = True
                            show yuri turned at t33
                        "Sayori, Natsuki, and Yuri":
                            $bbl_sayori = True
                            show sayori turned at t31
                            $bbl_natsuki = True
                            show natsuki turned at t32
                            $bbl_yuri = True
                            show yuri turned at t33
                "4 characters":
                    "Here are all 4 girls."
                    $bbl_monika = True
                    show monika forward at t41
                    $bbl_sayori = True
                    show sayori turned at t42
                    $bbl_natsuki = True
                    show natsuki turned at t43
                    $bbl_yuri = True
                    show yuri turned at t44
            $ test_poses_is_looping = True
        else:
            pass
        window hide
        $config.allow_skipping = False
        pause
        
        
        if bbl_monika:
            show monika om
        if bbl_sayori:
            show sayori om
        if bbl_natsuki:
            show natsuki om
        if bbl_yuri:
            show yuri om
        
        
        window hide
        pause
        
        
        if bbl_monika:
            show monika cm ce
        if bbl_sayori:
            show sayori cm ce
        if bbl_natsuki:
            show natsuki cm ce
        if bbl_yuri:
            show yuri cm ce
            
            
        window hide
        pause
            
            
        if bbl_monika:
            show monika om
        if bbl_sayori:
            show sayori om
        if bbl_natsuki:
            show natsuki om
        if bbl_yuri:
            show yuri om
            
            
        window hide
        pause
            
            
        if bbl_monika:
            show monika oe cm
        if bbl_sayori:
            show sayori oe cm
        if bbl_natsuki:
            show natsuki oe cm
        if bbl_yuri:
            show yuri oe cm
        
        
        
        jump black_background_loop_2



