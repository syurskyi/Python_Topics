x _ input("Insert numbers only: ")

while type(x) !_ fl..:
    try:
        x _ fl..(x)
    except ValueError:
        print("Error! Please insert only numbers...")
        x _ input("Insert numbers only: ")
print(x/2)