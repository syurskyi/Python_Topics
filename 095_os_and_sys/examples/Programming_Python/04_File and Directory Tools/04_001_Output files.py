# C:\temp> python
file = open('data.txt', 'w') # open output file object: creates
file.write('Hello file world!\n') # writes strings verbatim
# 18
# ######################################################################################################################

file.write('Bye file world.\n') # returns number chars/bytes written
# 18
# ######################################################################################################################

file.close() # closed on gc and exit too

# C:\temp> dir data.txt /B
# data.txt
# C:\temp> type data.txt
# Hello file world!
# Bye file world.
# ######################################################################################################################

open('somefile.txt', 'w').write("G'day Bruce\n") # write to temporary object
open('somefile.txt', 'r').read() # read from temporary object