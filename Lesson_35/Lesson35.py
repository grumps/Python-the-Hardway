#Lesson 35

def gold_room():
    print "This room is full of gold.  How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much  = int(next)
    else:
        dead("Man, learn to ype a number.")
    if how_much < 50:
        print "Nice you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room():
    print """There is a bear in here.\nThe bear has bunch of honey.\nThe bear is in front of another door.\nHow are you going to move the bear?"""
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next =="taunt bear" and not bear_moved:
            print "The bear has moved from the door. YOu can go through it now."
            bear_moved = True
        elif next == "taun bear" and bear_moved:
            dead("The bear gets pissed off and ches your lef off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print """here you see the great eveil Cthulhu. \n He, it, whatevere stare at you and you go insane.\nDo you flee for you life or eat your head?"""

    next = raw_input("> ")
    
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cithulhe_room()
def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
