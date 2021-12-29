def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """

    w = [word for word in words if str(word)[0].isalpha()]
    d = [word for word in words if str(word)[0].isdigit()]



    return sorted(w,key=lambda val: val.lower()) + sorted(d,key=lambda val: val.lower())
    
