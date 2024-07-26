# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

# Easier to convert to set to use set operations
# try indexing lists
a = {starter_list[0]} # TypeError: unhashable type: 'list'
b = {starter_list[1]}
c = {starter_list[2]}

# Use union to concatenate lists
flatten = a|b|c

# Convert to list and returned flattened version
print (list(flatten))