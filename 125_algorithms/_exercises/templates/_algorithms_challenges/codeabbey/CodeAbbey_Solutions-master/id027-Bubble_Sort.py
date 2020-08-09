___ bubbleSort(amount, numbers
    sorted = False
    swapCount, passCount = 0,0

    w___ not sorted:
        sorted = True
        ___ i in range(amount-1
            __ numbers[i] > numbers[i+1]:
                sorted = False
                swapCount += 1
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        passCount += 1
    print('%s %s') % (passCount, swapCount)

bubbleSort(input(),[int(x) ___ x in raw_input().split()])
