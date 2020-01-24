def interact():
    while True:
        try:
            user_input = int(input('Please input an integer:'))  # try to turn user input into an integer
        except ValueError:
            print('Please input an integer only.')  # print a message if user didn't input an integer
        else:
            print('{} is {}.'.format(user_input,
                                     'even' if user_input % 2 == 0 else 'odd'))  # print even/odd if the user input an integer
        finally:  # regardless of the previous input being valid or not
            user_input = input('Do you want to play again? (y/N):')  # ask if the user wants to play again
            if user_input != 'y':  # quit if the user didn't input `y`
                print('Goodbye.')
                break  # break the while loop to quit