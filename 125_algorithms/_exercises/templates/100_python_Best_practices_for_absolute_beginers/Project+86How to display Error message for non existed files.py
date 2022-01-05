fp  input("Enter file path: ")

___
    file  open(fp)
______ FileNotFoundError:
    print("Error! This file path does not exist...")
____:
    print(file.read())