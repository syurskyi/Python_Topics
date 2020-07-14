# tempList _ ||
# count _ 0
# 
# ___ getPos nodes												#Return position of first node
# 	St_node _ ? 0										#Data coming from selection
# 	St_posx _ ? 'xpos' .gV..
# 	St_posy _ ? 'ypos' .gV..
# 	St_posList _ ? ?
# 	r_ ?
# 
# ___ getNodes nodes, nlist									#Append node names to global list
# 	
#
# 	___ n __ nodes
# 		nl__.ap.. ?.n..
# 		
# 		
# 
# 	
# ___ sortNodes nlist											#Sort names in list
# 	?.s..
# 
# 
# ___ placeNodes start,nlist,jumpDist							#Position sorted nodes in global list
# 	startNode _ nlist
# 	posNode _ ?.tN.. ?
# 	
# 	? 'xpos' .sV.. st.. 0 + j..
# 	? 'ypos' .sV.. st.. 1 
# 
# 
# ___ arrangeNodes
# 	
# 	count _ 0
# 	
# 	firstPos _ getPos ?.sN..  						#Get position of first node
# 
# 				
# 	getNodes ?.sN..  tempList
# 
# 	sN.. tL..
# 
# 
# 	___ i __ tL..
# 		c.. +_ 100
# 		jump _ c.. + 100
# 		pN.. fP.. ? j..
# 
# 
# 	
