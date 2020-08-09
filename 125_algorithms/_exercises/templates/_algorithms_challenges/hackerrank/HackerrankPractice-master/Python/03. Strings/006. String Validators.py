# Problem: https://www.hackerrank.com/challenges/string-validators/problem
# Score: 10


s = input()
print(any([char.isalnum() ___ char in s]))
print(any([char.isalpha() ___ char in s]))
print(any([char.isdigit() ___ char in s]))
print(any([char.islower() ___ char in s]))
print(any([char.isupper() ___ char in s]))
