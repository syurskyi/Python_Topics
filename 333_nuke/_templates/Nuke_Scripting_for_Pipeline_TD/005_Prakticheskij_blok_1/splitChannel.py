compNodes _ {"paint":"START", "diffuse":"paint", "specular":"diffuse", "refl":"specular", "occlusion":"refl", "depth":"occlusion"}
compNodeOperations _ {"diffuse":"Merge:operation='mult';mix=1", "specular":"Merge:operation='plus';mix=1", "refl":"Merge:operation='plus';mix=1", "occlusion":"Merge:operation='mult';mix=0.75", "depth":"Copy:from0='rgba.red';to0='depth.Z'"}
addNodesBeforeComped _ {"paint":"ColorCorrect:", "diffuse":"Unpremult:|Grade:|Premult:", "specular":"Grade:", "refl":"Grade:", "occlusion":"Grade:", "depth":"Grade:"}
addNodesAfterComped _ {"depth":"ZBlur:"}
notCompNodes _ {"paint":"rotopaint:carpaint"}
createNotFoundChannels _ F..
autoAlignReaders _ T..
createNoOpNode _ T..
createDotNode _ T..
showDotLabel _ T..
noOpTileColor _ 0x9b00ff
nodeXOffset _ 180
nodeYOffset _ 150

_____ ?

___ getParentNode(layer, compNodes, mergeLayer):
	iteration _ 0
	parentNode _ layer
	while T..:
		parentNode _ compNodes[parentNode]
		__ parentNode __ mergeLayer:
			break

		__ parentNode __ 'START':
			break

		iteration +_ 1
		__ iteration > 20:
			print "ERROR:\nPLEASE CHECK IF THE NAMES OF THE PARENT-NAMES FIT TO THE LAYER-NAMES"
			parentNode _ -1
			break

	r_ parentNode

___ calculateAdditionalYOffset(additionalYOffset, nodeToAddCount, nodeYOffset, nodeNumber):
	__ nodeToAddCount*40 > nodeYOffset:
		__ nodeNumber > 1:
			__ nodeNumber __ 2:
				additionalYOffset _ 0
			additionalYOffset +_ (nodeToAddCount*40)-(nodeYOffset) - ((nodeNumber-1)*nodeYOffset)
		____
			additionalYOffset +_ (nodeToAddCount*40)-(nodeYOffset)
	r_ additionalYOffset


___ cN..(layer, nodeOperations, xPos, yPos):
	operationNode _ nodeOperations.sp__(':')
	operationParameters _ operationNode[1].sp__(';')
	operationNode _ operationNode[0]
	
	exec('thisNode = nuke.nodes.'  + st_(operationNode) + '(name="' + operationNode + ' ' + st_(layer) + '")')
	thisNode.setXYpos(in_(xPos), in_(yPos))
	
	___ parameter __ operationParameters:
		__ parameter !_ '':
			parameter _ parameter.sp__('=')
			exec("thisNode['" + parameter[0] + "'].setValue("+parameter[1]+")")
			
	r_ thisNode

___ autoComper
	allSelectedNodes _ ?.sN..
	mergeLayer _ {}
	mergeLayerInv _ {}
	layerHasReader _ {}
	nodesOrdered _ []
	allLayers _ {}
	layerType _ {}
	xPosMin _ 999999
	yPosMin _ 999999
	additionalYOffset _ 0
	additionalYOffsetFirst _ 0
	
	___ object __ compNodes:
		__ compNodes[object]  __ 'START':
			nodesOrdered.a__(object)
			break
	
	count _ 0
	___ object __ compNodes:
		___ object2 __ compNodes:
			childNode _ compNodes[object2]
			__ childNode __ nodesOrdered[count]:
				nodesOrdered.a__(object2)
				count +_ 1
				break
	

	___ thisNode __ allSelectedNodes:
		thisLayers _ {}
		allChannels _ thisNode.channels()
		___ channel __ allChannels:
			thisData _ st_(channel.sp__('.')[0])
			thisLayers.update({thisData:''})
			
		__ le.(thisLayers) __ 1 and 'rgba' __ thisLayers:
			fileName _ thisNode['file'].gV..()
			fileName _ fileName.sp__('/')
			fileName _ fileName[le.(fileName)-1]
			fileName _ fileName.sp__('.')[0]
			allLayers.update({fileName:thisNode})
			layerType.update({fileName:'file'})
		____
			___ layer __ thisLayers:
				allLayers.update({layer:thisNode})
				layerType.update({layer:'channel'})
	
	___ layer __ allLayers:
		layerLower _ layer.lower()
			
		__ in_(allLayers[layer]['xpos'].gV..()) < xPosMin:
			xPosMin _ allLayers[layer]['xpos'].gV..()
		__ in_(allLayers[layer]['ypos'].gV..()) < yPosMin:
			yPosMin _ allLayers[layer]['ypos'].gV..()
	
		___ compChannel __ compNodes:
			compThis _ T..
			__ layerLower.find(compChannel, 0, le.(layerLower)) > -1:
				__ compChannel __ notCompNodes:
					notNodes _ notCompNodes[compChannel].sp__(':')
					___ notNode __ notNodes:
						__ layerLower.find(notNode, 0, le.(layer)) > -1:
							compThis _ F..
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
	newAllLayers _ []
	___ node __ nodesOrdered:
		__ node __ mergeLayer:
			newAllLayers.a__(mergeLayer[node])
	___ layer __ allLayers:
		__ layer no. __ newAllLayers:
			newAllLayers.a__(layer)
	
	mergeCount _ -1
	nodeNumber _ -1
	
	___ layer __ newAllLayers:
		layerLower _ layer.lower()
		nodeNumber +_ 1
		layerOriginal _ layer
		__ layer __ mergeLayerInv:
			layer _ mergeLayerInv[layer]
			
		__ le.(allSelectedNodes) > 1 and autoAlignReaders __ T..:
			__ layerOriginal __ allLayers:
				allLayers[layerOriginal].setXYpos(in_(nodeNumber*nodeXOffset+xPosMin), in_(yPosMin))
		
		__ layerOriginal __ layerType:
			__ layerType[layerOriginal] __ 'channel':
				exec(st_(layer) +' = nuke.nodes.Shuffle(name = "' + st_(layerOriginal) + '_Shuffel", postage_stamp = True)')
				eval(layer).setXYpos(in_(nodeNumber*nodeXOffset+xPosMin), in_(yPosMin+2*nodeYOffset))
				__ layerOriginal __ allLayers:
					eval(layer).setInput(0, allLayers[layerOriginal])
					eval(layer)['in'].sV..(layerOriginal)
		
		__ createNoOpNode:
			noOpNode _ ?.n__.NoOp(name_layerOriginal, tile_color_noOpTileColor)
			noOpNode.setXYpos(in_(nodeNumber*nodeXOffset+xPosMin), in_(yPosMin+3*nodeYOffset))
			__ layerOriginal __ layerType:
				__ layerType[layerOriginal] __ 'file':
					noOpNode.setInput(0, allLayers[layerOriginal])
				____
					noOpNode.setInput(0, eval(layer))
		____
			__ layerOriginal __ layerType:
				__ layerType[layerOriginal] __ 'file':
					noOpNode _  allLayers[layerOriginal]
				____
					noOpNode _  eval(layer)
					
		exec(layer + "noOpNode = noOpNode")
		
		__ layer __ addNodesBeforeComped:
			nodeToAddCount _ 0
			nodeBefore _ eval(st_(layer)+"noOpNode")
			
			___ nodeToAdd __ addNodesBeforeComped[layer].sp__('|'):
				xPos _ nodeNumber*nodeXOffset+xPosMin
				yPos _ yPosMin+4*nodeYOffset + (nodeToAddCount*40)
				noOpNode _ cN..(layer, nodeToAdd, xPos, yPos)
				noOpNode.setInput(0, nodeBefore)
				
				nodeToAddCount +_ 1
				nodeBefore _  noOpNode
			
			additionalYOffset _ calculateAdditionalYOffset(additionalYOffset, nodeToAddCount, nodeYOffset, nodeNumber)
	
		__ layer __ mergeLayer:
			exec(layer + " = noOpNode")
			exec(layer + "Node = noOpNode")
			
			mergeCount +_ 1
			
			parentNode _ getParentNode(layer, compNodes, mergeLayer)
	
			__ parentNode !_ 'START':
				xPos _ xPosMin
				yPos _ mergeCount*nodeYOffset+yPosMin+4*nodeYOffset+additionalYOffset + additionalYOffsetFirst
				thisNode _ cN..(layer, compNodeOperations[layer], xPos, yPos)
	
				exec(layer + "Node = thisNode")
				
				__ mergeCount > 0 and createDotNode __ T..:
					#Create Dot-Nodes
					dot _ ?.n__.Dot(note_font_size_20)
					__ showDotLabel:
						dot['label'].sV..(' ' + st_(layerOriginal))
					dot.setXYpos( in_(eval(layer)['xpos'].gV..()+35), in_(thisNode['ypos'].gV..()+3) )
					dot.setInput(0, eval(layer))
					exec(layer +" = dot")
					
				__ layer __ addNodesAfterComped:
					nodeToAddCount _ 1
					nodeBefore _ eval(st_(layer)+"Node")
					
					___ nodeToAdd __ addNodesAfterComped[layer].sp__('|'):
						xPos _ xPosMin
						yPos _ mergeCount*nodeYOffset+yPosMin+4*nodeYOffset+additionalYOffset + additionalYOffsetFirst + (nodeToAddCount*40)
						thisNode _ cN..(layer, nodeToAdd, xPos, yPos)
						thisNode.setInput(0, nodeBefore)
						
						nodeToAddCount +_ 1
						nodeBefore _ thisNode
					
					additionalYOffsetFirst _ calculateAdditionalYOffset(additionalYOffsetFirst, nodeToAddCount, nodeYOffset, 1)
					
					exec(layer + "NodeAdd = thisNode")
						
	___ layer __ mergeLayer:
		parentNode _ getParentNode(layer, compNodes, mergeLayer)
		
		__ parentNode !_ 'START':
			__ parentNode __ addNodesAfterComped:
				parentNode _ parentNode + "NodeAdd"
			____
				parentNode _ parentNode + "Node"
			
			exec(layer+"Node.setInput(1, " + layer + ")")
			exec(layer+"Node.setInput(0, " + st_(parentNode) + ")")