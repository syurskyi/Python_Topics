#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

____ c.. _______ C..
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


___ best_match_per_wine(wine_type="all"
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """

    __ wine_type __ "red":
        wines = RED_WINES
    ____ wine_type __ "white":
        wines = WHITE_WINES
    ____ wine_type __ "sparkling":
        wines = SPARKLING_WINES
    ____ wine_type __ "all":
        wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    ____:
        r.. V...

    max_wine = ""
    max_cheese = ""
    max_cheese_score = 0

    ___ wine __ wines:
        ___ cheese __ CHEESES:

            match_score = s..((C..(wine.l.. & C..(cheese.l..
            )).values
            similarity_score = match_score / (1 + pow(l..(wine) - l..(cheese), 2))

            __ similarity_score > max_cheese_score:
                max_wine = wine
                max_cheese = cheese
                max_cheese_score = match_score

    r.. (max_wine, max_cheese, max_cheese_score)


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
    all_wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    wine_match_scoring    # dict
    ___ wine __ all_wines:
        wine_match_scoring[wine]    # list
        ___ cheese __ CHEESES:
            match_score = s..((C..(wine.l.. & C..(cheese.l..
            )).values
            similarity_score = match_score / (1 + pow(l..(wine) - l..(cheese), 2))
            wine_match_scoring[wine].a..((cheese, similarity_score))

    best_5matches    # list
    ___ wine, cheeses_scored __ wine_match_scoring.i..:
        cheese = s..(cheeses_scored, key=operator.itemgetter(1), r.._T..[:10]
        cheese = s..(cheese, key=l.... x: (-x[1], x[0]))[:5]
        best_5matches.a..((wine, [name ___ name, score __ cheese]))

    r.. s..(best_5matches)

    
#if __name__ == "__main__":
    #print(best_match_per_wine("white"))
    #print(match_wine_5cheeses())