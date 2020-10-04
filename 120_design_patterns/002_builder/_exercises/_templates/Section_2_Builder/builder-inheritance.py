# c_ Person
#     ___ -
#         name _ N..
#         position _ N..
#         date_of_birth _ N..
#
#     ___ -s
#         r_ _* n..| born on d..| works as a p...|
#
#     ??
#     ___ new
#         r_ P..
#
# c_ PersonBuilder
#     ___ -
#         person _ P..
#
#     ___ build
#         r_ ?
#
#
# c_ PersonInfoBuilder PB..
#     ___ called ____ name
#         p__.? _ ?
#         r_
#
#
# c_ PersonJobBuilder PIB..
#     ___ works_as_a ____ position
#         p__.? _ ?
#         r_
#
#
# c_ PersonBirthDateBuilder PJB..
#     ___ born ____ date_of_birth
#         p__.? _ ?
#         r_
#
#
# __ _______ __ ______
#     pb _ PBDB
#     me _ ?\
#         .c..('Dmitri')\
#         .w..('quant')\
#         .b..('1/1/1980')\
#         .b..  # this does NOT work in C#/C++/Java/...
#     print ?
