#Study Drills from Topic 10

formatter = "%r %r %r %r"
print formatter % (
	"I am really learning python.",
	"And am loving it real good.",
	"Python actually seems fun",
	"And easy to learn."
)

x = "Jesus had %d disciples" % 12
print "\nI said: %r." % x

print "Samuel is such an intelligent %s." % 'dude'
print "Samuel is such an intelligent %s." % 'guy'

hilarious = "Hmmmmm"
joke_evaluation = "Isn't that so interesting?! %r"
print joke_evaluation % hilarious

print """
There's something going on here.
With the three double-quotes,
we'll be able to type as much as we like.
Even $ lines if we want, or 5 or 6.
"""

Alphabets = "A\nB\nC\nD\nE\nF"
print "Alphabets from A to F:", Alphabets

tabby_cat = "\tStart every \bnew paragraph \athis way\\carriage \rreturn"
print tabby_cat