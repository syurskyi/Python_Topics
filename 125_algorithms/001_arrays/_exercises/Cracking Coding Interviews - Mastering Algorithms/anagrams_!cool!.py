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
# 		r_ F..
#
# 	dict1 =
# 	dict2 =
#
# 	___ i __ ra.. le. _1
# 		__ ? ? no. __ ?.k..
# 			? ? ? _ 1
# 		____
# 			? ? ? +_ 1
#
# 	___ i __ ra.. le. w_2
# 		__ ? ? no. __ ?.k..
# 			? ? ? _ 1
# 		____
# 			? ? ? += 1
#
# 	___ key, value __ ?.i..
# 		__ ? k.. !_ v..
# 			r_ F..
#
# 	r_ T..
#
# print(?("abc", "cba"))
# print(?("cinema", "iceman"))
# print(?("bumblebee", "icecream"))
# print(?("abc", "abc"))
