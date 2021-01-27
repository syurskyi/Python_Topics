# REVERSE SOLUTION


___ reverse(strng
    __ le_(strng) <= 1:
        r_ strng
    r_ strng[le_(strng) - 1] + reverse(strng[0:le_(strng) - 1])


# IS PALINDROME SOLUTION


___ isPalindrome(strng
    __ le_(strng) == 0:
        r_ True
    __ strng[0] != strng[le_(strng) - 1]:
        r_ False
    r_ isPalindrome(strng[1:-1])


# SOME RECURSIVE SOLUTION


___ someRecursive(arr, cb
    __ le_(arr) == 0:
        r_ False
    __ not (cb(arr[0])):
        r_ someRecursive(arr[1:], cb)
    r_ True


___ isOdd(num
    __ num % 2 == 0:
        r_ False
    ____
        r_ True


# FLATTEN SOLUTION


___ flatten(arr
    resultArr = []
    ___ custItem __ arr:
        __ type(custItem) is list:
            resultArr.extend(flatten(custItem))
        ____
            resultArr.append(custItem)
    r_ resultArr