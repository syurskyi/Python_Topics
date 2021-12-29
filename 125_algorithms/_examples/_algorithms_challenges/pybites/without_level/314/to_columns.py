from typing import List  # not needed when we upgrade to 3.9
from itertools import zip_longest


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    names = list(map(lambda x: f'| {x:10}', names))
    groups = zip_longest(*[iter(names)] * cols, fillvalue='')
    for group in groups:
        print(''.join(group))
