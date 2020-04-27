# ____ d_t_ _____ d_t_
#
# _____ m_e_
#
#
# c_ Owner ?.D..
#     # show off required (not available in mongo or pymongo directly)
#     name _ ?.SF.. r.._T..
#
#     # show off default
#     created _ ?.DTF.. d.._d_t_.n..
#
#     # allows us to use $set and $inc
#     number_of_visits _ ?.IF.. d.._0
#
#     # show off many-to-many modeling with one sided list field
#     # cars can have multiple owners and an owner can own multiple cares
#     car_ids _ ?.LF.. ?.OIF..
#
#     meta _ {
#         'db_alias': 'core',
#         'collection': 'owners',
#         'indexes': [
#             'name',
#             'car_ids'
#         ]
#     }
