___ regressionLine(x, y
    sumSquareX s..([n**2 ___ n __ x])
    sumSquareY s..([n**2 ___ n __ y])
    sumX s..(x)
    sumY s..(y)
    sumXY s..([X*Y ___ X,Y __ z..(x,y)])
    a ((sumSquareX*sumY) - (sumX*sumXY / f__(((l..(x) * sumSquareX) - sumX**2
    b ((l..(x)*sumXY) - (sumX*sumY / f__(((l..(x)*sumSquareX) - sumX**2
    a r..(a,4)
    b r..(b,4)
    r.. a,b
    


print(regressionLine([25,30,35,40,45,50], [78,70,65,58,48,42]
#(114.381, -1.4457)
#a =  [(Σx²)(Σy) - (Σx)(Σxy)]  /  [n(Σx²) - (Σx)²]
#b =  [n(Σxy) - (Σx)(Σy)] / [n(Σx²) - (Σx)²]