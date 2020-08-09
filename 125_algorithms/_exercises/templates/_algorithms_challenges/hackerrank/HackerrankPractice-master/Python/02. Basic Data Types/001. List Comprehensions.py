# Problem: https://www.hackerrank.com/challenges/list-comprehensions/problem
# Score: 10


x, y, z, n = [int(input()) ___ _ in range(4)]
listOfAnswers = [[i, j, k] ___ i in range(x + 1) ___ j in range(y + 1) ___ k in range(z + 1) __ i + j + k != n]
print(listOfAnswers)
