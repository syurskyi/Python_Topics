___ collatzSequence(tests
    data = raw_input().split()
    answer = []
    
    ___ test in range(tests
        count = 0
        value = int(data[test])
        
        w___ value != 1:
            __ value % 2 __ 0:
                value /= 2
            ____
                value = 3 * value + 1
            count += 1
        answer.append(str(count))
    print(' '.join(answer))
collatzSequence(input())
