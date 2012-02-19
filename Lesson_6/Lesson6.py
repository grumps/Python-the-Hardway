# Lesson 6 - String and Text

#--- Variables---#

x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who %s and those %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #curious to see if this causes a syntax, or what it prints.

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e