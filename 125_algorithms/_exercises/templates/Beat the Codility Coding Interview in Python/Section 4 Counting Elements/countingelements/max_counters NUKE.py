# This is the solution for CountingElements > MaxCounters
#
# This is marked as RESPECTABLE difficulty

___ solution(N, A):
    counters  [0] * N
    start_line  0
    current_max  0
    ___ i __ A:
        x  i - 1
        __ i > N:
            start_line  current_max
        ____ counters[x] < start_line:
            counters[x]  start_line + 1
        ____:
            counters[x] + 1
        __ i < N and counters[x] > current_max:
            current_max  counters[x]
    ___ i __ r..(0, l..(counters)):
        __ counters[i] < start_line:
            counters[i]  start_line
    r.. counters

print (solution(5, [3, 4, 4, 6, 1, 4, 4]))
