______ ma__

___ i in range(int(input())):
    x1,y1,x2,y2,x3,y3 = list(map(int,input().split()))
    
    #distance formula

    a = ma__.sqrt((x2-x1)**2 + (y2-y1)**2)
    b = ma__.sqrt((x3-x1)**2 + (y3-y1)**2)
    c = ma__.sqrt((x3-x2)**2 + (y3-y2)**2)
    
    #Heron's formula s = 1/2(a+b+c)
    s = 0.5 * (a + b + c)
    s1= abs(s-a) 
    s2 = abs(s-b) 
    s3 =abs(s-c)
    area = s * s1 * s2 * s3
    __ (area - int(area)) > 0.5:
        area += 0.5
        area = int(area)
    ____
        area = int(area)
    area = ma__.sqrt(area)
    print(area,end=' ')