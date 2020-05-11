# Filename: linkedlist.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is to create a doubly linked list example.
#          The single linked list can be achieved by removing the previous node reference.


# Name: Node
# Arguments: (object) - inhereting from object class
# Purpose: This is a template for a node in a linked list
c_ Node o..
    
    #Constructor:
    ___  -   dataSet, next _ N.., prev _ N..
        data _ dataSet
        nextNode _ next
        prevNode _ prev

    #Getter for next node:
    ___ getNextNode 
        r_ nextNode

    #Setter for next node:
    ___ setNextNode   next
        nextNode _ next

    #Getter for previous node:
    ___ getPrevNode 
        r_ prevNode

    #Setter for previous node:
    ___ setPrevNode   prev
        prevNode _ prev

    #Getter for data:
    ___ getData 
        r_ data

    #Setter for data:
    ___ setData   dataSet
        data _ dataSet

# Name: LinkedList
# Arguments: (object) - inhereting from object class
# Purpose: This class holds methods for LinkedList controls (getSize, addNode, removeNode, findNode, getAllData)
c_ LinkedList  o..
    	#Constructor:
	___  -   rootNode _ N..
		root _ rootNode
		size _ 0
		
	___ getSize 
		r_ size
		
	___ addNode   dataSet
		newNode _ Node (dataSet, root)
		__ (root
			root.setPrevNode(newNode)
		root _ newNode
		size +_ 1
		
	___ removeNode   dataSet
		thisNode _ root
		
		w__ (thisNode
			__ thisNode.getData() __ dataSet:
				next _ thisNode.getNextNode()
				prev _ thisNode.getPrevNode()
				
				__ (next
					next.setPrevNode(prev)
				__ (prev
					prev.setNextNode(next)
				____:
					root _ thisNode
					
				size -_ 1
				#Confirmed that node  was removed
				r_ T..
			____:
				thisNode _ thisNode.getNextNode()
		
		#Could not find the specified data - nothing removed
		r_ F..
		
	___ findNode   dataSet
		thisNode _ root
		w__ (thisNode
			__ (thisNode.getData() __ dataSet
			    r_ dataSet
			____:
			    thisNode _ thisNode.getNextNode()
		r_ N..

	___ getAllData
		dataList _ # list
		thisNode _ root
		__ (root __ N..
			dataList.a..(N..)
			r_ dataList
		w__ (thisNode
			dataList.a..(thisNode.getData())
			thisNode _ thisNode.getNextNode()
		
		r_ dataList
