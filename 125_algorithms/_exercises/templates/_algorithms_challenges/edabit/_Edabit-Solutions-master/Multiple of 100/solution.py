___ divisible(num
    __ num >= 100 and num % 100 __ 0:
        r_ True
    ____ num __ 0:
        r_ True
    ____ num < 0 and num % 100 __ 0:
        r_ True
    ____
        r_ False
