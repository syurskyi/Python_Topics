___ get_word(left, right):
    return left.capitalize() + right



___ test():
    print("test has started")
    __ get_word("reli", "able") != "Reliable":
        print("error1")
    __ get_word("maga", "zine") != "Magazine":
        print("error2")
    __ get_word("offi", "cial") != "Official":
        print("error3")
