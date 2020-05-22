# #!/usr/bin/python
# _____ ?
# ____ c.. _____ c..
#
#
# ___ add_part part_name vendor_list
#     # statement for inserting a new row into the parts table
#     insert_part _ "I.. I.. parts(part_name) V..(%s) RETURNING part_id;"
#     # statement for inserting a new row into the vendor_parts table
#     assign_vendor _ "I.. I.. vendor_parts(vendor_id,part_id) V..(%s,%s)"
#
#     conn _ N..
#     ___
#         params _ c..
#         conn _ ?.c.. $$p..
#         cur _ ?.c..
#         # insert a new part
#         ?.e.. i_p..  p_n..
#         # get the part id
#         part_id _ ?.f_o.. 0
#         # assign parts provided by vendors
#         ___ v_i. __ v_l..
#             ?.e.. a_v..  v_i. p_i.
#
#         # commit changes
#         ?.c..
#     ______  E.., ?.DE.. __ error
#         print ?
#     f__
#         __ c.. __ no. N..
#             ?.c..
#
#
# __ _____ __ ______
#     ? 'SIM Tray', (1, 2
#     ? 'Speaker', (3, 4
#     ? 'Vibrator', (5, 6
#     ? 'Antenna', (6, 7
#     ? 'Home Button', (1, 5
#     ? 'LTE Modem', (1, 5