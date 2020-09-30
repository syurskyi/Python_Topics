x _ 20
y _ 30
z _ 40

value _ input("Insert variable x,y,z only: ")

___
    exec("print("+value+")")
______ NameError:
    print("Incorrect variable name!")