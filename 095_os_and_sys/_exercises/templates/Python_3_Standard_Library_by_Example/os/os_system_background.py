#!/usr/bin/env python3
"""Running a command in the background
"""

#end_pymotw_header
______ __
______ time

print('Calling...')
__.system('date; (sleep 3; date) &')

print('Sleeping...')
time.sleep(5)
