___ isEvenOrOdd(num
    __ num % 2 __ 0:
        r.. "even"
    ____
        r.. "odd"


___ test
    print("test has started")
    __ isEvenOrOdd(3) !_ "odd":
        print("error1")
    __ isEvenOrOdd(0) !_ "even":
        print("error2")
    __ isEvenOrOdd(-3) !_ "odd":
        print("error3")
    __ isEvenOrOdd(-0) !_ "even":
        print("error4")
