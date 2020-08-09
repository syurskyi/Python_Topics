___ dig_pow(n, p
    total = su.([(int(d)**power) ___ power,d in enumerate([d ___ d in str(n)],p)])
    r_ -1 __ total%n != 0 else int(total/n)

print(dig_pow(46288, 3))