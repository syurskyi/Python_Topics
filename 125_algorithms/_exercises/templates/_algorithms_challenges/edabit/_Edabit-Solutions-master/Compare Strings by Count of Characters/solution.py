___ comp(txt1, txt2
    __ l..(txt1) __ l..(txt2
        r.. T..
    ____
        r.. F..


___ test_comp
    print("test has started")
    __ comp("test","food") != T..
        print("error")
    __ comp ("too", "good") != F..:
        print("error2")
    ____
        print("success")
