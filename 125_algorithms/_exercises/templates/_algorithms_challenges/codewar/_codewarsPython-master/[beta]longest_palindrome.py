#remodify to match python 2
___ longest_palindrome (s
    print(s)
    __ le.(s) __ 0:
        r_ 0
    ___ isPalindrome(string
        r_ string __ ''.join(string[::-1])
    ___ i in range(le.(s)-1,-1,-1
        print([i ___ i in range(le.(s)-i)],i)
        ___ j in [i ___ i in range(le.(s)-i)]:
            __ isPalindrome(s[j:i+j+1]
                r_ le.(s[j:i+j+1])



print(longest_palindrome('baablkj12345432133d'))    
print(longest_palindrome('baa'))
print(longest_palindrome('abba'))