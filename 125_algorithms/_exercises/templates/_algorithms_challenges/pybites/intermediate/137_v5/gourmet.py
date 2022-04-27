# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Pairs wines and cheeses by similarity of wine name and cheese name.
# """
#
# ____ i.. _______ p.. g..
# ____ c.. _______ C.. n..
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
# WINE_LIST
#     red  ?
#     white  ?
#     sparkling ?
#     all  ? + ? + ?
#
#
# Scores n.. 'Scores', 'wine cheese score'
#
#
# ___ calculate_similarity cheese wine
#     wine_count C.. ?.l..
#     cheese_count C.. ?.l..
#     common_letters ? & ?
#     similarity s.. ?.v.. / (1 + (l.. w.. - l.. c.. ** 2
#     r.. ?
#
#
# ___ best_match_per_wine wine_type_"all"
#     """ wine cheese pair with the highest match score
#     returns a tuple which contains wine, cheese, score
#     """
#     __ wine_type __ ?
#         wines ? ?
#     ____ ? __ ? 'all'
#         w.. ?
#     ____
#         r.. V... 'Wine not recognised'
#     cheeses ?
#     hi_score ? '', '', 0
#     ___ wine cheese __ p.. ? ?
#         similarity ? ? ?
#         __ ? > h__.s..
#             h.. ? ? ? ?
#     r.. t.. ?
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
#     scores    # list
#     ___ wine cheese __ p.. W.. 'all'  C..
#         similarity ? ? ?
#         ?.a.. ? ? ? ?
#     scores s.. ? k.._l.... x ?.w.. -?.s.. ?.c..
#     res    # list
#     ___ k g __ g.. s.. l.... x ?.w..
#         ?.a.. k ?.c.. ___ ? __ g |5
#     r.. ?
