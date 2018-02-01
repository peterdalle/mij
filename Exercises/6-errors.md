# Exercise 6: Error handling

**Goal:** Understand some common error messages, and how to solve them.

Under [References](#references) you'll find some help.

At the bottom you'll also find [Supplementary studies](#supplementary-studies) if you want to deepen your knowledge, as well as [Answers](#answers).

## Do this

Run this code lines and think about (a) why this errors occurs and (b) how to solve it.

1. 
      ```py
      name = "John Doe"
      print(Name)
      ```
2. 
      ```py
      Print("John Doe")
      ```
3. 
      ```py
      for workday in ["Monday", "Tuseday", "Wednesday", "Thursday", "Friday"]
          print(workday)
      ```
4. 
      ```py
      age = 25
      print("You are " + age + " years old.")
      ```
5. 
      ```py
      interests = ["Python", "Jupyter Notebooks", "pip"]
      print(interests[3])
      ```      

## References

Remember:

- it has to be `:` at the end of `if`, `for` and `def`
- the code after `:` bust be indented with `Tab`
- Python make a difference between lower case and UPPER CASE
- Python start counting at 0

### Types of errors

![](/Exercises/my-code-isnt-working.png)

## Supplmentary studies

Read more about how you can catch and deal with errors in your code with [Exception Handling](https://www.learnpython.org/en/Exception_Handling).

## Answers

1.  `NameError: name 'Name' is not defined`. Lower case and UPPER CASE is different in Python. Write `name` instead of `Name`:
      ```py
      name = "John Doe"
      print(name)
      ```
2. `NameError: name 'Print' is not defined`. Write `print` instead of `Print`:
      ```py
      print("John Doe")
      ```
3. `SyntaxError: invalid syntax` occurs because of a missing `:` at the end of `for`:
      ```py
     for workday in ["Monday", "Tuseday", "Wednesday", "Thursday", "Friday"]:
          print(workday)
      ```
4. `TypeError: Can't convert 'int' object to str implicitly` means that the variable `age` is an integer and cannot be mixed with strings. It has to be converted to a string with `str()`:
      ```py
      age = 25
      print("You are " + str(age) + " years old.")
      ```
5. `IndexError: list index out of range`. Remember that Python starts counting from 0? That means that if you try to get an index outside the bounds of the list (index `[3]` in this case), you get `IndexError`. Change to 2 instead:
      ```py
      interests = ["Python", "Jupyter Notebooks", "pip"]
      print(interests[2])
      ```    
