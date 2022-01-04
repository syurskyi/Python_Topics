# Problem: https://www.hackerrank.com/challenges/collections-counter/problem
# Score: 10


_______ collections


number_of_shoes = i..(input())
sizes_in_stock = collections.Counter(map(i.., input().s..()))

total_revenue = 0

___ _ __ r..(i..(input())):
    size, price = map(i.., input().s..())
    __ sizes_in_stock[size]:
        total_revenue += price
        sizes_in_stock[size] -= 1

print(total_revenue)
