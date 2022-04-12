___ check_valid_tr_number(number
    __ l..(s..(number !_ 11 o. any([s..(c) n.. __ '0123456789' ___ c __ s..(number)]
        r.. F..
    sum_13579 s..([i..(number[n]) * 7 ___ n __ r..(0,9) __ n __ (0,2,4,6,8)])
    sum_2468 s..([i..(number[n]) ___ n __ r..(0,9) __ n __ (1,3,5,7)])
    __ (sum_13579-sum_2468) % 10 !_ i..(number[9]
        r.. F..
    __ s..([i..(number[n]) ___ n __ r..(10)]) % 10 !_ i..(number[10]
        r.. F..
    r.. T..


print(check_valid_tr_number('10167994524'
print(check_valid_tr_number('36637640050'