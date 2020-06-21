 # Content management systems often put their newly created articles in directory structure based on the current year and month. The next example demonstrates this.
# new_article.py

#!/usr/bin/env python

from pathlib import Path
import datetime

now = datetime.datetime.now()
year = now.year
month = now.month

name = input('Enter article name:')

path1 = Path('articles') / str(year) / str(month)
path1.mkdir(parents=True)

path2 = path1 /  f'{name}.txt'

path2.touch()

print(f'Article created at: {path2}')

# The program ask an input from the users. It creates a new text file based on the current year and month.