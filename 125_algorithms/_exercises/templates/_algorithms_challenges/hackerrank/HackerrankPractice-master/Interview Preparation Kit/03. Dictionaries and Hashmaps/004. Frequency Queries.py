# Problem: https://www.hackerrank.com/challenges/frequency-queries/problem
#  Score: 40


____ c.. _______ d..


arr d..(i..)
frequencies d..(i..)
result    # list
___ i __ r..(i..(input())):
    command, value map(i.., input().s..
    __ command __ 1:
        arr[value] += 1
        frequencies[arr[value]] += 1
        frequencies[arr[value] - 1] -_ 1
    __ command __ 2 a.. arr[value] !_ 0:
        arr[value] -_ 1
        frequencies[arr[value]] += 1
        frequencies[arr[value] + 1] -_ 1
    __ command __ 3:
        result.a..(1 __ frequencies[value] > 0 ____ 0)

___ i __ result:
    print(i)
