words = ("It's almost Holidays and PyBites wishes You a "
             "Merry Christmas and a Happy 2019").split()

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    # this works because: >>> sorted([True, False])
    # [False, True]
    return sorted(words, key=lambda x: (str(x).lower(), x[0].isdigit() ))


print(sort_words_case_insensitively(words))