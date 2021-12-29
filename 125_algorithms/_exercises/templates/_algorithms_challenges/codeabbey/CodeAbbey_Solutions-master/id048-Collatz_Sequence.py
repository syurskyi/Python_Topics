___ collatzSequence(tests):
    data = raw_input().s..
    answer    # list
    
    ___ test __ r..(tests):
        count = 0
        value = int(data[test])
        
        while value != 1:
            __ value % 2 __ 0:
                value /= 2
            ____:
                value = 3 * value + 1
            count += 1
        answer.a..(str(count))
    print(' '.join(answer))
collatzSequence(input())
