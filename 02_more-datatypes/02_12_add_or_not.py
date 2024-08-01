# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# Initialize empty set for storing number inputs
num_ = set()

# Initialize points
points = 5

while len(num_) <= 10:
    # Prompt user for numbers
    num = input("Please enter a random number here: ")
    # Add number to set if not already in it
    if num not in num_:
        num_.add(num)
    else:
        print("This number already exists in the set.")
        # Deduct points by 1
        points -= 1
        print(points)
    # Determine losers
    if (points == 0):
        print("Uh oh, you lost!")
        break
    # Determine winners
    if (len(num_) > 10): 
        print("Congratulations, you win!")
        break
    continue

# Verify number of items in set
print(num_)