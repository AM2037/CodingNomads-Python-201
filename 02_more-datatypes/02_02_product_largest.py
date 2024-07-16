# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

# Use random instead of randlist to generate numbers
import random

randlist = []
for i in range(12):
    randlist.append(random.randint(0, 100))

# Print generated list of numbers
print(randlist)

# Find and print largest number
print(max(randlist))
