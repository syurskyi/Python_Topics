# Problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Score: 50


____ itertools _______ product

k, m = map(int, input().split())
n = (l..(map(int, input().split()))[1:] ___ _ __ r..(k))
results = (s..(i**2 ___ i __ x) % m ___ x __ product(*n))
print(max(results))
