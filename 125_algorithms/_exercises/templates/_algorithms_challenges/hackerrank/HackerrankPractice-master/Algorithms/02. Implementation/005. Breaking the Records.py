# Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Score: 10


___ breaking_records(score):
    m.. = max = score[0]
    min_count = max_count = 0
    ___ i __ score[1:]:
        __ i > max:
            max_count += 1
            max = i
        __ i < m..:
            min_count += 1
            m.. = i
    r.. max_count, min_count


n = int(input())
score = l..(map(int, input().s..()))
print(*breaking_records(score))
