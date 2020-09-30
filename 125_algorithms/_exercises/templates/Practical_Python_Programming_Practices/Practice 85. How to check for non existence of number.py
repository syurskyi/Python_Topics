x _ 20
y _ 30
z _ 40

value _ input("Insert variable x,y,z only: ")

try:
    exec("print("+value+")")
except NameError:
    print("Incorrect variable name!")