# Exercise 3: if-statements

**Goal:** Control program flow with `if`,` elif` and `else`.

Under [References](#references) you'll find some help.

At the bottom you'll also find [Supplementary studies](#supplementary-studies) if you want to deepen your knowledge, as well as [Answers](#answers).

## Do this

1. Create two variables:
    - the variable `age` with your age
    - the variable `friendsage` with your best friend's age
2. Write an if-statement that compares your friend's age with your age:
    - if the ages are identical, display the message `Identical age!`
    - if the ages are different, display the message `Not identical age!`
3. Create the variable `agedifference` and calculate the difference between your age and your friend's age

## References

Remember:

- it must be `:` at the end of the line with `if`,` elif` and `else`, like so:
```py
if age == 1:
   print("Text here. Remember to indent this line.")
```
- The code that appears at the line after `:` must be indented with the `Tab` key on your keyboard

### If-statements

Check for a person's legal age:
```py
age = 16

if age >= 18:
  print ( "Legal age!")
else:
  print ("Not legal age!")
```

Check if the age is 18 or older but under 65. Then check if the age is under 18. If no criterion is met, go to else:
```py
if age >= 18 and age < 65:
  print ("You are of working age.")
elif age < 18:
  print ("You are underage.")
else:
  print ("You're ready for 'the home' as we say in Swedish for retirement home.")
```

### Comparisons

A comparison such as `age == 18` is called an *expression*. An expression always gives the result `True` or` False`. An expression may be more or less complicated by combining comparisons with `and` as well as `or`. But avoid making it all too difficult to read!

Comparison | Description | Example
---------- | -------------- | --------------------------
`==` | Is equal to | `age == 15`
`! =` | Not equal to | `age != 15`
`>` | Larger than | `age > 15`
`<` | Less than | `age < 15`
`<=` | Equal to or less than | `age <= 15`
`> =` | Equal to or greater than | `age >= 15`
`and` | Both comparisons must be true | `age > 15 and age < 45`
`or` | At least one comparison must be true | `age == 18 or age == 65`
`not` | Negates comparison | `age > 15 and not age == 50`

```py
age = 16
married = true

if age < 18 and married:
  print ("You are part of an underage marriage.")
elif age >= 18 and married:
  print ("You're married and of legal age.")
elif married:
  print ("You're married.")
elif not married:
  print ("You're not married.")
else:
  print ("We can't even define you.")
```

## Supplmentary studies

Read [Conditions](https://www.learnpython.org/en/Conditions).

## Answers

Create variables:
```py
age = 25
friendsage = 23
```

Compare variables:
```py
if age == friendsage:
  print ("Identical age!")
else:
  print ("Not identical age!")
```

Calculate age difference:
```py
agedifference = age - friendsage
agedifference = abs(ageifference)
print("Difference this year: " + str (agedifference))
```

Note:

- `abs` is a function that returns absolute numbers, which means that the minus sign is removed.
- `str` is a function that converts the number to a string (otherwise they can not be used together).
