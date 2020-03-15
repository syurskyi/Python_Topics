# c_ Director
#     __builder _ N..
#
#     ___ setBuilder  builder
#         __?  ?
#
#     ___ getCar
#         car _ C..
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
#         i _ 0
#         w____ ? < 4
#             wheel _ __b__.gW..
#             car.aW.. ?
#             ? +_ 1
#
#         r_ c..
#
#
# # The whole product
# c_ Car
#     ___ -
#         __wheels _ li..
#         __engine _ N..
#         __body _ N..
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
#         wheel _ W..
#         ?.s.. _ 22
#         r_ ?
#
#     ___ getEngine
#         engine _ E..
#         ?.h.. _ 400
#         r_ ?
#
#     ___ getBody
#         body _ B..
#         ?.s.. _ "SUV"
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
#     shape _ N..
#
#
# ___ main
#     jeepBuilder _ J..  # initializing the class
#
#     director _ D..
#
#     # Build Jeep
#     print("Jeep")
#
#     ?.sB... j..
#     jeep _ ?.gC..
#     ?.s..
#     print("")
#
#
# __ _______ __ ______
#     ?
