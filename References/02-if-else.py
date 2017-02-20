"""
Use if-statements to control what happens in the program (i.e., the
flow of programs). If-statements use boolean logic. They check if
something is true.
"""

# First, we create some variables.
age = 46
married = True

# Is age 46?
if age == 46:
	print("This will be printed on the screen because age equals 46.")

# Is age NOT 46?
if age != 46:
	print("This will not be printed...")
else:
	print("...but this will.")


# Is the person married?
if married:
	print("The person is married.")

if not married:
	print("The person is not married.")

# Does 1 equal 1?
if 1 == 1: 
	print("Of course, 1 always equals 1.")

# We can see if something is True by printing it:
print(age == 46)    # Is age equal to 46?
print(age != 46)    # Is age NOT equal to 46?
print(age > 46)     # Is age above 46?
print(age < 46)     # Is age below 46?
print(age <= 46)    # Is age below, or equal, to 46?
print(age >= 46)    # Is age above, or equal, to 46?

# We can also combine two logic operations with AND and OR:
print(age > 70 and age < 100)    # Is age above 70 AND below 100?
print(age > 70 or age < 100)     # Is age above 70 OR below 100?

# Don't make them to long, like this. This can become quite hard to read.
# Try to make it easier to read by adding parentheses.
if age > 20 or (age == 5 and age < 45) or age > 4 and age != 2 or (married == False and age < 2):
	print("This is true, but the code is hard to understand.")

# However, we often want to check a lot of things with one variable.
# We therefore use the elif ("else if") and else. Note that Python will
# stop at the first if-statement that comes True!
if age == 20:
	print("This will happen if age is 20.")
elif age > 5:
	print("This will happen if age is above 5.")
else:
	print("If nothing above was True, then this will always happen.")