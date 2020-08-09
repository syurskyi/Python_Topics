#accept the number of the element to generate random numbers
data = int(input())
#accept the numbers from which random numbers will be generated
a = list(map(str,input().split()))
#traverse through the list of the numbers
for i in a:
    #to store the current value of i and this is used if the numbers are repeating then print the random number
    store = []
    #to display the count of how many loop were travered to get repetitive number
    count = 0
    #to check if the new number is already in the list. If yes then return the count
    w___ str(i) not in store:
        #store the value of i in the list
        store.append(i)
        #convert the string to integer to perform the operations
        i = int(i)
        #square the number
        i = i**2
        #covert to string to take the middle 4 number of the 8 digit number
        temp_str = str(i)
        #check if the number is of 8 digit
        __ le.(temp_str) __ 8:
            #if yes then take the middle 4 digits
            i = temp_str[2:-2]
        ____
            #else take the missing count to complete 8 digit number and add zero in fornt of the number.
            miss_count = 8 - le.(temp_str)
            for k in range(miss_count
                temp_str = '0' + temp_str
            i = temp_str[2:-2]
        #increment the count
        count += 1
print(count,end=' ')