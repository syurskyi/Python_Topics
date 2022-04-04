_______ c..

___ dice_poker
    rolls = i..(input
    answer    # list
    
    ___ roll __ r..(rolls
        roll = input().s..
        values = s..([x ___ x __ c...C..(roll).v..)

        __ s..(roll) __  '2', '3', '4', '5', '6' :
            answer.a..('big-straight')
        ____ s..(roll) __  '1', '2', '3', '4', '5' :
            answer.a..('small-straight')
        ____ values __ [2, 3]:
            answer.a..('full-house')
        ____ values __ [1, 2, 2]:
            answer.a..('two-pairs')
        ____ values __ [5]:
            answer.a..('yacht')
        ____ values __ [1, 4]:
            answer.a..('four')
        ____ values __ [1, 1, 3]:
            answer.a..('three')
        ____ values __ [1, 1, 1, 2]:
            answer.a..('pair')
        ____:
            answer.a..('none')
        
    print(' '.j..(answer
dice_poker()
