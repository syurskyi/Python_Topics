# c_ Creature
#     ___ - name, attack, defense
#         d.. _ d..
#         a.. _ a..
#         n.. _ n..
#
#     ___ -s
#         r_ _*|n.. ||a../|d..
#
#
# c_ CreatureModifier
#     ___ - creature
#         ?  ?
#         next_modifier _ N..
#
#     ___ add_modifier modifier
#         __ next_modifier
#             ?.a.. ?
#         ____
#             n.. _ ?
#
#     ___ handle
#         __ n..
#             n___.h..
#
#
# c_ NoBonusesModifier C..
#     ___ handle
#         print('No bonuses for you!')
#
#
# c_ DoubleAttackModifier C..
#     ___ handle
#         print(_*Doubling |c___.n..''s attack')
#         c__.a.. *_ 2
#         s___ .h..
#
#
# c_ IncreaseDefenseModifier C..
#     ___ handle
#         __ c___.a.. <_ 2:
#             print(_*Increasing |c__.n..''s defense')
#             c____.d.. +_ 1
#         s___ .h..
#
#
# __ _______ __ ______
#     goblin _ C.. 'Goblin', 1, 1
#     print ?
#
#     root _ C.. ?
#
#     ?.a.. N.. ?
#
#     ?.a.. D.. ?
#     ?.a.. D.. ?
#
#     # no effect
#     ?.a.. I.. ?
#
#     ?.h..  # apply modifiers
#     print ?
