# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define furrson = Character("Furrson")
define rabblock = Character("Rabblock")


image rabblock normal neutral = "rabblock_normal_neutral"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show rabblock_normal_neutral 

    # These display lines of dialogue.

    rabblock "Welcome to the Treehouse Manor Mr R.H. Furrson! Today we are here to solve the murder of young Mr. Sprinkles Now I hope you understand how this works right? Basically we complete each others"
    menu:
        "Sentences?":
            rabblock "Perfect!" 
    
    # So are you ready to help me find all the clues scattered around the Manor? (__yes__)? Okay let’s do this!”

    # Detective Rabblock Nose:
    # “Perfect! Now lets head into (__Stairs__) and see what we can find!”


    # This ends the game.

    return
