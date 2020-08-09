INDENTS = 4


___ print_hanging_indents(poem
    indent = False
    for line in poem.splitlines(
        l = line.strip()
        __ le.(l) __ 0:
            indent = False
            continue
        __ indent:
            print(f'{" " * INDENTS}{l}')
        ____
            print(f'{l}')
            indent = True
