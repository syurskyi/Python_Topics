VALID_COLORS =  'blue', 'yellow', 'red' 


___ my_print_colors
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    w... T...
        inp = input("Enter color:").l..
        __ inp __ 'quit':
            print("bye")
            _____

        __ inp n.. __ VALID_COLORS:
            print("Not a valid color")
            _____
    # this else is useless
        ____:
            print(inp)

    # thou shall not stop after a match!!!
            _____

___ print_colors
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    w... T...
        color = input('Enter a color: ').l..
        __ color __ 'quit':
            print('bye')
            _____

        __ color n.. __ VALID_COLORS:
            print('Not a valid color')
            _____

        print(color)

print_colors()