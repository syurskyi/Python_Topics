# -*- coding: utf-8 -*-

import re

email = "test@mail.ru"
p = re.compile(r"""(?P<name>[a-z0-9_.-]+) # Название ящика
        @                                     # Символ "@"
        (?P<host>(?:[a-z0-9-]+\.)+[a-z]{2,6}) # Домен
        """, re.I | re.VERBOSE)
r = p.search(email)
r.group("name")                           # Название ящика
# 'test'
r.group("host")                           # Домен
# 'mail.ru'