___ tickets(people
    cashier = {100:0,50:0,25:0}
    ___ pay in people:
        __ pay __ 25:
            cashier[25] += 1
        ____ pay __ 50:
            __ cashier[25] __ 0:
                r_ 'NO'
            cashier[50] += 1
            cashier[25] -= 1
        ____
            cashier[100] += 1
            __ cashier[50] >= 1 and cashier[25] >= 1:
                cashier[50] -= 1
                cashier[25] -= 1
            ____ cashier[25] >= 3:
                cashier[25] -= 3
            ____
                r_ 'NO'
    r_ 'YES'


print(tickets([25,25,25,100,25,50]))    