#Lesson 18 


#this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r," % (arg1, arg2)
    
# ok that *args is actually pointless, we can do this:
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2; %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# no arguments takes here.
def print_none():
    print "I got nutt'n."

print_two ("Resnick", "Max")
print_two_again ("Shaw", "Zed")
print_one ("First!")
print_none()

