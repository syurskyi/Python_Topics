_______ csv
____ collections _______ Counter

_______ requests

CSV_URL = 'https://bit.ly/2HiD2i8'


___ get_csv
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() __ session:
        r.. session.get(CSV_URL).content.decode('utf-8')


___ create_user_bar_chart(content: s..):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    reader = csv.DictReader(content.splitlines())
    counter = Counter()
    ___ row __ reader:
        counter[row['tz']] += 1
    l = s..(counter)
    ___ timezone __ l:
        print(f'{timezone:25} | {"+" * counter[timezone]}')
