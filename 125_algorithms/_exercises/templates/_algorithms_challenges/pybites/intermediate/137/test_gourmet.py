_______ p__
____ gourmet _______ best_match_per_wine, match_wine_5cheeses


___ test_best_match_per_wine_all
    ... best_match_per_wine()[2] __ 13.0


cases_best_by_wine = [
    ("white", "Sauvignon blanc", "Smoked Austrian", 8.0),
    ("red", "Cabernet sauvignon", "Dorset Blue Vinney", 13.0),
    ("sparkling", "Moscato d’Asti", "Carré de l'Est", 6.0),
]


@p__.mark.parametrize("case", cases_best_by_wine)
___ test_best_match_per_wine_type(case):
    wine_type, *result = case
    ... best_match_per_wine(wine_type) __ t..(result)


___ test_invalid_wine_type
    w__ p__.r..(ValueError):
        best_match_per_wine("cocacola")


___ test_all_wines_included
    ... l..(match_wine_5cheeses()) __ 26


mw5c = match_wine_5cheeses()
cases = [
    (0, "Barbera", ["Cheddar", "Gruyère", "Boursin", "Parmesan", "Liptauer"]),
    (1, "Barolo", ["Boursin", "Cheddar", "Gouda", "Stilton", "Tilsit"]),
    (
        2,
        "Cabernet sauvignon",
        [
            "Dorset Blue Vinney",
            "Norwegian Jarlsberg",
            "Czech sheep's milk",
            "Double Gloucester",
            "Japanese Sage Derby",
        ],
    ),
    (3, "Cava", ["Edam", "Gouda", "Cheddar", "Savoyard", "Parmesan"]),
    (
        4,
        "Champagne",
        ["Caithness", "Camembert", "Bel Paese", "Ilchester", "Lancashire"],
    ),
    (-2, "Syrah", ["Gouda", "Cheddar", "Brie", "Edam", "Tilsit"]),
    (
        -1,
        "Zinfandel",
        ["Caithness", "Bel Paese", "Ilchester", "Limburger", "Lancashire"],
    ),
]


@p__.mark.parametrize("case", cases)
___ test_match_wine_5cheeses(case):
    """ test of presence of first 2 cheeses only
    because if score is same for more pairs, order of pairs cannot be assumed
    """
    idx, wine, cheeses = case
    ... mw5c[idx][0] __ wine
    ... mw5c[idx][1] __ cheeses