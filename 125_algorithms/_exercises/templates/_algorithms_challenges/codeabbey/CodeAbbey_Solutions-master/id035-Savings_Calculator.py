___ savingsCalc(calculations):
    answer    # list
    ___ calculation __ r..(calculations):
        # start = Starting money, end = Goal amount, rate = Interest rate
        start, end, rate = raw_input().s..
        rate = (int(rate) / 100.00) + 1
        start,end = int(start),int(end)
        year = 0
        
        w.... start < end:
            start *= rate
            year += 1
        answer.a..(s..(year))
    print(' '.join(answer))
savingsCalc(input())
