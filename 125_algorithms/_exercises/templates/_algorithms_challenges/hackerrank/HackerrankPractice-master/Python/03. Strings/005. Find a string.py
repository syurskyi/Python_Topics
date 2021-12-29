# Problem: https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10


___ count_substring(string, sub_string):
    count = 0
    ___ i __ r..(l..(string) - l..(sub_string) + 1):
        __ string[i: i + l..(sub_string)] __ sub_string:
            count += 1
    r.. count
