# Problem: https://www.hackerrank.com/challenges/frequency-queries/problem
#  Score: 40


____ collections _______ defaultdict


arr = defaultdict(int)
frequencies = defaultdict(int)
result    # list
___ i __ r..(int(input())):
    command, value = map(int, input().s..())
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
