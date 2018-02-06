# Exercise 4: for-loops

**Goal:** Use for-loops to control how lists are presented on the screen.

Under [References](#references) you'll find help.

At the bottom you'll find [Supplementary studies](#supplementary-studies) and [Answers](#answers).

## Do this

1. Create the list variable `interests` with five of your interests
2. Write a for-loop that writes each one of your interests on the screen
3. Write an if-statement inside the for-loop that checks if one of your interest is `python` or `programming`

## References

Remember:

- it has to be `:` at the end of `for`
- the code after `:` bust be indented with `Tab`

### Lists

Create a list with numbers or strings:
```py
numbers = [1, 2, 3]
interests = ["python", "knyppling", "monopol"]
```

### For

Go through row by row (`i` is varaible that is created automatically, you can call it whatever you want):
```py
for i in numbers:
	print(i)
```

Get the first and second row from the list by index (note that Python start counting at 0):
```py
print(interests[0]) # First index
print(interests[1]) # Second index
```

We can also get values from the list by putting the index directly into the for-loop. But first, we need to know how long the list is with `len()`:
```py
num_interests = len(interests)

for i in range(num_interests):
	print(interests[i])
```

## Supplementary studies

If you mix lower case and UPPER CASE text if-stataments will not work since `"TEST" == "test"` is False.

But if you put `.lower()` on all varaibles everything is lower cased and `"test" == "test"` is then True.
```py
interests = ["PYTHON", "ICEHOCKEY", "MONOPOLY"]

for hobby in interets:
	if hobby.lower() == "python":
		print("Yay! You like Python!")
	else:
		print("You really HATE Python, don't you?")
```

Read [List Comprehension](https://www.learnpython.org/en/List_Comprehensions).

## Answers

Create variables:
```py
interests = ["python", "icehockey", "monopoly", "x-games", "clubbing seals"]
```

Go through list of and look for "python" or "programming":
```py
for hobby in interests:
	if hobby == "python" or hobby == "programming":
		print("Yay! You're a code nerd!")
	else:
		print("Why do you HATE code nerds?!")
```
