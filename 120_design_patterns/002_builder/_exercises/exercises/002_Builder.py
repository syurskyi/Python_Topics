# #!/usr/bin/env python
# # Written by: DGC
#
# ______ a..
#
# #==============================================================================
# c_ Vehicle o..
#
#     ___ -  type_name
#         type _ ?
#         wheels _ N..
#         doors _ N..
#         seats _ N..
#
#     ___ view
#         print(
#             "This vehicle is a " +
#             ty.. +
#             " with; " +
#             st. w.. +
#             " wheels, " +
#             st. d.. +
#             " doors, and " +
#             st.s.. +
#             " seats."
#             )
#
# #==============================================================================
# c_ VehicleBuilder o..
#     """
#     An abstract builder class, for concrete builders to be derived from.
#     """
#     __m__ _ ___.____
#
#     ??.?
#     ___ make_wheels
#         ra..
#
#     ??.?
#     ___ make_doors
#         ra..
#
#     ??.?
#     ___ make_seats
#         ra..
#
# #==============================================================================
# c_ CarBuilder VB..
#
#     ___ -
#         vehicle _ V.. "Car "
#
#     ___ make_wheels
#         ?.w.. _ 4
#
#     ___ make_doors
#         ____.?.d.. _ 3
#
#     ___ make_seats
#         ?.s.. _ 5
#
# #==============================================================================
# c_ BikeBuilder VB..
#
#     ___ -
#         vehicle _ V.. "Bike
#
#     ___ make_wheels
#         ?.w.. _ 2
#
#     ___ make_doors
#         ?.d.. _ 0
#
#     ___ make_seats
#         ____.?.s.. _ 2
#
# #==============================================================================
# c_ VehicleManufacturer o..
#     """
#     The director class, this will keep a concrete builder.
#     """
#
#     ___ -
#         builder _ N..
#
#     ___ create
#         """
#         Creates and returns a Vehicle using ____.builder
#         Precondition: not ____.builder is N..
#         """
#         a.. no. b.. __ N.., "No defined builder"
#         ?.m..
#         ?.m..
#         ?.m..
#         r_ ?.?
#
# #==============================================================================
# __ ______ __ _____
#     manufacturer _ VM..
#
#     ?.b.. _ CB..
#     car _ ?.c..
#     ?.v..
#
#     ?.b.. _ BB..
#     bike _ ?.c..
#     ?.v..
