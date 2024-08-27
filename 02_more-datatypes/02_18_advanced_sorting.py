# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

# Dictionary of favorite books series and number of books in each
favorite_book_series = {"Harry Potter": 7, "The Southern Reach Series": 3, "Miss Peregrine's Home for Peculiar Children": 6}

# Sort dictionary into list of tuples
tups = [(k,v) for k,v in favorite_book_series.items()]
print(tups)