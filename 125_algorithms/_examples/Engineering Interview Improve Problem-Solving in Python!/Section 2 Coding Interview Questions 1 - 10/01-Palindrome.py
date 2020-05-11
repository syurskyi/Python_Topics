#Palindrome abc -> cba
#           aba -> aba

def reverse_string(s):
    print(s)
    result = ""
    for c in s:
        result = c + result
    print('The reverse string is ->', result)
    return result


def is_palindrome(s):
    return s == reverse_string(s)


print(is_palindrome("abc"))
print(is_palindrome("aba"))
