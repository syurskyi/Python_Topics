___ poker(hands
    r_ allmax(hands, key=hand_rank)


___ allmax(iterable, key=None
    result, maxval = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xval = key(x)
        __ not result or xval > maxval:
            result, maxval = [x], xval
        ____ xval __ maxval:
            result.append(x)
    r_ result


___ hand_rank(hand
    card_ranks = ["..23456789TJQKA".index(r) for r, s in hand]
    groups = [(card_ranks.count(i), i) for i in set(card_ranks)]
    groups.sort(reverse=True)
    counts, ranks = zip(*groups)
    __ ranks __ [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    straight = (le.(counts) __ 5) and (max(ranks) - min(ranks) __ 4)
    flush = le.(set([s for r, s in hand])) __ 1
    r_ (9 __ counts __ (5,) else
            8 __ straight and flush else
            7 __ counts __ (4, 1) else
            6 __ counts __ (3, 2) else
            5 __ flush else
            4 __ straight else
            3 __ counts __ (3, 1, 1) else
            2 __ counts __ (2, 2, 1) else
            1 __ counts __ (2, 1, 1, 1) else
            0, ranks)
