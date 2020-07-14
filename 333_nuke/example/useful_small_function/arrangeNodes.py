import nuke
#Nuke Node Arranger 2014 v0.0.1a
#Written by David Robinson 
#www.davidrobinsonvfx.com

tempList = []
count = 0

def getPos(nodes):												#Return position of first node
	St_node = nodes[0]											#Data coming from selection
	St_posx = St_node['xpos'].getValue()
	St_posy = St_node['ypos'].getValue()
	St_posList = [St_posx, St_posy]
	return St_posList

def getNodes(nodes, nlist):										#Append node names to global list
	
	
	for n in nodes:
		nlist.append(n.name())
		
		

	
def sortNodes(nlist):											#Sort names in list
	nlist.sort()


def placeNodes(start,nlist,jumpDist):							#Position sorted nodes in global list
	startNode = nlist
	posNode = nuke.toNode(startNode)
	
	posNode['xpos'].setValue(start[0] + jumpDist)
	posNode['ypos'].setValue(start[1])


def arrangeNodes():
	
	count = 0
	
	firstPos = getPos( nuke.selectedNodes() )						#Get position of first node

				
	getNodes( nuke.selectedNodes(), tempList )

	sortNodes(tempList)


	for i in tempList:
		count += 100
		jump = count + 100
		placeNodes(firstPos,i, jump)


	
