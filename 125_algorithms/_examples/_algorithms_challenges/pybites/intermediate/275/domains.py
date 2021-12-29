from collections import Counter

import bs4
import requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    soup_content = soup.find(class_="content")
    soup_table = soup_content.find(class_="middle_info_noborder")
    soup_row = soup_table.find_all("tr")
    return [row.select("td td td")[2].get_text() for row in soup_row]


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    most_common_prep = []
    for email in emails:
        domain = email.split("@")[1]
        if domain in common_domains:
            continue
        else:
            most_common_prep.append(domain)

    most_common = Counter(most_common_prep)
    return most_common.most_common(2)


if __name__ == "__main__":
    #get_common_domains()
    get_most_common_domains(["a@gmail.es", "b@googlemail.com", "c@somedomain.com", "d@somedomain.com", "e@somedomain.com", "f@hotmail.fr"])