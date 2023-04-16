#This file's specifically here to give you an example script, showing the MPT poses and tags in action.

label example_layeredimage_script:
    
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    
    
    #This first section intentionally throws all 4 girls on screen at the start, and has them emoting and interacting with each other.
    #There's definitely a lot going on here, but keep in mind...even if you're still fresh to using this tool, it should be *much easier* to understand what characters are doing just glancing at the code, even before you run the script.
    
    
    "It's kind of an unusual day today..."
    #We start by showing everyone on screen, so we have to establish that they're using a pose when they're first brought on-screen.  Monika uses "forward", and everyone else uses "turned".  We're also going to show them all in their casual outfits because...why not?
    show monika forward casual dist at t41
    show sayori turned casual lsur at t44
    show yuri turned casual sad rup lup at t43
    show natsuki turned casual anno at t42
    "I'm about to meet up with everyone else from the Literature Club to walk to school together like I usually do."
    "But...something seems off.  Normally they'd happily greet me and we'd be on our way...but...they look kind of...upset?"
    #Everyone's moods just changed, but all the defaults are still in place - including all the autotags, so their mouths remain "closed", their eyes remain "open", and their brows change to the relevant graphic.
    #Yuri's arms are still up after this change; remember that mood doesn't affect arms for anyone.
    show monika neut
    show natsuki neut
    show sayori happ
    show yuri neut
    "As I approach them, their faces - particularly Sayori's - soften a bit as they recognize me."
    mc "Hey guys!  Is...something up?"
    #We now start doing a bit more:
    #Both Monika and Sayori change mood again, and get the "awkward sweat drop" graphic on their faces.
    #Natsuki changes her pose to "cross" - so she's now got her crossed arms.
    #Yuri has the most - she changes mood, drops both her arms back down, and switches from the default eye tag of "oe" - an autotag that changes on mood - to the other autotag for eyes, "ce".  Now she's showing the closed eyes for this mood.
    show monika worr awkw
    show natsuki cross flus
    show sayori nerv awkw
    show yuri sad ce rdown ldown
    mc "You don't seem as...energetic as usual."
    mc "Is...everything okay...?"
    #Sayori starts to talk, so of course we open her mouth with "om".
    show sayori om rup at f44 zorder 2
    s "Y-yeah~...of course everything's okay, [player]~..."
    show natsuki angr blus
    s e1a "Why wouldn't it be...?"
    #We refresh Sayori's character for this next line.
    $sref()
    #At this point, immediately *after* the sref() call, Sayori is currently defaulted to every default there can be for her turned pose.  This means she's currently showing the same as if you'd introduced her new to the screen, meaning she's showing on-screen as if you just wrote out:
    #show sayori turned ldown rdown neut cm oe brow nobl
    #The very next line, however, gives her attribute tags again, so the player effectively goes from seeing the pose she had right *before* the refresh line to the pose on the very next line, without seeing the in-between graphics.
    #You never have to use the sref() (or any of the functions for other characters) if you don't want to, but it is nice to have a relatively short phrase to type that can reset a character if you just want to start from scratch.
    show sayori lsur casual awkw at t44 zorder 1
    show natsuki turned om ce at hf42
    show yuri shoc om awkw rup lup
    show monika lsur awkw
    n "Oh, you're {i}seriously{/i} going to try and hide this from [player] too!?"
    #The exact same thing as we just did with refreshing Sayori happens again - this time for 3 characters: Sayori, Monika, and Yuri.
    $mref()
    $yref()
    $sref()
    show monika casual dist awkw
    show sayori casual flus awkw rup lup om
    show yuri casual anno awkw
    n cross oe "I can't believe you right now...why do we even hang out with your stupid a-"
    show natsuki vsur awkw at t42 zorder 1
    show yuri om vang -rup -lup at f43 zorder 2
    show sayori vsur cm
    show monika vsur
    y "Natsuki!  Calm yourself!"
    $nref()
    show natsuki casual sad ce cm awkw
    y angr ce rup "I am similarly distressed by Sayori's behavior, but that is no reason to be so nasty to her!"
    y oe rdown "I'm certain that if we listen to her, she will be able to explain herself..."
    #Now we switch back to Natsuki's "turned" pose.
    show monika worr
    show natsuki turned oe rhip
    show sayori dist
    y nerv om awkw rup lup "...I...I-I...apologize for shouting, Natsuki..."
    show yuri ce cm at t43 zorder 1
    show natsuki om at f42 zorder 2
    n "No...it's okay...you're right, Yuri..."
    n ce rdown "I'm...just upset.  I'm sorry for losing my cool like that..."
    show natsuki cm at t42 zorder 1
    show yuri oe
    #Take note - instead of using an autotag for Monika's eyes, we're using a specific eye tag - "e1b".  We'll come back to this in a bit.
    show monika neut awkw e1b lpoint at t41 zorder 2
    "Before I think to say anything else, I notice Monika trying to quietly get my attention...as she motions off to the side."
    #Now that we've done a lot with a whole screen of characters, lets switch gears for a bit - now we're going to talk to a single character for a bit, and see how much quicker and easier it is to engage in a conversation with them, constantly talking back and forth with them.
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    show sayori at thide
    hide sayori
    show monika ldown at t11
    "We walk a few feet away from the rest of the group, the light din of their conversation still audible in the background as Monika and I start to whisper to each other."
    mc "Okay, so...what's going on?  What happened...?"
    #Monika's going to change mood a few times here, so all the autotags will update...but remember, she currently has a specific tag for her eyes, "e1b".  As a result, her eyes will NOT update with her mood changing.
    #They'll stay that same graphic until we give her a different tag - either a different specific tag, one of the eye autotags, or we refresh her with the command (Which effectively resets them back to the autotag "oe")
    m angr om rhip "Sayori might have...ruined our club meeting for today."
    show monika cm
    mc "What...?  How!?"
    m anno om "Okay...do you remember the end of the club meeting yesterday...?"
    m lpoint "And what Sayori asked to do at the end of it...?"
    #We're now going to return Monika's eyes to the "oe" tag, so that they start matching up with her mood again.
    #Remember, there's multiple ways to do this, such as just removing the tag entirely with "-e1b" - and we'll do the same with her arm:
    show monika cm -e1b -lpoint
    mc "Uhhh...let me think..."
    show monika b1d
    "Monika starts to tap her foot, as I struggle to think about what she might be getting at..."
    m om "You...need some help there, [player]...?"
    show monika cm
    mc "Look, I'm sorry I'm having difficulty remembering...I definitely remember that I was a bit, y'know, {i}distracted{/i} at the end there..."
    show monika flus brow rdown nobl
    mc "{i}You{/i} remember what was going on right at the end there, don't you...?"
    show monika happ awkw
    "A smile starts to creep across Monika's face, but in a way that it seems like she's struggling to hold her composure."
    m laug ce blus rhip "{i}Pffft...{/i}"
    "Her face loses the battle as she openly grins, desperately trying to contain her laughter."
    show monika e2c rdown
    "Fortunately for us, it looks like none of the other girls take notice."
    m happ om ce "I'm...so sorry...it's just that..."
    show monika cm e1b awkw
    mc "Yeah, yeah, I know...I'm sure I'll laugh about it later too..."
    mc "I just wish that Yuri didn't confuse me with Natsuki...I know she's pretty tall, but I'm not {i}that{/i} short!"
    m om lpoint blus oe "I know!  I saw the look of confusion on your face when she suddenly hugged you super-tight and said 'I love you...'"
    m laug cm "{i}Pfffft...{/i}"
    m om ce ldown "...And...and...how shocked Natsuki was, seeing you two like that!"
    m rhip oe "...And...heheh...and how {i}mad{/i} she was a second later...!"
    #Natsuri FTW.
    show monika cm
    "Monika starts to lose the battle not to laugh again..."
    show monika ce
    "At this rate, I need to stop her before she gets the other club member's attentions...!"
    $mref()
    show monika casual vsur awkw
    mc "Okay, yeah, seriously - calm down!  They're gonna hear."
    show monika worr
    mc "Plus, Natsuki punched me so hard that I think I might have a bone bruise now..."
    m om "You're right...I'm sorry..."
    show monika cm rhip
    mc "It's okay...at least it didn't take too long for everyone to realize it was an accident..."
    $mref()
    show monika casual rhip
    mc "...But my {i}point{/i} is that I wasn't paying attention to what you and Sayori were doing at the time because of it!"
    m om "Yeah, that's a good point."
    m lpoint "Right...so, it was Sayori's turn to borrow the game's console last night, right?"
    show monika cm
    mc "..."
    show monika anno
    mc "...I already don't like where this is going."
    m om e1b ldown rdown "...Yeah, you're really not going to like it."
    show monika cm oe
    mc "Alright...what exactly did she do...?"
    m om ce "See for yourself...did you look at the school yet?"
    show monika oe cm
    mc "What...?  What's wrong with-"
    "I quickly turn my head to glance over to where the school building is as I say this...and the words catch in my mouth as I look at the school."
    "Or...rather, where there is now {i}a completely empty lot where our school used to be.{/i}"
    mc "..."
    show monika angr ce rhip
    mc "Wha...where...ummm!?"
    show monika oe lpoint
    "Monika just silently points into the sky above us."
    mc "..."
    mc "...Okay, that's a really dumb mistake to make, I realize, but it's not {i}that{/i} hard to just reset the school's Z value to zero, is it?"
    m vang om "{i}It is when she left the console IN THE SCHOOL TOO!{/i}"
    show monika cm
    mc "{i}What!?  Are you kidding me!{/i}"
    mc "How...how are we supposed to fix {i}that!?{/i}"
    m ce om ldown rdown "I don't know yet either!  Just...{i}aaargh!{/i}"
    m angr oe "This is probably going to require someone to code in a new one or something, just to get the good one back..."
    show monika cm
    mc "Why'd she even do that, anyway...?"
    m curi om rhip "Well, to her credit...she {i}was{/i} just trying to make the walk to the school quicker by moving it {i}to{/i} us, here..."
    show monika cm
    mc "...Oh, you're right!  It's directly above us, isn't it?"
    show monika sad awkw
    mc "Well...I guess she was at least trying to be...helpful...?"
    m anno om rdown lpoint "I guess so...but I'm still annoyed."
    m angr ce "This is exactly the sort of thing I was afraid of when we first agreed to share the console in the first place!"
    show monika anno oe cm
    mc "Yeah, but we knew that going in, and still agreed to do it anyway, right...?"
    show monika neut nobl
    mc "I guess...try not to be so hard on her?  She had good intentions...I know she didn't do it on purpose..."
    m om rhip "Yeah...I suppose you're right.  This isn't the end of the world or anything..."
    m happ awkw lpoint ce "...I guess we could try and view this as a learning opportunity, since now we need to make our own console to get the old one back!"
    show monika nobl oe cm ldown
    mc "That's a great idea!"
    mc "..."
    show monika curi
    mc "Actually...that makes me wonder..."
    m om "What's on your mind?"
    show monika cm
    mc "Well...I'm wondering if we could try and put in some new features when we make the new console...?"
    m lean casual happ om "Ooooh...?"
    m blus "What did you have in mind, [player]...?"
    show monika cm
    mc "...Ahhh..."
    show monika neut blaw
    mc "I just..."
    show monika anno
    mc "...I was just thinking about, like...making it bigger or something..."
    m bful om "Oh.  I see..."
    m cm "..."
    show monika blaw neut
    mc "Well...we could...talk about some more features when we're working on it...right...?"
    m nobl om "Yeah, I suppose so..."
    $mref()
    show monika forward casual doub blaw
    mc "Okay, should we go tell the other club members?"
    show monika worr awkw rhip
    mc "...Y'know, before they get riled up at Sayori again...?"
    m neut nobl rdown om "Yeah...let's go do that."
    
    
    
    jump test_menu

















