____ c.. _______ Counter
_______ __
____ bs4 _______ BeautifulSoup
_______ requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


___ get_common_domains(url=COMMON_DOMAINS
    """Scrape the url return the 100 most common domain names"""

    ___
        response = requests.get(url)
        response.raise_for_status()
    ______:
        print('error in getting data')
        r.. []

    
    soup = BeautifulSoup(response.text)

    rows = soup.find(attrs=TARGET_DIV).find_all('tr')


    r.. [value.getText(strip=T..) ___ row __ rows ___ value __ row.select('td:nth-child(3)')]


___ get_domain(s__


    r.. __.s..(r'@(.+)',s__).group(1)


___ get_most_common_domains(emails, common_domains_ N..
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    __ common_domains __ N..
        common_domains = get_common_domains()
        
    # your code
    c =  Counter(domain ___ domain __ map(get_domain,emails) __ domain n.. __ common_domains).most_common()
    r.. c



__ _______ __ _______


    print(get_common_domains
