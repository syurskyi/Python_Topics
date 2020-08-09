___ isEvenOrOdd(num
    __ num % 2 __ 0:
        r_ "even"
    ____
        r_ "odd"


___ test(
    print("test has started")
    __ isEvenOrOdd(3) != "odd":
        print("error1")
    __ isEvenOrOdd(0) != "even":
        print("error2")
    __ isEvenOrOdd(-3) != "odd":
        print("error3")
    __ isEvenOrOdd(-0) != "even":
        print("error4")
