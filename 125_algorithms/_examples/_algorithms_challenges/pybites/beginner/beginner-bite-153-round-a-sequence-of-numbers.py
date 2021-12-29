"""
It's time to get mathematical! In this Bite we ask that you complete the round_up_or_down function that receives a
transactions list of floats and an optional up argument.

If up is True (default) you round them up to the nearest full integer, if it is False, you round down to the nearest
full integer. Return a new list with the rounded int values.

Use whatever method you see fit, good luck!
"""

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    rounded = []
    for f in transactions:
        if up == True:
            f = f + 1
        r = int(f)
        rounded.append(r)
    return rounded


l = [4.5, 3.2, 6.9]
print(round_up_or_down(l, up=False))


