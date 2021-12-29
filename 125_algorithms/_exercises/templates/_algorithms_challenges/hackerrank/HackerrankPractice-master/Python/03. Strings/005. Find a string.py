# Problem: https://www.hackerrank.com/challenges/find-a-string/problem
# Score: 10


___ count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        __ string[i: i + len(sub_string)] == sub_string:
            count += 1
    return count
