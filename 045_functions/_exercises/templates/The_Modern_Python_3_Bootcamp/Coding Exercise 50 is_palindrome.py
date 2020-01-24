# Here's the simpler version that doesn't ignore whitespace.
# I reverse the string using a slice [::-1] and compare that to the original string, which returns True or False.


def is_palindrome(string):
    return string == string[::-1]

# The Bonus Version:
#
# For the more advanced version that ignores whitespace,
# I first remove all whitespace from the input string using a string method called replace() .
# What I'm actually doing is replacing all spaces(" ") with empty strings ("").
# I save the result to a new variable I call stripped .  Then, I simply check if stripped is a palindrome,
# using the same logic I did in the previous solution.


def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]