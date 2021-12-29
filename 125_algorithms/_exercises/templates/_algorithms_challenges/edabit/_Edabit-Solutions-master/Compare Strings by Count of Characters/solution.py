___ comp(txt1, txt2):
    __ l..(txt1) __ l..(txt2):
        r.. True
    ____:
        r.. False


___ test_comp():
    print("test has started")
    __ comp("test","food") != True:
        print("error")
    __ comp ("too", "good") != False:
        print("error2")
    ____:
        print("success")
