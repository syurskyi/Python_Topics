___ comp(txt1, txt2):
    __ len(txt1) == len(txt2):
        return True
    else:
        return False


___ test_comp():
    print("test has started")
    __ comp("test","food") != True:
        print("error")
    __ comp ("too", "good") != False:
        print("error2")
    else:
        print("success")
