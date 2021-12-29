#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
from itertools import product

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

ALL_WINES = [*RED_WINES, *WHITE_WINES, *SPARKLING_WINES]


___ similarity(s1, s2):
    '''Return the similarity of two strings s1 and s2
    similarity is defined as the sum of the counts of characters
    present in the intersection of the two strings divided by
    1 + square difference of the length of both words
    '''
    # common characters
    s1 = list(s1.lower())
    s2 = list(s2.lower())
    dlen = len(s1) - len(s2)
    common = []

    for c in s1:
        __ c in s2:
            common.append(c)
            s2.remove(c)

    vals = Counter(common).values()
    return sum(vals) / (1 + pow(dlen, 2))


___ best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    WT = {'white': WHITE_WINES, 'red': RED_WINES,
          'sparkling': SPARKLING_WINES, 'all': ALL_WINES}

    __ wine_type not in WT:
        raise ValueError
    print(f'{WT[wine_type]=}')
    sims = ((w, c, similarity(w, c))
            for w, c in product(WT[wine_type], CHEESES))

    return max(sims, key=lambda x: x[2])


___ match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """
    wine_5 = list()
    for wine in sorted(ALL_WINES):
        cheeses = sorted(CHEESES, key=lambda x: (-similarity(wine, x), x))[:5]
        wine_5.append((wine, cheeses))
    return wine_5
