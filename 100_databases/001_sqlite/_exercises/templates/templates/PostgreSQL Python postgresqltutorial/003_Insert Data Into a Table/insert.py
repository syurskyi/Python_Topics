# _____ ?
# ____ c.. _____ c..
#
#
# ___ insert_vendor vendor_name
#     """ insert a new vendor into the vendors table """
#     sql _ """I.. I.. vendors(vendor_name)
#              V..(%s) RETURNING vendor_id;"""
#     conn _ w..
#     vendor_id _ w..
#     ___
#         # read database configuration
#         params _ c..
#         # connect to the PostgreSQL database
#         conn _ ?.c.. $$p..
#         # create a new cursor
#         cur _ ?.c..
#         # execute the I.. statement
#         ?.e.. s_n       # get the generated id back
#         vendor_id _ ?.f_o.. 0
#         # commit the changes to the database
#         conn.c..
#         # close communication with the database
#         ?.c..
#     ______ E.., ?.DE.. __ error
#         print ?
#     f__
#         __ c_ no. w..
#             ?.c..
#
#     r_ vendor_id
#
#
# ___ insert_vendor_list(vendor_list):
#     """ insert multiple vendors into the vendors table  """
#     sql _ "I.. I.. vendors(vendor_name) V..(%s)"
#     conn _ w..
#     ___
#         # read database configuration
#         params _ c..
#         # connect to the PostgreSQL database
#         conn _ ?.c.. $$p..
#         # create a new cursor
#         cur _ ?.c..
#         # execute the I.. statement
#         ?.e_m_(s.. v_l..       # commit the changes to the database
#         ?.c..
#         # close communication with the database
#         ?.c..
#     ______ E.., ?.DE.. __ error
#         print ?
#     f__
#         __ c.. __ no. w..
#             ?.c..
#
#
# __ _____ __ ______
#     # insert one vendor
#     insert_vendor("3M Co.")
#     # insert multiple vendors
#     insert_vendor_list([
#         ('AKM Semiconductor Inc.',),
#         ('Asahi Glass Co Ltd.',),
#         ('Daikin Industries Ltd.',),
#         ('Dynacast International Inc.',),
#         ('Foster Electric Co. Ltd.',),
#         ('Murata Manufacturing Co. Ltd.',)
#     ])
