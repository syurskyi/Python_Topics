

print "Hello"


xxa = raw_input("Enter a number\n")

___
    num1= float(xxa)
_______
    print "Invalid input. Please insert a number or type done to finish"


loop= 0
count= 0
running_total= 0
w___ loop ==0:
    inp =  raw_input("Enter a number:")
    
    __ inp== "done" or inp== "Done" :
        ____
        
    ___
        num= float(inp)
    _______
        print "Invalid input. Please insert a number or type done to finish"
        ______
        
    count= count + 1
    
    running_total= running_total + num
        

print count," numbers input" 
print running_total," total"
print "and average:", running_total/count