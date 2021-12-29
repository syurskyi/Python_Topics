INDENTS = 4


___ print_hanging_indents(poem):
    indent = False
    ___ line __ poem.splitlines():
        l = line.s..
        __ l..(l) __ 0:
            indent = False
            continue
        __ indent:
            print(f'{" " * INDENTS}{l}')
        ____:
            print(f'{l}')
            indent = True
