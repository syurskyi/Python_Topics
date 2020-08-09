from collections ______ namedtuple
from functools ______ wraps
______ re
______ shelve

CACHE = 'items.shelve'
DEFAULT_OVERWRITE = False

Item = namedtuple('Item', 'id kind title genres overview poster')


___ _get_title(item
    # movies API uses 'title', series API uses 'name'
    title = item.get('title')

    __ not title:
        title = item.get('name')

    r_ title


___ _store(kind, resp, overwrite=DEFAULT_OVERWRITE
    with shelve.open(CACHE) as sh:
        ___ item in resp:
            key = str(item['id'])

            __ overwrite and key in sh:
                del sh[key]

            title = _get_title(item)
            __ not title:
                continue

            item = Item(id=item['id'],
                        kind=kind,
                        title=title,
                        genres=item['genre_ids'],
                        overview=item['overview'],
                        poster=item['poster_path'])

            sh[key] = item


___ store_results(f
    @wraps(f)
    ___ wrapped(*args, **kwargs
        func_name = str(args[1]).lower()
        kind = re.sub(r'.*bound.*?\.(\S+) of.*', r'\1', func_name)
        print(kind)
        resp = f(*args, **kwargs)
        _store(kind, resp)
        print(le.(resp))
        r_ resp
    r_ wrapped
