# _____ n__ .m_s.. __ m_s..
# ____ n__ .c.. _____ ?
# ____ n__ .e.. _____ ?
# ____ n__ .s.. _____ ?
#
#
# ___ main
#     p_h..
#     c_m..
#     # update_doc_versions()
#     u_l..
#
#
# # noinspection PyProtectedMember
# # def update_doc_versions():
# #     for car in Car.objects():
# #         car._mark_as_changed('vi_number')
# #         car.save()
#
#
# ___ print_header
#     print('----------------------------------------------')
#     print('|                                             |')
#     print('|           SERVICE CENTRAL v.02              |')
#     print('|               prod edition                  |')
#     print('|                                             |')
#     print('----------------------------------------------')
#     print()
#
#
# ___ config_mongo
#     m_s__.g_i..
#         'the_db_admin',
#         'the-password-3809b81f-ba37-403d-8013-a1ebaf13cf94',
#         10001,
#         '107.170.211.24'
#     )
#
#
# ___ user_loop
#     w__ T..
#         print("Available actions:")
#         print(" * [a]dd car")
#         print(" * [l]ist cars")
#         print(" * [p]oorly serviced")
#         print(" * perform [s]ervice")
#         print(" * e[x]it")
#         print()
#         ch _ in.. "> " .s.. .l..
#         __ ? __ 'a'
#             a..
#         ____ ? __ 'l'
#             l..
#         ____ ? __ 's'
#             s..
#         ____ ? __ 'p'
#             s_p_s_c..
#         ____ no. ? o. ? __ 'x'
#             print("Goodbye")
#             b..
#
#
# ___ add_car
#     model _ in.. "What is the model? "
#     make _ 'Ferrari'  # input("What is the make? ")
#     year _ int in.. "Year built? "
#
#     car _ ?
#     ?.y.. _ y..
#     ?.m.. _ m..
#     ?.m.. _ m..
#
#     engine _ ?
#     ?.h.. _ 590
#     ?.m.. _ 22
#     ?.l.. _ 4.0
#
#     ?.? _ ?
#
#     ?.s..
#
#
# ___ list_cars
#     cars _ ?.o.. .o_b. "-year"
#     ___ car __ ?
#         print("@ -- @ with vin @ (year @)".f..
#             ?.m.., ?.m.., ?.v.. ?.y..
#         print("@ of service records".f.. le. ?.s_h..
#         ___ s __ ?.s_h..
#             print("  * $|;,.0_ @".f.. ?.p.. ?.d..
#     print()
#
#
# ___ find_car
#     print("TODO: find_car")
#
#
# ___ service_car
#     # vin = input("What is the VIN of the car to service? ")
#     # car = Car.objects(vi_number=vin).first()
#     # if not car:
#     #     print("Car with VIN {} not found!".format(vin))
#     #     return
#     #
#     # service = ServiceHistory()
#     # service.price = float(input("What is the price? "))
#     # service.description = input("What type of service is this? ")
#     # service.customer_rating = int(input("How happy is our customer? [1-5] "))
#     #
#     # car.service_history.append(service)
#     # car.save()
#
#     vin _ in.. "What is the VIN of the car to service? "
#     service _ ?
#     ?.p.. _ fl.. in.. "What is the price? "
#     ?.d.. _ in.. "What type of service is this? "
#     ?.c_r.. _ in. in.. "How happy is our customer? [1-5] "
#
#     updated _ ?.o.. vi_number_v.. .u_o.. push__service_history_s..
#     __ ? __ 0
#         print("Car with VIN @ not found!".f.. v..
#         r_
#
#
# ___ show_poorly_serviced_cars
#     level _ in. in.. "What max level of satisfaction are we looking for? [1-5] "
#     # { "service_history.customer_rating": {$lte: level} }
#     cars _ ?.o.. service_history__customer_rating__lte_l..
#     ___ car __ ?
#         print("@ -- @ with vin @ (year @)".f..
#             ?.m.. ?.m.. ?.v.. ?.y..
#         print("@ of service records".f.. le. ?.s_h..
#         ___ s __ ?.s_h..
#             print("  * Satisfaction: @ $|;,.0_ @".f..(
#                 ?.c.. ?.p.. ?.d..
#     print()
#
#
# __ ______ __ ______
#     ?
