___ triangle(calculations):
    answer    # list
    ___ calculation __ r..(calculations):
        [a,b,c] = raw_input().s.. 
        [a,b,c] = int(a),int(b),int(c)
        minNum = m..(int(a),int(b),int(c))
        maxNum = max(int(a),int(b),int(c))

        ___ x __ [a,b,c]:
            __ int(x) != minNum a.. int(x) != maxNum:
                midNum = x
        a,b,c = minNum, midNum, maxNum
        __ (a+b) > c:
            answer.a..(s..('1'))
        ____:
            answer.a..(s..('0'))
    print(' '.join(answer))
triangle(input())
