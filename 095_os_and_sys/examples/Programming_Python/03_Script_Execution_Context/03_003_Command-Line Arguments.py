import sys
sys.argv
# ['']

import sys
print(sys.argv)

# C:\...\PP4E\System> python testargv.py
# ['testargv.py']
# C:\...\PP4E\System> python testargv.py spam eggs cheese
# ['testargv.py', 'spam', 'eggs', 'cheese']
# C:\...\PP4E\System> python testargv.py -i data.txt -o results.txt
# ['testargv.py', '-i', 'data.txt', '-o', 'results.txt']