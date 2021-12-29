#accepting the two strings
s1 = ''.join(i ___ i __ input() __ i.islower())
s2 = ''.join(i ___ i __ input() __ i.islower())
#using sorted to arrange the string in order before processing them
s1 = s..(s1)
s2 = s..(s2)

#defining the method mix
___ mix(s1,s2):
    
    s1 = ''.join(i ___ i __ s1 __ i.islower())
    s2 = ''.join(i ___ i __ s2 __ i.islower())

    s1 = s..(s1)
    s2 = s..(s2)
    #s1_dic is used to store the count of occurance of a particular
    #alphabet in string s1 and similarly of s2_dic for string s2
    s1_dic = {}
    s2_dic = {}
    
    #sub_str is used to store the alphabets for the number of counts(iterations)
    # for example: count of n is 5 thus sub_str will hold sub_str = 'nnnnn'
    sub_str = ''
    
    #main_string holds the final string that is to be returned
    main_string = ''
    
    #res_string is used to store the sub_str for alphabets and then later it is sorted
    res_string    # list

    #this for loop is used to record the count of a particular alphabet in the dictionary for string s1
    ___ i __ s1:
        count = s1.c.. i)
        #check if the current character is present in dictionary. if not then add the char to dictionary
        __ i n.. __ s1_dic:
            s1_dic[i] = count
    #this for loop is used to record the count of a particular alphabet in the dictionary for string s2
    ___ i __ s2:
        count = s2.c.. i)
        #check if the current character is present in dictionary. if not then add the char to dictionary
        __ i n.. __ s2_dic:
            s2_dic[i] = count

    #print(s1_dic)
    #print(s2_dic)
    
    # to check the if the same element are present in both the dictionary of s1 and s2
    ___ i __ s1_dic:
        sub_str = ''
        __ i __ s2_dic:
            #here the count>1 constraint is taken care of 
            __ s1_dic[i] > 1 o. s2_dic[i] > 1:
                #if the same element is present in both s1 and s2 and count is same
                __ s1_dic[i] __ s2_dic[i]:
                    ___ j __ r..(s1_dic[i]):
                        sub_str += i
                    res_string.a..('=:' + sub_str)
                #if the same element is present in both s1 and s2 and count of s1 is greater than s2
                ____ s1_dic[i] > s2_dic[i]:
                    ___ j __ r..(s1_dic[i]):
                        sub_str += i
                    res_string.a..('1:' + sub_str)
                ____:
                    ___ j __ r..(s2_dic[i]):
                        sub_str += i
                    res_string.a..('2:' + sub_str)
        ____:
            __ s1_dic[i] > 1:
                ___ j __ r..(s1_dic[i]):
                    sub_str += i
                res_string.a..('1:' + sub_str)
                
    ___ i __ s2_dic:
        sub_str = ''
        __ i n.. __ s1_dic:
            __ s2_dic[i] > 1:
                ___ j __ r..(s2_dic[i]):
                    sub_str += i
                res_string.a..('2:' + sub_str)
                
            
                    
        

# Once we got the string here the problem is that it is not sorted the form that is desired
#so the next few cycles will help us to sort the given string according to the desired result
#here the string is sorted on the basis of the length of the string
    
    ___ i __ r..(l..(res_string)):
        ___ j __ r..(0,l..(res_string)-1):
            
            # check if the string is less than the next item in the list if yes swap the two string
            __ l..(res_string[j]) < l..(res_string[j+1]):
                res_string[j],res_string[j+1]= res_string[j+1],res_string[j]
            
            #check if the string is having the same lenth
            ____ l..(res_string[j]) __ l..(res_string[j+1]):
               
                #check if the string first element is integer or has a '=' 
                #here try and except block helps program from terminating
                try:
                    #convert the strings first element to float 
                    check_int1 = float(res_string[j][0])
                    check_int2 = float(res_string[j+1][0])
                    #if the variable is in integer form then proceed
                    __ check_int1.is_integer() a.. check_int2.is_integer():
                        
                        #Here we check if the integer is greater or no if yes then swap
                        __ check_int1 > check_int2:
                            res_string[j],res_string[j+1]=res_string[j+1],res_string[j]
                            
                        #if the integer is equal then we check for the 
                        #precedence of the char in alphabet set and sort accordingly
                        ____ check_int1 __ check_int2:
                            __ res_string[j][2] > res_string[j+1][2]:
                                res_string[j],res_string[j+1]=res_string[j+1],res_string[j]
                except:
                    
                    #if jth and j+1th element has = sign then proceed
                    __ res_string[j][0] __ '=' a.. res_string[j+1][0] __ '=':
                        
                        #if the char of jth is greater than j+1th char then swap
                        __ res_string[j][2] > res_string[j+1][2]:
                            res_string[j],res_string[j+1]=res_string[j+1],res_string[j]
                            
                    # if the jth element is having the '=' sign then it is swaped
                    ____ res_string[j][0] __ '=':
                        res_string[j],res_string[j+1] = res_string[j+1],res_string[j]
                    
                    ____:
                        pass
            ____:
                pass
    
    
    main_string = '/'.join(s..(e) ___ e __ res_string)
    r.. main_string
    
mix(s1,s2)