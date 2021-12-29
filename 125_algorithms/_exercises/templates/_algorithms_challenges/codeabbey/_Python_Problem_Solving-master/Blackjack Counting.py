#accept the range of input
___ i __ r..(int(input())):
    #accept the types of card
    a = input().s..
    # sort the list keeping A at the end
    predefined_list = ['A']
    a =s..(a, key=l.... x: x __ predefined_list)
    tot = 0
    #for all elements in a
    ___ j __ a:
        try:
            #check if number or not
            temp = float(j)
            tot +=  temp
        except:
            #check if it is other than 'A' then add 10 to total TKJQ
            __ j != 'A':
                tot += 10
            ____:
                #if A then check whether adding A = 11 it goes above 21
                __ tot + 11 > 21:
                    #check if it goes above 21 after adding A = 1
                    __ tot + 1 > 21:
                        #if yes then add 1
                        tot += 1
                    ____:
                        #else add 1
                        tot += 1   
                ____:
                    #else add 11
                    tot += 11
    #check the tot
    __ tot <= 21:
        print(int(tot),end= ' ')
    ____:
        print("Bust",end = ' ')

            
            