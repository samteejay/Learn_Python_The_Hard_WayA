# Strings and Text
# Declarations of variables placing strings inside strings and use of formatted characters
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x 
print "I also said: '%s'." % y 

hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation % hilarious 

w = "This is the left side of..."
e = "a string with the right side."

print w + e  

# Play
a = "Take heed to yourself"
d = "all the flocks that the HolyGhost has made you an Overseer."

print "%s and %r" % (a, d)

