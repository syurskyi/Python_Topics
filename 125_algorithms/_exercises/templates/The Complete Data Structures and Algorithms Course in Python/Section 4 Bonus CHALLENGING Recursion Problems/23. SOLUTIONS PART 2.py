# REVERSE SOLUTION


___ reverse(strng
    __ len(strng) <= 1:
        return strng
    return strng[len(strng) - 1] + reverse(strng[0:len(strng) - 1])


# IS PALINDROME SOLUTION


___ isPalindrome(strng
    __ len(strng) == 0:
        return True
    __ strng[0] != strng[len(strng) - 1]:
        return False
    return isPalindrome(strng[1:-1])


# SOME RECURSIVE SOLUTION


___ someRecursive(arr, cb
    __ len(arr) == 0:
        return False
    __ not (cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True


___ isOdd(num
    __ num % 2 == 0:
        return False
    ____
        return True


# FLATTEN SOLUTION


___ flatten(arr
    resultArr = []
    for custItem in arr:
        __ type(custItem) is list:
            resultArr.extend(flatten(custItem))
        ____
            resultArr.append(custItem)
    return resultArr