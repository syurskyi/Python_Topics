#import string
___ solution(s__,markers
    
    stringSplit s__.s..('\n')

    ___ stripSentence(s
        afterStrip s
        ___ m __ markers:
            __ m __ s a.. l..(afterStrip) > l..(s[:s.find(m)].r..:
                afterStrip s[:s.find(m)].r..()
        r.. afterStrip
    r.. '\n'.j..([stripSentence(s) ___ s __ stringSplit])

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
print(solution("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"]
#