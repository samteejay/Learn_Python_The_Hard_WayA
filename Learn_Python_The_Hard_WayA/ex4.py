# Variables and Names
# Needed informations about the car
cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

# informations to print out
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Study Drill4
i = 7.0
x = 4.0
j = 5.5

print "The addition of i and x will give %s." % (i + x)
print x * j, "Is the multiplicative result of x and j"
print "The number", i % j, "is the decimal part of i divided by j."