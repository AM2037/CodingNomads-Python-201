# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

keys_dict = {}

# Define dictionary keys & values
for key in range(1,11):
    v = key * key
    keys_dict[key] = v

# Print resulting dictionary
print(keys_dict)
