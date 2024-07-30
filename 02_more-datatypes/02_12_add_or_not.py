# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# Initialize empty set of number entries
num_ = set()

# Initialize duplicate number count
points = 5

# Set rules for adding user's number inputs to the set or not
while True:
    # Prompt user for number
    num = input("Please enter number here: ")

    # Rules for adding numbers to set
    # if (num not in num_) and (points!=0): # Refactoring this line to see if it fixes 
    # the only stopping after 0 points instead of winning
    if (num not in num_):
        # Syntax similar to append: set.add(elem)
        # try except to catch errors aka can't be converted
        try:
            int(num)
        except TypeError:
            print(f"{num} could not be converted to int.")
            break
        # Continue loop if num can be converted to int
        num_.add(num)
    else:
        # Prevent duplicate entries
        print("This number already exists in the set.")
        # Deduct points by 1
        points -= 1
    # Continue loop until 5 points have been deducted
    continue

# TODO: Moving this section (lines 42-49) out from earlier loop broke winning/losing altogether -- FIX
# Determine losers
if (points == 0):
    print("Uh oh, you lost!")

# Determine winners
if (len(num_) > 10): 
    print("Congratulations, the set is larger than 10 numbers so you WIN!")

# Verify number of items in set
print(num_)