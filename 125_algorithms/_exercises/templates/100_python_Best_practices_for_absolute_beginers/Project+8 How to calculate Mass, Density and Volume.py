mdv  input("Choose one to calculate(m,d,v) : ")

__ mdv __ 'm':
    d  float(input("Density: "))
    v  float(input("Volume: "))
    result  d*v #This is for mass
elif mdv __ 'd':
    m  float(input("Mass: "))
    v  float(input("Volumn: "))
    result  m/v #This is for density
elif mdv __ 'v':
    m  float(input("Mass: "))
    d  float(input("Density: "))
    result  m/d;
print("%.2f" % result)