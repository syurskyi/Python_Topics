# c_ Fibonacci
#
# 	___ -
# 		memoizeTable _    # dict  # O(1)
# 		?|0 _ 0
# 		?|1 _ 1
#
# 	___ fibonacciMemoize n
#
# 		__ ? __ m..
# 			r_ m..|?
#
# 		m..|?-1 _ f.. ?-1
# 		m..|?-2 _ f.. ?-2
#
# 		calculatedNumber _ m..|?-1] + m..|?-2] # O(1)
# 		m..|?] _ ?
#
# 		r_ c..
#
# 	___ naiveApproach n
#
# 		# f(n) _ f(n-1) + f(n-2) where f(0) _ 0 and f(1) _ 1
#
# 		__ ? __ 0: r_ 0
# 		__ ? __ 1: r_ 1
#
# 		r_ ? ?-1 + ? ?-2
#
# __ _______ __ ______
#
# 	fibonacci _ ?
# 	print( ?.n.. 100

