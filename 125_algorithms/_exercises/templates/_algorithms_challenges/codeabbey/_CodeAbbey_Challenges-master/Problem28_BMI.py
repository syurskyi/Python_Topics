with open("prob28.txt") as infile:
    infile.readline()
    data= infile.readlines()
    ___ line in data:
        weight,height = line.strip().split(" ")
        bmi = lambda x,y : int(x)/(float(y)**2)
        
        ans =float(bmi(weight,height))
        __ ans < 18.5:
            print("under",end=" ")
        ____ ans < 25.0:
            print("normal",end=" ")
        ____ ans < 30.0:
            print("over",end= " ")
        ____
            print("obese",end=" ")
            
