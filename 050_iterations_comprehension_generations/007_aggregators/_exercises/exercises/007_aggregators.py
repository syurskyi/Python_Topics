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
# w___ o... car-brands.txt a_ f
#     ___ row i_ f:
#         print le. r.. r.. e.._''
#
# w___ o... car-brands.txt a_ f
#     result _ al. m.. l_____ row le. row >_ 3 f
# print r..
#
# w___ o... car-brands.txt a_ f
#     result _ an. m.. l____ row le. row > 10 f
# print r....
#
# w___ o... car-brands.txt a_ f
#     result _ an. ma. l_____ row le. row > 13 f
# print r...
#
# w___ o... car-brands.txt a_ f
#     result _ an. le. row > 13 ___ row i_ f
# print r...
