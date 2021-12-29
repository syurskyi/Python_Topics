#number of measurements to inserted
data = int(input())
#enter all the measurements seperated by space
mea = l..(map(float, input().s..()))
#this array is used to store the results
mea_store    # list

#traversing through each element of the measurements
___ i __ r..(l..(mea)):
    #if first element then store it in the result
    __ i __ 0:
        mea_store.a..(mea[i])
    #if last element then store it in the result array
    ____ i__ l..(mea)-1:
        mea_store.a..(mea[i])
        break
    #else calculate the average of the middle numbers and store in the result
    ____:
        res = (mea[i]+mea[i-1]+mea[i+1])/3
        mea_store.a..(res)
        
#printing the values 
___ i __ mea_store:
    print(i,end=' ')
    