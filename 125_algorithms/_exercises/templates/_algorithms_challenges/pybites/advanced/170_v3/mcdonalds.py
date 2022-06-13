# _______ p.... __ pd
#
# data "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# # load the data in once, functions will use this module object
# df __.r.. ?
#
# __.o__.m__.c.. N..  # ignore warnings
#
#
# ___ get_food_most_calories df_?
#     """Return the food "Item" string with most calories"""
#     s ?.s.. by_'Calories' a.._F..
#     r.. s 'Item' .h.. 1.v..
#
#
# ___ get_bodybuilder_friendly_foods df_? excl_drinks_F..
#     """Calulate the Protein/Calories ratio of foods and return the
#        5 foods with the best ratio.
#
#        This function has a excl_drinks switch which, when turned on,
#        should exclude 'Coffee & Tea' and 'Beverages' from this top 5.
#
#        You will probably need to filter out foods with 0 calories to get the
#        right results.
#
#        Return a list of the top 5 foot Item stings."""
#     s ? ?.C.. !_ 0
#     __ ?
#         ? ? ~?.C...i.. 'Coffee & Tea', 'Beverages'
#     ? 'Ratio'  _ s.P.. / ?.C..
#     ? ?.s.. by_'Ratio' a.._F..
#     r.. ? 'Item' .h.. 5 .v..
