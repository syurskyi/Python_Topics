_______ itertools

rank = [str(i) ___ i __ r..(2,11)] + ['J', 'Q', 'K', 'A']
print(l..(rank))

suits = ['H', 'C', 'D', 'S']

deck = [card ___ card __ itertools.product(rank, suits)]
print(deck)

combinations = [combination ___ combination __ itertools.combinations(deck, 5)]

print(l..(combinations))