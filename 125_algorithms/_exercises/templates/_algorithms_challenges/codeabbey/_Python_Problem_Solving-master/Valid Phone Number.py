f = open('file.txt','r')
a =[]
for y in f:
    y = y.rstrip()
    __ len(y) == 12 or len(y)== 14:
        __ y[3] == '-':
            a,b,c = y.split('-')
            __ len(a) == 3 and len(b)==3 and len(c)==4:
                print(y,end='\n')
        elif y[0]=='(' and y[4] == ')' and y[9]=='-':
            print(y,end='\n')   