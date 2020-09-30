___ hurdle_jump(hurdles, jump_height
    __ hurdles __   # list:
        r_ True
    hurdles.sort()
    __ hurdles[-1] <= jump_height:
        r_ True
    ____
        r_ False


___ test(
    print("test has started")
    __ hurdle_jump([1,2,1], 1) != False:
        print("error1")
    __ hurdle_jump([1, 2, 3, 4, 5], 5) != True:
        print("error2")
    __ hurdle_jump(  # list, 4) != True:
        print("error3")
