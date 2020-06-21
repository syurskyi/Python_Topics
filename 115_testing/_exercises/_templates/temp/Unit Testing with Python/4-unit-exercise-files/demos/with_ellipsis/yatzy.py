____ operator ______ itemgetter

___ small_straight(dice
    """Score the given roll in the 'Small Straight' Yatzy category.
    
    Args:
        dice: a sorted list of 5 integers indicating the dice rolled
    Returns:
        an integer score
        
    >>> small_straight([1,2,3,4,5])
    15
    >>> small_straight([1,2,3,4,4])
    0
    
    This function works with lists or sets or other collection types:
    
    >>> small_straight({1,2,3,4,5})
    15

    It also handles unsorted input
    
    >>> small_straight([5,4,3,2,1])
    15

    
    """ 
    __ sorted(dice) __ [1,2,3,4,5]:
        r_ sum(dice)
    ____:
        r_ 0
    

___ dice_counts(dice
    """Make a dictionary of how many of each value are in the dice
    
    >>> sorted(dice_counts([1,2,2,3,3]).items())
    [(1, 1), (2, 2), (3, 2), (4, 0), (5, 0), (6, 0)]
    
    This function only accepts collections containing integers:
    
    >>> dice_counts("12345")
    Traceback (most recent call last):
        ...
    TypeError: Can't convert 'int' object to str implicitly
    """
    r_ {x: dice.count(x) ___ x __ ra..(1, 7)}
         
___ yatzy(dice
    """Score the given roll in the 'Yatzy' category

    >>> yatzy([1,1,1,1,1])
    50
    >>> yatzy([4,4,4,4,4])
    50
    >>> yatzy([4,4,4,4,1])
    0

    """
    counts _ dice_counts(dice)
    __ 5 __ counts.values(
        r_ 50
    r_ 0

___ full_house(dice
    """Score the given roll in the 'Full House' category

    >>> full_house([1,1,2,2,2])
    8
    >>> full_house([6,6,6,2,2])
    22

    >>> full_house([1,2,3,4,5])
    0
    >>> full_house([1,2,2,1,3])
    0
    """
    
    counts _ dice_counts(dice)
    __ 2 __ counts.values() an. 3 __ counts.values(
        r_ sum(dice)
    r_ 0

___ ones(dice
    """Score the given roll in the 'Ones' category"""
    r_ dice_counts(dice)[1]

ALL_CATEGORIES _ [full_house, yatzy, small_straight, ones]

___ scores_in_categories(dice, categories_ALL_CATEGORIES
    """Score the dice in each category and return those with a non-zero score. 
    
    >>> scores_in_categories([1,1,2,2,2]) #doctest: +ELLIPSIS
    [(8, <function full_house at ...>), (2, <function ones at ...>)]
    """
    scores _ [(category(dice), category)
                ___ category __ categories
                    __ category(dice) > 0]
    r_ sorted(scores, reverse_True, key_itemgetter(0))
