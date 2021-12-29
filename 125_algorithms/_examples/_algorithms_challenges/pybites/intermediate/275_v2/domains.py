from collections import Counter
import re
from bs4 import BeautifulSoup
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""

    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print('error in getting data')
        return []

    
    soup = BeautifulSoup(response.text)

    rows = soup.find(attrs=TARGET_DIV).find_all('tr')


    return [value.getText(strip=True) for row in rows for value in row.select('td:nth-child(3)')]


def get_domain(string):


    return re.search(r'@(.+)',string).group(1)


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()
        
    # your code
    c =  Counter(domain for domain in map(get_domain,emails) if domain not in common_domains).most_common()
    return c



if __name__ == "__main__":


    print(get_common_domains())
