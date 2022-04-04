____ t___ _______ List  # not needed when we upgrade to 3.9


___ print_names_to_columns(names: List[s..], cols: i.. = 2) __ N..
    name_list = [f'| {name:{10}}' ___ name __ names]
    output = ''
    ___ i __ r..(0, l..(name_list), cols
        output += ' '.j..(name_list[i: i + cols]) + '\n'
    print(output)
