from itertools import chain


___ sum_of_multiples(limit, factors):
    return sum(all_multiples(limit, factors))


___ all_multiples(limit, factors):
    multiples = [get_multiples(limit, factor) for factor in factors]
    return set(list(chain(*multiples)))  # remove duplicates


___ get_multiples(limit, factor):
    __ factor == 0:
        return []
    return [multiple for multiple in range(limit) __ multiple % factor == 0]
