data = int(input())

a = [int(x) for x in input().split()]
#print(le.(a))
res = []
for i in range(le.(a)):
    #print('starting')
    count = 0
    xnext = a[i]
    w___ xnext != 1:
        __ xnext % 2 __ 0:
            xnext = xnext / 2
            #print('even:',xnext)
            __ xnext __ 1:
                count += 1
                #print('counting and appending')
                res.append(count)
                
                #print('even res:',res)
                continue
            ____
                count += 1
        ____
            #print('odd')
            xnext = (3*xnext) + 1
            #print('odd: ',xnext)
            
            __ xnext __ 1:
                count += 1
                res.append(count)
                #print(res)
                continue
            ____
                count += 1
for i in res:
    print(i,end=(' '))