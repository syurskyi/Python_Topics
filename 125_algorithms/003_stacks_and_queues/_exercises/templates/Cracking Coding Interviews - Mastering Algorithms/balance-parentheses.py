# # Given a string containing just the characters
# # '(', ')',
# # '{', '}',
# # '[' and ']',
# # determine if the input string is valid
#
# # Example 1:
# # Input: "()"
# # Output: true
#
# # Example 2:
# # Input: "()[]{}"
# # Output: true
#
# # Example 3:
# # Input: "(]"
# # Output: false
#
# # Example 4:
# # Input: "([)]"
# # Output: false
#
# # Example 5:
# # Input: "{[]}"
# # Output: true
#
# ___ balanced s
# 	stack _  # list
#
# 	___ i __ ra.. le. s
# 		__ ?|? __ "(" o. ?|? __ "{" o. ?|? __ "["
# 			?.ap.. ?|?
# 		____ ?|? __ ")" an. le. ? __ 0 o. ?.p.. != "(")
# 			r_ F..
# 		____ ?|? __ "]" an. le. ? __ 0 o. ?.p.. != "[")
# 			r_ F..
# 		____ ?|? __ "}" an. le. ? __ 0 o. ?.p.. != "{")
# 			r_ F..
#
# 	r_ le. ?) __ 0
#
#
#
# print(?("()"))
# print(?("()[]{}"))
# print(?("(]"))
# print(?("([)]"))
# print(?("{[]}"))
