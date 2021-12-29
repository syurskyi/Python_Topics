# Problem:  https://www.hackerrank.com/challenges/itertools-product/problem
# Score: 10


____ itertools _______ product


a = l..(map(int, input().split()))
b = l..(map(int, input().split()))
print(*l..(product(a, b)))
