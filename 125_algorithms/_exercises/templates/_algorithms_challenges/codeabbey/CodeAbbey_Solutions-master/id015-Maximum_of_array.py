___ findRange(numbers):
    answer = []
    minNum, maxNum = 0,0
    numbers = numbers.split()
    for x in numbers:
        __ int(x) < int(minNum):
            minNum = x
        __ int(x) > int(maxNum):
            maxNum = x
    print(str(maxNum) + " " + str(minNum))
findRange(raw_input())
