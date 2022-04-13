____ c.. _______ C..
____ ___ _______ B..
_______ r__
_______ __

COMMON_DOMAINS ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV {"class": "middle_info_noborder"}


___ get_common_domains(url=COMMON_DOMAINS
    """Scrape the url return the 100 most common domain names"""

    response r__.g.. COMMON_DOMAINS)
    soup B..(response.text, 'html.parser')
    right_table ?.f.. 'div', TARGET_DIV)

    domains    # list
    ___ row __ right_table.findAll('tr'
        cells row.findAll('td')
        domains.a..(cells[2].f.. text=T..

    r.. domains


___ get_most_common_domains(emails, common_domains_ N..
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    __ common_domains __ N..
        common_domains get_common_domains()

    l    # list
    ___ email __ emails:
        m.. __.f.. _ @(\w+.\w+)', email)[0]
        __ m.. n.. __ get_common_domains
            l.a..(m..)

    r.. s..(l..(C..(l).i.., r.._T..