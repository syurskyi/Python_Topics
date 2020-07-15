compNodes = {"paint":"START", "diffuse":"paint", "specular":"diffuse", "refl":"specular", "occlusion":"refl", "depth":"occlusion"}
compNodeOperations = {"diffuse":"Merge:operation='mult';mix=1", "specular":"Merge:operation='plus';mix=1", "refl":"Merge:operation='plus';mix=1", "occlusion":"Merge:operation='mult';mix=0.75", "depth":"Copy:from0='rgba.red';to0='depth.Z'"}
addNodesBeforeComped = {"paint":"ColorCorrect:", "diffuse":"Unpremult:|Grade:|Premult:", "specular":"Grade:", "refl":"Grade:", "occlusion":"Grade:", "depth":"Grade:"}
addNodesAfterComped = {"depth":"ZBlur:"}
notCompNodes = {"paint":"rotopaint:carpaint"}
createNotFoundChannels = False
autoAlignReaders = True
createNoOpNode = True
createDotNode = True
showDotLabel = True
noOpTileColor = 0x9b00ff
nodeXOffset = 180
nodeYOffset = 150

import nuke

def getParentNode(layer, compNodes, mergeLayer):
	iteration = 0
	parentNode = layer
	while True:
		parentNode = compNodes[parentNode]
		if parentNode in mergeLayer:
			break

		if parentNode == 'START':
			break

		iteration += 1
		if iteration > 20:
			print "ERROR:\nPLEASE CHECK IF THE NAMES OF THE PARENT-NAMES FIT TO THE LAYER-NAMES"
			parentNode = -1
			break

	return parentNode

def calculateAdditionalYOffset(additionalYOffset, nodeToAddCount, nodeYOffset, nodeNumber):
	if nodeToAddCount*40 > nodeYOffset:
		if nodeNumber > 1:
			if nodeNumber == 2:
				additionalYOffset = 0
			additionalYOffset += (nodeToAddCount*40)-(nodeYOffset) - ((nodeNumber-1)*nodeYOffset)
		else:
			additionalYOffset += (nodeToAddCount*40)-(nodeYOffset)
	return additionalYOffset


def createNode(layer, nodeOperations, xPos, yPos):		
	operationNode = nodeOperations.split(':')
	operationParameters = operationNode[1].split(';')
	operationNode = operationNode[0]
	
	exec('thisNode = nuke.nodes.'  + str(operationNode) + '(name="' + operationNode + ' ' + str(layer) + '")') 
	thisNode.setXYpos(int(xPos), int(yPos))
	
	for parameter in operationParameters:
		if parameter != '':
			parameter = parameter.split('=')
			exec("thisNode['" + parameter[0] + "'].setValue("+parameter[1]+")")
			
	return thisNode 	

def autoComper():
	allSelectedNodes = nuke.selectedNodes()
	mergeLayer = {}
	mergeLayerInv = {}
	layerHasReader = {}
	nodesOrdered = []
	allLayers = {}
	layerType = {}
	xPosMin = 999999
	yPosMin = 999999
	additionalYOffset = 0
	additionalYOffsetFirst = 0
	
	for object in compNodes:
		if compNodes[object]  == 'START':
			nodesOrdered.append(object)
			break
	
	count = 0
	for object in compNodes:
		for object2 in compNodes:
			childNode = compNodes[object2]
			if childNode == nodesOrdered[count]:
				nodesOrdered.append(object2)
				count += 1
				break
	

	for thisNode in allSelectedNodes:	
		thisLayers = {}
		allChannels = thisNode.channels()	
		for channel in allChannels:
			thisData = str(channel.split('.')[0])
			thisLayers.update({thisData:''})
			
		if len(thisLayers) == 1 and 'rgba' in thisLayers:
			fileName = thisNode['file'].getValue()
			fileName = fileName.split('/')
			fileName = fileName[len(fileName)-1]
			fileName = fileName.split('.')[0]
			allLayers.update({fileName:thisNode})
			layerType.update({fileName:'file'})
		else:
			for layer in thisLayers:
				allLayers.update({layer:thisNode})
				layerType.update({layer:'channel'})
	
	for layer in allLayers:
		layerLower = layer.lower()
			
		if int(allLayers[layer]['xpos'].getValue()) < xPosMin:
			xPosMin = allLayers[layer]['xpos'].getValue()
		if int(allLayers[layer]['ypos'].getValue()) < yPosMin:
			yPosMin = allLayers[layer]['ypos'].getValue()	
	
		for compChannel in compNodes:
			compThis = True
			if layerLower.find(compChannel, 0, len(layerLower)) > -1:  
				if compChannel in notCompNodes:
					notNodes = notCompNodes[compChannel].split(':')
					for notNode in notNodes:
						if layerLower.find(notNode, 0, len(layer)) > -1:
							compThis = False 
							break
		
				if compThis == True:
					mergeLayer.update({compChannel:layer})
					mergeLayerInv.update({layer:compChannel})
					layerHasReader.update({layer:''}) 
	
	if createNotFoundChannels == True:
		for node in nodesOrdered:
			if node not in allLayers:
				if node not in mergeLayer:
					mergeLayer.update({node:node})
					mergeLayerInv.update({node:node})
	newAllLayers = []
	for node in nodesOrdered:
		if node in mergeLayer:
			newAllLayers.append(mergeLayer[node])
	for layer in allLayers:
		if layer not in newAllLayers:
			newAllLayers.append(layer)
	
	mergeCount = -1
	nodeNumber = -1
	
	for layer in newAllLayers:
		layerLower = layer.lower()
		nodeNumber += 1
		layerOriginal = layer
		if layer in mergeLayerInv: 
			layer = mergeLayerInv[layer]
			
		if len(allSelectedNodes) > 1 and autoAlignReaders == True:
			if layerOriginal in allLayers:
				allLayers[layerOriginal].setXYpos(int(nodeNumber*nodeXOffset+xPosMin), int(yPosMin))
		
		if layerOriginal in layerType:
			if layerType[layerOriginal] == 'channel':
				exec(str(layer) +' = nuke.nodes.Shuffle(name = "' + str(layerOriginal) + '_Shuffel", postage_stamp = True)')
				eval(layer).setXYpos(int(nodeNumber*nodeXOffset+xPosMin), int(yPosMin+2*nodeYOffset))
				if layerOriginal in allLayers:
					eval(layer).setInput(0, allLayers[layerOriginal])
					eval(layer)['in'].setValue(layerOriginal)
		
		if createNoOpNode:
			noOpNode = nuke.nodes.NoOp(name=layerOriginal, tile_color=noOpTileColor)
			noOpNode.setXYpos(int(nodeNumber*nodeXOffset+xPosMin), int(yPosMin+3*nodeYOffset))
			if layerOriginal in layerType:		
				if layerType[layerOriginal] == 'file':
					noOpNode.setInput(0, allLayers[layerOriginal])
				else:
					noOpNode.setInput(0, eval(layer))
		else:
			if layerOriginal in layerType:		
				if layerType[layerOriginal] == 'file':
					noOpNode =  allLayers[layerOriginal]	
				else:
					noOpNode =  eval(layer)
					
		exec(layer + "noOpNode = noOpNode")
		
		if layer in addNodesBeforeComped:
			nodeToAddCount = 0
			nodeBefore = eval(str(layer)+"noOpNode")
			
			for nodeToAdd in addNodesBeforeComped[layer].split('|'):
				xPos = nodeNumber*nodeXOffset+xPosMin 
				yPos = yPosMin+4*nodeYOffset + (nodeToAddCount*40)
				noOpNode = createNode(layer, nodeToAdd, xPos, yPos)
				noOpNode.setInput(0, nodeBefore)
				
				nodeToAddCount += 1
				nodeBefore =  noOpNode
			
			additionalYOffset = calculateAdditionalYOffset(additionalYOffset, nodeToAddCount, nodeYOffset, nodeNumber)
	
		if layer in mergeLayer:
			exec(layer + " = noOpNode")
			exec(layer + "Node = noOpNode")
			
			mergeCount += 1
			
			parentNode = getParentNode(layer, compNodes, mergeLayer)
	
			if parentNode != 'START':		                   
				xPos = xPosMin 
				yPos = mergeCount*nodeYOffset+yPosMin+4*nodeYOffset+additionalYOffset + additionalYOffsetFirst
				thisNode = createNode(layer, compNodeOperations[layer], xPos, yPos)
	
				exec(layer + "Node = thisNode")
				
				if mergeCount > 0 and createDotNode == True:
					#Create Dot-Nodes
					dot = nuke.nodes.Dot(note_font_size=20)
					if showDotLabel:
						dot['label'].setValue(' ' + str(layerOriginal))
					dot.setXYpos( int(eval(layer)['xpos'].getValue()+35), int(thisNode['ypos'].getValue()+3) )			
					dot.setInput(0, eval(layer))
					exec(layer +" = dot")
					
				if layer in addNodesAfterComped:
					nodeToAddCount = 1
					nodeBefore = eval(str(layer)+"Node")
					
					for nodeToAdd in addNodesAfterComped[layer].split('|'):
						xPos = xPosMin 
						yPos = mergeCount*nodeYOffset+yPosMin+4*nodeYOffset+additionalYOffset + additionalYOffsetFirst + (nodeToAddCount*40)
						thisNode = createNode(layer, nodeToAdd, xPos, yPos)
						thisNode.setInput(0, nodeBefore)
						
						nodeToAddCount += 1
						nodeBefore = thisNode
					
					additionalYOffsetFirst = calculateAdditionalYOffset(additionalYOffsetFirst, nodeToAddCount, nodeYOffset, 1)
					
					exec(layer + "NodeAdd = thisNode")
						
	for layer in mergeLayer:		
		parentNode = getParentNode(layer, compNodes, mergeLayer)
		
		if parentNode != 'START':
			if parentNode in addNodesAfterComped:
				parentNode = parentNode + "NodeAdd"
			else:
				parentNode = parentNode + "Node"
			
			exec(layer+"Node.setInput(1, " + layer + ")")
			exec(layer+"Node.setInput(0, " + str(parentNode) + ")")