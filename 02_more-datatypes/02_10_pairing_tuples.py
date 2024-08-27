# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

import random

list_length = random.randint(1, 20)
randlist = list()
for i in range(list_length):
    randlist.append(random.randint(1, 100))

# Sort numbers
sorted_nums = sorted(randlist)

# Use string slicing notation to group numbers into pairs and print results
tups = list(zip(sorted_nums[::2],sorted_nums[1::2]))
print(tups)

    




