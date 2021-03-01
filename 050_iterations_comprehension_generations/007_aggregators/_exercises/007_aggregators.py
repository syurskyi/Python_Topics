# # Aggregators
# # Suppose we want to test if an iterable contains only numeric values.
# # First, we need to figure out how we determine if something is a number.
#
# l _ 10 20 30 40
#
# is_all_numbers = True
# ___ item i_ l
#     i_ n.. isi... i... Number
#         is_all_numbers _ F..
#         b...
# print i...
#
# l _ 10 20 30 40 hello
#
# is_all_numbers _ T..
# ___ item i_ l:
#     i_ n.. isi... i... Number
#         is_all_numbers _ F...
#         b....
# print i.....
#
# # Aggregator
# # Suppose we have a file and we want to make sure that all the rows in the file have length > some number.
# # We can easily test to make sure that every brand in our file is at least 3 characters long:
# # And we can test to see if any line is more than 10 characters:
# # More than 13?
# # Of course, we can also do this using generator expressions instead of map:
#
# row
# w___ o... car-brands.txt __ f
#     ___ ? __ ?
#         print le. ? ? e.._''
#
# w___ o... car-brands.txt __ f
#     result _ al. m.. l_____ ? le. ? >_ 3 ?
# print ?
#
# w___ o... car-brands.txt __ f
#     result _ an. m.. l____ ? le. ? > 10 ?
# print ?
#
# w___ o... car-brands.txt __ f
#     result _ an. ma. l_____ ? le. ? > 13 ?
# print ?
#
# w___ o... car-brands.txt __ f
#     result _ an. le. ? > 13 ___ ? __ ?
# print ?
