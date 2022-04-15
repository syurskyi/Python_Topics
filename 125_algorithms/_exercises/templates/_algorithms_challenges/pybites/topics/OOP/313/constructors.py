_______ __


c_ DomainException(E..
    """Raised when an invalid is created."""


c_ Domain:

    ___ - , name
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        name name
        __ n.. __.m.. _ .*\.[a-z]{2,3}$', name
            r.. DomainException
        
    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively

    ??
    ___ parse_url(cls, url
        url_domain __.f.. _ (?:^https?:\/\/([^\/]+)(?:[\/,]|$)|^(.*)$)", url)
        r.. Domain(url_domain 0 0 )

    ??
    ___ parse_email(cls, email
        email_domain __.f.. _ @(.*\.[a-z]+)', email)
        r.. Domain(email_domain 0

    ___ -s(self) __ s..
        r.. _* name}'

print(Domain.parse_url('http://www.khooville.com'
#print(Domain.parse_email('sckhoo@khooville.com'))
