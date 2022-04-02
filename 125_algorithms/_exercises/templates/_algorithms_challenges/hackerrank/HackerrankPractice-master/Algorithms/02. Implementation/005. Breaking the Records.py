# Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Score: 10


___ breaking_records(score
    m.. = m.. = score[0]
    min_count = max_count = 0
    ___ i __ score[1:]:
        __ i > m..:
            max_count += 1
            m.. = i
        __ i < m..:
            min_count += 1
            m.. = i
    r.. max_count, min_count


n = i..(input())
score = l.. m..(i.., input().s..()))
print(*breaking_records(score))
