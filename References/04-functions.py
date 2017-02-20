"""
Functions is used to group things together, and keep things in logical places.
Functions saves time and keeps the code tidy. Then you can call the function,
and the things inside the function is executed.
"""

# This will create the function "SayHello". It does not return any value.
def SayHello():
	print("Hello!")
	print("Is it me you're looking for?")
	print("I can see it in your eyes")
	print("I can see it in your smile")
	print("You're all I've ever wanted")

# Every time we call SayHello, the content inside the function will execute.
SayHello()
SayHello()
SayHello()


# We can also pass arguments ("what") to a function.
def Say(what):
	print("What do you mean " + what + "'?!")

Say("Foo")
Say("Bar")


# We can also return a value with a function.
def Calculate(x, y):
	z = x * y        # Multiply x and y.
	return(z)        # Return the value (i.e., make it available outside the function).


# When our function Calculate(x, y) returns a value, we can set the value to a variable:
ourvalue = Calculate(5, 5)
print(ourvalue)

# But we can also omit the variable:
print(Calculate(5, 5))