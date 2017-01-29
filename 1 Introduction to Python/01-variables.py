"""
How to create variables of different types, such as numbers and text.
"""

# String variables.
firstname = "John"
lastname = "Doe"
name = firstname + " " + lastname

# Sometimes you want to put quotation marks in the text.
nickname = 'John "The Ripper" Doe'

# If you have a long text, you can split it on multiple lines by using three quotes.
biography = """This is my complete biography.
I will write at least
three lines and that's it.
"""

# Integers.
age = 46

# Decimal number (float).
height = 175.4

# True/False (boolean).
researcher = True
married = False

# Lets add 10 years to our age.
futureage = age + 10

# Lets put it all together.
text = "Hello " + name + "! You are " + str(age) + " years old and " + str(height) + " centimeters tall. You will be " + str(futureage) + " years in the future."

# Print the text on the screen.
print(text)

# A list of things.
interests = ["programming", "journalism", "writing"]

# Print the interests by using the index of the list:
print("You're interests:")
print(interests[0]) # Print index 0 of the list.
print(interests[1]) # Print index 1 of the list.
print(interests[2]) # Print index 2 of the list.

# Dictionaries are key-value pairs.
# Name, age, and height are keys - everything else are values.
person = { 'name': "John Doe",
			'age': 46,
			'height': 175.4
		}

print(person["name"])
print(person["age"])