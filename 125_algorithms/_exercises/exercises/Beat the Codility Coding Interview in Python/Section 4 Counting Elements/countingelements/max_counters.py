# This is the solution for CountingElements > MaxCounters
#
# This is marked as RESPECTABLE difficulty

def solution(N, A):
    counters = [0] * N
    start_line = 0
    current_max = 0
    for i in A:
        x = i - 1
        if i > N:
            start_line = current_max
        elif counters[i] < start_line:
            counters[i] = start_line + 1
        else:
            counters[i] += 1
        if i <= N and counters[i] > current_max:
            current_max = counters[i]
    for i in range(0, len(counters)):
        if counters[i] < start_line:
            counters[i] = start_line
    return counters

print (solution(5, [3, 4, 4, 6, 1, 4, 4]))
