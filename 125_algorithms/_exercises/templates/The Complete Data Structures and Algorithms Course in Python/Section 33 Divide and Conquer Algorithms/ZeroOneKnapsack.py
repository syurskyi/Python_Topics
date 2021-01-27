#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Zero One Knapsack in Python

c_ Item:
    ___  -   profit, weight
        profit = profit
        weight = weight

___ zoKnapsack(items, capacity, currentIndex
    __ capacity <=0 or currentIndex < 0 or currentIndex >= le_(items
        r_ 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = zoKnapsack(items, capacity, currentIndex+1)
        r_ max(profit1, profit2)
    ____
        r_ 0

mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(zoKnapsack(items, 7, 0))