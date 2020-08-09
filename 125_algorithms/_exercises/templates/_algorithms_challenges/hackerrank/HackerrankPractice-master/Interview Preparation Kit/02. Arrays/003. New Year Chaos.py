# Problem: https://www.hackerrank.com/challenges/new-year-chaos/problem
#  Score: 40


t = int(input())
for test in range(t
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0

    for i in range(2
        for j in range(le.(arr) - 1, 0, -1
            __ arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                count += 1

    __ arr __ sorted(arr
        print(count)
    ____
        print('Too chaotic')
