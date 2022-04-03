_______ __
_______ u__.r..
_______ __

TMP = __.getenv("TMP", "/tmp")
DATA = 'safari.logs'
SAFARI_LOGS = __.p...j..(TMP, DATA)
PY_BOOK, OTHER_BOOK = '🐍', '.'

u__.r...u..(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


___ create_chart

    current_date = N..
    w__ o.. SAFARI_LOGS _ __ f:
        ___ line __ f:
            
            __ 'sending to slack channel' __ line:
                space_index = line.index(' ')
                date = line[:space_index]
                __ date != current_date:
                    __ current_date:
                        print()
                    current_date = date
                    print(date,end=' ')
                __ __.s..(r'python',previous_line,flags=__.I
                    char = PY_BOOK
                ____:
                    char = OTHER_BOOK
                print(char,end='')
            
            previous_line = line



__ _______ __ _______

    create_chart()
