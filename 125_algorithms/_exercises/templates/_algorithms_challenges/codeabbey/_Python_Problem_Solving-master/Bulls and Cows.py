#accept the number and the number of guesses
n,c = l..(map(str, input().split()))
#accept the guesses
guess = l..(map(str, input().split()))

#look for the bulls and cows
___ i __ guess:
    bull = False
    cow = False
    cow_count = 0
    bull_count = 0
    res = ''
    #look for the index , if the numbers of the real number and guess number positions are same
    ___ j __ r..(l..(i)):
        __ i[j] __ n:
            bull = True
            __ i[j] __ n[j]:
                cow = True
        __ bull and cow:
            cow_count += 1 
            bull = cow = False
        __ bull:
            bull_count += 1
            bull = False
    res = str(cow_count)+'-'+str(bull_count)
    print(res,end=' ')
            
                
    