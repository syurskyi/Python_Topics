# # Write a method to decide if two strings are anagrams or not.
#
# # "abc" "cba" => true
# # "cinema" "iceman" => true
# # "bumblebee" "icecream" => false
#
# # O(nlogn)
#
# ___ anagram word1 word2
# 	r_ so.. ? __ so.. ?
#
# # O(n) O(n)
#
# ___ anagram2 word1 word2
# 	__ le. ? != le. ?
# 		r_ F..
#
# 	dict1
# 	dict2
#
# 	___ i __ ra.. le. _1
# 		__ _1|? no. __ _1.k..
# 			_1|_1|? _ 1
# 		____
# 			_1|_1|? +_ 1
#
# 	___ i __ ra.. le. _2
# 		__ _2 ? no. __ _2.k..
# 			_2|_2|? _ 1
# 		____
# 			_2|_2 ? +_ 1
#
# 	___ key, value __ _1.it..
# 		__ _2|? != ?
# 			r_ F..
#
# 	r_ T..
#
# print(?("abc", "cba"))
# print(?("cinema", "iceman"))
# print(?("bumblebee", "icecream"))
# print(?("abc", "abc"))
