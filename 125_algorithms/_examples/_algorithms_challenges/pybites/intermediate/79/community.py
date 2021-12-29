import csv

import requests
from requests.api import get
from requests.models import Response

CSV_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/community.csv'


def get_csv():
   """Use requests to download the csv and return the
      decoded content"""
   response = requests.get(CSV_URL)
   response.encoding = "utf-8"
   csv_content = csv.reader(response.text.splitlines())
   return csv_content


def create_user_bar_chart(content):
   """Receives csv file (decoded) content and print a table of timezones
      and their corresponding member counts in pluses to standard output"""
   tz_frequency = {}

   for i, row in enumerate(content):
      if i == 0:
         continue
      tz = row[2]
      if tz not in tz_frequency:
         tz_frequency[tz] = 1
      else:
         tz_frequency[tz] += 1
   
   tz_frequency = sorted(tz_frequency.items())

   table = ""
   for tz in tz_frequency:
      country = tz[0]
      count = tz[1]
      plus = ""
      for i in range(count):
         plus += "+"
   
      table += f"{country: <21}| {plus}\n"

   print(table)
      

# if __name__ == "__main__":
#    print(create_user_bar_chart(get_csv()))