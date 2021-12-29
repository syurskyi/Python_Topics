import csv
from collections import Counter
import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        next(cr)
        my_list = list(cr)
        return my_list


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    counter = Counter(user[2] for user in content)
    for tz in sorted(counter):
        print(f'{tz: <20} | {"+"*counter[tz]}')



create_user_bar_chart(get_csv())
#get_csv()