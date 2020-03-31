# c_ Knapsack
#
# 	___ - numOfItems capacityOfKnapsack weightOfItems profitOfItems
# 		? ?
# 		? ?
# 		? ?
# 		? ?
# 		dpTable _ ||0 ___ x __ ra.. c..+1|| ___ x __ ra.. n..+1
#
# 	___ dynamicProgrammingApproach
#
# 		# no need to initialize because there are 0s by default !!!
#
# 		___ i __ ra.. 1 n..+1
# 			___ w __ ra.. 1 c..+ 1
#
# 				notTakingItem _ dT..|?-1 |?
# 				takingItem _ 0
#
# 				__ w..|i  <_ w
# 					t.. _ p..|i  + dT..|?-1 |?-w..|?
#
# 				dT..|? |?  _ ma. n.. t.. )
#
# 	___ showResult
#
# 		print("Total benefit: @"  dT..|n.. |c..   # digit
#
# 		w _ capacityOfKnapsack
# 		___ n __ ra.. n.. 0 -1
#
# 			__ dT..|? |w  !_0 an. dT..|? |w  !_ dT..|?-1 |w
# 				print("We take item #@"  ?   # digit
# 				w _ w - w..|?
#
# __ _______ __ ______
#
# 	numOfItems _ 4
# 	capacityOfKnapsack _ 7
# 	weightOfItems _ [0,1,3,4,5]
# 	p.. _ [0,1,4,5,7]
#
#
# 	knapsack _ ? n.. c.. w.. p..
# 	?.d..
# 	?.s..
