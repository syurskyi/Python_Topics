___ is_empty(dictionary
    __ l..(dictionary) __ 0:
        r.. T..
    ____
        r.. F..


___ test
    print("Test has started")
    d.. {"Name": "Eleven"}
    __ is_empty(d..) !_ F..:
        print("error1")
    b_dict    # dict
    __ is_empty(b_dict) !_ T..
        print("error2")
