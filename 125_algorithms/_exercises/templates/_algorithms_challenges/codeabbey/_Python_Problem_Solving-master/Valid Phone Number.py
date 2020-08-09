f = open('file.txt','r')
a =[]
___ y in f:
    y = y.rstrip()
    __ le.(y) __ 12 or le.(y)__ 14:
        __ y[3] __ '-':
            a,b,c = y.split('-')
            __ le.(a) __ 3 and le.(b)__3 and le.(c)__4:
                print(y,end='\n')
        ____ y[0]__'(' and y[4] __ ')' and y[9]__'-':
            print(y,end='\n')   