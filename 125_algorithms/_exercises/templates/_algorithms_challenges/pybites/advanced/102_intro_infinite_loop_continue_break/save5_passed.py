VALID_COLORS = ['blue', 'yellow', 'red']


___ print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        color = input("Enter a color or enter 'quit'")
        __ color __ "quit":
            print("bye")
            break
        ____ color __ VALID_COLORS:
            print(color.lower())
        ____:
            print("Not a valid color")
        pass