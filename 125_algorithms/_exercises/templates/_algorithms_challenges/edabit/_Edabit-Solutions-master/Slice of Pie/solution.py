___ equal_slices(total, people, each):
    __ people __ 0:
        r.. True
    __ people * each <= total:
        r.. True
    ____:
        r.. False


___ test():
    print("test has started")
    __ equal_slices(100, 0, 50) != False:
        print("error1")
    __ equal_slices(100 , 50, 2) != True:
        print("error2")
    __ equal_slices(30, 15 ,3) != False:
        print("error3")
