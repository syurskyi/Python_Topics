_______ c__
____ c.. _______ C..

_______ r__

CSV_URL 'https://bit.ly/2HiD2i8'


___ get_csv
    """Use requests to download the csv and return the
       decoded content"""
    w__ r__.S.. __ session:
        r.. session.g.. CSV_URL).content.d.. 'utf-8')


___ create_user_bar_chart(content: s..
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    reader c__.DictReader(content.s..
    counter C..()
    ___ row __ reader:
        counter[row 'tz']] += 1
    l s..(counter)
    ___ timezone __ l:
        print _*{timezone:25} | {"+" * counter[timezone]}')
