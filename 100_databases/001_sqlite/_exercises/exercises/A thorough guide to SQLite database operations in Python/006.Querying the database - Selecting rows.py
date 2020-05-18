# Selecting rows from an existing SQLite database
#
# _____ _3
#
# sqlite_file _ 'my_first_db.sqlite'    # name of the sqlite database file
# table_name _ 'my_table_2'	# name of the table to be queried
# id_column _ 'my_1st_column'
# some_id _ 123456
# column_2 _ 'my_2nd_column'
# column_3 _ 'my_3rd_column'
#
# # Connecting to the database file
# conn _ _3.co.. s_f..
# c _ ?.cu..
#
# # 1) Contents of all columns for row that match a certain value in 1 column
# ?.ex.. 'S.. * F.. @ W.. @_"Hi World"'.\
#         f.. tn_? cn_c_2
# all_rows _ ?.f..
# print('1):' ?
#
# # 2) Value of a particular column for rows that match a certain value in column_1
# ?.ex..('S.. (@) F.. @ W.. @_"Hi World"'.\
#         f.. coi_c_2 tn_? cn_c_2
# all_rows _ ?.f..
# print('2):'?
#
# # 3) Value of 2 particular columns for rows that match a certain value in 1 column
# ?.ex..('S.. @,@ F.. @ W.. @_"Hi World"'.\
#         f.. coi1_c_2, coi2_c_3 tn_? cn_c_2
# all_rows _ ?.f..
# print('3):' ?
#
# # 4) Selecting only up to 10 rows that match a certain value in 1 column
# ?.ex..('S.. * F.. @ W.. @_"Hi World" LIMIT 10'.\
#         f.. tn_? cn_c_2
# ten_rows _ ?.f..
# print('4):' ?
#
# # 5) Check if a certain ID exists and print its column contents
# ?.ex..("S.. * F.. @ W.. @_?".\
#         f.. tn_?, cn_c_2, idf_i_c.. (123456,
# id_exists _ ?.f..
# __ ?
#     print('5): @'.f.. ?
# ____
#     print('5): @ does not exist'.f.. s_i.
#
# # Closing the connection to the database file
# ?.cl..
