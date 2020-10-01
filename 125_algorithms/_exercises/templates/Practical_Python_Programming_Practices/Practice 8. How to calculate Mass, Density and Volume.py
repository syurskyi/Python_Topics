mdv _ i..("Choose one to calculate(m,d,v) : ")

__ mdv __ 'm':
    d _ fl..(i..("Density: "))
    v _ fl..(i..("Volume: "))
    result _ d*v #This is for mass
____ mdv __ 'd':
    m _ fl..(i..("Mass: "))
    v _ fl..(i..("Volumn: "))
    result _ m/v #This is for density
____ mdv __ 'v':
    m _ fl..(i..("Mass: "))
    d _ fl..(i..("Density: "))
    result _ m/d;
print("%.2f" % result)