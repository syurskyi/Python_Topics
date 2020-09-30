# Problem: https://www.hackerrank.com/challenges/py-check-subset/problem
# Score: 10


___ i __ range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))
