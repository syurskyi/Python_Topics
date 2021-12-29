____ typing _______ List  # not needed when we upgrade to 3.9
____ itertools _______ zip_longest


___ print_names_to_columns(names: List[str], cols: int = 2) -> N..
    names = l..(map(l.... x: f'| {x:10}', names))
    groups = zip_longest(*[iter(names)] * cols, fillvalue='')
    ___ group __ groups:
        print(''.join(group))
