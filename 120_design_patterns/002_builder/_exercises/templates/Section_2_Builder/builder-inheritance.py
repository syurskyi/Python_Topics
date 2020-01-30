# c_ Person:
#     ___ -  ____
#         ____.name _ N..
#         ____.position _ N..
#         ____.date_of_birth _ N..
#
#     ___ -s ____
#         r_ _* ____.n..| born on ____.d..| works as a ____.p...|
#
#     ??
#     ___ new
#         r_ P..
#
# c_ PersonBuilder:
#     ___ - ____
#         ____.person _ P..
#
#     ___ build ____
#         r_ ____.?
#
#
# c_ PersonInfoBuilder PB..
#     ___ called ____ name
#         ____.p__.? _ ?
#         r_ ____
#
#
# c_ PersonJobBuilder PIB..
#     ___ works_as_a ____ position
#         ____.p__.? _ ?
#         r_ ____
#
#
# c_ PersonBirthDateBuilder PJB..
#     ___ born ____ date_of_birth
#         ____.p__.? _ ?
#         r_ ____
#
#
# __ _______ __ ______
#     pb _ PBDB
#     me _ ?\
#         .called('Dmitri')\
#         .works_as_a('quant')\
#         .born('1/1/1980')\
#         .build()  # this does NOT work in C#/C++/Java/...
#     print ?
