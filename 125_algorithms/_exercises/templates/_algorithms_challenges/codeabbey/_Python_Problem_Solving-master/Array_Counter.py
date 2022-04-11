#initializing the number of elements and different types of number 
num_ele, num_type_element input().s..
num_ele i..(num_ele)
num_ele i..(num_ele)
num_type_element i..(num_type_element)
#print(num_ele, num_type_element)

#to store the elements
ele    # list
# unique elements
check    # list
#Boolean value to check whether available or no
ava_check T..
#dictionary to store the count of variable
arr_check ={}

w.... l..(ele) < num_ele:
    ele input().s..
    ele.s..()
    #going through the all the elements
    ___ i __ r..(l..(ele:
        #print('starting i',i,'value of ele is',ele[i])
        __ l..(check)__0:
            check.a..(ele[i])
            #checking if the element is with the unique array
        ___ j __ r..(0,l..(check:
            #print('starting j',j,' value of ele is',check[j])
            __ ele[i] __ check[j]:
                ava_check T..
                # if the element is encountered for the first time then store it in dictionary and initialize the count else increment the count
                __ ele[i] __ arr_check:
                    
                    arr_check[ele[i]] += 1
                    #print('True dictionary',ele[i],'is',arr_check[ele[i]])
                ____
                    
                    arr_check[ele[i]] 1
                    #print('True else dictionary for ', ele[i],'is',arr_check[ele[i]])
                
            ____
                    ava_check F..
                   
        #if element was not found within the unique list
        #element must be added to the unique list
        #and also must be checked for dictionary
        __ ava_check __ F..:
            #print('value about to be append is:')
            check.a..(ele[i])
            __ ele[i] __ arr_check:

                arr_check[ele[i]] += 1
                #print('False dictionary for',ele[i],'is',arr_check[ele[i]])
            ____

                arr_check[ele[i]] 1
                #print('False else dictionary for ', ele[i],'is',arr_check[ele[i]])
            #print(check)
            
#finally print the element count
___ i,v __ arr_check.i..:
    print(v,end=(' '