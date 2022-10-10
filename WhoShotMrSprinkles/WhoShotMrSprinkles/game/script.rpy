
$ renpy.input()

label start:

    scene bg room with dissolve

    
    show rabblock normal neutral with dissolve

    rabblock "Welcome to the Treehouse Manor Mr R.H. Furrson! Today we are here to solve the murder of young Mr. Sprinkles 
              Now I hope you understand how this works right? Basically we complete each others"
    menu:
        "Sentences?":
            rabblock "Perfect!"
        "Thoughts?":
            rabblock "Not Quite Furrson"
    
    rabblock "So you are to help me find so the clues scattered around the Manor?"
        
    rabblock "Our first stop should be the kitchen since there's been someone wishing to talk with us"

    jump kitchen


label kitchen:

    # (___) = Answer to input
    scene bg room with dissolve

    show rabblock normal neutral with dissolve 

    rabblock "You must be Chef B-Bop I'm Detective Rabblock Nose, this is my assistant Dr. Furrson"

    b_Bop "Owwh yoo twooth, yeeah i've 'eard bout youse. What youse want wit mae?"
    
    jump b_Bop_Questions_1
    

label b_Bop_Questions_1:

    default mS_Relation = False

    menu:
      "Mr Sprinkles Relationship" if mS_Relation == False:

        $ mS_Relation = True

        b_Bop "Mr Spinkles? oww yeeh that bloke! He was the ol' big head of the family, hes my (__2nd cousin__) you see. Paid well when I got me job over 'ere
        One morning tho, lil chump Bunny Boy found him in his (__Office__) when he was meant to be cookin 'upper! found him slumped loike mash powtaetoes!"

        furrson "Hmm, interesting"

    jump b_Bop_Questions_1
    
    # This ends the game.

    return
