#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# House Robber Problem  in Python

___ houseRobber(houses, currentIndex
    __ currentIndex >= le_(houses
        r_ 0
    ____
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex + 2)
        skipFirstHouse = houseRobber(houses, currentIndex+1)
        r_ max(stealFirstHouse, skipFirstHouse)

houses = [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))