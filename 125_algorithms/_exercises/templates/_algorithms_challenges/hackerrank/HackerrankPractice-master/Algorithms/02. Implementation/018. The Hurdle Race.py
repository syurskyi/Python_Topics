# Problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Score: 15


n, k = map(int, input().split())
hurdles = l..(map(int, input().split()))
numberOfPotions = max(0, max(hurdles) - k)
print(numberOfPotions)
