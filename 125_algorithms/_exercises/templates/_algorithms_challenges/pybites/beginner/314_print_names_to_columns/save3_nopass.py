from typing import List  # not needed when we upgrade to 3.9


___ print_names_to_columns(names: List[str], cols: int = 2) -> None:
    name_list = [f'| {name:{10}}' for name in names]
    output = ''
    for i in range(0, len(name_list), cols):
        output += ' '.join(name_list[i: i + cols]) + '\n'
    print(output)
