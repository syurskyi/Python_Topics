# c_ Director
#     __builder _ N..
#
#     ___ setBuilder  builder
#         __?  ?
#
#     ___ getCar
#         car = C..
#
#         # First goes the body
#         body _ __b__.g..
#         c__.s.. ?
#
#         # Then engine
#         engine _ __b__.g..
#         c__.s.. ?
#
#         # And four wheels
#         i = 0
#         w____ ? < 4
#             wheel = __b__.gW..
#             car.aW.. ?
#             ? +_ 1
#
#         r_ c..
#
#
# # The whole product
# c_ Car
#     ___ -
#         __wheels = li..
#         __engine = N..
#         __body = N..
#
#     ___ setBody  body
#         __?  ?
#
#     ___ attachWheel  wheel
#         __w__.ap.. ?
#
#     ___ setEngine engine
#         __?  ?
#
#     ___ specification
#         print("body: @"  __b__.s..      # string
#         print("engine horsepower: @"  __e__.h..   # digit
#         print("tire size: @\'"  __w.. 0 .s..    # digit
#
#
# c_ Builder
#     ___ getWheel
#         p..
#
#     ___ getEngine
#         p..
#
#     ___ getBody
#         p..
#
#
# c_ JeepBuilder B..
#
#     ___ getWheel
#         wheel = W..
#         ?.s.. _ 22
#         r_ ?
#
#     ___ getEngine
#         engine = E..
#         ?.h.. _ 400
#         r_ ?
#
#     ___ getBody
#         body = B..
#         ?.s.. = "SUV"
#         r_ body
#
#
# # Car parts
# c_ Wheel
#     size _ N..
#
#
# c_ Engine
#     horsepower _ N..
#
#
# c_ Body
#     shape = N..
#
#
# ___ main
#     jeepBuilder = J..  # initializing the class
#
#     director = D..
#
#     # Build Jeep
#     print("Jeep")
#
#     ?.sB... j..
#     jeep = ?.gC..
#     ?.s..
#     print("")
#
#
# __ _______ __ ______
#     ?
