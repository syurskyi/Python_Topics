# _____ u..
# _____ m_e_
#
# ____ n__.e.. _____ E..
# ____ n__.s_r.. _____ SR..
#
#
# c_ Car ?.D..
#     model _ ?.SF.. r.._T..
#     make _ ?.SF.. r.._T..
#     year _ ?.IF.. r.._T..
#     mileage _ ?.IF.. d.._0
#     vi_number _ ?.SF.. d.._l____ st. ?._4.r.. "-", ''
#
#     engine _ ?.EDF.. E.. r.._T..
#     service_history _ ?.EDLF.. SR..
#
#     # no need to reference owners here, that is entirely contained in owner class
#
#     meta _ {
#         'db_alias': 'core',
#         'collection': 'cars',
#         'indexes': [
#             'mileage',
#             'year',
#             'service_history.price',
#             'service_history.customer_rating',
#             'service_history.description',
#             {'fields': ['service_history.price', 'service_history.description']},
#             {'fields': ['service_history.price', 'service_history.customer_rating']},
#         ]
#     }
