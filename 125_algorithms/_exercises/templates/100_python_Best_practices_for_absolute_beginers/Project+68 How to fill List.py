from random import randint

def list_fill(first, qyt, mini, maxi):
    for i in range(qyt):
        first.append(randint(mini,maxi))

minimum  i..(input("Insert minimum value: "))
maximum  i..(input("Insert maximum value: "))
num  i..(input("Number of elements: "))
x  []

list_fill(x,num,minimum,maximum)
print(x)