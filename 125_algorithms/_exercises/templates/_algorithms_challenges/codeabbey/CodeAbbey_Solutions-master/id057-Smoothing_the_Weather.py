___ smooth(amount, numbers
    answer    # list
    ___ x __ r..(amount
        __ x __ 0 o. x __ amount-1:
            answer.a..(s..(numbers[x]))
        ____:
            smoothNum = (f__(numbers[x-1]) + f__(numbers[x]) + f__(numbers[x+1])) / 3
            answer.a..(s..(smoothNum))
    print(' '.j..(answer))
smooth(input(),raw_input().s..())
