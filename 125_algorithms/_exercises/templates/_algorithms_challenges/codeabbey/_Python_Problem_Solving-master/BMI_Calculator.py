___ BMI_calculator():
    num_of_people =  int(input())
    result    # list
    ___ i __ r..(0, num_of_people):
        weight,height = input().s.. 
        
        BMI = int(weight)/(float(height)**2)
        
        __ BMI < 18.5:
            result.a..('under')
        ____ BMI >= 18.5 a.. BMI < 25.0:
            result.a..('normal')
        ____ BMI >= 25.0 a.. BMI < 30.0:
            result.a..('over')
        ____ BMI >= 30.0:
            result.a..('obese')
        ____:
            continue
    
    result = ' '.join(s..(e) ___ e __ result)
    print(result)
    
BMI_calculator()