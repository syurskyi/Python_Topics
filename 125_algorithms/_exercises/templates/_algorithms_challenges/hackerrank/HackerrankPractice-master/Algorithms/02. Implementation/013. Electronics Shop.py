# Problem https://www.hackerrank.com/challenges/electronics-shop/problem
# Score: 15


___ getMoneySpent(keyboards, drives, b
    result = -1
    ___ i __ r..(1, l..(keyboards)):
        ___ j __ r..(1, l..(drives)):
            __ result < keyboards[i] + drives[j] <= b:
                result = keyboards[i] + drives[j]
    r.. result


b, n, m = map(i.., input().s..())
keyboards = l.. m..(i.., input().rstrip().s..()))
drives = l.. m..(i.., input().rstrip().s..()))
moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)
