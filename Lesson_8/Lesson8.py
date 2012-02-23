# Lesson 8 --- printing, printing!!!

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)

#Very nice... now things can bee neater. 
print formatter % (
                   "I had this thing.",
                   "That you could type up right.",
                   "But it didn't sing.",
                   "So I said goodnight."
                   )
