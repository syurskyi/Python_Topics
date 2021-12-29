import csv
import pandas as pd
from io import StringIO
import requests

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""


    response =requests.get(CSV_URL)


    return response.text













def create_user_bar_chart(content):
    """Receives csv file (decoded) content and print a table of timezones
       and their corresponding member counts in pluses to standard output
    """
    


    
    data = pd.read_csv(StringIO(content))
    

    max_length = data.tz.str.len().max()

    counts = data.tz.value_counts().sort_index()



    for tz,count  in counts.items():
        print(f"{tz:<{max_length + 1}}| {'+' * count}")










if __name__ == "__main__":


    content = get_csv()

    create_user_bar_chart(content)
