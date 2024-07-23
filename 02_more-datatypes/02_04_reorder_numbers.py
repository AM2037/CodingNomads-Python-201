# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

# Initialize empty list to append user input to
num_list = []

# Initialize loop count
count = 1

while count <= 10:
    # Prompt user for 10 numbers
    user_input = int(input("Please enter a number here: "))
    # Append input to list
    num_list.append(user_input)
    # Increase count by 1
    count += 1

# Print full list
print(num_list)

# Print first range of numbers: every other value
print(num_list[1::2])

# Reverse list first
rev_list = num_list[::-1]
# Print second range of numbers -- same syntax as before since 9th position 
# is now 2nd (aka 1 due to 0-indexing)
print(rev_list[1::2])
