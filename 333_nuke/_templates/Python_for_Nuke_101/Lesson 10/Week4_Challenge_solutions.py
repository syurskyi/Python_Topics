"""
WEEK 04: CHALLENGE 01
With the new knowledge you have gained this week, I would like you to extend our ShuffleRGBchannels() function to also
create a merge node that connects our 3 shuffle nodes, and set its operation to ‘max’.

Add the solution below to your shuffleShortcuts.py, below line 73 (  blueShuffle['ypos'].setValue(selectedNode_yPos+150)  )
"""

# Create merge node and set the operation to max, connect the inputs to our 3 shuffle nodes, then Transform the Merge node into place.
mergeNode _ nuke.createNode("Merge2")
mergeNode['operation'].setValue("max")
mergeNode.setInput(0, redShuffle)
mergeNode.setInput(1, greenShuffle)
mergeNode.setInput(3, blueShuffle)
mergeNode['xpos'].setValue(selectedNode_xPos)
mergeNode['ypos'].setValue(selectedNode_yPos+300)
