
image rabblock normal neutral = "rabblock_normal_neutral"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene intro_space with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "A quiet morning in the Agency of The Hare as Dr.R.H Furrson is sound asleep on the couch after a long day of detective work"

    "when suddenly..."

    "BANG!"

    show rabblock_normal

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
            rabblock "The case file came in around midnight."
        "Let me guess, someone has died when it's mean't to be their big celebration?":
            "Rabblock is in utter confusion"
            rabblock "How did you know that?"
            furrson "Case file just came in around midnight"
            rabblock "Oh right I was out with Bunnie Smalls last night!"

    rabblock "Well lets take a look shall we?"

    jump Report


label Report:

    $ option_1 = False
    $ option_2 = False

    $ next_Scene = False


    scene bg room with dissolve

    menu:
        "Victim?" if option_1 == False:
            $ option_1 = True
            furrson "Mr. C.Sprinkles, only a young bun it seems."
            rabblock "Partygoer as they say, he was hosting a party to celebrate his new mansion."
            
            jump Report

        "Location?" if option_2 == False:
            $ option_2 = True
            rabblock "Ah that's right!"
            furrson "Hmmm? What?"
            rabblock "Sprinkles had recently purchased the Tooth Tree Mansion, whole town was invited"
            furrson "Where's mine then?"
            rabblock "Oh long story bout that either way I attended"
            furrson "Sighs*"
            furrson "So did you notice anythng suspicious or unusual then"
            rabblock "I have my suspisions"
            
    rabblock "Anyways is it enough information?"
    menu:
        "Yes":
            rabblock "Okay lets move"
            jump Mansion_Entrance
        "No":
            jump Report

label Mansion_Entrance:

    scene bg room with dissolve

    "The duo soon arrive to find police scattered at the door..."

    "Police question the duo, notifying their presence and make their way through to the Chief"

    rabblock "Perfect! So are you ready to help me find all the clues scattered around the Manor?"  

    menu:
        "Yes":
            rabblock "Okay lets do this!"
        
            jump Kitchen

label Kitchen:

    scene bg room with dissolve

    rabblock "Hi there! I'm Detective Rabblock Nose, and you must be Chef B-Bop, can you tell me anything about Mr. Sprinkles?"

    bBop "He was the big head of our family, hes my (__Brother__) you see. We were a happy family we grew up together in this house."
    bBop "Then one morning our brother Benny Boy found him in his (__Office__) when he was meant to be doing paper work but found him hunched over his desk when he was shot!"

    rabblock "Hmm something smells (__fishy__) in here, where were u the night of the murder?"

    bBop "You think I’m a suspect? We called you here to find whoever killed Mr. Sprinkles not investigate us! That man kept on hoping around in places he shouldn’t be!"
    bBop "No wonder he ended up getting (_killed_)! It wasn’t me though I ain’t no (__Bunny__) killer!"

    furrson "Detective… did you notice the blood on his apron?"

    jump Office

label Office:

    scene bg room with dissolve

    show rabblock_normal_neutral

    rabblock "This is supposed to be where Mr. Sprinkles was the night of the murder, let’s have a look around shall we?"

    bBun "Oh.. Hi there, sorry I didn’t greet you at the (__Door__) I was just going through some of Mr. Sprinkle's things.."

    rabblock "You must be Mr. Sprinkles (__Wife__) Bun-Bun, I don’t mean to be rude or anything but I heard you had filed some domestic abuse paperwork a few years ago… This wasn’t a self defense act was it? I hope you know you won’t be in trouble if it was?"

    bBun "Oh no! It was nothing like that! I think you met (__B-Bop_) already I’m sorry for his crazy behaviour he loved his brother very much this has been just as hard on him as it has been for us…"
    bBun "We all just want to find who murdered my husband Mr Rabblock. You must understand that this is hard on all of us"

    rabblock "Furrson.. I think I notice a (__Gun__) on top of the (__Desk__)! Keep this information between the two of us! If we grab it after Bun-Bun leaves we could dust it for (__Paw__) prints! Hurry Furrson and think of a way to make her leave!"

    furrson "Uhhh Bun-Bun, I’m sorry to tell you that B-Bop actually (__accused__) you of murdering your (__husband__), he’s still in the (__Kitchen__)..."
    furrson "he said that you smell like a fox as well… Sorry…."

    bBun "HE DID NOT!!!!!!!" 
    bBun "Oh I’ll (__show__) him!! He’s totally going to get (__kicked__) out of the (__manor__)  when it’s in my name!"

    rabblock "You did it Mr Furrson! Now let’s see here.. Theres a few (_legal_) documents and a few bloodstained ones but what really concerns me is why was Bun Bun going through all of this stuff so soon?"
    rabblock "Did she not notice the (_gun_)? I’ll start (_dusting_) it to see if we can find any clues.. It’s definately a (__Bunny__) paw! And look apparently this rabbit is left handed! We just have to see which rabbit is left handed!"
    
    furrson "Just because the rabbit is left handed doesn’t means that their the (_murderer_) Detective! Keep that in mind!"

    rabblock "You're right Furrson, we should talk to Benny Boy the one B-bop mentioned, the one who apparently found him of the (_night__) of the (__Murder__)"

    jump Mansion_Entrance2

label Mansion_Entrance2:

    scene bg room with dissolve

    rabblock "Hi there! Are you (Benny boy)? We wanted to ask you a few questions about your brother if that’s okay."

    # This ends the game.

    return