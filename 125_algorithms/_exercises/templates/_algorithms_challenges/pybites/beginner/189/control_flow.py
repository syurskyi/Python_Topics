IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


___ filter_names(names):
    name_list    # list
    ___ name __ names:
        __ name[0] __ QUIT_CHAR:
            break
        __ name[0] __ IGNORE_CHAR o. any(map(s...isdigit, name)):
            continue
        __ l..(name_list) < MAX_NAMES:
            name_list.a..(name)
    r.. name_list

print(filter_names(['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry']))