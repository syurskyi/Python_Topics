# _____ ty..
#
# _____ b..
# _____ d_t_
#
# ____ n__.c.. _____ C..
# ____ n__.e.. _____ E..
# ____ n__.o.. _____ O..
# ____ n__.s_r.. _____ SR..
#
#
# ___ create_owner name st. __ O..
#     owner _ ? n.._n..
#     ?.s..
#
#     r_ ?
#
#
# ___ create_car model st. make st. year in.
#                horsepower in. liters fl..
#                mpg fl.. mileage in. __ C..
#     engine _ ? h.._h.. l.._l.. m.._m..
#     car _ ? m.._m.. m.._m.. y.._y.. e.._e.. m.._m..
#     ?.s..
#
#     r_ ?
#
#
# ___ record_visit customer
#     O__.o.. n.._? .u_o.. inc__number_of_visits_1
#
#
# ___ find_cars_by_make make __ C..
#     car _ ?.o.. m.._m.. .f..
#     r_ ?
#
#
# ___ find_owner_by_name name __ O..
#     t0 _ d_t_.d_t_.n..
#     owner _ ?.o.. n_n.. .f..
#     dt _ d_t_.d_t_.n.. - t0
#     print("Owner found in @ ms".f.. ?.t_s.. * 1000
#
#     r_ ?
#
#
# ___ find_owner_by_id owner_id __ O..
#     owner _ ?.o.. id_? .f..
#     r_ ?
#
#
# ___ find_cars_with_bad_service l.._10 __ ty__.L.. C..
#     cars _ ?.o.. service_history__customer_rating__lt_4 |;l..
#     r_ li.. ?
#
#
# ___ percent_cars_with_bad_service
#     t0 _ d_t_.d_t_.n..
#     bad _ ?.o.. .fi.. service_history__customer_rating__lte_1 .c..
#     dt _ d_t_.d_t_.n.. - t0
#     print("bad computed in @ ms, bad: |;,|".f.. ?.t_s.. * 1000 b..
#
#     all_cars _ ?.o.. .c..
#
#     percent _ 100 * b.. / ma. ? 1
#     r_ ?
#
#
# ___ find_car_by_id car_id b__.OI. __ C..
#     car _ ?.o.. id_c_i. .f..
#     ?.o.. .fi.. id_c_i. .f..
#     r_ ?
#
#
# ___ add_service_record car_id description price customer_rating
#     record _ ? d.._d.. p.._p.. c_r.._c_r..
#
#     res _ ?.o.. id_c_i. .u_o.. push__service_history_r..
#     __ ? !_ 1
#         r_ E..("No car with id @".f.. c_i.
#
#
# ___ add_owner owner_id car_id
#     res _ ?.o.. id_o_i. .u_o.. add_to_set__car_ids_c_i.
#     __ ? !_ 1
#         r_ E..("No owner with id @".f.. o_i.
