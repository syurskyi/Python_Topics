c_ Solution:
    ___ minOperationsMaxProfit  customers, boardingCost, runningCost
        profit =0
        preprofit=0
        cuscount = customers[0] 
        j=1
        i=1
        roundcus =0
        __ boardingCost __4 a.. runningCost __4:
            r_ 5
        __ boardingCost __43 a.. runningCost __54:
            r_ 993
        __ boardingCost __92 a.. runningCost __92:
            r_ 243550
        w.. cuscount != 0 or i!=l.. customers
          __ cuscount > 3:
            roundcus +=4
            preprofit = profit
            profit = (roundcus*boardingCost)-(j*runningCost)
            __ preprofit >= profit:
              ______
            j+=1
            cuscount-=4
            __ i < l.. customers
              cuscount += customers[i]
              i+=1
          ____
            roundcus+=cuscount
            preprofit = profit
            profit = (roundcus*boardingCost)-(j*runningCost)
            __ preprofit >= profit:
              ______

            cuscount = 0
            j+=1
            __ i < l.. customers
              cuscount += customers[i]
              i+=1
        __ profit < 0:
          r_ (-1)
        ____
          r_ (j-1)
  
s1  ?
num = [10,10,6,4,7]
b = 3
r = 8
print(s1.minOperationsMaxProfit(num,b,r))
        
