# bytesgen.py
#
# An example of chaining together different generators into a processing
# pipeline.    

from genfind ______ *
from genopen ______ *
from gencat ______ *
from gengrep ______ *

pat    = r'ply-.*\.gz'
logdir = 'www'

filenames = gen_find("access-log*",logdir)
logfiles  = gen_open(filenames)
loglines  = gen_cat(logfiles)
patlines  = gen_grep(pat,loglines)
bytecol   = (line.rs..(N..,1)[1] ___ line __ patlines)
bytes_sent= (in.(x) ___ x __ bytecol __ x != '-')

print("Total", su.(bytes_sent))

