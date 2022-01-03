# Problem: https://www.hackerrank.com/challenges/piling-up/problem
# Score: 50


____ collections _______ deque


___ i __ r..(int(input())):
    _, n = input(), deque(map(int, input().s..()))
    ans = T..

    ___ j __ r..(l..(n) - 1):
        __ n[0] >= n[1]:
            n.popleft()
        ____ n[-1] >= n[-2]:
            n.pop()
        ____:
            ans = F..
            break

    print('Yes' __ ans ____ 'No')
