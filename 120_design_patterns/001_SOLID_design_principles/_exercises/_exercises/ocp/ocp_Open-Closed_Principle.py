# ____ en.. ________ E..
#
#
# c_ Color E..
#     RED _ 1
#     GREEN _ 2
#     BLUE _ 3
#
#
# c_ Size(Enum):
#     SMALL _ 1
#     MEDIUM _ 2
#     LARGE _ 3
#
#
# c_ Product
#     ___ - name color size
#         ?  ?
#         ?  ?
#         ?  ?
#
#
# c_ ProductFilter
#     ___ filter_by_color products color
#         ___ p __ p...
#             __ ?.c.. __ c..
#                 y.. ?
#
#     ___ filter_by_size(self, products, size):
#         ___ p __ products:
#             __ ?.s.. __ s.. y.. ?
#
#     ___ filter_by_size_and_color products size color
#         ___ p __ p..
#             __ ?.c.. __ c.. an. ?.s.. __ s..
#                 y.. ?
#
#     # state space explosion
#     # 3 criteria
#     # c s w cs sw cw csw = 7 methods
#
#     # OCP = open for extension, closed for modification
#
#
# c_ Specification
#     ___ is_satisfied item
#         p..
#
#     # and operator makes life easier
#     ___ __and__  other
#         r_ A...  o..
#
#
# c_ Filter
#     ___ filter  items spec
#         p..
#
#
# c_ ColorSpecification S...
#     ___ - color
#         ?  ?
#
#     ___ is_satisfied item
#         r_ ?.c.. __ ?c..
#
#
# c_ SizeSpecification S..
#     ___ - size
#         ?  ?
#
#     ___ is_satisfied item
#         r_ ?.s.. __ ?s..
#
#
# c_ AndSpecification S..
#     ___ - spec1 spec2
#         _2 _ ?
#         _1 _ ?
#
#     ___ is_satisfied item
#         r_ ?_1.i.. ? an. \
#                ?_2.i.. ?
#
#
# c_ BetterFilter F..
#     ___ filter items spec
#         ___ item __ i..
#             __ s__.is... ?
#                 y.. ?
#
#
# apple _ P.. 'Apple' C__.G... S__.S..
# tree _ P.. 'Tree', C__.G.. S__.L..
# house _ P.. 'House', C__.B.. S__.L..
#
# products _ ?  ?  ?
#
# pf _ P..F..
# print('Green products (old):')
# ___ p __ p_.f.. pr... C__.G..
#     print(_* - |?.n.. i. green')
#
# # ^ BEFORE
#
# # v AFTER
# bf _ B..
#
# print('Green products (new):')
# green _ C.. C__.G..
# ___ p __ b_.f.. p... gr..
#     print(_* - |?.n.. is green')
#
# print('Large products:')
# large _ S.. S__.L..
# ___ p __ b_.f.. p.. l..
#     print(_* - |?.n... is large')
#
# print('Large blue items:')
# # large_blue _ AndSpecification(large, ColorSpecification(Color.BLUE))
# large_blue _ l.. an. C..S.. C__.B...
# ___ p __ b_.f.. p.. l_b..
#     print(_* - |?.n.. is large and blue')