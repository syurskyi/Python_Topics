# Problem: https://www.hackerrank.com/challenges/calendar-module/problem
# Score: 10


_______ calendar


m, d, y = map(int, input().s..())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
