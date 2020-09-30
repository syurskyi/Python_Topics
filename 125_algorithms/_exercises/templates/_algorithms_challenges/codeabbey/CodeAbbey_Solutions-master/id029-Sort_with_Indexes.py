___ sortIndexes(amount, values
    answer =   # list
    sortedValues = sorted(values)
    ___ sortedValue __ sortedValues:
        ___ x __ range(amount
            __ sortedValue __ values[x]:
                answer.append(str(x+1))
    print(' '.join(answer))
sortIndexes(input(),[int(x) ___ x __ raw_input().split()])
