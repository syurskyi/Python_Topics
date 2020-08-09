from collections ______ defaultdict
from datetime ______ datetime
______ shelve

from themoviedb ______ Movies, Tv, CACHE
from notifications ______ generate_mail_msg, mail_msg

SENT_CACHE = 'sent.shelve'

language = 'en'
num_pages = 3


___ update_store(
    mo = Movies()
    mo.get_now_playing()
    mo.get_upcoming()
    tv = Tv()
    tv.get_on_the_air()
    tv.get_popular()


___ load_store(
    items = defaultdict(lambda: defaultdict(list))

    with shelve.open(CACHE) as sh, shelve.open(SENT_CACHE) as ca:
        ___ key in sh:

            __ key in ca:
                continue
            ca[key] = datetime.utcnow()

            entry = sh[key]
            try:
                items[entry.kind][entry.listing].append(
                    entry)
            except:
                print(entry)

        r_ items


__ __name__ __ '__main__':
    update_store()
    items = load_store()
    content = generate_mail_msg(items)
    mail_msg(content)
