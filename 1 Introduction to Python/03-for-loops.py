"""
For-loops let you repeat something over and over again, for example on a list.
"""

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# We can print all the weekdays manually.
print(weekdays[0]) # Note, it starts with 0!
print(weekdays[1])
print(weekdays[2])
print(weekdays[3])
print(weekdays[4])
print(weekdays[5])

# Can we automate it? Yes, with for-loop.
# Loop through all weekdays.
for day in weekdays:
	print(day)

# Loop 10 times.
for i in range(10):
	print("#" + str(i)) # Note, i will start at 0!

# Go from 25 to 100, but only every other 5.
for i in range(25, 100, 5):
	print("Step " + str(i))

# Loop through all 7 weekdays by using the index [i].
for i in range(len(weekdays)):
	print(weekdays[i])

# Also works with numbers.
for num in [562, 5127, 42, 732]:
	print(num)