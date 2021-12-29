from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    name_list = [f'| {name:{10}}' for name in names]

    breaks = []
    for i in range(0, len(names), cols):
        breaks.append(f'| {names[i]:{10}}')

    output = ''
    if cols == 1:
        for entry in name_list:
            output += ''.join(entry) + '\n'
    if cols != 1:
        breaks.pop(0)
        for entry in name_list:
            if entry in breaks:
                output += '\n' + ''.join(entry)
            else:
                output += ''.join(entry)

    print(output)
