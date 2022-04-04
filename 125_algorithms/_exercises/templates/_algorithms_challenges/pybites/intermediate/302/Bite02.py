VALID_COLORS =  'blue', 'yellow', 'red'


___ print_colors
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    w... T...
        color = input("Enter a color, or quit to stop: ")
        __ color__"Quit" o. color__"quit":
            print('bye')
            _____
        __ color.l.. __ VALID_COLORS:
            print(color.l..
        ____
            print('Not a valid color')