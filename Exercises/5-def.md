# Exercise 5: Functions

**Goal:** Create functions that take input, change the input, and then return some new value.

Under [References](#references) you'll find help.

At the bottom you'll find [Supplementary studies](#supplementary-studies) and [Answers](#answers).

## Do this

1. Create a function named `isprogrammer`
      - the function should take an input variable named `interests`
      - the function should check if `interests` contain `programming` or `python`
      - the function should return `True` if `interests` contain these values, otherwise the function should return `False`
2. Create the variable `myinterests` as a list with five of your interests
3. Then write an if-statements that will show a message on the screen if you are a programmer, or a different message if you are not a programmer

## References

Remember

- it has to be `:` at the end of `if`, `for` and `def`
- the code after `:` bust be indented with `Tab`

### Functions

Create a function with the name `hello`:
```py
def hello():
	print("Hello World!")
```

Call the function `hello`:
```py
hello()
```

Create function that takes input variable and return a new value:
```py
def hellomessage(name, age):
	return("Hi {0}! You are {1} years old.".format(name, age))
```

Call the function and save the functions return value into a new variable:
```py
message = hellomessage("John Doe", 25)
print(message)
```

Create a function that check if age is below 18:
```py
def isunderaged(age):
	if age < 18:
		return(True)
	else:
		return(False)
```

Call the function:
```py
print(isunderaged(15))
```

## Supplementary studies

Read [Functions](https://www.learnpython.org/en/Functions).

Read also [Modules and Packages](https://www.learnpython.org/en/Modules_and_Packages) about how you use functions that other people have created (these are often called *libraries*).

## Answers

Create function:
```py
def isprogrammer(interests):
	for hobby in interests:
		if hobby == "python" or hobby == "programming":
			return(True)
	return(False)
```

Create list of interests and then call the function:
```py
myinterests = ["python", "icehockey", "monopoly", "x-games", "seal clubbing"]

if isprogrammer(myinterests):
	print("You're a programmer.")
else:
	print("You're not a programmer.")
```
