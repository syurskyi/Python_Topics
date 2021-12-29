words = ("Andrew Carnegie's 64-room chateau at 2 East 91st "
             "Street was converted into the Cooper-Hewitt National "
             "Design Museum of the Smithsonian Institution "
             "in the 1970's").split()

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    #temp = sorted(words, key=lambda test_str: test_str[:1].lower() + test_str[1:])
    return sorted(words, key=lambda x: (x[0].isdigit(), str(x).lower()))

print(sort_words_case_insensitively(words))