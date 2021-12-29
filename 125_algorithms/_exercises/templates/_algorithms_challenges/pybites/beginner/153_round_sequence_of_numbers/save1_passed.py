import math

___ round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    return list(math.ceil(i) __ up __ True else math.floor(i) for i in transactions)