____ typing _______ List  # not needed when we upgrade to 3.9


___ print_names_to_columns(names: List[str], cols: int = 2) -> N..
    name_list = [f'| {name:{10}}' ___ name __ names]

    breaks    # list
    ___ i __ r..(0, l..(names), cols):
        breaks.a..(f'| {names[i]:{10}}')

    output = ''
    __ cols __ 1:
        ___ entry __ name_list:
            output += ''.join(entry) + '\n'
    __ cols != 1:
        breaks.pop(0)
        ___ entry __ name_list:
            __ entry __ breaks:
                output += '\n' + ''.join(entry)
            ____:
                output += ''.join(entry)

    print(output)
