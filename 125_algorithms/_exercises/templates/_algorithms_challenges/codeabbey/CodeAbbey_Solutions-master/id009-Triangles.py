___ triangle(calculations
    answer = []
    for calculation in range(calculations
        [a,b,c] = raw_input().split()
        [a,b,c] = int(a),int(b),int(c)
        minNum = min(int(a),int(b),int(c))
        maxNum = max(int(a),int(b),int(c))

        for x in [a,b,c]:
            __ int(x) != minNum and int(x) != maxNum:
                midNum = x
        a,b,c = minNum, midNum, maxNum
        __ (a+b) > c:
            answer.append(str('1'))
        ____
            answer.append(str('0'))
    print(' '.join(answer))
triangle(input())
