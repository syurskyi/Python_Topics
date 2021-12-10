

print "Hello"


xxa = raw_input("Enter a number\n")

try:
    num1= float(xxa)
except:
    print "Invalid input. Please insert a number or type done to finish"


loop= 0
count= 0
running_total= 0
while loop ==0:
    inp =  raw_input("Enter a number:")
    
    if inp== "done" or inp== "Done" :
        break
        
    try:
        num= float(inp)
    except:
        print "Invalid input. Please insert a number or type done to finish"
        continue 
        
    count= count + 1
    
    running_total= running_total + num
        

print count," numbers input" 
print running_total," total"
print "and average:", running_total/count