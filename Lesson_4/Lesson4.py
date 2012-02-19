# Lesson 4 - Python the Hardway

#####Begin Variable Definition####################
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
###End of Variable Definition######################
###Begin Processing Data#############
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
###End Processing Data#############
###Display Processing#############
print "There are", cars, "cars available."
print "There are onl", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
###Display Processing#############
