from random import randint

mini  i..(input("Insert minimum number: "))
maxi  i..(input("Insert maximum number: "))

y  i..(input("Insert range of random numbers: "))

x  [randint(mini,maxi) for i in range(y)]

print(x)