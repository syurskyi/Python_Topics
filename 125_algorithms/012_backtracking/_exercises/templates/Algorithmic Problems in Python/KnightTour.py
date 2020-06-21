# c_ KnightTour
#
# 	___ - boardSize
# 		? ?
# 		xMoves _ [2, 1, -1, -2, -2, -1, 1, 2]
# 		yMoves _ [1, 2, 2, 1, -1, -2, -2, -1]
# 		solutionMatrix _ ||-1 ___ x __ ra.. bS..|| ___ x __ ra.. bS..||
#
# 	___ solveKnightTourProblem
#
# 		sM..||0|0 _ 0
#
# 		__ sP.. 1, 0, 0
# 			sS..
# 		____
# 			print('No feasible solution found...')
#
# 	___ solveProblem stepCount, x, y
#
# 		__ sC.. __ bS.. * bS..
# 			r_ T..
#
# 		___ i __ ra.. bS..
#
# 			nextX _ x + x..|?
# 			nextY _ y + y..|?
#
# 			__ isValidMove __X __Y
#
# 				sM..__X|__Y _  sC..
#
# 				__ sP.. sC..+1 __X __Y
# 					r_ T..
#
# 				sM..|__X __Y _ -1
#
# 		r_ F..
#
# 	___ isValidMove x, y
#
# 		__ x < 0 o. x >_ bS..
# 			r_ F..
#
# 		__ y < 0 or y >_ bS..
# 			r_ F..
#
# 		__ sM..|x |y > -1
# 			r_ F..
#
# 		r_ T..
#
# 	___ showSolution
#
# 		___ i __ ra.. bS..
# 			___ j _ ra.. bS..
# 				print(sM..|? |? e.._" "
#
# 			print('\n')
#
# __ _______ __ ______
#
# 	knightTour _ KnightTour(7)
# 	knightTour.solveKnightTourProblem()
#
#