# Using Set and Dictionary Comprehensions
# While the list comprehension in Python is a common tool, you can also create set and dictionary comprehensions.
# A set comprehension is almost exactly the same as a list comprehension in Python. The difference is that
# set comprehensions make sure the output contains no duplicates. You can create a set comprehension by
# using curly braces instead of brackets:
#
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)
# {'a', 'e', 'u', 'i'}

# Your set comprehension outputs all the unique vowels it found in quote. Unlike lists, sets don’t guarantee that items
# will be saved in any particular order. This is why the first member of the set is a, even though the first vowel
# in quote is i.
# Dictionary comprehensions are similar, with the additional requirement of defining a key:

squares = {i: i * i for i in range(10)}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# To create the squares dictionary, you use curly braces ({}) as well as a key-value pair (i: i * i) in your expression.
