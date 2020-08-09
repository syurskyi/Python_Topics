from collections ______ namedtuple
from functools ______ wraps
______ re
______ shelve

CACHE = 'items.shelve'
DEFAULT_OVERWRITE = True

Item = namedtuple('Item', 'id kind listing title genres overview release_date poster')  # noqa E501


___ _get_title(item
    # movies API uses 'title', series API uses 'name'
    title = item.get('title')

    __ not title:
        title = item.get('name')

    r_ title


___ _get_release_date(item
    # movies API uses 'release_date', series API uses 'first_air_date'
    release_date = item.get('release_date')

    __ not release_date:
        release_date = item.get('first_air_date')

    r_ release_date


___ _store(kind, listing, resp, overwrite=DEFAULT_OVERWRITE
    with shelve.open(CACHE) as sh:
        ___ item in resp:
            key = str(item['id'])

            __ overwrite and key in sh:
                del sh[key]

            title = _get_title(item)
            __ not title:
                continue

            release_date = _get_release_date(item)
            __ not release_date:
                continue

            item = Item(id=item['id'],
                        kind=kind,
                        listing=listing,
                        title=title,
                        genres=item['genre_ids'],
                        overview=item['overview'],
                        release_date=release_date,
                        poster=item['poster_path'])

            sh[key] = item


___ store_results(f
    @wraps(f)
    ___ wrapped(*args, **kwargs
        class_name = str(args[0]).lower()
        kind = re.sub(r'.*\.(\S+)\sobject.*', r'\1', class_name)
        print(kind)
        func_name = str(args[1]).lower()
        listing = re.sub(r'.*bound.*?\.(\S+) of.*', r'\1', func_name)
        print(listing)
        resp = f(*args, **kwargs)
        _store(kind, listing, resp)
        print(le.(resp))
        r_ resp
    r_ wrapped
