# Problem: https://www.hackerrank.com/challenges/repeated-string/problem
# Score: 20


___ repeated_string(s, n
    r_ n // le.(s) * s.count('a') + s[0: n % le.(s)].count('a')


s = input()
n = int(input())
print(repeated_string(s, n))
