#import string
___ solution(string,markers):
    
    stringSplit = string.s..('\n')

    ___ stripSentence(s):
        afterStrip = s
        ___ m __ markers:
            __ m __ s a.. l..(afterStrip) > l..(s[:s.find(m)].rstrip()):
                afterStrip = s[:s.find(m)].rstrip()
        r.. afterStrip
    r.. '\n'.join([stripSentence(s) ___ s __ stringSplit])

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"]))
#