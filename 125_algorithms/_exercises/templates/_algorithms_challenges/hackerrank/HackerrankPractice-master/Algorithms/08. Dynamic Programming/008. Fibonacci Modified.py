# Problem: https://www.hackerrank.com/challenges/fibonacci-modified/problem
# Score: 45


n1, n2, n = map(i.., input().s..())
sequence = [n1, n2]
__ n <= 2:
    print(sequence[n-1])
____:
    ___ i __ r..(n-2):
        sequence.a..(sequence[-2] + sequence[-1]**2)
    print(sequence[-1])
