# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}
from collections import defaultdict

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

def_dict = defaultdict(list)

# First list multiple values from each dictionary for duplicate keys
for d in (dict_1, dict_2):
    [def_dict[key].append(value) for key,value in d.items()]
    # Add duplicate values
    common_keys = {key: [sum(def_dict[key])] for key in def_dict.keys()}

print(common_keys)


