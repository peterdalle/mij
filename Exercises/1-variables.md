# Exercise 1: Variables

**Goal:** Create, change and combine variables.

Under [References](#references) you'll find some help.

At the bottom you'll also find [Supplementary studies](#supplementary-studies) if you want to deepen your knowledge, as well as [Answers](#answers).

## Do this

1. Create three variables:
     - one variable named `age` with your age
     - one variable named `firstname` with your first name
     - one variable named `lastname` with your (you guess it) last name
2. Show the content of the variables on the screen
3. Create two new variables:
     - create the variable `name` by combining `firstname` and `lastname`
     - create the variable `initials` by your initials from `firstname` and `lastname`
4. Show the content of the new variables on the screen

## References

### Print text on screen

Write any text on the screen:
```py
print("Hello World!")
```

### Variable types

Assign a value to a variable:
```py
name = "John"      # String (text)
age = 25           # Integer (whole number)
height = 175.3     # Float (decimal number)
married = False    # Boolean (True/False)
```

### Strings

Add two strings together:
```py
nyvariabel = variabel1 + variabel2
```

Use quotation marks inside a string:
```py
nickname = 'John "The Ripper" Doe'
```

Write a string spanning multiple lines:
```py
biography = """This is my complete biography.
I will write at least
three lines and that's it.
"""
```

Get the first character from the string, then write it to screen:
```py
name = "John"
print(name[0])
```

### Lists

Create a list with strings:
```py
interests = ["python", "journalism", "write"]
```

Print the contents of the list by using the index of the list, e.g. `[0]`, `[1]`.
```py
print("Your interests are:")
print(interests[0])
print(interests[1])
print(interests[2])
```

## Supplementary studies

A dictionary contains key/value pairs. This is an effective way to create complex data structures. Note that the code below looks exactly like [JSON](https://sv.wikipedia.org/wiki/JSON).
```py
person = { 'name': "John Doe",
           'age': 25,
           'height': 175.3
         }

print(person["name"])
print(person["age"])
```

Consider printing many variables with the `.format()` method. In this case, the order of the variables - `.format(name, age, length)` - willcorrespond to an index that can be used inside the string. `{0}` is the first variable, `{1}` is the second variable, and so on:
```py
name = "John"
age = 25
height = 175.3

print("{0} is {1} years old and {2} cm long.".format(name, age, length))
```

## Answers

Create variables:
```py
age = 25
firstname = "John"
lastname = "Doe"
name = firstname + " " + lastname
initials = firstname[0] + lastname[0]
```

Print variables by writing their name (it ooly works one at the time):
```py
age
firstname
lastname
name
initials
```

Print variables with `print(variable)` (recommended method):
```py
print(age)
print(firstname)
print(lastname)
print(name)
print(initials)
```
