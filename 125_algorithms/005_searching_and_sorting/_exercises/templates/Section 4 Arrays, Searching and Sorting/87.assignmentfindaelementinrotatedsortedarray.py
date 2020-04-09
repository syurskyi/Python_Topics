#
# ___ func myarray value
# 	l _ 0
# 	r _ le. ? - 1
# 	w__ l <_ r
# 		m _ (l + r) / 2
# 		__ ?|m __ ?
# 			r_ m
# 		__ ?|m >_ ?|l
# 			__ ?|l <_ v.. < ?|m
# 				r _ m - 1
# 			____0
# 				l _ m + 1
# 		____
# 			__ ?[m] < value <_ ?[r]:
# 				l _ m + 1
# 			____
# 				r _ m - 1
# 	r_ -1
#
# myarray _ [6,7,8,9,10,1,2,3,4,5]
#
# print ? ? 5
