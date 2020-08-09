# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Score: 10


______ collections


number_of_shoes = int(input())
sizes_in_stock = collections.Counter(map(int, input().split()))

total_revenue = 0

___ _ in range(int(input())):
    size, price = map(int, input().split())
    __ sizes_in_stock[size]:
        total_revenue += price
        sizes_in_stock[size] -= 1

print(total_revenue)
