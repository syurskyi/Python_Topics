# Problem: https://www.hackerrank.com/challenges/no-idea/problem
# Score: 50


_ = input()
array = input().split()
like = set(input().split())
dislike = set(input().split())
print(su.((i in like) - (i in dislike) ___ i in array))
