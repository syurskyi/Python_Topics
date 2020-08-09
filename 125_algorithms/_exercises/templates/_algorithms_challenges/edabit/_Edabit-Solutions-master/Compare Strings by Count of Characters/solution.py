___ comp(txt1, txt2
    __ le.(txt1) __ le.(txt2
        r_ True
    ____
        r_ False


___ test_comp(
    print("test has started")
    __ comp("test","food") != True:
        print("error")
    __ comp ("too", "good") != False:
        print("error2")
    ____
        print("success")
