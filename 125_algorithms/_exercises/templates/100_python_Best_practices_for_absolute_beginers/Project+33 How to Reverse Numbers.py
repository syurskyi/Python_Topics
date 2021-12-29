x  i..(input("Insert some numbers: "))
y  0

z  x

w___ x ! 0:
    digit  x%10
    x  x//10
    y  y*10
    y  y+digit
print("The reversed of ",z," = ",y)