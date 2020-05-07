from operator import itemgetter

def small_straight(dice):
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
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    else:
        return 0
    

def dice_counts(dice):
    """Make a dictionary of how many of each value are in the dice
    
    >>> sorted(dice_counts([1,2,2,3,3]).items())
    [(1, 1), (2, 2), (3, 2), (4, 0), (5, 0), (6, 0)]
    
    This function only accepts collections containing integers:
    
    >>> dice_counts("12345")
    Traceback (most recent call last):
        ...
    TypeError: Can't convert 'int' object to str implicitly
    """
    return {x: dice.count(x) for x in range(1, 7)}    
         
def yatzy(dice):
    """Score the given roll in the 'Yatzy' category

    >>> yatzy([1,1,1,1,1])
    50
    >>> yatzy([4,4,4,4,4])
    50
    >>> yatzy([4,4,4,4,1])
    0

    """
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0

def full_house(dice):
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
    
    counts = dice_counts(dice)
    if 2 in counts.values() and 3 in counts.values():
        return sum(dice)
    return 0

def ones(dice):
    """Score the given roll in the 'Ones' category"""
    return dice_counts(dice)[1]

ALL_CATEGORIES = [full_house, yatzy, small_straight, ones]

def scores_in_categories(dice, categories=ALL_CATEGORIES):
    """Score the dice in each category and return those with a non-zero score. 
    
    >>> scores_in_categories([1,1,2,2,2]) #doctest: +ELLIPSIS
    [(8, <function full_house at ...>), (2, <function ones at ...>)]
    """
    scores = [(category(dice), category) 
                for category in categories 
                    if category(dice) > 0]
    return sorted(scores, reverse=True, key=itemgetter(0))
