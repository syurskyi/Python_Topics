# In my solution, I use the built-in count()  to count the number of times letter  appears in string .
# I also downcase both string  and letter  to make it case-insensitive (you could also upcase both instead)


def single_letter_count(string, letter):
    return string.lower().count(letter.lower())
