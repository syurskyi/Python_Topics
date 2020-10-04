# c_ CoinChange
#
# 	# M - total amount and v[] coins
# 	___ naiveApproach M v index
#
# 		__ M < 0: r_ 0
# 		__ M __ 0: r_ 1
#
# 		__ ? __ le. v: r_ 0
#
# 		r_ ? M-v|i.. v i..| + ? M v i...+1
#
# 	# M - total amount and v[] coins
# 	___ dynamicProgrammingApproach v M
#
# 		dpTable _ ||0*|M+1 ___ x __ ra.. le. |v| +1
#
# 		#___ j __ range(M+1):
# 		#	dpTable[0][j] = 0
#
# 		___ i __ ra.. len v|+1
# 			dT.|? 0 _ 1
#
# 		___ i __ ra.. 1 le. v|+1
# 			___ j __ ra.. 1 M+1
#
# 				__ v|?-1 <_ ?
# 					dT..|? |? _ dT..|?-1 |? + dT..|? |?-v|?-1
# 				____
# 					dT..|? |? _ dT..|? - 1 |?
#
# 		print("Solution is: @"  dT..|le. v|||M   # digit
#
# __ _______ __ ______
#
# 	M = 1000
# 	coins = [1,2,3]
#
# 	coinChange = CoinChange()
# 	coinChange.dynamicProgrammingApproach(coins,M)
