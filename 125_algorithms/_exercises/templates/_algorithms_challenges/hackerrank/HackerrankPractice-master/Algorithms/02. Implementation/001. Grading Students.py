# Problem: https://www.hackerrank.com/challenges/grading/problem
# Score: 10


___ _ in range(int(input())):
    grade = int(input())
    __ grade >= 38 and grade % 5 >= 3:
        grade = (grade + 5) // 5 * 5
    print(grade)
