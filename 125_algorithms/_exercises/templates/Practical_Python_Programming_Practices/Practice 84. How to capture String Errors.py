x _ input("Insert numbers only: ")

while type(x) !_ float:
    try:
        x _ float(x)
    except ValueError:
        print("Error! Please insert only numbers...")
        x _ input("Insert numbers only: ")
print(x/2)