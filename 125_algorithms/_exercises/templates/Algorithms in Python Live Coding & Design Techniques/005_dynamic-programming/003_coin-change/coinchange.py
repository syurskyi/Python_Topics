import sys

# Recursive Approach
___ min_coins(coins, n, total
    __ total == 0:
        r_ 0

    result = sys.maxsize
    ___ i __ range(n
        __ coins[i] <= total:
            sub_result = min_coins(coins, n, total - coins[i])
            __ sub_result != sys.maxsize and sub_result + 1 < result:
                result = sub_result + 1
    r_ result


# DP : Top Down Approach
___ min_coins_top_down(coins, n, total, table
    __ total == 0:
        r_ 0

    __ total __ table:
        r_ total

    result = sys.maxsize
    ___ i __ range(n
        __ coins[i] <= total:
            sub_result = min_coins_top_down(coins, n, total - coins[i], table)
            __ sub_result != sys.maxsize and sub_result + 1 < result:
                result = sub_result + 1
    table[total] = result
    r_ result


# DP : Bottom Up Approach
___ min_coins_bottom_up(coins, n, total
    table = [0 ___ k __ range(total+1)]

    table[0] = 0

    ___ i __ range(1, total+1
        table[i] = sys.maxsize

    ___ i __ range(1, total + 1
        ___ j __ range(n
            __ coins[j] <= i:
                sub_result = table[i-coins[j]]
                __ sub_result != sys.maxsize and sub_result + 1 < table[i]:
                    table[i] = sub_result + 1
    r_ table[total]


__ __name__ == '__main__':
    coins = [1, 3, 5, 2]
    n = le_(coins)
    total = 9
    min_number = min_coins(coins, n, total)

    table = [[0 ___ x __ range(n+1)] ___ x __ range(total+1)]
    min = min_coins_top_down(coins, n, total, table)

    min_no = min_coins_bottom_up(coins, n, total)

    print('Minimum coins needed : ' , min_no , ' coins');
