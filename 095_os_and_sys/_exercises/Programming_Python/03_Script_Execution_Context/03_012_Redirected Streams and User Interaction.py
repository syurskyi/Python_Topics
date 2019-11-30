# C:\...\PP4E\System\Streams> python teststreams.py < input.txt | more
import more

if __name__ == '__main__': # when run, not when imported
    import sys
    if len(sys.argv) == 1: # page stdin if no cmd args
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())

# Hello stream world
# Enter a number>8 squared is 64
# Enter a number>6 squared is 36
# Enter a number>Bye
# ######################################################################################################################

from moreplus import more
more(open('adderSmall.py').read())
import sys
print(sum(int(line) for line in sys.stdin))
# C:\...\PP4E\System\Streams> python moreplus.py adderSmall.py

import sys
print(sum(int(line) for line in sys.stdin))
# C:\...\PP4E\System\Streams> python moreplus.py moreplus.py
# ######################################################################################################################

# import sys
# def getreply():
# ?n

#......\System\Streams> python teststreams.py < input.txt | python moreplus.py
# Hello stream world
# Enter a number>8 squared is 64
# Enter a number>6 squared is 36
# Enter a number>Bye