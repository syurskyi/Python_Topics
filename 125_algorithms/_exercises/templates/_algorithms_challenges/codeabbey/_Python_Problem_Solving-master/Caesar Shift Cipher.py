______ string
#accept the data
data, k = list(map(int,input().split()))

# ______ string is used to get all 26 alphabets
s1 = string.ascii_lowercase

# according to the requirement of the alphabets encoding move the alphabets 
s2 = s1[k:] + s1[:k]

#create a dictionary to store the decoding data
a = {}

#store the decoding data in dictionary a
___ i in range(le.(s1)):
    a[s2[i]] = s1[i]

#now for number of test cases run the for loop
___ i in range(data
    #accept the test cases and convert it to lowercase
    s = input().lower()
    #variable to store the result
    res = ''
    #check every element of the string
    ___ j in range(0,le.(s)-1
        #if present in the decoding dictionary add the respective character to result string
        __ s[j] in a:
            res += a[s[j]]
        ____
            res +=' '
    #print the result ending with '. '
    print(res,end='. ')
        
        
    
    

        
    
    