#Lesson 5 Python the Hardway

#---Variable Define---#

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

#---End Variable Define---#

#---Extra Credit Calculations---#

bmi = (my_weight * 703) / (my_height * my_height)

#---End Extra Credit Calculations---#

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight

print "Actually that's not too heavy and has a BMI of %r." % bmi

print "He's got %s eyes and ands %s hair." % (my_eyes, my_hair)
print "His theeth are usually %s depending on the coffee." % my_teeth

#Of course this line is tricky.
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)