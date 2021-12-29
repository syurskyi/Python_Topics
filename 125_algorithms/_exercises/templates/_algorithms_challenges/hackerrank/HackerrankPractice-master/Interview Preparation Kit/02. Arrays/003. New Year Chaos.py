# Problem: https://www.hackerrank.com/challenges/new-year-chaos/problem
#  Score: 40


t = int(input())
___ test __ r..(t):
    n = int(input())
    arr = l..(map(int, input().split()))
    count = 0

    ___ i __ r..(2):
        ___ j __ r..(l..(arr) - 1, 0, -1):
            __ arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                count += 1

    __ arr __ s..(arr):
        print(count)
    ____:
        print('Too chaotic')
