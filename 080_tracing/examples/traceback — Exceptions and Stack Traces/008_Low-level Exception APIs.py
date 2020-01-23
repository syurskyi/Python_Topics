# To process the traceback in some other way, such as formatting it differently, use extract_tb() to get the data in a usable form.
#
# traceback_extract_tb.py

import traceback
import sys
import os
from traceback_example import produce_exception

template = '{filename:<23}:{linenum}:{funcname}:\n    {source}'

try:
    produce_exception()
except Exception as err:
    print('format_exception():')
    exc_type, exc_value, exc_tb = sys.exc_info()
    for tb_info in traceback.extract_tb(exc_tb):
        filename, linenum, funcname, source = tb_info
        if funcname != '<module>':
            funcname = funcname + '()'
        print(template.format(
            filename=os.path.basename(filename),
            linenum=linenum,
            source=source,
            funcname=funcname)
        )

# The return value is a list of entries from each level of the stack represented by the traceback. Each entry is a tuple with four parts: the name of the source file, the line number in that file, the name of the function, and the source text from that line with whitespace stripped (if the source is available).
#
# $ python3 traceback_extract_tb.py
#
# format_exception():
# traceback_extract_tb.py:18:<module>:
#     produce_exception()
# traceback_example.py   :17:produce_exception():
#     produce_exception(recursion_level - 1)
# traceback_example.py   :17:produce_exception():
#     produce_exception(recursion_level - 1)
# traceback_example.py   :19:produce_exception():
#     raise RuntimeError()