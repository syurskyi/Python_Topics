#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# isPalindrome Solution


___ isPalindrome(strng
    __ len(strng) == 0:
        return True
    __ strng[0] != strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false