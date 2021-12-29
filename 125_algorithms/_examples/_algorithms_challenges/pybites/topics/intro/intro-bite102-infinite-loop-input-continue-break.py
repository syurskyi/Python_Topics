VALID_COLORS = ['blue', 'yellow', 'red']


def my_print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        inp = input("Enter color:").lower()
        if inp == 'quit':
            print("bye")
            break

        if inp not in VALID_COLORS:
            print("Not a valid color")
            continue
    # this else is useless
        else:
            print(inp)

    # thou shall not stop after a match!!!
            break

def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        color = input('Enter a color: ').lower()
        if color == 'quit':
            print('bye')
            break

        if color not in VALID_COLORS:
            print('Not a valid color')
            continue

        print(color)

print_colors()