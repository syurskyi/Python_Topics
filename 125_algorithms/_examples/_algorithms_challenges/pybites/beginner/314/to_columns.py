from typing import List  # not needed when we upgrade to 3.9

names = "Bob Julian Tim Sara Eva Ana Jake Maria".split()

def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    out_str = ''
    for index, name in enumerate(names, start=1):
        out_str += '| {}'.format(name.ljust(10))
        if not index%cols and index != len(names):
            out_str += '\n'
    print(out_str)

print_names_to_columns(names, 4)

