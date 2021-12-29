____ typing _______ List  # not needed when we upgrade to 3.9


___ print_names_to_columns(names: List[s..], cols: int = 2) -> N..
    x    # list
    ___ name __ names:
        __ names.index(name) % cols:
            x.a..(f'| {name:{10}}' + '\n')
        ____:
            x.a..(f'| {name:{10}}')

    print(''.join(x))