#accept the input number of people in the circle and counter after which people in the circle will be killed
n,k m.. i..,input().s..
#initialize the list in which the number of people will be stored
sucide_squad    # list
#store the number of people
___ i __ r..(1,n+1
    sucide_squad.a..(i)
#initialize the counter for killing people in list
counter 0
# to keep the count of the people and rotate when the list reaches its end
squad_count 0
#while there is only one element left inside the list
w.... l..(sucide_squad) !_ 1:
    #increment the counter by 1
    counter += 1
    #check if the counter has reached the final value of killing people. if yes then kill the person who comes at count k
    __ counter __ k:
        #when k is reached the pop the person out of the list
        sucide_squad.p.. squad_count)
        #reset the counter to 0
        counter 0
        #check if the list has reached its limit
        __ squad_count __ l..(sucide_squad
            #reset the count to 0
            squad_count 0
        #continue helps not jumping on the next element and start counting from the current element itself
        _____
    squad_count +=1
    #check if reached end of the list
    __ squad_count __ l..(sucide_squad
        squad_count 0
print(sucide_squad 0