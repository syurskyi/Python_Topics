# Each Path instance includes methods for working with the contents of the file to which it refers. For immediately retrieving the contents, use read_bytes() or read_text(). To write to the file, use write_bytes() or write_text(). Use the open() method to open the file and retain the file handle, instead of passing the name to the built-in open() function.
# pathlib_read_write.py
#
# import pathlib
#
# f = pathlib.Path('example.txt')
#
# f.write_bytes('This is the content'.encode('utf-8'))
#
# with f.open('r', encoding='utf-8') as handle:
#     print('read from open(): {!r}'.format(handle.read()))
#
# print('read_text(): {!r}'.format(f.read_text('utf-8')))
#
# The convenience methods do some type checking before opening the file and writing to it, but otherwise they are equivalent to doing the operation directly.
#
# $ python3 pathlib_read_write.py
#
# read from open(): 'This is the content'
# read_text(): 'This is the content'


