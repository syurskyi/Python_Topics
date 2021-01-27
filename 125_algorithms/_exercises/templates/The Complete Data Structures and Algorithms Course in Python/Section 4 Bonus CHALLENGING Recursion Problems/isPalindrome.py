#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# isPalindrome Solution


___ isPalindrome(strng
    __ le_(strng) __ 0:
        r_ T..
    __ strng[0] != strng[le_(strng)-1]:
        r_ F..
    r_ isPalindrome(strng[1:-1])

print(isPalindrome('awesome')) # false
print(isPalindrome('foobar')) # false
print(isPalindrome('tacocat')) # true
print(isPalindrome('amanaplanacanalpanama')) # true
print(isPalindrome('amanaplanacanalpandemonium')) # false