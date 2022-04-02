# Problem: https://www.hackerrank.com/challenges/frequency-queries/problem
#  Score: 40


____ c.. _______ defaultdict


arr = defaultdict(i..)
frequencies = defaultdict(i..)
result    # list
___ i __ r..(i..(input())):
    command, value = map(i.., input().s..
    __ command __ 1:
        arr[value] += 1
        frequencies[arr[value]] += 1
        frequencies[arr[value] - 1] -= 1
    __ command __ 2 a.. arr[value] != 0:
        arr[value] -= 1
        frequencies[arr[value]] += 1
        frequencies[arr[value] + 1] -= 1
    __ command __ 3:
        result.a..(1 __ frequencies[value] > 0 ____ 0)

___ i __ result:
    print(i)
