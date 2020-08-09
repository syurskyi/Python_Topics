___ BMI_calculator(
    num_of_people =  int(input())
    result = []
    ___ i in range(0, num_of_people
        weight,height = input().split()
        
        BMI = int(weight)/(float(height)**2)
        
        __ BMI < 18.5:
            result.append('under')
        ____ BMI >= 18.5 and BMI < 25.0:
            result.append('normal')
        ____ BMI >= 25.0 and BMI < 30.0:
            result.append('over')
        ____ BMI >= 30.0:
            result.append('obese')
        ____
            continue
    
    result = ' '.join(str(e) ___ e in result)
    print(result)
    
BMI_calculator()