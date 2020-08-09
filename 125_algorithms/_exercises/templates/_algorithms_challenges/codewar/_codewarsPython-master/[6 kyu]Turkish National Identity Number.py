___ check_valid_tr_number(number
    __ le.(str(number)) != 11 or any([str(c) not in '0123456789' for c in str(number)]
        r_ False
    sum_13579 = sum([int(number[n]) * 7 for n in range(0,9) __ n in (0,2,4,6,8)])
    sum_2468 = sum([int(number[n]) for n in range(0,9) __ n in (1,3,5,7)])
    __ (sum_13579-sum_2468) % 10 != int(number[9]
        r_ False
    __ sum([int(number[n]) for n in range(10)]) % 10 != int(number[10]
        r_ False
    r_ True


print(check_valid_tr_number('10167994524'))    
print(check_valid_tr_number('36637640050'))