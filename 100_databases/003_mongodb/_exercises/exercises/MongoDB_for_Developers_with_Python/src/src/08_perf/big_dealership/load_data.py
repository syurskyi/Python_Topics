# _____ n__.m_s.. __ m_s..
# _____ s__.c_s.. __ c_s..
# ____ n__.c.. _____ C..
# ____ n__.e.. _____ E..
# ____ n__.o.. _____ O..
#
# ____ d_t_ _____ d_t_
# _____ ra__
# ____ faker _____ F..
#
# ____ n__.service_record _____ SR..
#
#
# ___ main
#     # large data DB example
#     car_count _ 250_000
#     owner_count _ 100_000
#
#     # simple DB example
#     # car_count = 200
#     # owner_count = 100
#
#     m_s_.i..
#     c_d.
#
#     t0 _ d_t_.n..
#
#     fake _ c_f_a_s..
#     owners _ c_o.. fake count_o_c..
#     print("Created |;,.0_| owners".f.. le. ?
#     cars _ cr_c.. count_c_c..
#     print("Created |;,.0_| cars".f..le. ?
#     __ c.. an. o..
#         a_c_t_o.. o.. c..
#         c_s_r.. c.. f..
#
#     dt _ d_t_.n.. - t0
#     print("Done in @ sec".f.. ?.t_s..
#
#
# models _ |
#     'Ferrari 488 GTB',
#     'Ferrari 360 modena',
#     'F430',
#     '599 GTB Fiorano',
#     '458 Italia',
#     'LaFerrari',
#     'Testarossa',
#     'F12 Berlinetta',
#     '308 GTB/GTS',
#     'F355',
#     'California',
#     '575M Maranello',
#     'F50',
#     'F40',
#     'Enzo Ferrari',
# |
#
# service_operations _ |
#     ('Oil change', 200),
#     ('New tires', 1000),
#     ('New engine', 15000),
#     ('Body repair', 4000),
#     ('New seat', 5000),
#     ('Tune up', 1500),
#     ('Air filter', 100),
#     ('Flat tire', 200),
# |
#
#
# ___ create_faker_and_seed
#     fake _ ?
#     ?.s.. 42
#     ra__.s.. 42
#     r_ ?
#
#
# ___ clear_db
#     C__.d_c..
#     O__.d_c..
#
#
# ___ create_owners fake count_100
#     current_owner_count _ >.o.. .c..
#     __ ? >_ c..
#         print("There are currently |;,| owners. Skipping create.")
#         r_   # list
#
#     count _ count - current_owner_count
#
#     d_t__start _ d_t_ y.._2000 m.._1 d.._1
#     d_t__end _ d_t_ year_d_t_.n.. .y.. m.._1 d.._1
#
#     owners _ # list
#     print("Building owners")
#     ___ _ __ ra.. 0  c..
#         owner _ ?
#         ?.n.. _ f__.n..
#         ?.c.. _ f__.d_t_b_d.. d_t__start_d_t__start,
#                                                      d_t__e.._d_t__e..
#                                                      tz.._N..
#         ?.ap.. ?
#
#     print("Saving owners")
#     O__.o.. .i.. o.. l_b.._T..
#
#     r_ li.. O__.o..
#
#
# ___ create_cars count_200
#     current_car_count _ ?.o.. .c..
#     __ ? >_ c..
#         print("There are currently |;,| cars. Skipping create."
#         r_   # list
#
#     count _ c.. - c_c_c..
#
#     hp_factor _ 660
#     mpg_factor _ 21
#     liters_factor _ 4
#
#     cars _  # list
#     print("Building cars...")
#     ___ _ __ ra.. 0  c..
#         model _ ra__.ch.. m..
#         make _ 'Ferrari'
#         year _ ra__.r_i_ 1985 d_t_.n.. .y..
#         mileage _ ra__.r_i_ 0 150000
#
#         mpg _ in. m_f.. + m_f.. * ra__.ra__ / 4) * 10) / 10.0
#         horsepower _ in. h_f.. + h_f.. * ra__.ra__ / 2)
#         liters _ in. l_f.. + l_f.. * ra__.ra__ / 2) * 100) / 100.0
#
#         engine _ ? h.._h.. l.._l.. m.._m..
#         car _ ? m.._m.. m.._m.. y.._y.. e.._e.. m.._m..
#         c__.ap.. ?
#
#     print("Saving cars...")
#     C__.o.. .i.. ?
#
#     r_ li.. ?.o..
#
#
# ___ add_cars_to_owners owners li.. cars li..
#     ___ o __ ?
#         counter _ ra__.r_i_ 0, 5
#         ___ _ __ ra.. 0 ?
#             car _ ra__.ch.. ?
#             c_s_.a_o.. ?.i. ?.i.
#
#
# ___ create_service_records cars fake
#     d_t__start _ d_t_ y.._2000 m.._1 d.._1
#     d_t__end _ d_t_ year_d_t_.n.. .y.. m.._1 d.._1
#
#     ___ car __ c..
#         counter _ ra__.r_i_ 0, 10
#         is_positive _ ra__.r_i_ 0, 1 __ 1
#         ___ _ __ ra.. 0 c..
#             s _ ra__.ch.. s_o..
#             sr _ ?
#             ?.de.. _ ? 0
#             ?.da.. _ f__.d_t_b_d.. d_t__s.._d_t__s..
#                                                    d_t__e.._d_t__e..
#                                                    tz.._N..
#             ?.p.. _ in. ? 1 + ra__.ra__ - .5) * ? 1 / 4)
#             __ i_p..
#                 ?.c_r.. _ ra__.r_i_ 4, 5
#             ____
#                 ?.c_r.. _ ra__.r_i_ 1, 3
#             c__.s_h_.ap.. ?
#         c__.s..
#
#
# __ ______ __ ______
#     m..
