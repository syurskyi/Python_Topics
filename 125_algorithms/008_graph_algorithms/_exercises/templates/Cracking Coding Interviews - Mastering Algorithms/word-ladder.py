# # Example 1:
#
# # Input:
# # beginWord = "hit",
# # endWord = "cog",
# # wordList = ["hot","dot","dog","lot","log","cog"]
#
# # Output: 5
#
# # Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# # return its length 5.
#
#
# # Example 2:
#
# # Input:
# # beginWord = "hit"
# # endWord = "cog"
# # wordList = ["hot","dot","dog","lot","log"]
#
# # Output: 0
#
# # Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
#
# ____ stR.. _______ a_l..
# _______ co..
#
# C_ Node
# 	___ - word path
# 		? ?
# 		? ?
#
# ___ ladder begin end word_list
# 	queue _    # list
#
# 	words _ se. w..
#
# 	q__.ap.. ? ? |?
#
# 	w__ le. q.. > 0
# 		cur _ q__.po. 0
#
# 		cur_word _ c__.w..
# 		path _ c__.p..
#
# 		__ c.. __ end
# 			r_ p..
#
# 		___ i __ ra.. le. c..
# 			___ c __ a_l..
# 				potential_word _ c..|;? + ? + c..|?+1;
#
# 				__ potential_word __ words
# 					copy_path _ co__.d_c.. ?
# 					?.ap.. ?
# 					q__.ap.. ? p.. c..
# 					w__.r.. ?
#
# 	r_    # list
#
# print(ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# print(ladder("hit", "cog", ["hot","dot","dog","lot","log"]))
