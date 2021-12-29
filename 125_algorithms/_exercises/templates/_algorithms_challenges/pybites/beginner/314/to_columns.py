____ typing _______ List  # not needed when we upgrade to 3.9

names = "Bob Julian Tim Sara Eva Ana Jake Maria".s..

___ print_names_to_columns(names: List[str], cols: int = 2) -> N..
    out_str = ''
    ___ index, name __ enumerate(names, start=1):
        out_str += '| {}'.format(name.ljust(10))
        __ n.. index%cols and index != l..(names):
            out_str += '\n'
    print(out_str)

print_names_to_columns(names, 4)

