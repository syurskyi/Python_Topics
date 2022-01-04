____ typing _______ List  # not needed when we upgrade to 3.9


___ print_names_to_columns(names: List[s..], cols: i.. = 2) __ N..
    name_list = [f'| {name:{10}}' ___ name __ names]

    breaks    # list
    ___ i __ r..(0, l..(names), cols):
        breaks.a.. _*| {names[i]:{10}}')

    output = ''
    __ cols __ 1:
        ___ entry __ name_list:
            output += ''.j..(entry) + '\n'
    __ cols != 1:
        breaks.pop(0)
        ___ entry __ name_list:
            __ entry __ breaks:
                output += '\n' + ''.j..(entry)
            ____:
                output += ''.j..(entry)

    print(output)
