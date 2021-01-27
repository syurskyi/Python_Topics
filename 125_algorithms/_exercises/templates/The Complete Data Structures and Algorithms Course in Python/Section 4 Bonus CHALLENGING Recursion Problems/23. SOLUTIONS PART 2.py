# REVERSE SOLUTION


___ reverse(strng
    __ le_(strng) <= 1:
        r_ strng
    r_ strng[le_(strng) - 1] + reverse(strng[0:le_(strng) - 1])


# IS PALINDROME SOLUTION


___ isPalindrome(strng
    __ le_(strng) __ 0:
        r_ T..
    __ strng[0] != strng[le_(strng) - 1]:
        r_ F..
    r_ isPalindrome(strng[1:-1])


# SOME RECURSIVE SOLUTION


___ someRecursive(arr, cb
    __ le_(arr) __ 0:
        r_ F..
    __ no. (cb(arr[0])):
        r_ someRecursive(arr[1:], cb)
    r_ T..


___ isOdd(num
    __ num % 2 __ 0:
        r_ F..
    ____
        r_ T..


# FLATTEN SOLUTION


___ flatten(arr
    resultArr = []
    ___ custItem __ arr:
        __ type(custItem) __ li__:
            resultArr.extend(flatten(custItem))
        ____
            resultArr.ap..(custItem)
    r_ resultArr