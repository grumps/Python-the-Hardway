# Lesson 31

print "You enter a dark room with two doors.  Do you go through door #1 or Door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    
    bear = raw_input("> ")

    if bear == "1":
        #adding Good Job on a new line.
        print "The bear eats your face off. \n Good job!"
    elif bear == "2":
        print "The bear eats your legs off. \n Good job!"
    else:
        print "Well, doing %s is probably better. Bears runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yeling melodies."

    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a wind of jello \n Good job!"
    else:
        print "The insanity rots your eyes nto a pool of much. \n Good Job!"
else:
    print "You stumble around and fall on a knife and die. \n Good Job!"
