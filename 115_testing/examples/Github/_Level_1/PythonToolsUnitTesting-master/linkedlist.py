# Filename: linkedlist.py
# Programmer: Marcin Czajkowski
# Purpose: The purpose of this script is to create a doubly linked list example.
#          The single linked list can be achieved by removing the previous node reference.


# Name: Node
# Arguments: (object) - inhereting from object class
# Purpose: This is a template for a node in a linked list
class Node(object):
    
    #Constructor:
    def __init__(self, dataSet, next = None, prev = None):
        self.data = dataSet
        self.nextNode = next
        self.prevNode = prev

    #Getter for next node:
    def getNextNode (self):
        return self.nextNode

    #Setter for next node:
    def setNextNode (self, next):
        self.nextNode = next

    #Getter for previous node:
    def getPrevNode (self):
        return self.prevNode

    #Setter for previous node:
    def setPrevNode (self, prev):
        self.prevNode = prev

    #Getter for data:
    def getData (self):
        return self.data

    #Setter for data:
    def setData (self, dataSet):
        self.data = dataSet

# Name: LinkedList
# Arguments: (object) - inhereting from object class
# Purpose: This class holds methods for LinkedList controls (getSize, addNode, removeNode, findNode, getAllData)
class LinkedList (object):
    	#Constructor:
	def __init__(self, rootNode = None):
		self.root = rootNode
		self.size = 0
		
	def getSize (self):
		return self.size
		
	def addNode (self, dataSet):
		newNode = Node (dataSet, self.root)
		if (self.root):
			self.root.setPrevNode(newNode)
		self.root = newNode
		self.size += 1
		
	def removeNode (self, dataSet):
		thisNode = self.root
		
		while (thisNode):
			if thisNode.getData() == dataSet:
				next = thisNode.getNextNode()
				prev = thisNode.getPrevNode()
				
				if (next):
					next.setPrevNode(prev)
				if (prev):
					prev.setNextNode(next)
				else:
					self.root = thisNode
					
				self.size -= 1
				#Confirmed that node  was removed
				return True
			else:
				thisNode = thisNode.getNextNode()
		
		#Could not find the specified data - nothing removed
		return False
		
	def findNode (self, dataSet):
		thisNode = self.root
		while (thisNode):
			if (thisNode.getData() == dataSet):
			    return dataSet
			else:
			    thisNode = thisNode.getNextNode()
		return None

	def getAllData(self):
		dataList = []
		thisNode = self.root
		if (self.root == None):
			dataList.append(None)
			return dataList
		while (thisNode):
			dataList.append(thisNode.getData())
			thisNode = thisNode.getNextNode()
		
		return dataList
