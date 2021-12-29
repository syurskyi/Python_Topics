def get_username():
    # Ask the user to enter their username in this function
    # and return the username
    username = input("What is your username?")
    return username


def print_username(username):
    # Check for truthiness and print the username
    # Print the alternative text if there is no username
    if username == True:
        print(f"Your username is {username}.")
    else: 
        print("Sorry, no username was defined")
        