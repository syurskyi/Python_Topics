___ check_valid_tr_number(number):
    __ l..(str(number)) != 11 o. any([str(c) n.. __ '0123456789' ___ c __ str(number)]):
        r.. False
    sum_13579 = s..([int(number[n]) * 7 ___ n __ r..(0,9) __ n __ (0,2,4,6,8)])
    sum_2468 = s..([int(number[n]) ___ n __ r..(0,9) __ n __ (1,3,5,7)])
    __ (sum_13579-sum_2468) % 10 != int(number[9]):
        r.. False
    __ s..([int(number[n]) ___ n __ r..(10)]) % 10 != int(number[10]):
        r.. False
    r.. True


print(check_valid_tr_number('10167994524'))    
print(check_valid_tr_number('36637640050'))