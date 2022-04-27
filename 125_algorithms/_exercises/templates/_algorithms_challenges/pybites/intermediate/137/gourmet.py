# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Pairs wines and cheeses by similarity of wine name and cheese name.
# """
#
# ____ c.. _______ C..
# _______ o..
#
# CHEESES
#     "Red Leicester",
#     "Tilsit",
#     "Caerphilly",
#     "Bel Paese",
#     "Red Windsor",
#     "Stilton",
#     "Emmental",
#     "Gruyère",
#     "Norwegian Jarlsberg",
#     "Liptauer",
#     "Lancashire",
#     "White Stilton",
#     "Danish Blue",
#     "Double Gloucester",
#     "Cheshire",
#     "Dorset Blue Vinney",
#     "Brie",
#     "Roquefort",
#     "Pont l'Evêque",
#     "Port Salut",
#     "Savoyard",
#     "Saint-Paulin",
#     "Carré de l'Est",
#     "Bresse-Bleu",
#     "Boursin",
#     "Camembert",
#     "Gouda",
#     "Edam",
#     "Caithness",
#     "Smoked Austrian",
#     "Japanese Sage Derby",
#     "Wensleydale",
#     "Greek Feta",
#     "Gorgonzola",
#     "Parmesan",
#     "Mozzarella",
#     "Pipo Crème",
#     "Danish Fynbo",
#     "Czech sheep's milk",
#     "Venezuelan Beaver Cheese",
#     "Cheddar",
#     "Ilchester",
#     "Limburger",
#
#
# RED_WINES
#     "Châteauneuf-du-Pape",  # 95% of production is red
#     "Syrah",
#     "Merlot",
#     "Cabernet sauvignon",
#     "Malbec",
#     "Pinot noir",
#     "Zinfandel",
#     "Sangiovese",
#     "Barbera",
#     "Barolo",
#     "Rioja",
#     "Garnacha",
#
#
# WHITE_WINES
#     "Chardonnay",
#     "Sauvignon blanc",
#     "Semillon",
#     "Moscato",
#     "Pinot grigio",
#     "Gewürztraminer",
#     "Riesling",
#
#
# SPARKLING_WINES
#     "Cava",
#     "Champagne",
#     "Crémant d’Alsace",
#     "Moscato d’Asti",
#     "Prosecco",
#     "Franciacorta",
#     "Lambrusco",
#
#
#
# ___ best_match_per_wine wine_type_"all"
#     """ wine cheese pair with the highest match score
#     returns a tuple which contains wine, cheese, score
#     """
#
#     __ ? __ "red"
#         wines ?
#     ____ ? __ "white"
#         ? ?
#     ____ ? __ "sparkling"
#         ? ?
#     ____ ? __ "all"
#         ? ? + ? + ?
#     ____
#         r.. V...
#
#     max_wine ""
#     max_cheese ""
#     max_cheese_score 0
#
#     ___ wine __ ?
#         ___ cheese __ ?
#
#             match_score s.. C.. ?.l.. & C.. ?.l..
#             .v..
#             similarity_score ? / (1 + pow l.. ? - l.. c.. 2
#
#             __ s.. > m..
#                 m.. ?
#                 m.. ?
#                 m.. ?
#
#     r.. ? ? ?
#
#
# ___ match_wine_5cheeses
#     """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
#     where each tuple contains: wine, list of 5 best matching cheeses.
#     List of cheeses is sorted by score descending then alphabetically ascending.
#     e.g: [
#     ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
#     ...
#     ...
#     ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
#     ]
#     """
#     all_wines ? + ? + ?
#     wine_match_scoring    # dict
#     ___ wine __ ?
#         wine_match_scoring ?    # list
#         ___ cheese __ ?
#             match_score s.. C.. ?.l.. & C.. ?.l..
#             .v..
#             similarity_score ? / (1 + pow(l.. ? - l.. c.. 2
#             w.. ?.a.. c.. ?
#
#     best_5matches    # list
#     ___ wine cheeses_scored __ w__.i..
#         cheese s.. c.. k.._o__.i.. 1 r.._T.. |10
#         cheese s.. ? k.._l.... x -? 1 ? 0 |5
#         ?.a.. w.. name ___ ? s.. __ c..
#
#     r.. s.. ?
#
#
# #if __name__ == "__main__":
#     #print(best_match_per_wine("white"))
#     #print(match_wine_5cheeses())