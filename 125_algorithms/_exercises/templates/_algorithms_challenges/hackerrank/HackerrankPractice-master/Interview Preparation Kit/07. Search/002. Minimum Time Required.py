# Problem: https://www.hackerrank.com/challenges/minimum-time-required/problem
#  Score: 35


______ ma__


___ minimum_time(goal, machines
    min_days = ma__.ceil(goal / (le.(machines) / min(machines)))
    max_days = ma__.ceil(goal / (le.(machines) / max(machines)))
    w___ min_days < max_days:
        day = (min_days + max_days) // 2
        __ sum(day // i for i in machines) >= goal:
            max_days = day
        ____
            min_days = day + 1
    r_ min_days


n, goal = map(int, input().split())
machines = list(map(int, input().split()))
print(minimum_time(goal, machines))
