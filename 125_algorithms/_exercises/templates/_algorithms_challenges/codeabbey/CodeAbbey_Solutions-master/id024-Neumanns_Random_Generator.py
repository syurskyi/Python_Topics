# Python 3.4.3

___ neumanns(inputs):
    answer    # list
    ___ num __ [int(x) ___ x __ input().s.. ]:
        loop_count = 0
        new_num = num * num
        temp = ''
        repeats = [s..(num)]
        no_repition = True

        w.... no_repition:
            __ loop_count != 0:
                new_num = int(new_num) * int(new_num)
                
            new_num = s..(new_num)
            w.... l..(new_num) < 8:
                new_num = '0' + new_num
            new_num = new_num[2:-2]

            loop_count += 1
            __ new_num __ repeats:
                no_repition = False
                
            repeats.a..(new_num)
        answer.a..(s..(loop_count))
    print(' '.join(answer))
neumanns(input()) # This is input() is required to be wasted. Please ignore.
