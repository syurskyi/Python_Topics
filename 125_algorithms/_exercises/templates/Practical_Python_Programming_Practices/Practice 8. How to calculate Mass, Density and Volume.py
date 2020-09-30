mdv _ input("Choose one to calculate(m,d,v) : ")

__ mdv __ 'm':
    d _ fl..(input("Density: "))
    v _ fl..(input("Volume: "))
    result _ d*v #This is for mass
elif mdv __ 'd':
    m _ fl..(input("Mass: "))
    v _ fl..(input("Volumn: "))
    result _ m/v #This is for density
elif mdv __ 'v':
    m _ fl..(input("Mass: "))
    d _ fl..(input("Density: "))
    result _ m/d;
print("%.2f" % result)