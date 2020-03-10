# ____ w_r_ ______ WKD..
# 
# The weakref module allows the Python programmer to create weak references to objects.
# A weak reference to an object is not enough to keep the object alive: when the only remaining references to 
# a referent are weak references, garbage collection is free to destroy the referent and reuse its memory for something 
# else. A primary use for weak references is to implement caches or mappings holding large objects, where it's desired 
# that a large object not be kept alive solely because it appears in a cache or mapping.
# 
# For example, if you have a number of large binary image objects, you may wish to associate a name with each. 
# If you used a Python dictionary to map names to images, or images to names, the image objects would remain alive just
# because they appeared as values or keys in the dictionaries. The WeakKeyDictionary and WeakValueDictionary classes
# supplied by the weakref module are an alternative, using weak references to construct mappings that don't keep
# objects alive solely because they appear in the mapping objects. If, for example, an image object is a value in 
# a WeakValueDictionary, then when the last remaining references to that image object are the weak references held 
# by weak mappings, garbage collection can reclaim the object, and its corresponding entries in weak mappings 
# are simply deleted.
#
#
# c_ Positive
#
#     ___ -
#         _instance_data _ WKD..
#
#     ___ -g instance owner
#         __ i____ __ N..
#             r_ ?
#         r_ _i..|i____
#
#     ___ -s instance value
#         __ v___ <_ 0
#             r_ V...("Value @ __ not positive".f.. ?
#         _i..|i___ _ ?
#
#     ___ -d instance
#         r_ A... "Cannot delete attribute"
#
#
# c_ Planet
#
#     ___ -
#                  name
#                  radius_metres
#                  mass_kilograms
#                  orbital_period_seconds
#                  surface_temperature_kelvin
#         ?  ?
#         ?  ?
#         ?  ?
#         ?  ?
#         ?  ?
#
#     ??
#     ___ name
#         r_ _?
#
#     ??.?
#     ___ name value
#         __ no. ?
#             r_ V..("Cannot set empty Planet.name")
#         _n.. _ ?
#
#     radius_metres _ P..
#     mass_kilograms _ P..
#     orbital_period_seconds _ P..
#     surface_temperature_kelvin _ P..
#
#
# ___ main
#
#     mercury _ P..(*?
#                      radius_metres_2439.7e3,
#                      mass_kilograms_3.3022e23,
#                      orbital_period_seconds_7.60052e6,
#                      surface_temperature_kelvin_340)
#
#     venus _ P..(*?
#                    radius_metres_6051.8e3,
#                    mass_kilograms_4.8676e24,
#                    orbital_period_seconds_1.94142e7,
#                    surface_temperature_kelvin_737)
#
#     earth _ P..(*?
#                    radius_metres_6371.0e3,
#                    mass_kilograms_5.972e24,
#                    orbital_period_seconds_3.15581e7,
#                    surface_temperature_kelvin_288)
#
#     mars _ P..(*?
#                   radius_metres_3389.5e3,
#                   mass_kilograms_6.4185e23,
#                   orbital_period_seconds_5.93543e7,
#                   surface_temperature_kelvin_210)
#
#     r_ mercury, venus, earth, mars
#
# __ _______ __ ______ __
#   ?
