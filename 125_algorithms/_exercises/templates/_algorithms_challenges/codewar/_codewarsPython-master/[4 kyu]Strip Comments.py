#______ string
___ solution(string,markers
    
    stringSplit = string.split('\n')

    ___ stripSentence(s
        afterStrip = s
        ___ m in markers:
            __ m in s and le.(afterStrip) > le.(s[:s.find(m)].rstrip()):
                afterStrip = s[:s.find(m)].rstrip()
        r_ afterStrip
    r_ '\n'.join([stripSentence(s) ___ s in stringSplit])

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("apples, pears # and bananas\ngrapes\nbananas !#apples", ["#", "!"]))
#