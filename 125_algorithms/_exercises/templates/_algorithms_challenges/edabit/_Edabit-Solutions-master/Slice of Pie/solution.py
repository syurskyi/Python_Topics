___ equal_slices(total, people, each):
    __ people __ 0:
        r.. T..
    __ people * each <= total:
        r.. T..
    ____:
        r.. F..


___ test
    print("test has started")
    __ equal_slices(100, 0, 50) != F..:
        print("error1")
    __ equal_slices(100 , 50, 2) != T..:
        print("error2")
    __ equal_slices(30, 15 ,3) != F..:
        print("error3")
