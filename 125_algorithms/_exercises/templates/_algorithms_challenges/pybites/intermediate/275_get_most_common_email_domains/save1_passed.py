____ collections _______ Counter
____ bs4 _______ BeautifulSoup
_______ requests
_______ re

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


___ get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""

    response = requests.get(COMMON_DOMAINS)
    soup = BeautifulSoup(response.text, 'html.parser')
    right_table = soup.find('div', TARGET_DIV)

    domains    # list
    ___ row __ right_table.findAll('tr'):
        cells = row.findAll('td')
        domains.a..(cells[2].find(text=True))

    r.. domains


___ get_most_common_domains(emails, common_domains_ N..
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    __ common_domains __ N..
        common_domains = get_common_domains()

    l    # list
    ___ email __ emails:
        match = re.findall(r'@(\w+.\w+)', email)[0]
        __ match n.. __ get_common_domains():
            l.a..(match)

    r.. s..(l..(Counter(l).items()), r.._T..