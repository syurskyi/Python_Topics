___ savingsCalc(calculations):
    answer    # list
    ___ calculation __ r..(calculations):
        # start = Starting money, end = Goal amount, rate = Interest rate
        start, end, rate = raw_input().s..
        rate = (i..(rate) / 100.00) + 1
        start,end = i..(start),i..(end)
        year = 0
        
        w.... start < end:
            start *= rate
            year += 1
        answer.a..(s..(year))
    print(' '.j..(answer))
savingsCalc(input())
