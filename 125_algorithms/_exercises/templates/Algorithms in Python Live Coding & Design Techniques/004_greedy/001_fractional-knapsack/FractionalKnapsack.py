

___ get_max_value(wt, val, capacity
    items = [0]* le_(wt)

    ___ i __ range(0, le_(wt)):
        items[i] = Item(wt[i], val[i], i)

    items.sort(reverse= True)

    total_val = 0
    ___ item __ items:
        cur_wt = int(item.wt)
        cur_val = int(item.val)

        __ capacity - cur_wt >= 0:
            capacity = capacity - cur_wt
            total_val += cur_val
        ____
            fraction = capacity / cur_wt
            total_val += cur_val * fraction
            # capacity = int(capacity - (cur_wt * fraction))
            break

    r_ total_val


class Item:
    ___ __init__(self, wt, val, ind
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val//wt

    ___ __lt__(self, other
        r_ self.cost < other.cost

wt = [10, 40, 20, 30]
val = [60, 40, 100, 120]
capacity = 50

max_val = get_max_value(wt, val, capacity)
print('The maximum profit possible = ', max_val)


