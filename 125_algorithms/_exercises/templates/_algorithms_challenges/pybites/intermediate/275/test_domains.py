_______ p__

____ domains _______ get_common_domains, get_most_common_domains


@p__.fixture(scope="module")
___ common_domains
    r.. l..(get_common_domains())


___ test_get_common_domains(common_domains):
    ... l..(common_domains) __ 100
    first_3 = ['gmail.com', 'yahoo.com', 'hotmail.com']
    last_3 = ['live.ca', 'aim.com', 'bigpond.net.au']
    ... common_domains[:3] __ first_3
    ... common_domains[-3:] __ last_3


@p__.mark.parametrize("emails, expected", [
    (["a@gmail.com", "b@pybit.es", "c@pybit.es", "d@domain.de"],
     [('pybit.es', 2), ('domain.de', 1)]),
    (["a@hotmail.com", "b@gmail.com"], []),
    (["a@hotmail.com", "b@hotmail.se",
      "c@paris.com", "d@paris.com", "e@hotmail.it"],
     [('paris.com', 2), ('hotmail.se', 1)]),
    (["a@gmail.es", "b@googlemail.com", "c@somedomain.com",
      "d@somedomain.com", "e@somedomain.com", "f@hotmail.fr"],
     [('somedomain.com', 3), ('gmail.es', 1)]),
])
___ test_get_most_common_domains(common_domains, emails, expected):
    ... get_most_common_domains(emails, common_domains) __ expected