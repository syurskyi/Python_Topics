# # -*- coding: utf-8 -*-
#
# """
# Let’s look at how we can extract patterns from text using regular expressions in Python with the `__` module.
# """
#
# ______ __
#
# email = 'jose@tecladocode.com'
# expression = ?   #  would match as many consecutive set of letters in that range as possible
#
# matches = __.f_a_ ex.. em..
# print ?
#
# name = ? 0
# domain = _* ? 1 . ? 2
#
# """
# Of course, a better way of extracting the name and domain could be:
# """
#
# ______ __
#
# email = 'jose@tecladocode.com'
# expression = ?    #  would match as many consecutive set of letters in that range as possible with ekranirovanok tochkoj
#
# matches = __.f_a_ ex.. em..
# print ?
#
# """
# Or indeed:
# """
#
# email = 'jose@tecladocode.com'
# print ?.sp.. '@'  # lol
#
# """
# Let’s say you’ve got a price of an item in a strange format (e.g. extracted from a file):
# """
#
# ______ __
#
# price = 'Price: $189.50'
# expression = Price: 1? (2? 3? 2?    # 1.  end with
#                                     # 2. Returns a match where the string contains digits (numbers from 0-9)
#                                     #    would match as many consecutive set of letters in that range as possible
#                                     # 3. ekranirovannaja tochka
# matches = __.s.. e.. p..
# print ?.g.. 0  # entire match
# print ?.g.. 1  # first thing around brackets
#
# """
# Indeed if you can potentially have commas in your number:
# """
#
# ______ __
#
# price = 'Price: $11,489.50'
# expression = Price: 1? || 2? 3? 4? 5?    # 1.  end with
#                                          # 2. Returns a match where the string contains digits (numbers from 0-9) with comma
#                                          # 3. One or more occurrences
#                                          # 4. ekranirovannaja toch'hka
#                                          # 5. Returns a match where the string contains digits
#                                          #    would match as many consecutive set of letters in that range as possible
# matches = __.s.. e.. p..
# print(?.g.. 0  # entire match
# print(?.g.. 1  # first thing around brackets
#
# """
# Then you could turn the string matched into a proper Python float:
# """
#
# num = '11,489.50'
#
# num = ?.re.. (',', '')  # replace ',' for ''
# print fl.. ?
#
# """
# I would really recommend taking the time to look through regexr and the official Python documentation for `__` module,
# as it is really quite good:
#
# * https://docs.python.org/3/library/__.html
# * http://regexr.com
# """