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

    "A quiet morning in the Agency of The Hare as Dr.R.H Furrson is sound asleep on the couch after a long day of detective work"

    "when suddenly..."

    "BANG!"

    rabblock "FURRSON WAKE UP!"

    "Furrson falls off the couch, with a frightened look"

    furrson "uhhhhgh"

    menu:
        "What is it Rabblock?":
            rabblock "Why were you sleeping to begin with?!"
            furrson "Because unlike you I don't spend my carrots all day looking at the smallest hare on my paws!"
            rabblock "I do question most days why u bother coming along with me?"
        "Ugh... what happened?":
            rabblock "You were asleep, so when I came ru-"
            furrson "I know!, its an expression fool!"
            rabblock "foolish questions get foolish answers."

    rabblock "Anyways, have you seen our mail?"
    furrson "hmm? What is it now? We always get mail."
    rabblock "No, no, Not just some ordinary mail."
    rabblock "We've been invited to a party!"
    
    menu:
        "Hmm? A party?, well at least it it gives me a brea-":
            rabblock "To Die for!"
            furrson "I rest my tail"
            rabblock "The case file came in around midnight lets take a look."
        "Let me guess, someone has died when it's mean't to be their big celebration?":
            "Rabblock is in utter confusion"
            rabblock "how did you know that?"
            furrson "case file just came in around midnight"
            rabblock "oh right I was out with Bunnie Smalls last night!"
    

    # This ends the game.

    return
