# Some useful functions to write and read text files.

# Function to save text to a file.
def SaveToFile(filename, text):
	f = open(filename, mode="w")  # Open file for writing (w).
	f.write(text)
	f.close()


# Function to add text at the end of a text file.
def AppendToTextFile(filename, text):
	f = open(filename, mode="a")  # Open file for appending (a).
	f.write(text)
	f.close()


# Function to read all text in a file.
def ReadTextFile(filename):
	f = open(filename, mode="r")  # Open file for reading (r).
	text = f.read()
	f.close()
	return(text)


# Use them like this:
SaveToFile("file.txt", "My text to save.")

AppendToFile("file.txt", "Add this to the end of the existing file.")

text = ReadTextFile("file.txt")
print(text)