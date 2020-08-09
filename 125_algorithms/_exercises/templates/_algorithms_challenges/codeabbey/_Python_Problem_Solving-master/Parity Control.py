a = list(map(int,input().split()))
for i in a:
    __ 1 <=i <= 8 or 9<= i <= 31 or 33<= i <=45  :
        continue
    ____
        bits = '{:08b}'.format(i)
        temp_bin = []
        string = ''
        dec = 0
        for j in bits:
            temp_bin.append(j)
        __ bits.count('1') % 2 __ 0:
            __ temp_bin[0] __ '1':
                temp_bin[0] = '0'
                for k in temp_bin:
                    string += k
                dec = int(string,2)
                print(chr(dec),end='')
            ____
                print(chr(i),end='')
        ____
            __ temp_bin[0] __ '1':
                pass
            ____
                temp_bin[0] = '1'
                
                for k in temp_bin:
                    string += k
                dec = int(string,2)
                __ 128<= dec <= 255:
                    pass
                ____
                    #print(dec)
                    print(chr(dec),end='')