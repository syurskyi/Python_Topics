INDENTS = 4


___ print_hanging_indents(poem):
    indent = F..
    ___ line __ poem.splitlines():
        l = line.s..
        __ l..(l) __ 0:
            indent = F..
            continue
        __ indent:
            print(f'{" " * INDENTS}{l}')
        ____:
            print(f'{l}')
            indent = T..
