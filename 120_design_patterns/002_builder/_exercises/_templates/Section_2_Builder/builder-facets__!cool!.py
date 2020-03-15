# c_ Person
#     ___ -
#         print('Creating an instance of Person')
#         # address
#         street_address _ N...
#         postcode _ N...
#         city _ N...
#         # employment info
#         company_name _ N...
#         position _ N...
#         annual_income _ N...
# 
#     ___ -s __ st..
#         r_ _*Address: s..| p..| c.. \n' +\
#             _*Employed at c..| as a p.. earning a..
# 
# 
# c_ PersonBuilder  # facade
#     ___ -  person_N...
#         __ ? __ N...
#             ? _ P..
#         ____
#             ?  ?
# 
#     ??
#     ___ lives
#         r_ P.. p..
# 
#     ??
#     ___ works
#         r_ P.. p...
# 
#     ___ build
#         r_ p..
# 
# 
# c_ PersonJobBuilder PB..
#     ___ -  person
#         s__. - p..
# 
#     ___ at  company_name
#         ?.c.. _ c..
#         r_
# 
#     ___ as_a  position
#         p__.? _ ?
#         r_
# 
#     ___ earning  annual_income
#         p__.? _ ?
#         r_
# 
# 
# c_ PersonAddressBuilder PB..
#     ___  -  person
#         s__. - ?
# 
#     ___ at  street_address)
#         p__.? _ ?
#         r_
# 
#     ___ with_postcode  postcode
#         p__.? _ ?
#         r_
# 
#     ___ in_city city
#         p__.? _ ?
#         r_
# 
# 
# __ ______ __ _____
#     pb _ PB..
#     p _ ?\
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
#     person2 _ PB__.b..
#     print ?
