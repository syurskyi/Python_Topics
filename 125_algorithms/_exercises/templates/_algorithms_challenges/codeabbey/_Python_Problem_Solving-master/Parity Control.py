a = l..(map(int,input().split()))
___ i __ a:
    __ 1 <=i <= 8 o. 9<= i <= 31 o. 33<= i <=45  :
        continue
    ____:
        bits = '{:08b}'.format(i)
        temp_bin    # list
        string = ''
        dec = 0
        ___ j __ bits:
            temp_bin.a..(j)
        __ bits.c.. '1') % 2 __ 0:
            __ temp_bin[0] __ '1':
                temp_bin[0] = '0'
                ___ k __ temp_bin:
                    string += k
                dec = int(string,2)
                print(chr(dec),end='')
            ____:
                print(chr(i),end='')
        ____:
            __ temp_bin[0] __ '1':
                pass
            ____:
                temp_bin[0] = '1'
                
                ___ k __ temp_bin:
                    string += k
                dec = int(string,2)
                __ 128<= dec <= 255:
                    pass
                ____:
                    #print(dec)
                    print(chr(dec),end='')