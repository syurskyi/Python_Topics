___ limit_number(num, range_low, range_high
    __ num < range_low:
        r.. range_low
    ____ num > range_high:
        r.. range_high
    ____:
        r.. num

___ test
    print("test has started")
    __ limit_number(5, 1, 10) != 5:
        print("error1")
    __ limit_number(-3, 1, 10) != 1:
        print("error2")
    __ limit_number(14, 1, 10) != 10:
        print("error3")
