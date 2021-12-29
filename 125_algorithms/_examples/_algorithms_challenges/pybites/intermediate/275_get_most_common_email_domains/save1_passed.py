from collections import Counter
from bs4 import BeautifulSoup
import requests
import re

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""

    response = requests.get(COMMON_DOMAINS)
    soup = BeautifulSoup(response.text, 'html.parser')
    right_table = soup.find('div', TARGET_DIV)

    domains = []
    for row in right_table.findAll('tr'):
        cells = row.findAll('td')
        domains.append(cells[2].find(text=True))

    return domains


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    l = []
    for email in emails:
        match = re.findall(r'@(\w+.\w+)', email)[0]
        if match not in get_common_domains():
            l.append(match)

    return sorted(list(Counter(l).items()), reverse=True)