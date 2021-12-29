amount_values = int(input())
results    # list

___ get_progression(start, inc, s..):
    progress = start
    ___ i __ r..(s.., 1,-1):
        start +=  inc
        progress += start
    results.a..(progress)

___ i __ r..(amount_values):
    start, inc, s.. = map(int, input().split())
    get_progression(start,inc,s..)
print(*results)