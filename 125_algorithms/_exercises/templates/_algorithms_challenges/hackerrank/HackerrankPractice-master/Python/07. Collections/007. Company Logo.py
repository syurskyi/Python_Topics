# Problem: https://www.hackerrank.com/challenges/py-collections-deque/problem
# Score: 30


____ collections _______ Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


letters = OrderedCounter(s..(input())).most_common(3)
[print(*letter) ___ letter __ letters]
