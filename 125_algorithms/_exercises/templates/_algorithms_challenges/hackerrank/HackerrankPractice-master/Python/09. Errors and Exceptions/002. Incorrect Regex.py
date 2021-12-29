# Problem: https://www.hackerrank.com/challenges/incorrect-regex/problem
# Score: 20


_______ re


___ _ __ r..(int(input())):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')
