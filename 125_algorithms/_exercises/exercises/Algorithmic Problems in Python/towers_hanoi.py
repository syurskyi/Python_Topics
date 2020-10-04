#
# ___ hanoi n rod_from rod_middle  rod_to
#
# 	#when n-1 plates are in the final position
# 	__ ? __ 1
# 		print "Plate 1 from @ to @" ? ?
# 		r_
#
# 	#moving n-1 plates off the largest one to be able to move that
# 	? ?-1 ? ? ?
# 	#moving the actual largest one
# 	print "Plate @ from @ to @" ? ? ?
# 	#placing n-1 plates on the top of the largest one
# 	? ?-1 ? ? ?
#
# __ ____ __ _____
#
# 	hanoi(3,'A','B','C')