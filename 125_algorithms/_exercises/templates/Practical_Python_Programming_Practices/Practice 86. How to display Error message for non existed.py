fp _ input("Enter file path: ")

try:
    file _ open(fp)
except FileNotFoundError:
    print("Error! This file path does not exist...")
____
    print(file.read