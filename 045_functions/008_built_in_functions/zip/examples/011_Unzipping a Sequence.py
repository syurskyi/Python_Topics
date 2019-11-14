pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
numbers
# (1, 2, 3, 4)
letters
# ('a', 'b', 'c', 'd')