from copy ______ deepcopy

___ calculate_total(books
    groups = []
    ___ book in books:
        cheap_group = None
        groups.append([])
        ___ g, group in enumerate(groups
            __ book not in group:
                new_groups = deepcopy(groups)
                new_groups[g].append(book)
                cheap_group = min(new_groups, cheap_group or new_groups, key=_cost)
        groups = [g ___ g in cheap_group __ le.(g) > 0]
    r_ _cost(groups)


___ _cost(groups
    BOOKCOST = 800
    discounts = {n_books: n_books * BOOKCOST * discount ___
            n_books, discount in enumerate((0, 1, 0.95, 0.90, 0.80, 0.75))}
    r_ su.(discounts.get(le.(group)) ___ group in groups)
