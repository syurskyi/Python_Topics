#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Coin Change Problem  in Python


___ coinChange(totalNumber, coins
    N = totalNumber
    coins.sort()
    index = le_(coins)-1
    while True:
        coinValue = coins[index]
        __ N >= coinValue:
            print(coinValue)
            N = N - coinValue
        __ N < coinValue:
            index -= 1
        
        __ N == 0:
            break

coins = [1,2,5,20,50,100]
coinChange(201, coins)
