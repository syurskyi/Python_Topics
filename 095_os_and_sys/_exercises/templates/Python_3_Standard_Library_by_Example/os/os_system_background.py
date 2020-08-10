#!/usr/bin/env python3
"""Running a command in the background
"""

#end_pymotw_header
______ os
______ time

print('Calling...')
os.system('date; (sleep 3; date) &')

print('Sleeping...')
time.sleep(5)
