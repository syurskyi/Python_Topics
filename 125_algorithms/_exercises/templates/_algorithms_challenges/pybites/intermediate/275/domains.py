____ collections _______ Counter

_______ bs4
_______ requests

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


___ get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    soup_content = soup.find(class_="content")
    soup_table = soup_content.find(class_="middle_info_noborder")
    soup_row = soup_table.find_all("tr")
    r.. [row.select("td td td")[2].get_text() ___ row __ soup_row]


___ get_most_common_domains(emails, common_domains_ N..
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    __ common_domains __ N..
        common_domains = get_common_domains()

    most_common_prep    # list
    ___ email __ emails:
        domain = email.s..("@")[1]
        __ domain __ common_domains:
            continue
        ____:
            most_common_prep.a..(domain)

    most_common = Counter(most_common_prep)
    r.. most_common.most_common(2)


__ __name__ __ "__main__":
    #get_common_domains()
    get_most_common_domains(["a@gmail.es", "b@googlemail.com", "c@somedomain.com", "d@somedomain.com", "e@somedomain.com", "f@hotmail.fr"])