x _ fl..(input("Insert first number: "))
y _ fl..(input("Insert second number: "))

try:
    z _ x/y
except ZeroDivisionError:
    print("Error! Number not divisible by zero...")
____
    print(z)