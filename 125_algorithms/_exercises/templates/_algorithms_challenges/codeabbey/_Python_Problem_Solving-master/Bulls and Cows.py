#accept the number and the number of guesses
n,c  l.. m..(s.., i.. ).s..()))
#accept the guesses
guess  l.. m..(s.., i.. ).s..()))

#look for the bulls and cows
___ i __ guess:
    bull  F..
    cow  F..
    cow_count  0
    bull_count  0
    res  ''
    #look for the index , if the numbers of the real number and guess number positions are same
    ___ j __ r..(l..(i:
        __ i[j] __ n:
            bull  T..
            __ i[j] __ n[j]:
                cow  T..
        __ bull a.. cow:
            cow_count + 1 
            bull  cow  F..
        __ bull:
            bull_count + 1
            bull  F..
    res  s..(cow_count)+'-'+s..(bull_count)
    print(res,end' ')
            
                
    