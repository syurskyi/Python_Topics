# c_ HamiltonianProblem
#
# 	___ - adjacencyMatrix
# 		numOfVertexes _ le. ?
# 		hamiltonianPath _ |N..*?
# 		? ?
#
# 	___ hamiltonianCycle
#
# 		hamiltonianPath|0 _ 0
#
# 		__ no. fFS.. 1
# 			print('No feasible solution found...')
# 		____
# 			sHP..
#
# 	___ findFeasibleSolution position
#
# 		# check whether __ we are done -> the last node can be connected to the first in order to form a cycle?
# 		__ ? __ nOV..
# 			x _ hP..|? - 1
# 			y _ hP..[0]
# 			__ ( aM..[x][y]  __ 1): r_ T..
# 			____ r_ F..
#
# 		___ vertexIndex in ra.. 1 nOV..
#
# 			__ isFeasible vI.. ?
#
# 				hP..|? _ vI..
#
# 				__ fFS.. ?+1
# 					r_ T..
#
# 				# BACKTRACK
#
# 		r_ F..
#
# 	___ isFeasible vertex, actualPosition
#
# 		# first criteria: whether the two nodes are connected?
# 		__ aM..|hP..|a.. - 1|||v.. __ 0
# 			r_ F..
#
# 		# second criteria: whether we have already added this given node?
# 		___ i __ ra.. aP..
# 			__ hP..|? __ v..
# 				r_ F..
#
# 		r_ T..
#
# 	___ showHamiltonianPath
#
# 		print('Hamiltonian cycle exists: ')
#
# 		___ i __ ra.. nOV..
# 			print(hP..|?
#
# 		print(hP..|0
#
# __ _______ __ ______
#
# 	adjacencyMatrix _ [[0,1,0],
# 					   [1,0,1],
# 					   [1,1,0]
# 					  ]
#
# 	hamiltonian _ ? aM..
# 	?.hC..
#
#