# #!/usr/bin/env python
# # Written by: DGC
#
# ______ a..
#
# #==============================================================================
# c_ Vehicle o..
#
#     ___ - ____ type_name
#         ____.type _ ?
#         ____.wheels _ N..
#         ____.doors _ N..
#         ____.seats _ N..
#
#     ___ view ____
#         print(
#             "This vehicle is a " +
#             ____.ty.. +
#             " with; " +
#             st. ____.w.. +
#             " wheels, " +
#             st. ____.d.. +
#             " doors, and " +
#             st. ____.s.. +
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
#     ___ make_wheels ____
#         ra..
#
#     ??.?
#     ___ make_doors ____
#         ra..
#
#     ??.?
#     ___ make_seats ____
#         ra..
#
# #==============================================================================
# c_ CarBuilder VB..
#
#     ___ - ____
#         ____.vehicle _ V.. "Car "
#
#     ___ make_wheels ____
#         ____.?.w.. _ 4
#
#     ___ make_doors ____
#         ____.?.d.. _ 3
#
#     ___ make_seats ____
#         ____.?.s.. _ 5
#
# #==============================================================================
# c_ BikeBuilder VB..
#
#     ___ - ____
#         ____.vehicle _ V.. "Bike
#
#     ___ make_wheels ____
#         ____.?.w.. _ 2
#
#     ___ make_doors ____
#         ____.?.d.. _ 0
#
#     ___ make_seats ____
#         ____.?.s.. _ 2
#
# #==============================================================================
# c_ VehicleManufacturer o..
#     """
#     The director class, this will keep a concrete builder.
#     """
#
#     ___ - ____
#         ____.builder _ N..
#
#     ___ create ____
#         """
#         Creates and returns a Vehicle using ____.builder
#         Precondition: not ____.builder is N..
#         """
#         a.. no. ____.b.. __ N.., "No defined builder"
#         ____.?.m..
#         ____.?.m..
#         ____.?.m..
#         r_ ____.?.?
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
