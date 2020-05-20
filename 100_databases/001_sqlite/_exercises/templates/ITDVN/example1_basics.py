# _____ ?
#
# conn _ ?.c.. db._3
#
# ?.e.. 'C.. T.. "users" (id, first_name, last_name, birthday)'
# ?.e.. 'S.. _ F.. "users"'
# ?.e..
#     """I.. I.. users(id, first_name, last_name, birthday)
#        V.. (1, "Eugene", "Petrov", "09-11-1992")
#     """
# )
# ?.e..
#     """I.. I.. users(id, first_name, last_name, birthday)
#        V.. (2, "Viktor", "Ivanov", "10-11-1992"),
#               (3, "Dmitry", "Sidorov", "11-09-1992")
#     """
# )
#
# users _ ?.e.. 'S.. _ F.. "users"').f_a..
# print ?
# cursor _ ?.e.. 'S.. _ from "users";')
# print(?.f_o..
# print(?.f_o..
# print(?.f_o..
# # cursor.close()
#
# ___
#     c.. _ ?.e.. 'S.. _ F.. "tags"'
# _____ ?.O.. __ e
#     print ?
#
# first_name _ 'Dmitry'
# sql_text _ 'S.. _ F.. users W.. first_name = "@"'  ?
# print ?
# first_name _ '"Dmitry"'
# sql_text _ 'S.. _ F.. users W.. first_name = "@"' ?
# print ?
#
# sql_text _ 'S.. _ F.. "users" W.. id = @'  (10,)
# print ?
# sql_text2 _ 'S.. _ F.. "users" W.. id = @' ('0 or id like "%"',)
# print ?
#
# ?.e.. 'S.. _ F.. "users" W.. id = ?', (10,))
# ?.e.. 'S.. _ F.. "users" W.. id = :id', {'id': 10})
# ?.c..
