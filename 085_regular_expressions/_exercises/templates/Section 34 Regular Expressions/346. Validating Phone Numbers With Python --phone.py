# # -*- coding: utf-8 -*-
#
# ______ __
# # Returns first instance of phone number pattern:
# ___ e__ input
# 	phone_regex _ __.c.. _ 1? 2? 3? 2? ?3 -?2 ?3 ?1    # 1. Returns a match where the specified characters are at the beginning or at the end of a word
#                                                      # 2. Returns a match where the string contains digits (numbers from 0-9)
# 												       # 3. Exactly the specified number of occurrences - 3 , 4
# 	match _ ?.s.. ?
# 	__ ?
# 		r_ ?.g..
# 	r_ N..
#
# # Returns all instances of phone number pattern in a list
# ___ e__a_ input
# 	phone_regex _ __.c.. _ 1? 2? 3? 2? 3?-2? 3? 1?     # 1. Returns a match where the specified characters are at the beginning or at the end of a word
#                                                      # 2. Returns a match where the string contains digits (numbers from 0-9)
# 												       # 3. Exactly the specified number of occurrences - 3, 4
# 	r_ ?.f_a_ i..
#
# # One way of checking if entire string is valid phone number:
# # ___ i..(input):
# # 	phone_regex = __.c..(r'^\d{3} \d{3}-\d{4}$')
# # 	match = phone_regex.search(input)
# # 	if match:
# # 		return True
# # 	return False
#
# # Another way of doing the same thing, using the fullmatch method
# ___ i.. input
# 	phone_regex _ __.c.. _ 2? 3? 2? 3?-2? 3?         # 1. Returns a match where the specified characters are at the beginning or at the end of a word
#                                                    # 2. Returns a match where the string contains digits (numbers from 0-9)
# 												     # 3. Exactly the specified number of occurrences - 3, 4
# 	match _ ?.f_m_ ?
# 	__ ?
# 		r_ T..
# 	r_ F..
#
# # Calling our functions a bunch of times...
#
# print(e__("my number is 432 567-8976"))
# print(e__("my number is 432 567-897622"))
# print(e__("432 567-8976 asdjhasd "))
# print(e__("432 567-8976"))
#
# print(e__a_("my number is 432 567-8976 or call me at 345 666-7899"))
# print(e__a_("my number is 432 56"))
#
# print(i..("432 567-8976"))
# print(i..("432 567-8976 ads"))
# print(i..("asd 432 567-8976 d"))
#
#
#
