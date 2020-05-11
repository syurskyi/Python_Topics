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
#     s _ ?.re.. ' ', '' .lo__
#     t _ ?.re.. ' ', '' .lo__
# 
#     i_  le.?  !_ le.?
#         r_ F...
#     counter _      # dict
#     ___ letter __ s
#         __ ? __ c..
#             c.. ? +_ 1
#         ____
#             c... ? _ 1
# 
#     ___ letter __ t
#         __ ? __ c...
#             c... ? -_ 1
#         ____
#             r_ F...
# 
#     ___ k __ c...
#         __ ? k !_ 0
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
# c_ AnagramTest o..
# 
#     ___ test  sol
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
