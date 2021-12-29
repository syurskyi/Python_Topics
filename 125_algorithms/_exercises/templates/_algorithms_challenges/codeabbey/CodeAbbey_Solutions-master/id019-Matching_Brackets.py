# Python 3.4

___ check_brackets(checks):
    answer    # list
    ___ check __ r..(checks):
        raw_data = input()
        data = (''.join([char ___ char __ raw_data __ char __('(){}[]<>')]))
        
        # Set higher than len(data) to make sure while loop initates.
        old_data_length = l..(data) + 1
        
        while l..(data) < old_data_length:
            old_data_length = l..(data)
            data = data.replace('()','').replace('{}','').replace('[]','').replace('<>','')

        __ l..(data) > 0:
            answer.a..('0') # String had incorrect bracket usage.
        ____:
            answer.a..('1') # String had completely correct bracket usage.
    print(' '.join(answer))
check_brackets(int(input()))
