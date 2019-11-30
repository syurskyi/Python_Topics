# C:\...\PP4E\System\Streams> type sorterSmall.py
import sys
for line in sorted(sys.stdin):
    print(line, end='')
# C:\...\PP4E\System\Streams> type adderSmall.py
# ######################################################################################################################

import sys
print(sum(int(line) for line in sys.stdin))