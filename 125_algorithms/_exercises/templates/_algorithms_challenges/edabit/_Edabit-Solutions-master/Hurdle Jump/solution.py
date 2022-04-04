___ hurdle_jump(hurdles, jump_height
    __ hurdles __ []:
        r.. T..
    hurdles.s..()
    __ hurdles[-1] < jump_height:
        r.. T..
    ____
        r.. F..


___ test
    print("test has started")
    __ hurdle_jump([1,2,1], 1) ! F..:
        print("error1")
    __ hurdle_jump([1, 2, 3, 4, 5], 5) ! T..:
        print("error2")
    __ hurdle_jump([], 4) ! T..:
        print("error3")
