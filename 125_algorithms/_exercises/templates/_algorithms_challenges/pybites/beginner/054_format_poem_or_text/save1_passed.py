___ print_hanging_indents(poem):
    INDENTS = 4
    ___ line __ poem.split('\n'):
        __ line __ '': #for empty lines before, after, and in poem
            indent_needed = False
        ____ indent_needed: #for lines to be indented
            print(' ' * INDENTS + line.lstrip())
        ____: #for non-indented lines
            print(line.lstrip())
            indent_needed = True