# # We have to be careful when working with context managers and lazy iterators.
# # Consider this example where we want to create a generator from a file:
#
# print('#' * 52 + '  ### Caveat with Lazy Iterators')
#
# ______ cs
#
#
# ___ read_data
#     w___ o... 'nyc_parking_tickets_extract.csv' __ f
#         r_ cs_.re.. f delimiter_',', quotechar_'"'
#
# # for row in read_data():
# #     print(row)         # ValueError: I/O operation on closed file.
#
# # As you can see, read_data returns a lazy iterator (csv.reader), but by the time we iterate over it, the with context
# # that opened the file was exited, and the file was closed!
# # We have two possible solutions here:
# # The first one is not very desirable since it involves reading the entire file into memory by iterating the file
# # and putting it into a list before we exit the with block:
#
#
# print('#' * 52 + '  The first one is not very desirable since it involves reading the entire file into memory'
#                  '  by iterating the file and putting it into a list before we exit the `with` block:')
#
#
# ___ read_data
#     w___ o.. 'nyc_parking_tickets_extract.csv') __ f
#         r_ li cs_.re..  delimiter_',', quotechar_'"'
#
#
# ___ row __ ?
#     print ?
#
# # The second method, the one we have used quite a bit, involves yielding each row from the csv reader:
#
# print('#' * 52 + '  The second method, the one we have used quite a bit,'
#                  '  involves yielding each row from the csv reader:')
#
#
# ___ read_data
#     w___ o.. ('nyc_parking_tickets_extract.csv') __ f
#         y_____ f.. cs_.re.. f de..._',' quot.._'"'
#
#
# ___ row __ ?
#     print ?
