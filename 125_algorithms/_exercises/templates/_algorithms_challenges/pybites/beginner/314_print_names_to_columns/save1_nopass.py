____ typing _______ List  # not needed when we upgrade to 3.9


___ print_names_to_columns(names: List[s..], cols: int = 2) -> N..
    name_list = [f'| {name:{9}}' ___ name __ names]
    output = ''
    ___ i __ r..(0, l..(name_list), cols):
        output += ' '.join(name_list[i: i + cols]) + '\n'

    print(output)