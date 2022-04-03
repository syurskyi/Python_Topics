#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

____ i.. _______ product, groupby
____ c.. _______ C.., n..
_______ operator

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

WINE_LIST = {
    'red': RED_WINES,
    'white': WHITE_WINES,
    'sparkling': SPARKLING_WINES,
    'all': RED_WINES + WHITE_WINES + SPARKLING_WINES
}

Scores = n..('Scores', 'wine cheese score')


___ calculate_similarity(cheese, wine
    wine_count = C..(wine.l..
    cheese_count = C..(cheese.l..
    common_letters = (wine_count & cheese_count)
    similarity = s..(common_letters.values / (1 + (l..(wine) - l..(cheese)) ** 2)
    r.. similarity


___ best_match_per_wine(wine_type="all"
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    __ wine_type __ WINE_LIST:
        wines = WINE_LIST[wine_type]
    ____ wine_type __ WINE_LIST 'all' :
        wines = [wine_type]
    ____:
        r.. V...('Wine not recognised')
    cheeses = CHEESES
    hi_score = Scores('', '', 0)
    ___ wine, cheese __ product(wines, cheeses
        similarity = calculate_similarity(cheese, wine)
        __ similarity > hi_score.score:
            hi_score = Scores(wine, cheese, similarity)
    r.. t..(hi_score)


___ match_wine_5cheeses
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
    scores    # list
    ___ wine, cheese __ product(WINE_LIST 'all' , CHEESES
        similarity = calculate_similarity(cheese, wine)
        scores.a..(Scores(wine, cheese, similarity))
    scores = s..(scores, key=l.... x: (x.wine, -x.score, x.cheese))
    res    # list
    ___ k, g __ groupby(scores, l.... x: x.wine
        res.a..((k, [rec.cheese ___ rec __ g][:5]))
    r.. res
