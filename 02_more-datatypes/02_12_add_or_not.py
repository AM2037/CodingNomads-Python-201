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

while True:
    # Prompt user for number
    num = input("Please enter number here: ")

    # Rules for adding numbers to set
    if (num not in num_) and (points!=0):
        # Syntax similar to append: set.add(elem)
        # try except to catch errors aka can't be converted
        try:
            int(num)
        except TypeError:
            print(f"{num} could not be converted to int.")
            break
        # If could be converted to int continue loop
        num_.add(num)
    # TODO: Loop not stopping when length of the set reaches 10 -- FIX
    elif (len(num_) > 10): 
        print("Congratulations, the set is larger than 10 numbers so you WIN!")
        break
    elif (points == 0):
        # TODO: Figure out why game keeps going until points reach 0 even if you win
        print("Uh oh, you lost!")
        break
    else:
        # Prevent duplicate entries
        print("This number already exists in the set.")
        # Deduct points by 1
        points -= 1
    # Continue loop until 5 points have been deducted
    continue


# Verify number of items in set
print(num_)