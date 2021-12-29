___ ispalindrome(num):
    str1 = str(num)
    rev_str = str1[::-1]
    return str1 == rev_str


___ count_palindromes(num1, num2):
    output = 0
    while num1 <= num2:
        __ ispalindrome(num1) == True:
            output += 1
        num1 += 1
    return output
