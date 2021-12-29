#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator

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


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """

    if wine_type == "red":
        wines = RED_WINES
    elif wine_type == "white":
        wines = WHITE_WINES
    elif wine_type == "sparkling":
        wines = SPARKLING_WINES
    elif wine_type == "all":
        wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    else:
        raise ValueError

    max_wine = ""
    max_cheese = ""
    max_cheese_score = 0

    for wine in wines:
        for cheese in CHEESES:

            match_score = sum((Counter(wine.lower()) & Counter(cheese.lower()
            )).values())
            similarity_score = match_score / (1 + pow(len(wine) - len(cheese), 2))

            if similarity_score > max_cheese_score:
                max_wine = wine
                max_cheese = cheese
                max_cheese_score = match_score

    return (max_wine, max_cheese, max_cheese_score)


def match_wine_5cheeses():
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
    wine_match_scoring = {}
    for wine in all_wines:
        wine_match_scoring[wine] = []
        for cheese in CHEESES:
            match_score = sum((Counter(wine.lower()) & Counter(cheese.lower()
            )).values())
            similarity_score = match_score / (1 + pow(len(wine) - len(cheese), 2))
            wine_match_scoring[wine].append((cheese, similarity_score))

    best_5matches = []
    for wine, cheeses_scored in wine_match_scoring.items():
        cheese = sorted(cheeses_scored, key=operator.itemgetter(1), reverse=True)[:10]
        cheese = sorted(cheese, key=lambda x: (-x[1], x[0]))[:5]
        best_5matches.append((wine, [name for name, score in cheese]))

    return sorted(best_5matches)

    
#if __name__ == "__main__":
    #print(best_match_per_wine("white"))
    #print(match_wine_5cheeses())