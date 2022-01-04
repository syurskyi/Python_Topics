# Problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Score: 15


n, k = map(i.., input().s..())
hurdles = l..(map(i.., input().s..()))
numberOfPotions = max(0, max(hurdles) - k)
print(numberOfPotions)
