# ____ a.. ______ a..
# ____ e.. ______ E..
#
#
# c_ Relationship E..
#     PARENT = 0
#     CHILD = 1
#     SIBLING = 2
#
#
# c_ Person
#     ___ - name
#         ??  ?
#
#
# c_ RelationshipBrowser
#     ??
#     ___ find_all_children_of name p..
#
#
# c_ Relationships(RB..  # low-level
#     relations _     # list
#
#     ___ add_parent_and_child  parent child
#         ?r___.ap.. p.. R__.P... c..
#         ?r___.ap.. c.. R__.P... p..
#
#     ___ find_all_children_of  name
#         ___ r __ ?r..
#             __ ? 0 .? __ ? an. ? 1 __ R__.P..
#                 y.. ? 2 .n..
#
#
# c_ Research
#     # dependency on a low-level module directly
#     # bad because strongly dependent on e.g. storage type
#
#     # ___ __init__(self, relationships):
#     #     # high-level: find all of john's children
#     #     relations = relationships.relations
#     #     for r in relations:
#     #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
#     #             print(f'John has a child called {r[2].name}.')
#
#     ___ - browser
#         ___ p __ ?.find_all_children_of "John"
#             print _*John has a child called ?')
#
#
# parent = P.. ('John')
# child1 = P.. ('Chris')
# child2 = P.. ('Matt')
#
# # low-level module
# relationships = R..
# ?.a.. p.. c_1
# ?.a.. p.. c_2
#
# R.. ?
