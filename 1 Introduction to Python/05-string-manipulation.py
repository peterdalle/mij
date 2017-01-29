"""
Learn how to extract some text, replace text and find text inside a string.
"""

text = "The quick brown fox jumps over the lazy dog"

# Show the first, second and third character.
print(text[0]) # Note, it starts with 0!
print(text[1])
print(text[2])

# Show the first 0-3 characters, and 10-15 characters.
print(text[0:3])
print(text[10:15])

# Replace "fox" with "journalist".
print(text.replace("fox", "journalist"))

# Remove text from a string.
print(text.replace("The quick brown fox ", ""))

# Make text lowercase and UPPERCASE.
print(text.lower())
print(text.upper())

# How many characters long is the text?
print(len(text))

# Find the word "quick" in the text. Returns the position of the first character in the word.
print(text.find("quick"))

# What happens when we don't find the word? It will return -1.
print(text.find("journalism"))

# Lets go crazy.
text = text.replace("fox", "journalist")
text = text.replace("brown", "")
text = text.replace("dog", "editor")
text = "Alert: " + text + "!!!"
text = text.upper()
print(text)