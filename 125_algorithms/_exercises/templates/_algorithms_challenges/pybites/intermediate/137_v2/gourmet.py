# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Pairs wines and cheeses by similarity of wine name and cheese name.
# """
#
# ____ c.. _______ C..,d..
# _______ o..
# _______ i..
#
#
#
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
# mapping red ? white ? sparkling ? all ?+?+?
#
#
#
# ___ _calculate_similarity wine cheese
#     wine_length l.. ?
#     cheese_length l.. ?
#
#     counts_wine C.. ?.l..
#     counts_cheese C.. ?.l..
#
#     numerator s.. ? & ? .v..
#
#     denominator 1 + w.. - c.. **2
#
#     r.. ?/?
#
# ___ best_match_per_wine wine_type_"all"
#     """ wine cheese pair with the highest match score
#     returns a tuple which contains wine, cheese, score
#     """
#
#     __ ? n.. __ m..
#         r.. V... "Invalid Wie TYpe"
#
#
#     values m.. ?
#
#
#
#     maximum m.. i...p.. ? C.. k.._l.... x _c.. *x
#
#
#     r.. $? _c.. $?
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
#     all_wines mapping 'all'
#     wine_cheeses d.. l..
#
#     results    # list
#
#     ___ wine __ a..
#         sorted_list s.. C.. k.._l.... x (-(_? ? x ?
#         ?.a.. w.. ? |5
#
#
#     r.. s.. ? k.._l.... x ? 0

