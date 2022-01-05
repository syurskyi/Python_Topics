____ decimal _______ Decimal


___ check_split(item_total, tax_rate, tip, people):
    total = Decimal(item_total[1:])
    tax = Decimal(tax_rate[:-1]) / 100 + 1
    tip_p = Decimal(tip[:-1]) / 100 + 1
    grand_total = r..(r..(total * tax, 2) * tip_p, 2)
    s.. = r..(grand_total / people, 2)
    split_arr = [s.. ___ _ __ r..(people - 1)]
    split_arr.a..(grand_total - s..(split_arr))
    r.. f'{item_total[0]}{grand_total:.2f}', split_arr
