from random import random

x  random()*900+100
x  i..(x)
print(x)

s  str(x)

y  i..(s[0])#x//100
z  i..(s[1])#(x//10)%10
w  i..(s[2])#x % 10

print(y+z+w)