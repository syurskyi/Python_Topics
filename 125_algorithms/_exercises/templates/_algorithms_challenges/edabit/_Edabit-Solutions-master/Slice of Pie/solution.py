___ equal_slices(total, people, each):
    __ people == 0:
        return True
    __ people * each <= total:
        return True
    else:
        return False


___ test():
    print("test has started")
    __ equal_slices(100, 0, 50) != False:
        print("error1")
    __ equal_slices(100 , 50, 2) != True:
        print("error2")
    __ equal_slices(30, 15 ,3) != False:
        print("error3")
