def get_index_different_char(chars):
    for count, char in enumerate(chars):
        if str(char).isalnum():
            alnum = count
        else:
            not_alnum = count
    if (sum(1 for char in chars if str(char).isalnum())) >  (sum(1 for char in chars if not str(char).isalnum())):
        return not_alnum
    else:
        return alnum
