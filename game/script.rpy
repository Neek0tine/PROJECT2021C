# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define m = Character("Michael", color='#ffffff')
define c = Character("Player")


# The game starts here.

init:
    image movie = Movie(size=(1920, 1080), xalign=0.5, yalign=0.5, loop=False)
    image darken = "choice.png"

    
label start:
    $ show_quick_menu = False
    scene black
    show movie with dissolve
    play movie "./media/prologue.avi"
    pause 23
    stop movie
    hide movie
    play music "./media/prologue.mp3"
    scene office with dissolve
    $ show_quick_menu = True
    
    c "Huh.."
    c "Is this a prank?"
    c "Please don't make my bad day any worse .."
    
    show darken with dissolve
    menu first_main_branch:
        
        "What should I do?"
    
        "Leave it alone.":
            c "I'm not dealing with that."
            c "I have myself to take care of."
            c "I better leave soon."
            hide darken
            play music "./audio/timestandstill.mp3"
            show cityscape_3 with dissolve
            "And just like that, You avoided another unecessary ripple in your life."
            "Because a flat life is not something given, but something to strive for"
            "You, who wants your life to be as expected as possibble, "
            "are the kind of people who will survive even the deadliest of the doom"
            "Because when nothing is happening, you were already prepared"
            "And when something does happen, you are more than prepared"
            c "I'll get myself an expensive coffee today."
            c " ... hope you all the best, random stranger"
            
            
            $ renpy.quit()
            
        "Read More.":
            "Something"
            
        "Ask your friend for advice.":
            $ asked_friend = True
            "So it is [asked_friend]"
        
            
         



    return
