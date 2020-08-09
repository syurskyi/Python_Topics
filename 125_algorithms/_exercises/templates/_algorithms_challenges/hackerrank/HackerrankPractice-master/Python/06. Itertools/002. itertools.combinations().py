# Problem:  https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10


______ itertools


s = input().split()
string, number = sorted(s[0]), int(s[1])
___ i in range(1, number + 1
    print(*list(map(''.join, itertools.combinations(string, i))), sep='\n')
