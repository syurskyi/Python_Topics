import itertools

rank = [str(i) for i in range(2,11)] + ['J', 'Q', 'K', 'A']
print(len(rank))

suits = ['H', 'C', 'D', 'S']

deck = [card for card in itertools.product(rank, suits)]
print(deck)

combinations = [combination for combination in itertools.combinations(deck, 5)]

print(len(combinations))