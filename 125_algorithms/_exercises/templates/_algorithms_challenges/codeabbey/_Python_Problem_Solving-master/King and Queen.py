___ i in range(int(input())):
    K,Q = list(map(str,input().split()))
    # k and q consist of the character which K[0] and Q[0] holds respectively
    k = K[0]
    q = Q[0]
    # kp and qp are the position where the king and queen are located
    kp = int(K[1])
    qp = int(Q[1])
    
    #first condition check if the character of kind and queen are the same
    __ k __ q:
        print("Y",end = ' ')
    ____
        # Second condition check for example e > b 
        __ q > k:
            #even if the columns are different but the row value is same then return Y
            __ qp __ kp:
                print('Y',end = ' ')
            #if row of queen is greater than king row then reduce the value of king to check whether they meet
            ____ qp > kp:
                #get the ascii value of the the character of q
                ascii_val = ord(q)
                #iterate through the w___ loop w___ till the queen position is equal to king position
                # or ascii value of queen column is equal to kings column 
                w___ qp != kp or chr(ascii_val) != k:
                    #reduce the ascii value as king is at lower alphabet and queen position as king is at lower position(number)
                    ascii_val -= 1
                    qp -= 1
                    # if queen position reaches 0 or less than qp then return No and break
                    __ qp __ 0:
                        print('N',end=' ')
                        break
                # if the queen position is equal to kings position and queen character is same as kings
                # return Yes
                __ qp __ kp and chr(ascii_val) __ k:
                    print('Y',end = ' ')
            #if kings position is greater than qp
            ____ qp < kp:
                ascii_val = ord(q)
                #iterate through the w___ loop w___ till the queen position is equal to king position
                # or ascii value of queen column is equal to kings column 
                w___ qp != kp or chr(ascii_val) != k:
                    #reduce the ascii value as king is at lower alphabet and 
                    #increase queen position as king is at higher position(number)
                    ascii_val -= 1
                    qp += 1
                    __ qp > kp:
                        print('N',end=' ')
                        break
                __ qp __ kp and chr(ascii_val) __ k:
                    print('Y',end = ' ')
        #else if exact opposite of the above steps
        ____
             #even if the columns are different but the row value is same then return Y
            __ qp __ kp:
                print('Y',end = ' ')
            #if row of queen is greater than king row then reduce the value of king to check whether they meet
            ____ qp > kp:
                ascii_val = ord(q)
                w___ qp != kp or chr(ascii_val) != k:
                    ascii_val += 1
                    qp -= 1
                    __ qp __ 0:
                        print('N',end=' ')
                        break
                __ qp __ kp and chr(ascii_val) __ k:
                    print('Y',end = ' ')
            ____ qp < kp:
                ascii_val = ord(q)
                w___ qp != kp or chr(ascii_val) != k:
                    ascii_val += 1
                    qp += 1
                    __ qp > kp :
                        print('N',end=' ')
                        break
                __ qp __ kp and chr(ascii_val) __ k:
                    print('Y',end = ' ')
            