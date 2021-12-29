IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    name_list = []
    for name in names:
        if name[0] == QUIT_CHAR:
            break
        if name[0] == IGNORE_CHAR or any(map(str.isdigit, name)):
            continue
        if len(name_list) < MAX_NAMES:
            name_list.append(name)
    return name_list

print(filter_names(['tim', 'amber', 'ana', 'c1ndy', 'sara', 'molly', 'henry']))