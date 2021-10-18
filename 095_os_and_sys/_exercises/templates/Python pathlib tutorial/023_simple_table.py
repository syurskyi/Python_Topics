# When we work with files and directories, we can use PrettyTable module for nicer output.
# simple_table.py

# !/usr/bin/env python

from pathlib import Path
import datetime
from prettytable import PrettyTable

path = Path('C:/Users/Jano/Documents/')

pt = PrettyTable()
pt.field_names = ["File name", "Size", "Created"]

pt.align["File name"] = "l"
pt.align["Size"] = "r"
pt.align["Created"] = "l"

for e in path.glob('**/*.txt'):
    created = datetime.datetime.fromtimestamp(e.stat().st_ctime)
    size = e.stat().st_size
    pt.add_row([e.name, size, f"{created:%Y-%m-%d}"])

print(pt)

# The example displays all text files inside Documents in a nice table.The table contains three columns: file name, size, and creation date.
#
# $ simple_table.py
# +-------------------------------------------------------+-------+------------+
# | File
# name | Size | Created |
# +-------------------------------------------------------+-------+------------+
# | data.txt | 0 | 2019 - 02 - 27 |
# | eternal_return.txt | 10467 | 2019 - 03 - 03 |
# | potvrdenie.txt | 773 | 2019 - 01 - 14 |
# | text_processing.txt | 750 | 2019 - 02 - 18 |
# | website - inspire.txt | 62 | 2019 - 03 - 03 |
# | words.txt | 31 | 2018 - 12 - 30 |
# | Úvod
# do
# Symfony.txt | 7613 | 2019 - 03 - 04 |
# | robots.txt | 240 | 2019 - 01 - 01 |
# | robots.txt | 240 | 2019 - 02 - 03 |
# ...
#
# This is a sample partial output. In this tutorial, we have covered the standard Python pathlib module.