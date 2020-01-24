# Using a string (preferable solution):

answer = [char for char in "amazing" if char not in "aeiou"]

# Using a list:

answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]]
