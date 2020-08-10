#!/usr/bin/env python3
# encoding: utf-8
#
# Copyright (c) 2016 Doug Hellmann.  All rights reserved.
# Written for https://pymotw.com
#
"""pathlib types
"""

#end_pymotw_header
______ itertools
______ __
______ pathlib

root _ pathlib.Path('test_files')

# Clean up from previous runs.
__ root.e..():
    ___ f __ root.iterdir():
        f.u..()
____
    root.mkdir()

# Create test files
(root / 'file').write_text(
    'This is a regular file', encoding_'utf-8')
(root / 'symlink').symlink_to('file')
__.mkfifo(str(root / 'fifo'))

# Check the file types
to_scan _ itertools.chain(
    root.iterdir(),
    [pathlib.Path('/dev/disk0'),
     pathlib.Path('/dev/console')],
)
hfmt _ '{:18s}' + ('  {:>5}' * 6)
print(hfmt.f..('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block',
                  'Character'))
print()

fmt _ '{:20s}  ' + ('{!r:>5}  ' * 6)
___ f __ to_scan:
    print(fmt.f..(
        str(f),
        f.is_file(),
        f.is_dir(),
        f.is_symlink(),
        f.is_fifo(),
        f.is_block_device(),
        f.is_char_device(),
    ))
