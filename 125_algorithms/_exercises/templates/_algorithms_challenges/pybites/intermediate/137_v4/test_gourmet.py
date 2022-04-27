# _______ p__
# ____ ? _______ ? ?
#
#
# ___ test_best_match_per_wine_all
#     ... ?  2  __ 13.0
#
#
# cases_best_by_wine
#     ("white", "Sauvignon blanc", "Smoked Austrian", 8.0),
#     ("red", "Cabernet sauvignon", "Dorset Blue Vinney", 13.0),
#     ("sparkling", "Moscato d’Asti", "Carré de l'Est", 6.0),
#
#
#
# ?p__.m__.p. "case" ?
# ___ test_best_match_per_wine_type case
#     wine_type, $result ?
#     ... ? ? __ t.. ?
#
#
# ___ test_invalid_wine_type
#     w__ p__.r.. V...
#         ? "cocacola"
#
#
# ___ test_all_wines_included
#     ... l.. ? __ 26
#
#
# mw5c ?
# cases
#     (0, "Barbera", ["Cheddar", "Gruyère", "Boursin", "Parmesan", "Liptauer"]),
#     (1, "Barolo", ["Boursin", "Cheddar", "Gouda", "Stilton", "Tilsit"]),
#     (
#         2,
#         "Cabernet sauvignon",
#         [
#             "Dorset Blue Vinney",
#             "Norwegian Jarlsberg",
#             "Czech sheep's milk",
#             "Double Gloucester",
#             "Japanese Sage Derby",
#         ],
#     ),
#     (3, "Cava", ["Edam", "Gouda", "Cheddar", "Savoyard", "Parmesan"]),
#     (
#         4,
#         "Champagne",
#         ["Caithness", "Camembert", "Bel Paese", "Ilchester", "Lancashire"],
#     ),
#     (-2, "Syrah", ["Gouda", "Cheddar", "Brie", "Edam", "Tilsit"]),
#     (
#         -1,
#         "Zinfandel",
#         ["Caithness", "Bel Paese", "Ilchester", "Limburger", "Lancashire"],
#     ),
#
#
#
# ?p__.m__.p. "case" ?
# ___ test_match_wine_5cheeses case
#     """ test of presence of first 2 cheeses only
#     because if score is same for more pairs, order of pairs cannot be assumed
#     """
#     idx wine cheeses ?
#     ... m.. i.. 0  __ w..
#     ... m.. i.. 1 __ c..