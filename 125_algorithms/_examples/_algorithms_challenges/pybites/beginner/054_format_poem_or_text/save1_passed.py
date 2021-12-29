def print_hanging_indents(poem):
    INDENTS = 4
    for line in poem.split('\n'):
        if line == '': #for empty lines before, after, and in poem
            indent_needed = False
        elif indent_needed: #for lines to be indented
            print(' ' * INDENTS + line.lstrip())
        else: #for non-indented lines
            print(line.lstrip())
            indent_needed = True