# _______ __
#
# ____ ? _______ ?
#
#
# ___ test_text_to_one_col
#     text """My house is small but cosy."""
#     e..
#         r"^My house is small",
#         r"^but cosy."
#
#     output ? ? .s..  \n
#     ___ line m.. __ z.. ?  e..
#         ... __.s.. m.. ?
#
#
# ___ test_text_to_two_cols
#     text """My house is small but cosy.
#
#     It has a white kitchen and an empty fridge."""
#     e..
#         r"^My house is small\s+It has a white",
#         r"^but cosy\.\s+kitchen and an empty",
#         r".*fridge."
#
#     output ? ?.s..  \n
#     ___ line m.. __ z.. ?  e..
#         ... __.s.. m.. ?
#
#
# ___ test_text_to_three_cols
#     text """My house is small but cosy.
#
#     It has a white kitchen and an empty fridge.
#
#     I have a very comfortable couch, people love to sit on it."""
#     e..
#         r"^My house is small\s+It has a white\s+I have a very",
#         r"^but cosy\.\s+kitchen and an empty\s+comfortable couch,",
#         r".*fridge\.\s+people love to sit",
#         r".*on it."
#
#     output ? ?.s..  \n
#     ___ line m.. __ z.. ?  e..
#         ... __.s.. m.. ?
#
#
# ___ test_text_to_four_cols
#     text """My house is small but cosy.
#
#     It has a white kitchen and an empty fridge.
#
#     I have a very comfortable couch, people love to sit on it.
#
#     My mornings are filled with coffee and reading, if only I had a garden"""
#
#     e..
#         r"^My house is small\s+It has a white\s+I have a very\s+My mornings are",
#         r"^but cosy\.\s+kitchen and an empty\s+comfortable couch,\s+filled with coffee",
#         r".*fridge\.\s+people love to sit\s+and reading, if only",
#         r".*on it\.\s+I had a garden",
#
#     output ? ?.s..  \n
#     ___ line m.. __ z.. ?  e..
#         ... __.s.. m.. ?