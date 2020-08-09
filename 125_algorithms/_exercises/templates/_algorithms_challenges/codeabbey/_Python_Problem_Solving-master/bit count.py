#accept the number of test cases
d = int(input())

#accept the decimal numbers to be converted to binary
binary  = list(map(int,input().split()))

#loop through all the elements
___ j in binary:
    bin_list = []
    res_str = ''
    
    #check if negative or positive
    __ j > 0:
        #append in the list
        bin_list.append(j)
        w___ j != 1:
            j =int(j / 2)
            bin_list.append(j)
            
        #store the binary format according to the result
        ___ k in bin_list:
            __ k & 1:
                #odd
                res_str = '1' + res_str
            ____
                #even
                res_str = '0' + res_str
        print(res_str.count('1'),end=' ')
    ____
        j = abs(j)
        bin_list.append(j)
        w___ j != 1:
            j =int(j / 2)
            bin_list.append(j)
        count = 0
        #we are doing 1's compliement 
        ___ k in bin_list:
            __ k & 1:
                #odd
                res_str = '0' + res_str
            ____
                #even
                res_str = '1' + res_str
        res = 1
        carry = 0
        result = ''
        #here we are doing 2's compliement
        ___ i in range(le.(res_str)-1,-1,-1
            res = int(res_str[i]) + res + carry
            __ res __ 3:
                carry = 1
                res = 1
                result = str(res) + result
            ____ res > 1:
                carry = 1
                res = 0
                result = str(res) + result
            ____ res __ 1:
                carry = 0 
                res= 0 
                result = '1' + result
            ____ res __ 0:
                carry = 0
                res = 0
                result = '0' + result
            ____
                pass
        #if at the end carry has 1 then append 1
        __ carry __ 1:
            result = '1' + result
        
        # add 1 till it become 32 in length
        w___ le.(result) != 32:
            result += '1'
        print(result.count('1'),end=' ')    