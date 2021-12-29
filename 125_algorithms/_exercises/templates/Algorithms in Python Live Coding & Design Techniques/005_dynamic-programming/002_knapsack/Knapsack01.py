# DP : Top down Approach
___ get_max_profit_td(weight, price, n, capacity, values

    __ n __ 0 or capacity __ 0:
        values[n-1][capacity-1]  0
        r_ 0

    __ values[n-1][capacity-1] ! -1:
        r_ values[n-1][capacity-1]

    incl  0
    excl  0

    __ weight[n-1] < capacity:
        incl  price[n-1] + get_max_profit_td(weight, price, n-1, capacity - weight[n-1], values)
    excl  get_max_profit_td(weight, price, n-1, capacity, values)

    values[n-1][capacity-1]  ma_(incl, excl)
    r_ values[n-1][capacity-1]


# DP : Bottom Up Approach
___ get_max_profit_bu(weight, price, n, capacity

    values  [[0 ___ i __ ra__(capacity+1)] ___ i __ ra__(n+1)]

    ___ i __ ra__(n+1
        ___ j __ ra__(capacity+1
            __ i __ 0 or j __ 0 :
                values[i][j]  0
            ____
                incl  0
                excl  0
                __ weight[i-1] < j:
                    incl  price[i-1] + values[i-1][j- weight[i-1]]
                excl  values[i-1][j]
                values[i][j]  ma_(incl, excl)
    r_ values[n][capacity]


weight  [7, 5, 4]
price  [15, 8, 8]
capacity  10
n  le_(weight)

values  [[-1 ___ i __ ra__(capacity+1)] ___ i __ ra__(n+1)]
print(get_max_profit_bu(weight, price, n, capacity))
