# c_ QueensProblem
#
# 	___ - numOfQueens
# 		? ?
# 		chessTable _ ||None ___ i __ ra.. ?|| ___ j __ ra.. ?
#
# 	___ solveQueensProblem
#
# 		__ solve 0
# 			pQ..
# 		____
# 			print('There is no solution...')
#
# 	___ solve colIndex
#
# 		__ ? __ nOQ..
# 			r_ T..
#
# 		___ rowIndex __ ra.. nOQ..
#
# 			__ iPV.. rI.. cI..
#
# 				cT..|rI.. |cI.. _  1
#
# 				__ s.. cI..+1
# 					r_ T..
#
# 				# BACKTRACK
# 				cT..|rI.. |cI.. _ 0
#
# 		r_ F..
#
# 	___ isPlaceValid rowIndex columnIndex
#
# 		#same row
# 		___ i __ ra.. cI..
# 			__ cT..|rI.. |? __ 1
# 				r_ F..
#
# 		#from top left to bottom right
# 		j _ cI..
# 		___ i __ ra.. rI..,-1,-1
#
# 			__ j < 0
# 				b..
#
# 			__ cT..|? |? __ 1
# 				r_ F..
#
# 			j _ j -1
#
# 		#from bottom left to top right
# 		j _ columnIndex
# 		___ i __ ra.. rI.. le. cT..
#
# 			__ j < 0
# 				b..
#
# 			__ cT..|? |? __ 1
# 				r_ F..
#
# 			j _ j - 1
#
# 		r_ T..
#
# 	___ printQueens
#
# 		___ i __ ra.. nOQ..
# 			___ j __ ra.. nOQ..
#
# 				__ cT..|? |? __ 1
# 					print(' * ', e.._""
# 				____
# 					print(' - ', e.._""
#
# 			print('\n')
#
# __ _______ __ ______
#
# 	queensProblem _ ? 100
# 	?.sQP..
#
#
