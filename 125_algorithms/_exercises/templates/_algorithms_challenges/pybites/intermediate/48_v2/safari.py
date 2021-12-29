import os
import urllib.request
import re

TMP = os.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


___ create_chart():

    current_date = None
    with open(SAFARI_LOGS,'r') as f:
        for line in f:
            
            __ 'sending to slack channel' in line:
                space_index = line.index(' ')
                date = line[:space_index]
                __ date != current_date:
                    __ current_date:
                        print()
                    current_date = date
                    print(date,end=' ')
                __ re.search(r'python',previous_line,flags=re.I):
                    char = PY_BOOK
                else:
                    char = OTHER_BOOK
                print(char,end='')
            
            previous_line = line



__ __name__ == "__main__":

    create_chart()
