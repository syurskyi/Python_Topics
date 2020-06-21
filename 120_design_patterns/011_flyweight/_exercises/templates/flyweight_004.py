# """Flyweight pattern
#
# Separate an object into two parts:
#     1. an intrinsic, immutable part that can be shared across all instances
#        (state-independent)
#     2. an extrinsic, mutable part that is specific ___ each instance and cannot
#        be shared (state-dependent)
# """
# ______ ra..
# from a.. ______ A..
#
#
# c_ Model3D o..
#     p..
#
#
# c_ OrkModel M..
#     p..
#
#
# c_ AlienModel M..
#     p..
#
#
# c_ Intelligence o..
#     p..
#
#
# c_ HighIntelligence I..
#     p..
#
#
# c_ Enemy o..
#
#     immutables _ M.. I..
#
#     ___ -  position_0, 0
#         ?  ?
#
#
# c_ Ork E..
#
#     immutables _ O.. I..
#
#
# c_ Alien E..
#
#     immutables _ A.. I..
#
#
# c_ Queen A..
#
#     immutables _ A.. H..
#
#
# c_ Factory A..
#
#     pool _ di..
#
#     ??
#     ___ make_enemy ___ enemy_type position
#         this_module _ -i |-n
#         enemy_class _ g.. t_m.. e_t..
#
#         # add immutable objects to the pool if they are not already there
#         ___ imm __ e_c__.immutables:
#             immutable_name _ ?. -n
#             obj _ ___.p___.ge. i_n.. N..
#             __ o.. __ N..
#                 obj _ obj___. -n im.
#                 ___.po..|i_n.. _ ?
#                 print("NEW IMMUTABLE in the pool: @".f... i_n..
#
#         r_ e_c__ p_p..
#
# __ _______ __ ______
#     ork_model_identities _ li..
#     alien_model_identities _ li..
#     intelligence_identities _ li..
#     high_intelligence_identities _ li..
#
#     ___ i __ ra.. 10
#         x, y _ ra__.r_i_ 0, 100, ra__.r_i_ 0, 100
#         enemy _ F___.m_e.. "Ork", p... _ x, y
#         o____.ap.. i. ?.i.. 0
#         i____.ap.. i. e___.im.. 1
#         print e___
#
#     print("")
#     ___ i __ ra.. 10
#         x, y _  ra__.r_i_ 0, 100 , ra__.r_i_ 0, 100
#         enemy _ F___.m_e.. "Alien", p... _ x, y
#         a____.ap.. i. e___.im.. 0
#         i____.ap.. i. e___.im.. 1
#         print e___
#
#     print("")
#     ___ i __ ra.. 2
#         x, y _ ra__.r_i_ 0, 100 , ra__.r_i_ 0, 100
#         enemy _ F___.m_e.. "Queen", p.... _ x, y
#         a___.ap.. i. e___.im.. 0
#         h___.ap.. i. e___.im.. 1
#         print e___
#
#     print("\nImmutable parts of the same type share the same identity")
#     print("ork_model_identities:\n@".f... se. o..
#     print("alien_model_identities:\n@".f... se. a..
#     print("intelligence_identities:\n@".f... se. i..
#     print("high_intelligence_identities:\n@".f... se. h..
#     as... le. se. o.. __ 1
#     as... le. se. a.. __ 1
#     as... le. se. i.. __ 1
#     as... le. se. h.. __ 1
