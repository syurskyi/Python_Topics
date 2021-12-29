#run the for loop for the number of elements
___ i __ r..(int(input())):
    
    #accept the value of a,c,m,x,n in a list
    listo = l..(map(int,input().split()))
    
    #assign the list to variables
    a,c,m,x,n = listo
    
    #run the loop to get the value of the nth number
    ___ j __ r..(n):
        x = (a*x + c) % m
        
    #print the output
    print(x,end = ' ')