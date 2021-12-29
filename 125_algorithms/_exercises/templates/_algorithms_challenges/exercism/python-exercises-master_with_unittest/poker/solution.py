___ poker(hands):
    r.. allmax(hands, key=hand_rank)


___ allmax(iterable, key_ N..
    result, maxval    # list, N..
    key = key o. (l.... x: x)
    ___ x __ iterable:
        xval = key(x)
        __ n.. result o. xval > maxval:
            result, maxval = [x], xval
        ____ xval __ maxval:
            result.a..(x)
    r.. result


___ hand_rank(hand):
    card_ranks = ["..23456789TJQKA".index(r) ___ r, s __ hand]
    groups = [(card_ranks.c.. i), i) ___ i __ set(card_ranks)]
    groups.sort(r.._T..
    counts, ranks = zip(*groups)
    __ ranks __ [14, 5, 4, 3, 2]:
        ranks = [5, 4, 3, 2, 1]
    straight = (l..(counts) __ 5) and (max(ranks) - m..(ranks) __ 4)
    flush = l..(set([s ___ r, s __ hand])) __ 1
    r.. (9 __ counts __ (5,) ____
            8 __ straight and flush ____
            7 __ counts __ (4, 1) ____
            6 __ counts __ (3, 2) ____
            5 __ flush ____
            4 __ straight ____
            3 __ counts __ (3, 1, 1) ____
            2 __ counts __ (2, 2, 1) ____
            1 __ counts __ (2, 1, 1, 1) ____
            0, ranks)
