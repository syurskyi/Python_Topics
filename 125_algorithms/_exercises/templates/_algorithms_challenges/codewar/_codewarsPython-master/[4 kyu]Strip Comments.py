#import string
___ solution(string,markers):
    
    stringSplit = string.split('\n')

    ___ stripSentence(s):
        afterStrip = s
        for m in markers:
            __ m in s and len(afterStrip) > len(s[:s.find(m)].rstrip()):
                afterStrip = s[:s.find(m)].rstrip()
        return afterStrip
    return '\n'.join([stripSentence(s) for s in stringSplit])

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"]))
#