# _____ _3
#
# sqlite_file _ 'my_first_db.sqlite'    # name of the sqlite database file
# table_name _ 'my_table_3'   # name of the table to be created
# id_field _ 'id' # name of the ID column
# date_col _ 'date' # name of the date column
# time_col _ 'time'# name of the time column
# date_time_col _ 'date_time' # name of the date & time column
# field_type _ 'T...'  # column data type
#
# # Connecting to the database file
# conn _ _3.co.. s_f..
# c _ ?.cu..
#
# # Creating a new SQLite table with 1 column
# ?.ex.. 'C.. T.. @ (@ @ P.. K..)'\
#         .f..(tn_? fn_i.f.. ft_?
#
# # A) Adding a new column to save date insert a row with the current date
# # in the following format: YYYY-MM-DD
# # e.g., 2014-03-06
# ?.ex.. "ALTER T.. @ ADD COLUMN '@'"\
#          .f.. tn_? cn_d.c..
# # insert a new row with the current date and time, e.g., 2014-03-06
# ?.ex.. "I.. I.. @ (@, @) V..('some_id1', DATE('now'))"\
#          .f.. tn_? idf_? cn_d_c..
#
# # B) Adding a new column to save date and time and update with the current time
# # in the following format: HH:MM:SS
# # e.g., 16:26:37
# ?.ex.. "ALTER T.. @ ADD COLUMN '@'"\
#          .f.. tn_? cn_t_c..
# # update row for the new current date and time column, e.g., 2014-03-06 16:26:37
# ?.ex.. "U.. @ SET @_TIME('now') W.. @_'some_id1'"\
#          .f.. tn_? idf_? cn_t_c..
#
# # C) Adding a new column to save date and time and update with current date-time
# # in the following format: YYYY-MM-DD HH:MM:SS
# # e.g., 2014-03-06 16:26:37
# ?.ex.. "ALTER T.. @ ADD COLUMN '@'"\
#          .f.. tn_? cn_d_t_c..
# # update row for the new current date and time column, e.g., 2014-03-06 16:26:37
# ?.ex.. "U.. @ SET @_(CURRENT_TIMESTAMP) W.. @_'some_id1'"\
#          .f.. tn_? idf_? cn_d_t_c..
#
# # The database should now look like this:
# # id         date           time        date_time
# # "some_id1" "2014-03-06"   "16:42:30"  "2014-03-06 16:42:30"
#
# # 4) Retrieve all IDs of entries between 2 date_times
# ?.ex.. "S.. @ F.. @ W.. @ BETWEEN '2013-03-06 10:10:10' AND '2015-03-06 10:10:10'".\
#     f.. idf_? tn_? cn_d_t_c..
# all_date_times _ ?.f..
# print('4) all entries between ~2013 - 2015:' ?
#
# # 5) Retrieve all IDs of entries between that are older than 1 day and 12 hrs
# ?.ex.. "S.. @ F.. @ W.. DATE('now') - @ >_ 1 AND DATE('now') - @ >_ 12".\
#     f.. idf_? tn_? dc_? tc_?
# all_1day12hrs_entries _ ?.f..
# print('5) entries older than 1 day:' ?
#
# # Committing changes and closing the connection to the database file
# ?.co..
# ?.cl..
