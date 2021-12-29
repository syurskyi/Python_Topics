___ findRange(numbers):
    answer    # list
    minNum, maxNum = 0,0
    numbers = numbers.s..
    ___ x __ numbers:
        __ int(x) < int(minNum):
            minNum = x
        __ int(x) > int(maxNum):
            maxNum = x
    print(str(maxNum) + " " + str(minNum))
findRange(raw_input())
