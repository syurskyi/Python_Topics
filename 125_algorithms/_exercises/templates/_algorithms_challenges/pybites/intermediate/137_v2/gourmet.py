#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

____ c.. _______ C..,d..
_______ o..
_______ i..




CHEESES [
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

RED_WINES [
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

WHITE_WINES [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]

mapping {'red': RED_WINES,'white': WHITE_WINES,'sparkling': SPARKLING_WINES,'all': RED_WINES+WHITE_WINES+SPARKLING_WINES}



___ _calculate_similarity(wine,cheese
    wine_length l..(wine)
    cheese_length l..(cheese)
    
    counts_wine C..(wine.l..
    counts_cheese C..(cheese.l..

    numerator s..((counts_wine & counts_cheese).values

    denominator 1 + (wine_length - cheese_length)**2

    r.. numerator/denominator

___ best_match_per_wine(wine_type="all"
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """

    __ wine_type n.. __ mapping:
        r.. V...("Invalid Wie TYpe")


    values mapping[wine_type]

    

    maximum m..(i...product(values,CHEESES),key=l.... x: _calculate_similarity(*x


    r.. (*maximum,_calculate_similarity(*maximum











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
    all_wines mapping 'all'
    wine_cheeses d..(l..)
    
    results    # list

    ___ wine __ all_wines:
        sorted_list s..(CHEESES,key=l.... x: (-(_calculate_similarity(wine,x,x
        results.a..((wine,sorted_list[:5]

    
    r.. s..(results,key=l.... x:x 0






