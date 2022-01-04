___ is_empty(s):
    __ s __ "":
        r.. T..
    ____:
        r.. F..

___ test_empty
    print("test has started")
    __ is_empty("") != T..:
        print("error1")
    __ is_empty(10) != F..:
        print("error2")
    __ is_empty("tom") != F..:
        print("error3")
