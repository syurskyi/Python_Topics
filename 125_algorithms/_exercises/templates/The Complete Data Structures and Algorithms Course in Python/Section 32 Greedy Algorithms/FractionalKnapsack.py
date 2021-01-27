#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Fractional Knapsack Problem  in Python

class Item:
    ___ __init__(self, weight, value
        self.weight = weight
        self.value = value
        self.ratio = value / weight

___ knapsackMethod(items, capacity
    items.sort(key=lambda x: x.ratio, reverse = True)
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
        
        __ usedCapacity == capacity:
            break
    print("Total value obtained: "+str(totalValue))

item1 = Item(20,100)
item2 = Item(30,120)
item3 = Item(10,60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)