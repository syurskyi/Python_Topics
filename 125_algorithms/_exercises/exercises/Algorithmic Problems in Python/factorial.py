#
# ___ factorial n
#
# 	#base case: 1!=1 (factorial 1 is 1)
# 	__ ? __ 1
# 		r_ 1
#
# 	#we make a recursive call
# 	subres1 _ ? ?-1
#
# 	#we do some operations
# 	subres2 _ ?*?
#
# 	r_ ?
#
# ___ factorial_accumulator n accumulator_1
#
# 	#base case: 1!=1
# 	__ ? __ 1
# 		r_ ?
#
# 	#now it is a tail recursion !!!
# 	r_ ? ?-1 ?*?
#
# __  -n __ ____
#
# 	print ? 5