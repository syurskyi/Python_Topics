___ smooth(amount, numbers):
    answer    # list
    ___ x __ r..(amount):
        __ x __ 0 o. x __ amount-1:
            answer.a..(str(numbers[x]))
        ____:
            smoothNum = (float(numbers[x-1]) + float(numbers[x]) + float(numbers[x+1])) / 3
            answer.a..(str(smoothNum))
    print(' '.join(answer))
smooth(input(),raw_input().split())
