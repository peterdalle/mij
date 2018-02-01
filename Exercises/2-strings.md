# Exercise 2: Strings

**Goal:** Manipulate text strings.

Under [References](#references) you'll find help.

At the bottom you'll find [Supplementary studies](#supplementary-studies) and [Answers](#answers).

## Do this

1. Create the variable `text` with the content `Python is a programming language for stupid people`.
2. Replace `stupid` with `smart`. But save that in a new variable called `truth`.
3. Make the letters UPPER CASED.

## References

Remember:

- string variables start and end with `"`
- string variables over multiple lines start and end with `"""`
- string avriables can contain quotation marks, but then have to start and end with `'` instead.

### Create and read parts of string

Create string variable:
```py
text = "The quick brown fox jumps over the lazy dog"
```

Get the first character from the string:
```py
print(text[0])
```

Show the three first characters in the string (position 0-2 since Python start counting from 0):
```py
print(text[0:2])
```

How many characters long the string is:
```py
print(len(text))
```

Convert a number to a string with `str`:
```py
age = 25
print("Du är " + str(age) + " år gammal.")
```

### Manipulate string

Replace *fox* with *journalist* in a string:
```py
print(text.replace("fox", "journalist"))
```

Remove text from a string:
```py
print(text.replace("The quick brown fox ", ""))
```

Make text UPPER CASE, lower case or Title Case:
```py
print(text.lower())
print(text.upper())
print(text.title())
```

Find where the text *quick* is in the string, and return the position of the first character where it's found.
```py
print(text.find("quick"))
```

Try to find a word that doesn't exist in the string. Then -1 is returned:
```py
print(text.find("journalism"))
```

## Supplementary studies

Learn more about [Basic String Operations](https://www.learnpython.org/en/Basic_String_Operations).

## Answers

```py
text = "Python is a programming language for stupid people"
truth = text.replace("stupid", "smart")
truth = truth.upper()
print(truth)
```
