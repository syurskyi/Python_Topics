# _____ _3
#
#
# ___ connect sqlite_file
#     """ Make connection to an SQLite database file """
#     conn _ _3.co.. ?
#     c _ ?.cu..
#     r_ ? ?
#
#
# ___ close conn
#     """ Commit changes and close connection to the database """
#     # conn.c..
#     ?.cl..
#
#
# ___ total_rows cursor table_name print_out_F..
#     """ Returns the total number of rows in the database """
#     ?.ex... 'S.. COUNT(*) F.. @'.f.. t_n..
#     count _ ?.f..
#     __ p_o..
#         print('\nTotal rows: @'.f.. ? 0 0
#     r_ ? 0 0
#
#
# ___ table_col_info ? table_name print_out_F..
#     """ Returns a list of tuples with column informations:
#     (id, name, type, notnull, default_value, primary_key)
#     """
#     ?.ex... 'PRAGMA TABLE_INFO(@)'.f.. t_n..
#     info _ ?.f..
#
#     __ p_o..
#         print("\nColumn Info:\nID, Name, Type, NotNull, DefaultVal, PrimaryKey")
#         ___ col __ i..
#             print ?
#     r_ ?
#
#
# ___ values_in_col cursor table_name print_out_T..
#     """ Returns a dictionary with columns as keys
#     and the number of not-null entries as associated values.
#     """
#     ?.ex... 'PRAGMA TABLE_INFO(@)'.f.. t_n..
#     info _ ?.f..
#     col_dict _ di..
#     ___ col __ i..
#         c_d_|? 1 _ 0
#     ___ col __ c_d..
#         ?.ex...('S.. (@) F.. @ '
#                   'W.. @ IS N.. N..'.f.. c.. t_n..
#         # In my case this approach resulted in a
#         # better performance than using COUNT
#         number_rows _ le. ?.f..
#         c_d..|c.. _ ?
#     __ p_o..
#         print("\nNumber of entries per column:")
#         ___ i __ c_d__.it..
#             print('@: @'.f.. ? 0 ? 1
#     r_ ?
#
#
# __ _______ __ _____
#
#     sqlite_file _ 'my_first_db.sqlite'
#     table_name _ 'my_table_3'
#
#     conn, c _ co..  s_f..
#     t_r.. c, t_n.. p_o.._T..
#     t_c_i.. c, t_n.., print_out_True
#     # next line might be slow on large databases
#     v_i_c.. c, t_n.., print_out_T..
#
#     cl.. co..
