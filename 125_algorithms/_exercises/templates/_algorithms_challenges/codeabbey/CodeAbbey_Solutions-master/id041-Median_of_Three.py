___ findMedian(amount
        answer = []
        ___ x in range(amount
                [a, b, c] = raw_input().split()
                minNum = min(int(a), int(b), int(c))
                maxNum = max(int(a), int(b), int(c))
                ___ x in [a, b, c]:
                    __ int(x) != minNum and int(x) != maxNum:
                        answer.append(str(x))
        print(' '.join(answer))
findMedian(input())
