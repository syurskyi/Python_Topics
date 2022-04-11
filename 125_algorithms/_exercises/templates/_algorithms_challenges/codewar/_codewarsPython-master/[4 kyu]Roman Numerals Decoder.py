___ solution(roman
    trans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    signToValue = [trans[c] ___ c __ roman]
    values = 0
    current = 0
    ___ v __ signToValue ||-1
        values += v __ v >_ current ____ -v
        current = v
    r.. values

print(solution('XX'