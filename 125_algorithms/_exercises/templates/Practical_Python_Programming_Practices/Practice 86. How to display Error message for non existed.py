fp _ i..("Enter file path: ")

___
    file _ o..(fp)
______ FileNotFoundError:
    print("Error! This file path does not exist...")
____
    print(file.read