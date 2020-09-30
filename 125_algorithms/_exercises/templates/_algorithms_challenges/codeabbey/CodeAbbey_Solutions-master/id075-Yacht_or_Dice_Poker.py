______ collections

___ dice_poker(
    rolls = int(input())
    answer =   # list
    
    ___ roll __ range(rolls
        roll = input().split()
        values = sorted([x ___ x __ collections.Counter(roll).values()])

        __ sorted(roll) __ ['2', '3', '4', '5', '6']:
            answer.append('big-straight')
        ____ sorted(roll) __ ['1', '2', '3', '4', '5']:
            answer.append('small-straight')
        ____ values __ [2, 3]:
            answer.append('full-house')
        ____ values __ [1, 2, 2]:
            answer.append('two-pairs')
        ____ values __ [5]:
            answer.append('yacht')
        ____ values __ [1, 4]:
            answer.append('four')
        ____ values __ [1, 1, 3]:
            answer.append('three')
        ____ values __ [1, 1, 1, 2]:
            answer.append('pair')
        ____
            answer.append('none')
        
    print(' '.join(answer))
dice_poker()
