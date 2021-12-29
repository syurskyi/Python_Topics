def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    #print(text)
    #print(len(text))
    #print(len(text.lstrip(' ')))
    return len(text) - len(text.lstrip(' '))




print(count_indents('    string'))