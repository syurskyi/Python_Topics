words = ("It was the twenty9th of October when it was questioned"
             "the meaning of nuMbers and weather hiding a number Inside"
             "tex56t should be treated as a word or another number").s..

___ sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    #temp = sorted(words, key=lambda test_str: test_str[:1].lower() + test_str[1:])
    temp = s..(words, key=s...lower)
    temp1    # list
    ___ index, word __ e..(temp):
        __ n.. word[0].i..
            temp1.a..(temp[index])
    ___ index, word __ e..(temp):
        __ word[0].i..
            temp1.a..(temp[index])
    r.. temp1

print(sort_words_case_insensitively(words))