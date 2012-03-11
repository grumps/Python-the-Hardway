#Lesson 33

#function
def create_list(num_list, i):
    #used for the interval eq in the loop
    interval = i
    numbers = []
    print num_list
    #added the equalto 
    while i <= num_list:
        print "At the top is is %d" % i
        numbers.append(i)
        i = interval + i
        print "Numbers now: ", numbers
        print "At the bottom is %d" % i
    return numbers

#user input
print "Enter the size of the list: "
user_list_size = int(raw_input("> "))

#used for debugging:
#print "You entered %d" % user_list_size

print "Enter the interval:"
user_interval = int(raw_input("> "))

#sends to function create_list
users_list = create_list(user_list_size, user_interval)

print "The numbers: "
for num in users_list:
    print num
