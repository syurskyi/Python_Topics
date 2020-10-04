# c_ MazeProblem
#
# 	___ - mazeTable
# 		? ?
# 		mazeSize _ le. ?
# 		solutionTable _ ||0 *? ___ x __ ra.. ?
#
# 	___ solveMaze
#
# 		__ solve 0,0
# 			shR..
# 		____
# 			print('No feasible solution has found...')
#
# 	___ solve x, y
#
# 		__ isFinished x y
# 			r_ T..
#
# 		__ isValid x y
#
# 			sT..|x |y _ 1  #it is valid so it is part of the solution
#
# 			__ s.. x+1 y
# 				r_ T..  #  go forward in x direction
#
# 			__ s.. x y+1
# 				r_ T..
#
# 			__ s.. x-1 y
# 				r_ T..  #  go forward in x direction
#
# 			__ s.. x y-1
# 				r_ T..
#
# 			sT..|x |y _ 0 # no feasible solution: backtrack
#
# 		r_ F..
#
# 	___ isFinished x y
#
# 		__ x __ mS..-1 an. y __ mS..-1
# 			sT..|x |y _ 1
# 			r_ T..
#
# 		r_ F..
#
# 	___ isValid x y
#
# 		__ x < 0 o. x >_ mS..: r_ F..
# 		__ y < 0 o. y >_ mS..: r_ F..
# 		__ mT..|x |y __ 0: r_ F..
#
# 		r_ T..
#
# 	___ showResult
#
# 		___ i __ ra.. mS..
# 			___ j __ ra.. mS..
# 				__ sT..|? |?__ 1
# 					print(' S ' e.._""
# 				____
# 					print(' - ', e.._""
#
# 			print('\n')
#
#
# __ _______ __ ______
#
# 	mazeTable _ [[ 1, 1, 1, 1 ,1],
# 				 [ 0, 0, 0, 1, 0],
# 			     [ 1, 1, 1, 1, 0],
# 			     [ 1, 0, 0, 0, 0],
# 				 [ 1, 1, 1, 1, 1]
# 				];
#
# 	mazeProblem _ ? ?
# 	?.sM..
#
#