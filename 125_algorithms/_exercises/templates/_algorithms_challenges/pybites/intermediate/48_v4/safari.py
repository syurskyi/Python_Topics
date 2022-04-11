_______ __
_______ __
_______ u__.r..
____ c.. _______ d..
____ d__ _______ d__

TMP __.g.. TMP  /tmp
DATA 'safari.logs'
SAFARI_LOGS __.p...j..(TMP, DATA)
PY_BOOK, OTHER_BOOK '🐍', '.'

u__.r...u..(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
    SAFARI_LOGS
)


___ _parse_book_line(line
    """returns a dict representing the line"""
    out_dict d..()
    date __.f.. _*_ 0-9]{2}-[0-9]{2})', line)[0]
    out_dict 'date'  = d__.s..(date, '%m-%d')
    out_dict 'title'  = __.f..(r'DEBUG.*- (.*)', line)[0]
    r.. out_dict


___ create_chart

    chart d..(s..)
    w__ o.. SAFARI_LOGS, _ __ f:
        prev f.readline()
        ___ line __ f:
            __ 'sending to slack channel' __ line:
                detail _parse_book_line(prev)
                char PY_BOOK __ 'python' __ detail 'title' .l.. ____ '.'
                chart[detail 'date']] += char

            prev line

    ___ key __ s..(chart.k..
        print('{} {}'.f..(key.s..('%m-%d'), chart[key]
