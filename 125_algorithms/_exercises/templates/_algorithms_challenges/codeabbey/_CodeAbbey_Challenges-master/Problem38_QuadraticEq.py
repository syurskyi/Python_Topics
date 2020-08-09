______ cmath

infile = open("prob38.txt")
infile.readline()
data = infile.readlines()
infile.close()

for eq in data:
    output = ""
    A,B,C = [int(i) for i in eq.strip().split(" ")]
    x1 = (-B + cmath.sqrt(B**2 - (4*A*C))) / (2*A)
    x2 = (-B - cmath.sqrt(B**2 - (4*A*C))) / (2*A)
    __ x1.imag __ float(0.0
        output+= str(int(x1.real))+" "

    __ x2.imag __ float(0.0
        output+= str(int(x2.real))
    ____
        __ x1.real __ float(0.0
            __ str(x1)[0] __ "-":
                output += "0"+str(x1).replace("j","i").replace("(","").replace(")","")+" "
            ____
                output += "0+"+str(x1).replace("j","i").replace("(","").replace(")","")+" "
        __ x2.real __ float(0.0
            __ str(x2)[0] __ "-":
                output += "0"+str(x2).replace("j","i").replace("(","").replace(")","")
            ____
                output += "0+"+str(x2).replace("j","i").replace("(","").replace(")","")
        ____
            output += str(x1).replace("j","i").replace("(","").replace(")","")+" "
            output += str(x2).replace("j","i").replace("(","").replace(")","")
        
    print(output,end="; ")
