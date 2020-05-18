# _____ _____
#
# sqlite_file_____ 'my_first_db.sqlite'    # name of the sqlite database file
# table_name_____ 'my_table_2'   # name of the table to be created
# id_column_____ 'my_1st_column' # name of the P.. K.. column
# new_column_____ 'unique_names'  # name of the new column
# column_type_____ 'T...' # E.g., IN.., T..., N.., RE., BLOB
# index_name_____ 'my_unique_index'  # name for the new unique index
#
# # Connecting to the database file
# conn_____ _____.co.. s_f..
# c_____ ?.cu..
#
# # Adding a new column and update some record
# ?.ex.. "ALTER T.. @ ADD COLUMN '@' @"\
#         .f... tn_? cn_? ct_?
# ?.ex.. "U.. @ SET @_'sebastian_r' W.. {idf}_123456".\
#         f... tn_table_name, idf_id_column, cn_new_column
#
# # Creating an unique index
# ?.ex.. 'C.. INDEX @ on @(@)'\
#         .f...(ix_? tn_? cn_?
#
# # Dropping the unique index
# # E.g., to avoid future conflicts with update/insert functions
# ?.ex.. 'D.. INDEX @'.f...(ix_?
#
# # Committing changes and closing the connection to the database file
# ?.co..
# ?.cl..
