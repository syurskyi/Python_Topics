_______ string
#accept the data
data, k = l..(map(i..,input().s..()))

# import string is used to get all 26 alphabets 
s1 = string.ascii_lowercase

# according to the requirement of the alphabets encoding move the alphabets 
s2 = s1[k:] + s1[:k]

#create a dictionary to store the decoding data
a    # dict

#store the decoding data in dictionary a
___ i __ r..(l..(s1)):
    a[s2[i]] = s1[i]

#now for number of test cases run the for loop
___ i __ r..(data):
    #accept the test cases and convert it to lowercase
    s = input().l..
    #variable to store the result
    res = ''
    #check every element of the string
    ___ j __ r..(0,l..(s)-1):
        #if present in the decoding dictionary add the respective character to result string
        __ s[j] __ a:
            res += a[s[j]]
        ____:
            res +=' '
    #print the result ending with '. '
    print(res,end='. ')
        
        
    
    

        
    
    