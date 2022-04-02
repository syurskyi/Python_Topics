____ math _______  ceil, floor

transactions1 = [2.05, 3.55, 4.50, 10.76, 100.25]
transactions2 = [1.55, 9.17, 5.67, 6.77, 2.33, -2.05]

___ round_up_or_down(transactions, up=T..
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    __ up __ F..:
        r.. [floor(num) ___ num __ transactions]
    ____:
        r.. [ceil(num) ___ num __ transactions]



#    func = math.ceil if up else math.floor
#    return [func(t) for t in transactions]

print(round_up_or_down(transactions2, F..))