 # The following example is a practical program which outputs the contents of the specified directory in a hierarchical tree structure.
# tree.py

#!/usr/bin/env python

____ p.. ______ P__

___ tree(directory):

    print(f'+ {directory}')

    ___ path __ sorted(directory.rglob('*')):

        depth = len(path.relative_to(directory).parts)
        spacer = '    ' * depth

        # print(f'{spacer}+ {path.name}')

        __ path.is_file():
            print(f'{spacer}f {path.name}')
        else:
            print(f'{spacer}d {path.name}')

path = P__.home() / 'Downloads'

tree(path)

# The program outputs the contents of the Downloads directory in a tree structure.