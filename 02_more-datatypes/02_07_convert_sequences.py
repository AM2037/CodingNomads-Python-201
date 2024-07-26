# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

# String → tuple
tup = tuple(string)

# Verify tuple
print(tup)

# Tuple → list
ls = list(tup)
print(ls)

# c → k
ls[0] = "k"
# Verify change
print(ls)

# List → tuple and display result
print(tuple(ls))