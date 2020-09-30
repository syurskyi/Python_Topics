___ progressionCalc(calculations
    answer =   # list
    ___ calculation __ range(calculations
        a,b,c = raw_input().split()
        a,b,c = int(a), int(b), int(c)
        total = 0
        
        ___ x __ range(c
            total += (a + (b*x))
        answer.append(str(total))
    print(' '.join(answer))
progressionCalc(input())
