# Problem: https://www.hackerrank.com/challenges/frequency-queries/problem
#  Score: 40


from collections ______ defaultdict


arr = defaultdict(int)
frequencies = defaultdict(int)
result = []
___ i in range(int(input())):
    command, value = map(int, input().split())
    __ command __ 1:
        arr[value] += 1
        frequencies[arr[value]] += 1
        frequencies[arr[value] - 1] -= 1
    __ command __ 2 and arr[value] != 0:
        arr[value] -= 1
        frequencies[arr[value]] += 1
        frequencies[arr[value] + 1] -= 1
    __ command __ 3:
        result.append(1 __ frequencies[value] > 0 else 0)

___ i in result:
    print(i)
