____ t___ _______ L..  # not needed when we upgrade to 3.9

names = "Bob Julian Tim Sara Eva Ana Jake Maria".s..

___ print_names_to_columns(names: L..[s..], cols: i.. = 2) __ N..
    out_str = ''
    ___ index, name __ e..(names, start=1
        out_str += '| {}'.f..(name.ljust(10))
        __ n.. index%cols a.. index != l..(names
            out_str += '\n'
    print(out_str)

print_names_to_columns(names, 4)

