mdv _ input("Choose one to calculate(m,d,v) : ")

__ mdv __ 'm':
    d _ float(input("Density: "))
    v _ float(input("Volume: "))
    result _ d*v #This is for mass
elif mdv __ 'd':
    m _ float(input("Mass: "))
    v _ float(input("Volumn: "))
    result _ m/v #This is for density
elif mdv __ 'v':
    m _ float(input("Mass: "))
    d _ float(input("Density: "))
    result _ m/d;
print("%.2f" % result)