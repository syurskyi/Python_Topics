x  20
y  30
z  40

value  input("Insert variable x,y,z only: ")

___
    exec("print("+value+")")
______ NameError:
    print("Incorrect variable name!")