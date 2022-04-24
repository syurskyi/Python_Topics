# Python 3.4

___ check_brackets(checks
    answer    # list
    ___ check __ r..(checks
        raw_data  i.. )
        data  (''.j..([char ___ char __ raw_data __ char __('(){}[]<>')]
        
        # Set higher than len(data) to make sure while loop initates.
        old_data_length  l..(data) + 1
        
        w.... l..(data) < old_data_length:
            old_data_length  l..(data)
            data  data.r..('()','').r..('{}','').r..('[]','').r..('<>','')

        __ l..(data) > 0
            answer.a..('0') # String had incorrect bracket usage.
        ____
            answer.a..('1') # String had completely correct bracket usage.
    print(' '.j..(answer
check_brackets(i..(i.. )))
