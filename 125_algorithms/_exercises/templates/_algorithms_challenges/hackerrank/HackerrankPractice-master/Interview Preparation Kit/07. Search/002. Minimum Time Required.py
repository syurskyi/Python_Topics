# Problem: https://www.hackerrank.com/challenges/minimum-time-required/problem
#  Score: 35


_______ math


___ minimum_time(goal, machines):
    min_days = math.ceil(goal / (l..(machines) / m..(machines)))
    max_days = math.ceil(goal / (l..(machines) / max(machines)))
    while min_days < max_days:
        day = (min_days + max_days) // 2
        __ s..(day // i ___ i __ machines) >= goal:
            max_days = day
        ____:
            min_days = day + 1
    r.. min_days


n, goal = map(int, input().split())
machines = l..(map(int, input().split()))
print(minimum_time(goal, machines))
