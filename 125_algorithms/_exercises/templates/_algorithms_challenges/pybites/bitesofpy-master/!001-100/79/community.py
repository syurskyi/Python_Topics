______ csv
from collections ______ Counter

______ requests

CSV_URL = 'https://bit.ly/2HiD2i8'


___ get_csv(
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as session:
        r_ session.get(CSV_URL).content.decode('utf-8')


___ create_user_bar_chart(content: str
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    reader = csv.DictReader(content.splitlines())
    counter = Counter()
    for row in reader:
        counter[row['tz']] += 1
    l = sorted(counter)
    for timezone in l:
        print(f'{timezone:25} | {"+" * counter[timezone]}')
