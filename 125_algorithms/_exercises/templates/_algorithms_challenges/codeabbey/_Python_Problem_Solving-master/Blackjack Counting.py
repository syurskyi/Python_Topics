#accept the range of input
for i in range(int(input())):
    #accept the types of card
    a = input().split()
    # sort the list keeping A at the end
    predefined_list = ['A']
    a =sorted(a, key=lambda x: x in predefined_list)
    tot = 0
    #for all elements in a
    for j in a:
        try:
            #check if number or not
            temp = float(j)
            tot +=  temp
        except:
            #check if it is other than 'A' then add 10 to total TKJQ
            __ j != 'A':
                tot += 10
            else:
                #if A then check whether adding A = 11 it goes above 21
                __ tot + 11 > 21:
                    #check if it goes above 21 after adding A = 1
                    __ tot + 1 > 21:
                        #if yes then add 1
                        tot += 1
                    else:
                        #else add 1
                        tot += 1   
                else:
                    #else add 11
                    tot += 11
    #check the tot
    __ tot <= 21:
        print(int(tot),end= ' ')
    else:
        print("Bust",end = ' ')

            
            