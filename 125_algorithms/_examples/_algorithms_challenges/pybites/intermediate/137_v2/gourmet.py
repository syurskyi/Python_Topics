#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter,defaultdict
import operator
import itertools




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

mapping = {'red': RED_WINES,'white': WHITE_WINES,'sparkling': SPARKLING_WINES,'all': RED_WINES+WHITE_WINES+SPARKLING_WINES}



def _calculate_similarity(wine,cheese):
    wine_length = len(wine)
    cheese_length = len(cheese)
    
    counts_wine = Counter(wine.lower())
    counts_cheese = Counter(cheese.lower())

    numerator = sum((counts_wine & counts_cheese).values())

    denominator = 1 + (wine_length - cheese_length)**2

    return numerator/denominator

def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """

    if wine_type not in mapping:
        raise ValueError("Invalid Wie TYpe")


    values = mapping[wine_type]

    

    maximum = max(itertools.product(values,CHEESES),key=lambda x: _calculate_similarity(*x))


    return (*maximum,_calculate_similarity(*maximum))











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
    all_wines = mapping['all']
    wine_cheeses = defaultdict(list)
    
    results = []

    for wine in all_wines:
        sorted_list = sorted(CHEESES,key=lambda x: (-(_calculate_similarity(wine,x)),x))
        results.append((wine,sorted_list[:5]))

    
    return sorted(results,key=lambda x:x[0])






