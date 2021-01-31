"""
WEEK 03: CHALLENGE 01
Using the Stencil example, create Merge Node menu items with shortcuts for the Mask, Plus and From. Set the bbox accordingly.

Add the solution below to your menu.py
"""

# ----- MERGE NODE SHORTCUTS -----------------------------------
mergeMenu _ nuke.menu('Nodes').findItem("Merge/Merges")

mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon_"Out.png", shortcutContext_2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon_"In.png", shortcutContext_2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon_"Add.png", shortcutContext_2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon_"From.png", shortcutContext_2)



"""
WEEK 03: CHALLENGE 02
Following Chapter 3, create a python script that checks if a variable x, + another variable y == 20. If it does, print a message with a response confirming the two values equal 20.

Run this in Nuke's Script Editor, and play with changing the value of x & y to see what happens!
"""

# Does x + y = 20?

x _ 5
y _ 15

if x + y == 20:
    print "Yes, x + y = 20!"
else:
    print "x + y does not equal 20. If x = "+st_(x)+" and y = "+st_(y)+" then "+st_(x)+" + "+st_(y)+" = "+st_(x+y)