# ____ Previous.? _______ ? ? ?
#
# ASSERT_ERROR ("One or more expected foods not in "
#                 "get_bodybuilder_friendly_foods's return value")
#
#
# ___ test_get_food_most_calories
#     a.. ?
#     e.. 'Chicken McNuggets (40 piece)'
#     ... a.. __ e..
#
#
# ___ test_get_food_most_calories_smaller_population
#     """Extra test to prevent hardcoding the return value"""
#     df_breakfast ? ? 'Category'  __ 'Breakfast'
#
#     a.. ? ?
#     e.. 'Big Breakfast with Hotcakes (Large Biscuit)'
#     ... a.. __ e..
#
#
# ___ test_get_bodybuilder_friendly_foods
#     actual_with_drinks l.. ?
#     e.. =  'Premium Bacon Ranch Salad with Grilled Chicken',
#                 'Nonfat Latte (Small)',
#                 'Nonfat Latte (Large)',
#                 'Premium Southwest Salad with Grilled Chicken',
#                 'Nonfat Latte (Medium)'
#     ... a.. food __ ? ___ ? __ e.. A..
#
#
# ___ test_get_bodybuilder_friendly_foods_excluding_liquid_food
#     actual_wo_drinks l.. ? e.._T..
#     e.. =  'Premium Bacon Ranch Salad with Grilled Chicken',
#                 'Premium Southwest Salad with Grilled Chicken',
#                 'Premium Grilled Chicken Classic Sandwich',
#                 'Premium Grilled Chicken Ranch BLT Sandwich',
#                 'Premium Grilled Chicken Club Sandwich'
#     ... a.. food __ ? ___ ? __ e.. A..