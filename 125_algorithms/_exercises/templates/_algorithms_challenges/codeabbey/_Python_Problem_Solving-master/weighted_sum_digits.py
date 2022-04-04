#ask user for number of records
data = i..(input
result    # list
#run the following logic while list result is less than data
w.... l..(result) < data:
    #split all the records so that it can be accessed differently
    num = input().s..
    ___ i __ r..(0,l..(num:
        
        digitsum = 0
        #take data individually to perform weighted sum
        currnum = num[i]
        
        #get the length of the current weighted sum
        ___ j __ r..(1,l..(currnum)+1
            #calculate the sum
            digitsum +=j * i..(currnum[j-1])
        #appending the result to the result list
        result.a..(digitsum)

#displaying the records
___ i __ result:
    print(i,end=(' '