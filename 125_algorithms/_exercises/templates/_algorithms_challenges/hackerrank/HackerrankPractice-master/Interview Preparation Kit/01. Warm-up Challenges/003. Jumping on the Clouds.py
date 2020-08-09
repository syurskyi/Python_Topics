# Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
#  Score: 20


___ jumping_on_clouds(n, c
    c.append(0)
    ans = 0
    position = 0
    w___ position < n-1:
        position += (c[position+2] __ 0) + 1
        ans += 1
    r_ ans


n = int(input())
c = list(map(int, input().rstrip().split()))
print(jumping_on_clouds(n, c))
