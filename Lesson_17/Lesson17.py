#Lesson 17

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#I'm not bothering with this, I don't think it would make it faster, and it makes the the program more complex.

indata = open(from_file, 'r')
input = indata.read()


print "The input file is %d bytes long" % len(input)

print "Does the output file exist %r" % exists(to_file)
print "Ready, hit 'RETURN' to continue, 'CTRL-C (^C) to abort."
raw_input()

output = open(to_file, 'w')
output.write(input)

print "Alright, all done."

output.close()
indata.close()