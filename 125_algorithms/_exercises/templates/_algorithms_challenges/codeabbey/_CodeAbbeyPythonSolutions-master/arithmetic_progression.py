amount_values i..(input
results    # list

___ get_progression(start, inc, s..
    progress start
    ___ i __ r..(s.., 1,-1
        start +=  inc
        progress += start
    results.a..(progress)

___ i __ r..(amount_values
    start, inc, s.. map(i.., input().s..
    get_progression(start,inc,s..)
print(*results)