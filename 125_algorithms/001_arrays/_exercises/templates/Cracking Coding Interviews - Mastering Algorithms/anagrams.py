# # Write a method to decide __ two strings are anagrams or not.
#
# # "abc" "cba" => true
# # "cinema" "iceman" => true
# # "bumblebee" "icecream" => false
#
# # O(nlogn)
#
# ___ anagram word1 word2
# 	r_ so..? __ so.. ?
#
# # O(n) O(n)
#
# ___ anagram2 word1 word2
# 	__ le. ? !_ le. ?
# 		r_ False
#
# 	dict1 =
# 	dict2 =
#
# 	___ i __ ra.. le. w_1
# 		__ w_1 ? no. __ d_1.k..
# 			d_1 w_1 ? _ 1
# 		____
# 			d_1 w_1 ? +_ 1
#
# 	___ i __ ra.. le. w_2
# 		__ w_2 ? no. __ d_2.k..
# 			d_2 w_2 ? _ 1
# 		____
# 			d_2 w_2 ? += 1
#
# 	___ key, value __ d_1.i..
# 		__ d_2 k.. !_ v..
# 			r_ F..
#
# 	r_ T..
#
# print(?("abc", "cba"))
# print(?("cinema", "iceman"))
# print(?("bumblebee", "icecream"))
# print(?("abc", "abc"))
