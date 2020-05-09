# Filename: linkedlist.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is to create a doubly linked list example.
#          The single linked list can be achieved by removing the previous node reference.


# Name: Node
# Arguments: (object) - inhereting from object class
# Purpose: This is a template for a node in a linked list
c_ Node(object):
    
    #Constructor:
    ___  -   dataSet, next _ None, prev _ None):
        data _ dataSet
        nextNode _ next
        prevNode _ prev

    #Getter for next node:
    ___ getNextNode 
        r_ nextNode

    #Setter for next node:
    ___ setNextNode   next):
        nextNode _ next

    #Getter for previous node:
    ___ getPrevNode 
        r_ prevNode

    #Setter for previous node:
    ___ setPrevNode   prev):
        prevNode _ prev

    #Getter for data:
    ___ getData 
        r_ data

    #Setter for data:
    ___ setData   dataSet):
        data _ dataSet

# Name: LinkedList
# Arguments: (object) - inhereting from object class
# Purpose: This class holds methods for LinkedList controls (getSize, addNode, removeNode, findNode, getAllData)
c_ LinkedList (object):
    	#Constructor:
	___  -   rootNode _ None):
		root _ rootNode
		size _ 0
		
	___ getSize 
		r_ size
		
	___ addNode   dataSet):
		newNode _ Node (dataSet, root)
		if (root):
			root.setPrevNode(newNode)
		root _ newNode
		size +_ 1
		
	___ removeNode   dataSet):
		thisNode _ root
		
		while (thisNode):
			if thisNode.getData() == dataSet:
				next _ thisNode.getNextNode()
				prev _ thisNode.getPrevNode()
				
				if (next):
					next.setPrevNode(prev)
				if (prev):
					prev.setNextNode(next)
				else:
					root _ thisNode
					
				size -_ 1
				#Confirmed that node  was removed
				r_ True
			else:
				thisNode _ thisNode.getNextNode()
		
		#Could not find the specified data - nothing removed
		r_ False
		
	___ findNode   dataSet):
		thisNode _ root
		while (thisNode):
			if (thisNode.getData() == dataSet):
			    r_ dataSet
			else:
			    thisNode _ thisNode.getNextNode()
		r_ None

	___ getAllData
		dataList _ []
		thisNode _ root
		if (root == None):
			dataList.append(None)
			r_ dataList
		while (thisNode):
			dataList.append(thisNode.getData())
			thisNode _ thisNode.getNextNode()
		
		r_ dataList
