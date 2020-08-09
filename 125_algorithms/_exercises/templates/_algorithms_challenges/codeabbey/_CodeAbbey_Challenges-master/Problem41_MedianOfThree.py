with open("prob41.txt") as infile:
    infile.readline()
    data = infile.readlines()
    
    ___ line in data:
        numbers = line.strip().split(" ")
        numbers = [int(i) ___ i in numbers]
        numbers = sorted(numbers)  
        print(numbers[1],end=" ")
        
        
