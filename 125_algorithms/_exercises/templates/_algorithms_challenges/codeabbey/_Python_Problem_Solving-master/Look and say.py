# ask for number of iterations
num_iter = int(input('Enter the number of iterations:'))
#initialize the starting element of the sequence
start_num = input('Enter the starting string of the sequence:')

#define the function of lookand say
___ look_and_say(data,maxlen):
    result    # list
    #first iteration to iterate through given iterations by the user
    ___ i __ r..(maxlen-1):
        # defining the number of count of a particular character in the string
        count = 1
        #list to store the count of the character and the character
        res_string    # list
        #Loop for traversing through the length of the given string
        ___ k __ r..(0,l..(data)):
            try:
                #check if the next element is same as the previous element and update the count
                __ data[k] __ data[k+1]:
                    count += 1
                ____:
                    #if the next element is different then store the count as well as the character
                    res_string.a..(s..(count) + data[k])
                    #reinitialize the count
                    count = 1
            except:
                #if the loop has reached its last element then store the count of the character of last element.
                __ k __ l..(data)-1:
                    res_string.a..(s..(count) + data[k])
        #print the updated string with updated count
        data = ''.j..(s..(e) ___ e __ res_string)
        result.a..(data)
        #print(start_num)
    r.. result

look_and_say(start_num,num_iter)