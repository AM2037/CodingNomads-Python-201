# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

# Prompt user for input string
input = str(input("Do you play pokemon go? Why or why not? "))

# Split input into individual words
words = input.split()
print(words)

# Convert words -> tuples with loop comprehension
tups = [tuple(word) for word in words]
print(tups)