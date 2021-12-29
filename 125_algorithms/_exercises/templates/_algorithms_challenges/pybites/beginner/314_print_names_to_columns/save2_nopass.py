from typing import List  # not needed when we upgrade to 3.9


___ print_names_to_columns(names: List[str], cols: int = 2) -> None:
    x = []
    for name in names:
        __ names.index(name) % cols:
            x.append(f'| {name:{10}}' + '\n')
        else:
            x.append(f'| {name:{10}}')

    print(''.join(x))