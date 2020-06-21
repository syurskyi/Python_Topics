# c_ ComputerState o..
#     name _ "state"
#     allowed _    # list
#
#     ___ switch state
#         __ ?.name __ a...
#             print('Current:',?,' => switched to new state', ?.n..
#             __cl..__ _ ?
#         ____
#             print('Current:',?,' => switching to',?.n..,'not possible.')
#
#     ___ -s
#         r_ n..
#
#
# c_ Off C..
#     n.. _ *off
#     a... _ |*on
#
# c_ On C..
#     name _ *on
#     a... _ |*off *suspend *hibernate
#
# c_ Suspend C..
#     name _ *suspend
#     a... _ |*on
#
# c_ Hibernate C..
#     name _ *hibernate
#     a... _ |*on
#
#
# c_ Computer o..
#     ___ - model_*HP
#         st__ _ O..
#
#     ___ change state
#         ?.switch ?
#
#
# __ ________ __ _______
#     comp _ C..
#     # Switch on
#     ?.c... On
#     # Switch off
#     ?.c... Off
#
#     # Switch on again
#     ?.c... On
#     # Suspend
#     ?.c... S...
#     # Try to hibernate - cannot!
#     ?.c... H..
#     # switch on back
#     ?.c... On
#     # Finally off
#     ?.c... Off