___ check_valid_tr_number(number
    __ le.(str(number)) != 11 or any([str(c) not __ '0123456789' ___ c __ str(number)]
        r_ False
    sum_13579 = su.([int(number[n]) * 7 ___ n __ range(0,9) __ n __ (0,2,4,6,8)])
    sum_2468 = su.([int(number[n]) ___ n __ range(0,9) __ n __ (1,3,5,7)])
    __ (sum_13579-sum_2468) % 10 != int(number[9]
        r_ False
    __ su.([int(number[n]) ___ n __ range(10)]) % 10 != int(number[10]
        r_ False
    r_ True


print(check_valid_tr_number('10167994524'))    
print(check_valid_tr_number('36637640050'))