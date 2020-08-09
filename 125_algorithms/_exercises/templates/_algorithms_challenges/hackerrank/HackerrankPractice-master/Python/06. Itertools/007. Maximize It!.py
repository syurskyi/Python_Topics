# Problem: https://www.hackerrank.com/challenges/maximize-it/problem
# Score: 50


from itertools ______ product

k, m = map(int, input().split())
n = (list(map(int, input().split()))[1:] ___ _ in range(k))
results = (su.(i**2 ___ i in x) % m ___ x in product(*n))
print(max(results))
