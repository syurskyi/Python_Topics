VALID_COLORS = ['blue', 'yellow', 'red']


___ my_print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        inp = input("Enter color:").lower()
        __ inp == 'quit':
            print("bye")
            break

        __ inp not in VALID_COLORS:
            print("Not a valid color")
            continue
    # this else is useless
        else:
            print(inp)

    # thou shall not stop after a match!!!
            break

___ print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        color = input('Enter a color: ').lower()
        __ color == 'quit':
            print('bye')
            break

        __ color not in VALID_COLORS:
            print('Not a valid color')
            continue

        print(color)

print_colors()