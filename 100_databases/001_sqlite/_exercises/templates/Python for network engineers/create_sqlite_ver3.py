# ______ __
# ______ _3
# ______ re
#
# data_filename _ 'dhcp_snooping.txt'
# db_filename _ 'dhcp_snooping.db'
# schema_filename _ 'dhcp_snooping_schema.sql'
#
# regex _ ?.c.. ('(___1) +(___1) +__2 +__1 +(__2) +(__1)')    # 1 соответствует заполненному полю
#                                                             # 2 соответствует цифре
#
# result _      # list
#
# w__ o.. dhcp_snooping.txt __ data
#     ___ line __ ?
#         match _ r___.s.. ?
#         __ ?
#             r__.ap.. ?.g..
#
# db_exists _ __.pa__.ex.. d_f..
#
# conn _ _3.c.. d_f..
#
# __ no. d_e..
#     print('Creating schema...')
#     w__ o.. s_f.. _ __ f
#         schema _ ?.r..
#     c__.ex.. ?
#     print('Done')
# ____
#     print('Database exists, assume dhcp table does, too.')
#
# print('Inserting DHCP Snooping data')
#
# ___ row __ result
#     ___
#         w__ c..
#             query _ i.. i.. dhcp |m.. ip, vlan, interface
#                        v @ @ @ @
#             c__.ex.. q.. r..
#     ______ _3.IntegrityError __ e:
#         print *Error occured:  ?
#
# ?.c..
