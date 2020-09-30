fp _ input("Enter file path: ")

try:
    file _ o..(fp)
except FileNotFoundError:
    print("Error! This file path does not exist...")
____
    print(file.read