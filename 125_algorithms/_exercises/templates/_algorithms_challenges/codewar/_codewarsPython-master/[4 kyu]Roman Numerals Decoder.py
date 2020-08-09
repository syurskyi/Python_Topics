___ solution(roman
    trans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    signToValue = [trans[c] ___ c in roman]
    values = 0
    current = 0
    ___ v in signToValue[::-1]:
        values += v __ v >= current else -v
        current = v
    r_ values

print(solution('XX'))    