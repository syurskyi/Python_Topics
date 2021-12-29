___ get_username():
    # Ask the user to enter their username in this function
    # and return the username
    username = input("What is your username?")
    return username


___ print_username(username):
    # Check for truthiness and print the username
    # Print the alternative text if there is no username
    __ username:
        print(f"Your username is {username}.")
    else: 
        print("Sorry, no username was defined.")
        