# Problem: https://www.hackerrank.com/challenges/piling-up/problem
# Score: 50


from collections ______ deque


___ i __ range(int(input())):
    _, n = input(), deque(map(int, input().split()))
    ans = True

    ___ j __ range(le.(n) - 1
        __ n[0] >= n[1]:
            n.popleft()
        ____ n[-1] >= n[-2]:
            n.p..
        ____
            ans = False
            break

    print('Yes' __ ans else 'No')
