x _ float(input("Insert first number: "))
y _ float(input("Insert second number: "))

try:
    z _ x/y
except ZeroDivisionError:
    print("Error! Number not divisible by zero...")
____
    print(z)