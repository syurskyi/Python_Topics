# _____ __
# titles = [
#     "Significant Others (1987)",
#     "Tales of the City (1978)",
#     "The Days of Anna Madrigal (2014)",
#     "Mary Ann in Autumn (2010)",
#     "Further Tales of the City (1982)",
#     "Babycakes (1984)",
#     "More Tales of the City (1980)",
#     "Sure of You (1989)",
#     "Michael Tolliver Lives (2007)"
# ]
# titles.s..
# fixed_titles _   # list
#
# pattern = __.c...  _ 1? title 2? |3? |4?) \ || 1? date 5? 6? \    # 1. Named capturing group 2. Starts with
#                                                                # 3. Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
#                                                                # 4. One or more occurrences
#                                                                # 5. Returns a match where the string contains digits (numbers from 0-9)
#                                                                # 6. Exactly the specified number of occurrences - from 2 to 6
# ___ book __ t..
#     # result = pattern.sub("\g<2> - \g<1>", book)
#     result = p__.s..("\g<date> - \g<title>" b..
#
#     f__.a.. r...
# f_t.s...
# print f_t
