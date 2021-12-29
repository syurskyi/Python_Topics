words = ("It was the twenty9th of October when it was questioned"
             "the meaning of nuMbers and weather hiding a number Inside"
             "tex56t should be treated as a word or another number").split()

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    #temp = sorted(words, key=lambda test_str: test_str[:1].lower() + test_str[1:])
    temp = sorted(words, key=str.lower)
    temp1 = []
    for index, word in enumerate(temp):
        if not word[0].isdigit():
            temp1.append(temp[index])
    for index, word in enumerate(temp):
        if word[0].isdigit():
            temp1.append(temp[index])
    return temp1

print(sort_words_case_insensitively(words))