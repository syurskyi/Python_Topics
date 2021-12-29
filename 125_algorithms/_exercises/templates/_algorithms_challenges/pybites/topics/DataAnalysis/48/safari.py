#import os
#import urllib.request

#TMP = os.getenv("TMP", "/tmp")
#DATA = 'safari.logs'
#SAFARI_LOGS = os.path.join(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

#urllib.request.urlretrieve(
#    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
#    SAFARI_LOGS
#)


___ create_chart():
    #count = 0
    with open('safari.logs', encoding="utf-8") as f:
        all_lines = f.readlines()
        lines = [line.rstrip() for line in all_lines]
        #print(len(lines))
        current_date = ''
        outstr = ''
        for line in range(len(lines)):
            #print(lines[line])
                __ '- sending to slack channel' in lines[line]:
                    first, second = str(lines[line-1]).split('root         DEBUG')
                    log_date = first[:5]
                    __ log_date != current_date:
                        print(outstr)
                        outstr = ''
                        outstr += log_date+' '
                    __ 'python' in second.lower():
                        outstr += PY_BOOK
                    else:
                        outstr += OTHER_BOOK
                    current_date = log_date
        __ outstr != '':
            print(outstr)

create_chart()