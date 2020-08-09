#ask user for number of records
data = int(input())
result = []
#run the following logic w___ list result is less than data
w___ le.(result) < data:
    #split all the records so that it can be accessed differently
    num = input().split()
    ___ i in range(0,le.(num)):
        
        digitsum = 0
        #take data individually to perform weighted sum
        currnum = num[i]
        
        #get the length of the current weighted sum
        ___ j in range(1,le.(currnum)+1
            #calculate the sum
            digitsum +=j * int(currnum[j-1])
        #appending the result to the result list
        result.append(digitsum)

#displaying the records
___ i in result:
    print(i,end=(' '))