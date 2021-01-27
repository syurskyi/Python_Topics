#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Fractional Knapsack Problem  in Python

c_ Item:
    ___  -   weight, value
        weight = weight
        value = value
        ratio = value / weight

___ knapsackMethod(items, capacity
    items.sort(key=lambda x: x.ratio, reverse = T..)
    usedCapacity = 0
    totalValue = 0
    ___ i __ items:
        __ usedCapacity + i.weight <= capacity:
            usedCapacity += i.weight
            totalValue += i.value
        ____
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
        
        __ usedCapacity __ capacity:
            break
    print("Total value obtained: "+st.(totalValue))

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)