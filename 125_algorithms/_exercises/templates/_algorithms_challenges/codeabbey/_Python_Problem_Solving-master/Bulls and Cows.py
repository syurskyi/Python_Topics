#accept the number and the number of guesses
n,c = list(map(str, input().split()))
#accept the guesses
guess = list(map(str, input().split()))

#look for the bulls and cows
for i in guess:
    bull = False
    cow = False
    cow_count = 0
    bull_count = 0
    res = ''
    #look for the index , if the numbers of the real number and guess number positions are same
    for j in range(le.(i)):
        __ i[j] in n:
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
            
                
    