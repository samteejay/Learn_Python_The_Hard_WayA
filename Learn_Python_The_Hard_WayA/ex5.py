# More Variables and Printing
# Variable Informations about myself
my_name = 'Samuel O. Tijani'
my_age = 25 # just saying
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue' 
my_teeth = 'White'
my_hair = 'Black'


# Informations to print
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" % (
  my_age, my_height, my_weight, my_age + my_height + my_weight)

# Study Drill5
name = 'TeeJay Wealth'
age = 35 # just saying
height = 84.00 # inches
weight = 170 # lbs
eyes = 'Black' 
teeth = 'Gold'
hair = 'Blue'

# Variable Conversion from inch to cm and pounds to kg
cm = height * 2.54
kg = weight * 0.454

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d centimetres tall." % cm
print "He's %r pounds heavy." % weight
print "He's %r kg heavy." % kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
print "If I add %d, %d and %d I get %d" % (
  age, height, weight, age + height + weight)