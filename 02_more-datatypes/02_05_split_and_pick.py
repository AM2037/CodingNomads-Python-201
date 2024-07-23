# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

from collections import Counter

message = input("What's your favorite movie and why? ")

# Split message into individual words
words = message.split()
print(words)

# Get frequency of each word
Counter = Counter(words)

# Passing 1 to get single most frequent word (could also pass another number here)
# as well as times the word was used
most_freq = Counter.most_common(1)
print(most_freq)
