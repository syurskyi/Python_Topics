# Problem: https://www.hackerrank.com/challenges/python-mutations/problem
# Score: 10


___ mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]
