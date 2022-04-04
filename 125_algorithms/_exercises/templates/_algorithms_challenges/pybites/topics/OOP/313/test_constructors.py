_______ p__

____ constructors _______ Domain, DomainException


___ test_create_domain_from_name
    domain = Domain("google.com")
    ... s..(domain) __ "google.com"
    domain = Domain("nu.nl")
    ... s..(domain) __ "nu.nl"


___ test_invalid_domain
    w__ p__.r..(DomainException
        Domain("nu.nlll")


?p__.m__.p.("arg, expected", [
    ("https://pybit.es", "pybit.es"),
    ("http://pybit.es", "pybit.es"),
    ("https://pybit.es/get-python-source.html", "pybit.es"),
    ("https://nu.nl", "nu.nl"),
    ("https://python.org/", "python.org"),
    ("https://stackoverflow.com/a/14836456", "stackoverflow.com"),
])
___ test_create_domain_from_url(arg, e..
    domain = Domain.parse_url(arg)
    ... t..(domain) __ Domain
    ... s..(domain) __ e..


?p__.m__.p.("arg, expected", [
    ("bob@pybit.es", "pybit.es"),
    ("bob@gmail.com", "gmail.com"),
    ("tim@example.net", "example.net"),
    ("sara@hotmail.co.uk", "hotmail.co.uk"),
])
___ test_create_domain_from_email(arg, e..
    domain = Domain.parse_email(arg)
    ... t..(domain) __ Domain
    ... s..(domain) __ e..