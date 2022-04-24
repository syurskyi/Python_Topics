a i.. )
x l.. m..(i.., i.. ).s..()))

temp 0
temp_ind    # list

# traversing through all the elements of the list expect first.
___ i __ r..(1,l..(x:
    #storing the current element in the temp variable 
    #to compare with element which are sorted
    temp x[i]
    temp_i i
    count 0
    #traverse through the elements which are sorted backwards
    ___ j __ r..(i-1,-1,-1
        #if the temp element is smaller than the sorted number swap them 
        #and see if the n-1 is small or big and continue
        __ temp < x[j]:
            #print('\n comparing',temp,x[j])
            x[temp_i],x[j] x[j],temp
            #decrement the temp_i to traverse backward
            temp_i -_ 1
            count += 1
    print(count,end =' ')
    
#print('\n',x)