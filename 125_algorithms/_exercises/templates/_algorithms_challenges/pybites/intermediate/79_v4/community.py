____ collections _______ Counter
_______ csv
_______ requests


CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'
FMT_STR = '{tz:21}| {bar}'


___ get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    r.. requests.get(url=CSV_URL).content.decode()


___ create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    rows = csv.DictReader(content.splitlines())
    counts = s..(Counter([r['tz'] ___ r __ rows]).i..,
                    key=l.... x: x[0])

    ___ c __ counts:
        print(FMT_STR.f..(tz=c[0], bar='+' * c[1]))
