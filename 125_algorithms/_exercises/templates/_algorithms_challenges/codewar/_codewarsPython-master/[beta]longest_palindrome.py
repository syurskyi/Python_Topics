#remodify to match python 2
___ longest_palindrome (s):
    print(s)
    __ len(s) == 0:
        return 0
    ___ isPalindrome(string):
        return string == ''.join(string[::-1])
    for i in range(len(s)-1,-1,-1):
        print([i for i in range(len(s)-i)],i)
        for j in [i for i in range(len(s)-i)]:
            __ isPalindrome(s[j:i+j+1]):
                return len(s[j:i+j+1])



print(longest_palindrome('baablkj12345432133d'))    
print(longest_palindrome('baa'))
print(longest_palindrome('abba'))