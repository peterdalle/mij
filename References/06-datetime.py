# This file prints the current date and time in many different ways.

from datetime import *     # We want to import all date and time functions from the "datetime" library.

# Print the current date.
print(datetime.now())                        # 2017-01-18 13:48:07.365920
print(datetime.today())                      # 2017-01-18 13:48:07.365920
print(datetime.today().date())               # 2017-01-18
print(datetime.today().year)                 # 2017
print(datetime.today().month)                # 1
print(datetime.today().day)                  # 18

# Print the current time.
print(datetime.today().time())               # 13:48:07.365920
print(datetime.today().hour)                 # 13
print(datetime.today().minute)               # 48
print(datetime.today().second)               # 7
print(datetime.today().microsecond)          # 365920

# Print a custom time.
print(datetime(2007, 12, 6))                              # 2007-12-06 00:00:00
print(datetime(2007, 12, 6, 16, 29, 43))                  # 2007-12-06 16:29:43

# Interpret dates written in any kind of format.
print(datetime.strptime("07-12-06", "%y-%m-%d"))          # 2007-12-06 00:00:00
print(datetime.strptime("2007 12 06", "%Y %m %d"))        # 2007-12-06 00:00:00

# Formats current date time in any way.
print(datetime.now().strftime("%Y-%m-%d %H:%M"))          # 2017-01-18 13:48