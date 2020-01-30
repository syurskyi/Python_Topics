# c_ Person:
#     ___ -
#         print('Creating an instance of Person')
#         # address
#         ____.street_address = N...
#         ____.postcode = N...
#         ____.city = N...
#         # employment info
#         ____.company_name = N...
#         ____.position = N...
#         ____.annual_income = N...
# 
#     ___ -s __ st..
#         r_ _*Address: ____.s..| ____.p..| ____.c.. \n' +\
#             _*Employed at ____.c..| as a ____.p.. earning ____.a..
# 
# 
# c_ PersonBuilder:  # facade
#     ___ - ____ person_N...
#         __ ? __ N...
#             ____.? = P..
#         ____
#             ____.?  ?
# 
#     ??
#     ___ lives ____
#         r_ P.. ____.p..
# 
#     ??
#     ___ works ____
#         r_ P.. ____.p...
# 
#     ___ build ____
#         r_ ____.p..
# 
# 
# c_ PersonJobBuilder PB..
#     ___ - ____ person
#         s__. - p..
# 
#     ___ at ____ company_name
#         ____.?.c.. _ c..
#         r_ ____
# 
#     ___ as_a ____ position
#         ____.p__.? _ ?
#         r_ ____
# 
#     ___ earning ____ annual_income
#         ____.p__.? _ ?
#         r_ ____
# 
# 
# c_ PersonAddressBuilder PB..
#     ___  - ____ person
#         s__. - ?
# 
#     ___ at ____ street_address)
#         ____.p__.? _ ?
#         r_ ____
# 
#     ___ with_postcode ____ postcode
#         ____.p__.? _ ?
#         r_ ____
# 
#     ___ in_city ____ city
#         ____.p__.? _ ?
#         r_ ____
# 
# 
# __ ______ __ _____
#     pb = PB..
#     p = ?\
#         .lives\
#             .at('123 London Road')\
#             .in_city('London')\
#             .with_postcode('SW12BC')\
#         .works\
#             .at('Fabrikam')\
#             .as_a('Engineer')\
#             .earning(123000)\
#         .b..
#     print ?
#     person2 = PB__.b..
#     print ?
