"""
貌似今日头条笔试？第三题。

两个人选卡牌，每张卡牌都有两个分值 x, y。选到卡牌时x加给自己，y加给团队。
给一组卡牌，求两个人选的卡牌 x 相等且y最大的情况。


思路：
根据 y 的分值先排序。

之后进行判断：

若里面的x相加是奇数直接跳过，在进行一次将此时下标排除的判断，最后都不通过将最小的一个y值的卡牌放入废弃池。
若里面的x相加是偶数：
    排序：
    1. 取末尾一个数，若大于目标（x相加/2）则返回 False。将最小的一个y值的卡牌放入废弃池。
    2. 等于直接返回True.
    3. 小于的情况减去。

    对剩余的进行Dp:
    每一个都有两种操作：
    1. 减去或不减。
    2. 大于的不减，小于的也可以不减。
    3. 直到有一个是0或都不是，返回 False。

---
判断还是这么判断，只不过不废弃了，直接用itertools生成从大到小生成数据，先倒序，然后len(x) - 2

这样直接返回只适用于没有负数的情况，若有负数需要全部计算后在进行判断。

此种方法属于暴力法...效率不高.
最差会有 
n * (n-1) / (n - 1) + n * (n-1) / (n-2) ....次。

做完3道已经用了接近两个小时。。


"""


test = [
[3, 1],
[2, 2],
[1, 4],
[1, 4]
]

test2 = [
[7, 1],
[6, 2],
[5, 3],
[4, 4],
[3, 5],
[2, 6],
[1, 7],
[1, 7]

]

import itertools


___ maxCardsScope(cards

    cards = s..(cards, k.._l... x: x[1], reverse=True)

    result_cards _ # dict

    currentCards = cards
    allCardsScopes = s..([x[0] ___ x __ cards])

    __ allCardsScopes % 2 __ 0:
        __ judgeEqual(cards, allCardsScopes / 2
            r_ s..([x[1] ___ x __ cards])
            # result_cards[sum([x[1] for x in cards])] = [cards]


    ___ x __ r..(l..(cards)-1, 1, -1
        ___ i __ itertools.combinations(cards, x
            temp = s..([t[0] ___ t __ i])
            __ temp % 2 != 0:
                c_

            __ judgeEqual(i, temp / 2
                r_ s..([t[1] ___ t __ i])


___ judgeEqual(cards, target
    cards = s..(cards, k.._l... x: x[0], reverse=True)
    __ cards[0][0] __ target:
        r_ True

    __ cards[0][0] > target:
        r_ False

    __ cards[0][0] < target:
        # init = target - cards[0][0]
        dp = {-1: [target]}

        ___ i, d __ enumerate(cards
            temp = dp[i-1].copy()
            ___ x __ dp[i-1]:
                __ x - d[0] __ 0:
                    r_ True

                __ x - d[0] > 0:
                    temp.append(x - d[0])
            dp[i] = temp
    
    r_ False


print(maxCardsScope(test2))
