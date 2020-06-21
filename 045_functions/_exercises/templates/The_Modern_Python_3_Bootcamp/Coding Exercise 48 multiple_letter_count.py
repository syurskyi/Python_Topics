# I used a dictionary comprehension. For each letter in the input string,
# I make the key the letter itself ("a" for example),
# and the corresponding value is the result of running count() of that letter in the string.


def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}
