# -*- coding: utf-8 -*-
import urllib.error
import urllib.request

from functools import lru_cache


@lru_cache(maxsize=24)
def get_webpage(module):
    """
    Поиск странице модуля
    """
    webpage = "https://docs.python.org/3/library/{}.html".format(module)

    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None


if __name__ == '__main__':
    modules = ['functools', 'collections', 'os', 'sys']
    for module in modules:
        page = get_webpage(module)

        if page:
            print("{} страница модуля найдена!".format(module))