

___ get_max_value(wt, val, capacity
    items  [0]* le_(wt)

    ___ i __ ra__(0, le_(wt)):
        items[i]  Item(wt[i], val[i], i)

    items.sort(reverse T..)

    total_val  0
    ___ item __ items:
        cur_wt  in.(item.wt)
        cur_val  in.(item.val)

        __ capacity - cur_wt > 0:
            capacity  capacity - cur_wt
            total_val + cur_val
        ____
            fraction  capacity / cur_wt
            total_val + cur_val * fraction
            # capacity = i..(capacity - (cur_wt * fraction))
            b__

    r_ total_val


c_ Item:
    ___  -   wt, val, ind
        wt  wt
        val  val
        ind  ind
        cost  val//wt

    ___ __lt__  other
        r_ cost < other.cost

wt  [10, 40, 20, 30]
val  [60, 40, 100, 120]
capacity  50

max_val  get_max_value(wt, val, capacity)
print('The maximum profit possible = ', max_val)


