#accept the number of test cases
d = i..(input())

#accept the decimal numbers to be converted to binary
binary  = l..(map(i..,input().s..()))

#loop through all the elements
___ j __ binary:
    bin_list    # list
    res_str = ''
    
    #check if negative or positive
    __ j > 0:
        #append in the list
        bin_list.a..(j)
        w.... j != 1:
            j =i..(j / 2)
            bin_list.a..(j)
            
        #store the binary format according to the result
        ___ k __ bin_list:
            __ k & 1:
                #odd
                res_str = '1' + res_str
            ____:
                #even
                res_str = '0' + res_str
        print(res_str.c.. '1'),end=' ')
    ____:
        j = abs(j)
        bin_list.a..(j)
        w.... j != 1:
            j =i..(j / 2)
            bin_list.a..(j)
        count = 0
        #we are doing 1's compliement 
        ___ k __ bin_list:
            __ k & 1:
                #odd
                res_str = '0' + res_str
            ____:
                #even
                res_str = '1' + res_str
        res = 1
        carry = 0
        result = ''
        #here we are doing 2's compliement
        ___ i __ r..(l..(res_str)-1,-1,-1):
            res = i..(res_str[i]) + res + carry
            __ res __ 3:
                carry = 1
                res = 1
                result = s..(res) + result
            ____ res > 1:
                carry = 1
                res = 0
                result = s..(res) + result
            ____ res __ 1:
                carry = 0 
                res= 0 
                result = '1' + result
            ____ res __ 0:
                carry = 0
                res = 0
                result = '0' + result
            ____:
                p..
        #if at the end carry has 1 then append 1
        __ carry __ 1:
            result = '1' + result
        
        # add 1 till it become 32 in length
        w.... l..(result) != 32:
            result += '1'
        print(result.c.. '1'),end=' ')