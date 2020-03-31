# c_ RodCutting
#
# 	___ -  lengthOfRod prices
# 		?  ?
# 		?  ?
# 		dpTable = ||0 * l.. + 1 ___ x __ ra.. le. p..
#
# 	___ dynamicProgrammingApproach lengthOfRod prices
#
# 		# 2 for loops to make sure the first row / column have all zeros !!!
#
# 		___ i __ ra.. 1 le. p..
# 			___
# 			j __ ra.. 1 l.. + 1
#
# 				__ ? <_ ?
# 					dT..|? |?  _ ma. dT..|?-1 |?  p..|? +dT..|? |?-?
# 				____
# 					dT..|? |?  _ dT..|?-1 |? ;
#
# 	___ showResults
#
# 		print("Max profit is: $@"  dT..|le. p...|-1 |l..    # digit
#
# 		columnIndex _ l...
# 		rowIndex _ le. p..-1
#
# 		w__ ? > 0 o. ? > 0
#
# 			__ dT..|r.. |c..  __ dT..|r..-1 |c..
# 				r.. _ r.. - 1
# 			____
# 				print("We make cut: " r.. "m")
# 				c.. _ c.. - r...
#
# __ _______ __ ______
#
# 	lengthOfRod = 5
# 	prices = [0,2,5,7,3]
#
# 	rodCutting = ? l.. p..
# 	?.d.. l.. p..
# 	?.s..
