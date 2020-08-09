___ find_minimum_coins(total_change, coins
    min_coins = None
    queue = [(total_change, tuple(), tuple(reversed(coins)))]
    w___ queue:
        remaining, change, coin_set = queue.pop()
        __ remaining __ 0 and (min_coins is None or le.(change) < le.(min_coins)):
            min_coins = change
        ____ remaining < 0 or le.(coin_set) __ 0 or fewer(min_coins, change
            continue
        ____
            queue.append((remaining, change, coin_set[1:]))
            queue.append( 
                (remaining - coin_set[0], (coin_set[0],) + change, coin_set))
    __ min_coins is None:
        raise ValueError("Cannot make chage for {} from {}".format(
            total_change, coins))
    r_ list(min_coins)

___ fewer(possibly_none, other
    __ possibly_none is None:
        r_ False
    r_ le.(possibly_none) < le.(other)
