compNodes = {"paint":"START", "diffuse":"paint", "specular":"diffuse", "refl":"specular", "occlusion":"refl", "depth":"occlusion"}
compNodeOperations = {"diffuse":"Merge:operation='mult';mix=1", "specular":"Merge:operation='plus';mix=1", "refl":"Merge:operation='plus';mix=1", "occlusion":"Merge:operation='mult';mix=0.75", "depth":"Copy:from0='rgba.red';to0='depth.Z'"}
addNodesBeforeComped = {"paint":"ColorCorrect:", "diffuse":"Unpremult:|Grade:|Premult:", "specular":"Grade:", "refl":"Grade:", "occlusion":"Grade:", "depth":"Grade:"}
addNodesAfterComped = {"depth":"ZBlur:"}
notCompNodes = {"paint":"rotopaint:carpaint"}
createNotFoundChannels = False
autoAlignReaders = T..
createNoOpNode = T..
createDotNode = T..
showDotLabel = T..
noOpTileColor = 0x9b00ff
nodeXOffset = 180
nodeYOffset = 150

_____ ?

___ getParentNode(layer, compNodes, mergeLayer):
	iteration = 0
	parentNode = layer
	while T..:
		parentNode = compNodes[parentNode]
		__ parentNode __ mergeLayer:
			break

		__ parentNode __ 'START':
			break

		iteration += 1
		__ iteration > 20:
			print "ERROR:\nPLEASE CHECK IF THE NAMES OF THE PARENT-NAMES FIT TO THE LAYER-NAMES"
			parentNode = -1
			break

	r_ parentNode

___ calculateAdditionalYOffset(additionalYOffset, nodeToAddCount, nodeYOffset, nodeNumber):
	__ nodeToAddCount*40 > nodeYOffset:
		__ nodeNumber > 1:
			__ nodeNumber __ 2:
				additionalYOffset = 0
			additionalYOffset += (nodeToAddCount*40)-(nodeYOffset) - ((nodeNumber-1)*nodeYOffset)
		else:
			additionalYOffset += (nodeToAddCount*40)-(nodeYOffset)
	r_ additionalYOffset


___ cN..(layer, nodeOperations, xPos, yPos):
	operationNode = nodeOperations.split(':')
	operationParameters = operationNode[1].split(';')
	operationNode = operationNode[0]
	
	exec('thisNode = nuke.nodes.'  + str(operationNode) + '(name="' + operationNode + ' ' + str(layer) + '")') 
	thisNode.setXYpos(in_(xPos), in_(yPos))
	
	___ parameter __ operationParameters:
		__ parameter != '':
			parameter = parameter.split('=')
			exec("thisNode['" + parameter[0] + "'].setValue("+parameter[1]+")")
			
	r_ thisNode

___ autoComper
	allSelectedNodes = ?.selectedNodes()
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
	
	___ object __ compNodes:
		__ compNodes[object]  __ 'START':
			nodesOrdered.a__(object)
			break
	
	count = 0
	___ object __ compNodes:
		___ object2 __ compNodes:
			childNode = compNodes[object2]
			__ childNode __ nodesOrdered[count]:
				nodesOrdered.a__(object2)
				count += 1
				break
	

	___ thisNode __ allSelectedNodes:
		thisLayers = {}
		allChannels = thisNode.channels()	
		___ channel __ allChannels:
			thisData = str(channel.split('.')[0])
			thisLayers.update({thisData:''})
			
		__ le.(thisLayers) __ 1 and 'rgba' __ thisLayers:
			fileName = thisNode['file'].gV..()
			fileName = fileName.split('/')
			fileName = fileName[le.(fileName)-1]
			fileName = fileName.split('.')[0]
			allLayers.update({fileName:thisNode})
			layerType.update({fileName:'file'})
		else:
			___ layer __ thisLayers:
				allLayers.update({layer:thisNode})
				layerType.update({layer:'channel'})
	
	___ layer __ allLayers:
		layerLower = layer.lower()
			
		__ in_(allLayers[layer]['xpos'].gV..()) < xPosMin:
			xPosMin = allLayers[layer]['xpos'].gV..()
		__ in_(allLayers[layer]['ypos'].gV..()) < yPosMin:
			yPosMin = allLayers[layer]['ypos'].gV..()
	
		___ compChannel __ compNodes:
			compThis = T..
			__ layerLower.find(compChannel, 0, le.(layerLower)) > -1:
				__ compChannel __ notCompNodes:
					notNodes = notCompNodes[compChannel].split(':')
					___ notNode __ notNodes:
						__ layerLower.find(notNode, 0, le.(layer)) > -1:
							compThis = False 
							break
		
				__ compThis __ T..:
					mergeLayer.update({compChannel:layer})
					mergeLayerInv.update({layer:compChannel})
					layerHasReader.update({layer:''}) 
	
	__ createNotFoundChannels __ T..:
		___ node __ nodesOrdered:
			__ node no. __ allLayers:
				__ node no. __ mergeLayer:
					mergeLayer.update({node:node})
					mergeLayerInv.update({node:node})
	newAllLayers = []
	___ node __ nodesOrdered:
		__ node __ mergeLayer:
			newAllLayers.a__(mergeLayer[node])
	___ layer __ allLayers:
		__ layer no. __ newAllLayers:
			newAllLayers.a__(layer)
	
	mergeCount = -1
	nodeNumber = -1
	
	___ layer __ newAllLayers:
		layerLower = layer.lower()
		nodeNumber += 1
		layerOriginal = layer
		__ layer __ mergeLayerInv:
			layer = mergeLayerInv[layer]
			
		__ le.(allSelectedNodes) > 1 and autoAlignReaders __ T..:
			__ layerOriginal __ allLayers:
				allLayers[layerOriginal].setXYpos(in_(nodeNumber*nodeXOffset+xPosMin), in_(yPosMin))
		
		__ layerOriginal __ layerType:
			__ layerType[layerOriginal] __ 'channel':
				exec(str(layer) +' = nuke.nodes.Shuffle(name = "' + str(layerOriginal) + '_Shuffel", postage_stamp = True)')
				eval(layer).setXYpos(in_(nodeNumber*nodeXOffset+xPosMin), in_(yPosMin+2*nodeYOffset))
				__ layerOriginal __ allLayers:
					eval(layer).setInput(0, allLayers[layerOriginal])
					eval(layer)['in'].sV..(layerOriginal)
		
		__ createNoOpNode:
			noOpNode = ?.nodes.NoOp(name=layerOriginal, tile_color=noOpTileColor)
			noOpNode.setXYpos(in_(nodeNumber*nodeXOffset+xPosMin), in_(yPosMin+3*nodeYOffset))
			__ layerOriginal __ layerType:
				__ layerType[layerOriginal] __ 'file':
					noOpNode.setInput(0, allLayers[layerOriginal])
				else:
					noOpNode.setInput(0, eval(layer))
		else:
			__ layerOriginal __ layerType:
				__ layerType[layerOriginal] __ 'file':
					noOpNode =  allLayers[layerOriginal]	
				else:
					noOpNode =  eval(layer)
					
		exec(layer + "noOpNode = noOpNode")
		
		__ layer __ addNodesBeforeComped:
			nodeToAddCount = 0
			nodeBefore = eval(str(layer)+"noOpNode")
			
			___ nodeToAdd __ addNodesBeforeComped[layer].split('|'):
				xPos = nodeNumber*nodeXOffset+xPosMin 
				yPos = yPosMin+4*nodeYOffset + (nodeToAddCount*40)
				noOpNode = cN..(layer, nodeToAdd, xPos, yPos)
				noOpNode.setInput(0, nodeBefore)
				
				nodeToAddCount += 1
				nodeBefore =  noOpNode
			
			additionalYOffset = calculateAdditionalYOffset(additionalYOffset, nodeToAddCount, nodeYOffset, nodeNumber)
	
		__ layer __ mergeLayer:
			exec(layer + " = noOpNode")
			exec(layer + "Node = noOpNode")
			
			mergeCount += 1
			
			parentNode = getParentNode(layer, compNodes, mergeLayer)
	
			__ parentNode != 'START':
				xPos = xPosMin 
				yPos = mergeCount*nodeYOffset+yPosMin+4*nodeYOffset+additionalYOffset + additionalYOffsetFirst
				thisNode = cN..(layer, compNodeOperations[layer], xPos, yPos)
	
				exec(layer + "Node = thisNode")
				
				__ mergeCount > 0 and createDotNode __ T..:
					#Create Dot-Nodes
					dot = ?.nodes.Dot(note_font_size=20)
					__ showDotLabel:
						dot['label'].sV..(' ' + str(layerOriginal))
					dot.setXYpos( in_(eval(layer)['xpos'].gV..()+35), in_(thisNode['ypos'].gV..()+3) )
					dot.setInput(0, eval(layer))
					exec(layer +" = dot")
					
				__ layer __ addNodesAfterComped:
					nodeToAddCount = 1
					nodeBefore = eval(str(layer)+"Node")
					
					___ nodeToAdd __ addNodesAfterComped[layer].split('|'):
						xPos = xPosMin 
						yPos = mergeCount*nodeYOffset+yPosMin+4*nodeYOffset+additionalYOffset + additionalYOffsetFirst + (nodeToAddCount*40)
						thisNode = cN..(layer, nodeToAdd, xPos, yPos)
						thisNode.setInput(0, nodeBefore)
						
						nodeToAddCount += 1
						nodeBefore = thisNode
					
					additionalYOffsetFirst = calculateAdditionalYOffset(additionalYOffsetFirst, nodeToAddCount, nodeYOffset, 1)
					
					exec(layer + "NodeAdd = thisNode")
						
	___ layer __ mergeLayer:
		parentNode = getParentNode(layer, compNodes, mergeLayer)
		
		__ parentNode != 'START':
			__ parentNode __ addNodesAfterComped:
				parentNode = parentNode + "NodeAdd"
			else:
				parentNode = parentNode + "Node"
			
			exec(layer+"Node.setInput(1, " + layer + ")")
			exec(layer+"Node.setInput(0, " + str(parentNode) + ")")