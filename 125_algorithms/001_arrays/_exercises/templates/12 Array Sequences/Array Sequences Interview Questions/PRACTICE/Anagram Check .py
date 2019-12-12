# # %%
# '''
# # Anagram Check
# ## Problem
# Given two strings, check to see i_ they are anagrams. An anagram is when the two strings can be written using
# the exact same letters (so you can just rearrange the letters to get a different phrase or word).
# For example:
#     "public relations" is an anagram of "crap built on lies."
#     "clint eastwood" is an anagram of "old west action"
# **Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".**
# ## Solution
# 
# Fill out your solution below:
# '''
# 
# 
# # %%
# # 242. Valid Anagram(https://leetcode.com/problems/valid-anagram/description/)
# ___ anagram s t
#     """
#     :type s: str
#     :type t: str
#     :rtype: bool
#     """
#     s _ s.re.. ' ', '' .lo__
#     t _ t.re.. ' ', '' .lo__
# 
#     i_  le. s  !_ le. t
#         r_ F...
#     counter _      # dict
#     ___ letter i_ s
#         i_ l.. i_ c..
#             c.. l.. +_ 1
#         e___
#             c... l.. _ 1
# 
#     ___ letter i_ t
#         i_ l.. i_ c...
#             c... l.. -_ 1
#         e___
#             r_ F...
# 
#     ___ k i_ c...
#         i_ c... k !_ 0
#             r_ F...
# 
#     r_ T...
#     p..
# 
# 
# # %%
# anagram 'dog', 'god' 
# 
# # %%
# anagram 'clint eastwood', 'old west action' 
# 
# # %%
# anagram 'aa', 'bb' 
# 
# # %%
# '''
# # Test Your Solution
# Run the cell below to test your solution
# '''
# 
# # %%
# """
# RUN THIS CELL TO TEST YOUR SOLUTION
# """
# f___ n___.t... _______ a_e
# 
# 
# class AnagramTest object :
# 
#     ___ test self, sol :
#         a._e. ? 'go go go', 'gggooo' , T... 
#         a._e. ? 'abc', 'cba' , T...
#         a._e. ? 'hi man', 'hi     man' , T..
#         a._e. ? 'aabbcc', 'aabbc' , F... 
#         a._e. ? '123', '1 2' , F... 
#         print('ALL TEST CASES PASSED')
# 
# 
# # Run Tests
# t _ ? 
# ?.t.. a.. 
# 
# # %%
# # t.test(anagram2)
# 
# # %%
# '''
# # Good Job!
# '''
