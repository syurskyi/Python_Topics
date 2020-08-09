# Problem: https://www.hackerrank.com/challenges/nested-list/problem
# Score: 10


___ secondLowestGrade(classList
    secondLowestScore = sorted(set(_[1] for _ in classList))[1]
    result = sorted([_[0] for _ in classList __ _[1] __ secondLowestScore])
    r_ result


numberOfStudents = int(input())
classList = []
for i in range(numberOfStudents
    classList.append([str(input()), float(input())])
print('\n'.join(secondLowestGrade(classList)))
