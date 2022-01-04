____ typing _______ List  # not needed when we upgrade to 3.9
____ i.. _______ zip_longest


___ print_names_to_columns(names: List[s..], cols: i.. = 2) __ N..
    names = l..(map(l.... x: f'| {x:10}', names))
    groups = zip_longest(*[i..(names)] * cols, fillvalue='')
    ___ group __ groups:
        print(''.j..(group))
