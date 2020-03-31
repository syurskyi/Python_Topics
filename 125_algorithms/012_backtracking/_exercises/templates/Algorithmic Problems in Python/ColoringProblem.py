# c_ ColoringProblem
#
# 	___ - numOfVertices numOfColors graphMatrix
# 		? ?
# 		? ?
# 		colors _ |0 *nOV..
# 		? ?
#
# 	___ solveColoringProblem
#
# 		__ solve 0
# 			sR..
# 		____
# 			print('No feasible solution with the given parameters...')
#
# 	___ solve nodeIndex
#
# 		__ ? __ nOV..
# 			r_ T..
#
# 		#try all colors
# 		___ cI.. __ ra.. 1 nOC..+1
#
# 			__ isColorValid ? cI..
# 				#assign and proceed with next vertex
# 				c.. |? _ cI..
#
# 				__ solve ?+1
# 					r_ T..
#
# 				#BACKTRACK !!!
#
# 		r_ F..
#
# 	___ isColorValid nodeIndex colorIndex
#
# 		___ i __ ra.. nOV..
# 			__ gM..|nI.. |? __ 1 an. cI.. __ c..|?
# 				r_ F..
#
# 		r_ T..
#
# 	___ showResult
#
# 		___ i __ ra.. nOV..
# 			print('Node @ has color index: @' ? c..|?  # digit
#
#
# __ _______ __ ______
#
# 	graphMatrix _ [[0,1,0,1,0],
# 				   [1,0,1,0,1],
# 				   [0,1,0,1,0],
# 				   [1,1,1,0,1],
# 				   [0,0,0,1,0]
# 				  ]
#
# 	numOfColors _ 3
# 	numOfVertices _ 5
#
#
# 	coloringProblem _ ? nOV.. nOC.. gM..
# 	?.sCP..
