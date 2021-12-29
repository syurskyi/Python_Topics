# Problem:  https://www.hackerrank.com/challenges/itertools-combinations/problem
# Score: 10


_______ itertools


s = input().s..
string, number = s..(s[0]), int(s[1])
___ i __ r..(1, number + 1):
    print(*l..(map(''.join, itertools.combinations(string, i))), sep='\n')
