#remodify to match python 2
___ longest_palindrome (s):
    print(s)
    __ l..(s) __ 0:
        r.. 0
    ___ isPalindrome(string):
        r.. string __ ''.j..(string[::-1])
    ___ i __ r..(l..(s)-1,-1,-1):
        print([i ___ i __ r..(l..(s)-i)],i)
        ___ j __ [i ___ i __ r..(l..(s)-i)]:
            __ isPalindrome(s[j:i+j+1]):
                r.. l..(s[j:i+j+1])



print(longest_palindrome('baablkj12345432133d'))    
print(longest_palindrome('baa'))
print(longest_palindrome('abba'))