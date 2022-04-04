___ find_minimum_coins(total_change, coins
    __ total_change < 0:
        r.. V...("cannot find negative change values")
    min_coins_required = [1e9] * (total_change + 1)
    last_coin = [0]*(total_change + 1)
    min_coins_required[0] = 0
    last_coin[0] = -1
    ___ change __ r..(1, total_change + 1
        final_result = min_coins_required[change]
        ___ coin __ coins:
            __ coin <= change:
                result = min_coins_required[change - coin] + 1
                __ result < final_result:
                    final_result = result
                    last_coin[change] = change - coin
        min_coins_required[change] = final_result
    __ min_coins_required[total_change] __ 1e9:
        r.. V...("no combination can add up to target")
    ____
        last_coin_value = total_change
        array    # list
        w....(last_coin[last_coin_value] != -1
            array.a..(last_coin_value-last_coin[last_coin_value])
            last_coin_value = last_coin[last_coin_value]
        r.. array
