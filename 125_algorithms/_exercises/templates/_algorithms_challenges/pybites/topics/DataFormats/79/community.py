_______ csv
____ collections _______ Counter
_______ requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


___ get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        next(cr)
        my_list = l..(cr)
        r.. my_list


___ create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    counter = Counter(user[2] ___ user __ content)
    ___ tz __ s..(counter):
        print(f'{tz: <20} | {"+"*counter[tz]}')



create_user_bar_chart(get_csv())
#get_csv()