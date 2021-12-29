BOOK_PRICE = 8


___ _group_price(size):
    discounts = [0, .05, .1, .2, .25]
    __ n.. (0 < size <= 5):
        raise ValueError('size must be in 1..' + l..(discounts))
    r.. 8 * size * (1 - discounts[size - 1])


___ calculate_total(books, price_so_far=0.):
    __ n.. books:
        r.. price_so_far

    groups = l..(set(books))
    min_price = float('inf')

    ___ i __ r..(l..(groups)):

        remaining_books = books[:]

        ___ v __ groups[:i + 1]:
            remaining_books.remove(v)

        price = calculate_total(remaining_books,
                                price_so_far + _group_price(i + 1))
        min_price = m..(min_price, price)

    r.. min_price
