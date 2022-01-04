_______ __


c_ DomainException(Exception):
    """Raised when an invalid is created."""


c_ Domain:

    ___ - , name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        name = name
        __ n.. __.m..(r'.*\.[a-z]{2,3}$', name):
            raise DomainException
        
    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively

    @classmethod
    ___ parse_url(cls, url):
        url_domain = __.findall(r"(?:^https?:\/\/([^\/]+)(?:[\/,]|$)|^(.*)$)", url)
        r.. Domain(url_domain[0][0])

    @classmethod
    ___ parse_email(cls, email):
        email_domain = __.findall(r'@(.*\.[a-z]+)', email)
        r.. Domain(email_domain[0])

    ___ __str__(self) -> s..:
        r.. f'{name}'

print(Domain.parse_url('http://www.khooville.com'))
#print(Domain.parse_email('sckhoo@khooville.com'))
