# Enter your code within the following function
def get_username():
    while True:
        username = input("Please type in the name 'PyBites':")
        if username == "PyBites":
            break
        else:
            print("Invalid username.")