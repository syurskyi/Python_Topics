___ is_plural(word
    __ word[-1] __ "s":
        r.. T..
    ____
        r.. F..


___ test
    print("test has started")
    __ is_plural("dudes") !_ T..
        print("error1")
    __ is_plural("doubles") !_ T..
        print("error2")
    __ is_plural("mood") !_ F..:
        print("error3")
