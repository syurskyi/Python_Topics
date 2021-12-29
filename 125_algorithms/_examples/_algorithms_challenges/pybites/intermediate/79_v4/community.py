from collections import Counter
import csv
import requests


CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'
FMT_STR = '{tz:21}| {bar}'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    return requests.get(url=CSV_URL).content.decode()


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    rows = csv.DictReader(content.splitlines())
    counts = sorted(Counter([r['tz'] for r in rows]).items(),
                    key=lambda x: x[0])

    for c in counts:
        print(FMT_STR.format(tz=c[0], bar='+' * c[1]))
