# -*- coding: utf-8 -*-

# Лямдба-выражения позволяют нам превратить следующий код:

colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]

def normalize_case(string):
    return string.casefold()


normalized_colors = map(normalize_case, colors)

# Вот в такой код:


colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]

normalized_colors = map(lambda s: s.casefold(), colors)