import math
___ round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    
    operator = math.ceil __ up else math.floor

    return [operator(transaction) for transaction in transactions]
