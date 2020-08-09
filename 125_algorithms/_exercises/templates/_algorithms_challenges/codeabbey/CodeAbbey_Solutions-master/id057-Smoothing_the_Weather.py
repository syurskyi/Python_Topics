___ smooth(amount, numbers
    answer = []
    ___ x in range(amount
        __ x __ 0 or x __ amount-1:
            answer.append(str(numbers[x]))
        ____
            smoothNum = (float(numbers[x-1]) + float(numbers[x]) + float(numbers[x+1])) / 3
            answer.append(str(smoothNum))
    print(' '.join(answer))
smooth(input(),raw_input().split())
