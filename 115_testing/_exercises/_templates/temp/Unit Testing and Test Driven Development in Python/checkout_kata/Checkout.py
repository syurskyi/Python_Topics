
c_ Checkout:
    c_ Discount:
        ___  -   nbrItems, price
            nbrItems _ nbrItems
            price _ price

    ___  - 
        prices _ {}
        discounts _ {}
        items _ {}


    ___ addDiscount  item, nbrOfItems, price
        discount _ Discount(nbrOfItems, price)
        discounts[item] _ discount


    ___ addItemPrice  item, price
        prices[item] _ price

    ___ addItem  item
        __ item no. __ prices:
            r_ Exception("Bad Item")

        __ item __ items:
            items[item] +_ 1
        else:
            items[item] _ 1

    ___ calculateTotal
        total _ 0
        for item, cnt __ items.items(
            total +_ calculateItemTotal(item, cnt)
        r_ total

    ___ calculateItemTotal  item, cnt
        total _ 0
        __ item __ discounts:
            discount _ discounts[item]
            __ cnt >_ discount.nbrItems:
                total +_ calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total +_ prices[item] * cnt
        else:
            total +_ prices[item] * cnt

        r_ total

    ___ calculateItemDiscountedTotal  item, cnt, discount
        total _ 0
        nbrOfDiscounts _ cnt / discount.nbrItems
        total +_ nbrOfDiscounts * discount.price
        remaining _ cnt % discount.nbrItems
        total +_ remaining * prices[item]
        r_ total
