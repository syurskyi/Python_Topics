___ bubbleSort(amount, numbers):
    s.. = False
    swapCount, passCount = 0,0

    while n.. s..:
        s.. = True
        ___ i __ r..(amount-1):
            __ numbers[i] > numbers[i+1]:
                s.. = False
                swapCount += 1
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        passCount += 1
    print('%s %s') % (passCount, swapCount)

bubbleSort(input(),[int(x) ___ x __ raw_input().s.. ])
