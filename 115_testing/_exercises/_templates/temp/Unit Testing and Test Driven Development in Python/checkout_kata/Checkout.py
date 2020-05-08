
c_ Checkout:
    c_ Discount:
        ___  -   nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    ___  - (self):
        self.prices = {}
        self.discounts = {}
        self.items = {}


    ___ addDiscount  item, nbrOfItems, price):
        discount = self.Discount(nbrOfItems, price)
        self.discounts[item] = discount


    ___ addItemPrice  item, price):
        self.prices[item] = price

    ___ addItem  item):
        if item not in self.prices:
            raise Exception("Bad Item")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    ___ calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    ___ calculateItemTotal  item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.nbrItems:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total

    ___ calculateItemDiscountedTotal  item, cnt, discount):
        total = 0
        nbrOfDiscounts = cnt / discount.nbrItems
        total += nbrOfDiscounts * discount.price
        remaining = cnt % discount.nbrItems
        total += remaining * self.prices[item]
        return total
