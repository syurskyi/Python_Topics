# Python 3.4

___ check_brackets(checks
    answer = []
    ___ check in range(checks
        raw_data = input()
        data = (''.join([char ___ char in raw_data __ char in('(){}[]<>')]))
        
        # Set higher than le.(data) to make sure w___ loop initates.
        old_data_length = le.(data) + 1
        
        w___ le.(data) < old_data_length:
            old_data_length = le.(data)
            data = data.replace('()','').replace('{}','').replace('[]','').replace('<>','')

        __ le.(data) > 0:
            answer.append('0') # String had incorrect bracket usage.
        ____
            answer.append('1') # String had completely correct bracket usage.
    print(' '.join(answer))
check_brackets(int(input()))
