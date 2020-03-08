# """Mediator pattern
# """
# ______ ra__
# ______ ti__
#
#
# c_ ControlTower o...
#
#     ___ -
#         available_runways _ l..
#         engaged_runways _ l..
#
#     ___ authorize_landing
#         __ no. a_r..:
#             print("Request denied. No available runways")
#             r_ F...
#
#         ____
#             runway _ a_r...po.
#             e_r__.ap.. ?
#             print("Request granted. Please land on runway @".f.. ?
#             s..
#             r_ T..
#
#     ___ authorize_takeoff
#         # for simplicity, all takeoff requests are granted
#         ti__.sl.  ra__.r_i.. 0 2
#         runway _ e_r__.po.
#         a_r...ap.. ?
#         s..
#
#     ___ status
#         print(
#             "The control tower has @ available runway/s".f..|
#                 le. a_r..
#             |
#         |
#
#
# c_ Airplane o...
#
#     ___ -
#         control_tower _ N..
#
#     ??
#     ___ registered
#         r_ T.. __ c_t.. __ no. N.. ____ F...
#
#     ___ register control_tower
#         ?  ?
#         print("An airplane registers with the control tower")
#
#     ___ request_landing
#         is_authorized _ c_t___.a_l..
#         __ ?
#             la..
#
#     ___ land
#         print("The airplane @ lands".f.. ?
#
#     ___ takeoff
#         print("The airplane @ takes off".f.. ?
#         c_t___.a_t..
#
#
# c_ Runway o...
#
#     ___ register control_tower
#         print("A runway has been registered with the control tower")
#         c_t___.a_r...ap.. ?
#         c_t___.st..
#
#
# ___ main
#     print("There is an airport with 2 runways and a control tower\n")
#     r1 _ R..
#     r2 _ R..
#     ct _ C..
#     r1.r__(ct)
#     r2.r___(ct)
#
#     print("\n3 airplanes approach the airport and register with the tower")
#     a1 _ A...
#     a2 _ A...
#     a3 _ A...
#     a1.r___(ct)
#     a2.r___(ct)
#     a3.r___(ct)
#
#     print(
#         "\nTwo airplanes request for landing. There are enough runways, so "
#         "the requests are granted"
#     )
#     a1.request_landing()
#     a2.request_landing()
#
#     print(
#         "\nThe third airplane also makes a request for landing. There are no"
#         " runways available, so the request is denied"
#     )
#     a3.request_landing()
#
#     print(
#         "\nAfter a while, the first airplane takes off, so now the third "
#         "airplane can land"
#     )
#     a1.takeoff()
#     a3.request_landing()
#
#
# __ _______ __ ______
#     ?
