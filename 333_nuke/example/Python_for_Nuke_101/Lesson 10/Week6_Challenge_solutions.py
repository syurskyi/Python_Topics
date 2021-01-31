"""
WEEK 06: CHALLENGE 01

Fix the error checking in shortcut_NodeCustomizer.py so that we can set the node colour without adding a label.
"""

"""
In line 64 of the provided shortcut_nodeCustomizer.py file, remove the 'return',
that way, when both the comment & knob label's values are nothing, it errors and
skips to the next if statement, which is where we're setting our node colour.

Also, we have to add another if statement to the first if statement, like so:
"""

# If the user doesn't enter any data or change anything, pop open a message and exit the window.
if comment_input == "" and panel.value("Knob") == "None":
    if panel.value("Change Node Colour?") == False:
        nuke.message("Please enter a node label")

"""
So if the comment_input and the knob value have no values entered, before the script throws an error,
it's going to check whether the 'Change Node Colour?' checkbox is checked. If it isn't, the error is thrown.

But in our example, we're trying to change the node colour without setting any other values.
So that second 'if' statement will return 'True'. Usually, this would be passed off to the
'else' part of the if/else statement, but we haven't provided an 'else' here. So when:
"""
panel.value("Change Node Colour?") == True

"""
It skips the rest of the if / elif / else statement, and goes straight to line 81 where
we're setting the node's 'tile_color' knob.

Check the included '/.nuke/python/shortcut_NodeCustomizer.py' file for the completed solution.

"""






"""
WEEK 06: CHALLENGE 02
Create a panel that creates a user-specified node, a user-specified amount of times.

This was super tricky because you had to find knowledge I hadn't taught you yet!
"""

def create_nodes():


    # Create a panel
    panel = nuke.Panel("Node Creator")

    # Add knobs
    panel.addSingleLineInput("Node Class", "")
    panel.addSingleLineInput("Number of Nodes to create", "")

    # Show the panel
    if not panel.show():
        return

    # Add the user-input values from our knobs to variables for easy access
    nodeClass = panel.value("Node Class")
    number = panel.value("Number of Nodes to create")


    # --- ERROR CHECKING ---------------------------------------------

    # Check if node class has been filled in. If not, show an error message to the user.
    if nodeClass == "":
        nuke.message("Please enter a node Class to create")
        return

    # Check if number has been entered. If not, show an error message to the user.
    if number == "":
        nuke.message("Please enter the number of "+nodeClass+" nodes you would like to create.")
        return

    # Check if the user input data for the number of nodes to create is actually a number. If not, show an error message.
    # Let's use try / except here instead for bonus points!
    try:
    	int(number)
	except:
		nuke.message("Please enter a number, not text, for the amount of "+nodeClass+" nodes you want to create...")


    # Iterate from 0 to the number input by the user. Since the input returns a string, we have to convert it to an integer.
    for i in range(0, int(number)):
        # For every iteration, we're creating a node, defined by the node Class entered by the user.
        try:
        	nuke.createNode(nodeClass)
    	except:
	        nuke.message(nodeClass+" is not a valid Node Class")
	        return


# Run the function
create_nodes()




"""
WEEK 06: BONUS POINTS
Use try/except for error checking, instead of if / else.


As you can see at the end of the above example, we're doing exactly that! There's a small difference in handling errors this way,
but it's sometimes preferential. When you run an if statement, and that statement returns false, it's going to return an error.
Whereas when you "try" something, is passes that error through to the exception.

It's very similar logic to if / else, although it's a little cleaner programatically.
"""

