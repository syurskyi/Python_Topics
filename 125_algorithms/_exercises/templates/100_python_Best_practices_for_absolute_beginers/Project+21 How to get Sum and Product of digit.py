x  abs(i..(input("Insert integer values only: ")))

s..  0
mul  1

w___ x ! 0:
    digit  x%10
    s.. + digit
    mul * digit

    x  x/10

print("Sum of digit = ",s..)
print("Product of digit = ",mul)