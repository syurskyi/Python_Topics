"""
WEEK 07: CHALLENGE 01

Create a dictionary that holds the name of five to ten people you know, and their ages. Then show a message box with a human-readable message. E.g:
• Dad is 62 years old
• Karen is 26 years old
• etc.

Bonus points: Print the names of the people in the list in their 20s or 30s.

Extra bonus points: Count the totals and print a list of how many people you know in their 20’s, 30’s, 40’s, 50’s and 60’s.

"""

# Create dictionary of people & their ages.
dictionary _ {'Dad': 62, 'Mum': 58, 'Thomas': 34, 'Karen': 26, 'Bobby': 32, 'Ryan': 28, 'Ravi': 27, 'Hannah': 30, 'Lisa': 34, 'Jeremy': 12}

# Print a heading to tell the user what is being displayed.
print "\n\nAGES OF PEOPLE I KNOW:\n"

# Loop through the dictionary.
___ person __ dictionary:
    # Print person (key) is dictionary[person] (value) years old.
    print person+" is "+st_(dictionary[person])+" years old."

# Print another heading to tell the user what is being displayed.
print "\n\nPEOPLE I KNOW IN THEIR TWENTIES:\n"

# Loop through the dictionary.
___ person __ dictionary:
    # If the keys in the dictionary have a value of less-than 30 and more-than-or-equal-to 20, then:
    if dictionary[person] < 30 and dictionary[person] >_ 20:
        # Print the keys (names of the people) who's values (ages) match the above conditions.
        print person


# EXTRA BONUS POINTS

# Create some lists to hold the names of people in each category
twenties _ []
thirties _ []
forties _ []
fifties _ []
sixties _ []

# Loop through the dictionary.
___ person __ dictionary:
    # If the keys in the dictionary have a value of less-than 30 and more-than-or-equal-to 20, then:
    if dictionary[person] < 30 and dictionary[person] >_ 20:
        # Add the names of the people (keys) who's ages (values) match the above conditions.
        twenties.append(person)


# RINSE AND REPEAT FOR EACH CATEGORY

___ person __ dictionary:
    if dictionary[person] < 40 and dictionary[person] >_ 30:
        thirties.append(person)

___ person __ dictionary:
    if dictionary[person] < 50 and dictionary[person] >_ 40:
        forties.append(person)

___ person __ dictionary:
    if dictionary[person] < 60 and dictionary[person] >_ 50:
        fifties.append(person)

___ person __ dictionary:
    if dictionary[person] < 70 and dictionary[person] >_ 60:
        sixties.append(person)


# Print a couple line breaks...
print "\n\n"

# Print some human-readable strings to return the results.

# The magic is happening by finding the number of items in each list using the len() function,
# then converting that number to a string.
print "I know "+st_(len(twenties))+" people in their 20's"
print "I know "+st_(len(thirties))+" people in their 30's"
print "I know "+st_(len(forties))+" people in their 40's"
print "I know "+st_(len(fifties))+" people in their 50's"
print "I know "+st_(len(sixties))+" people in their 60's"
        




"""
WEEK 07: CHALLENGE 02

Add functionality to our shortcut_operationSwitcher() function to switch between log2lin and lin2log in the Log2Lin node.

"""

# Add the new key:value item to your dictionary
merge_ops _ {'over':'under', 'mask':'stencil', 'plus':'from', 'multiply':'divide', 'max':'min', 'conjoint-over':'disjoint-over', 'log2lin':'lin2log'}

# Then add a second condition to the if statement, to account for the new node class.
if node.Class() == "Merge2" or node.Class() == "Log2Lin":
        




"""
WEEK 07: CHALLENGE 03

Add functionality to our shortcut_operationSwitcher() function to create an “Invert” node if no other node is selected.

"""

# Right at the start of our function, we should run a try/except statement.

# If a node is selected, we assign it to a variable called 'node'.

# If a node isn't selected, a ValueError will be thrown which triggers the 'except' statement.
# An Invert node will be created, and then the function will exit.

try:
    node _ nuke.sN..
except:
    nuke.createNode('Invert')
    return



# Check out the shortcut_operationSwitcher.py file in the python folder for this weeks course material to see Challenge 02 & 03 in action!