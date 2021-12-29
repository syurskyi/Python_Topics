_______ random


class TinyUrl2:
    ___ __init__(self):
        self.chars = [str(i) ___ i __ r..(10)]
        self.chars.extend(chr(i) ___ i __ r..(ord('a'), ord('z') + 1))
        self.chars.extend(chr(i) ___ i __ r..(ord('A'), ord('Z') + 1))

        self.host = 'http://tiny.url/'
        self.size = 6
        self.lg2st = {}
        self.st2lg = {}

        self.custom_lg2st = {}
        self.custom_st2lg = {}

    ___ createCustom(self, url, key):
        """
        :type url: str
        :type key: str
        :rtype: str
        """
        __ n.. url o. n.. key:
            r.. 'error'

        __ (
            url __ self.custom_lg2st and
            key __ self.custom_st2lg
        ):
            r.. self.get_tiny_url(key)

        __ (
            url n.. __ self.custom_lg2st and
            key n.. __ self.custom_st2lg
        ):
            self.custom_lg2st[url] = key
            self.custom_st2lg[key] = url
            r.. self.get_tiny_url(key)

        r.. 'error'

    ___ longToShort(self, url):
        """
        :type url: str
        :rtype: str
        """
        __ n.. url:
            r.. 'error'
        __ url __ self.lg2st:
            r.. self.get_tiny_url(self.lg2st[url])
        __ url __ self.custom_lg2st:
            r.. self.get_tiny_url(self.custom_lg2st[url])

        key = self.get_hash_key(self.size)
        while key __ self.st2lg:
            key = self.get_hash_key(self.size)

        self.lg2st[url] = key
        self.st2lg[key] = url
        r.. self.get_tiny_url(key)

    ___ shortToLong(self, url):
        """
        :type url: str
        :rtype: str
        """
        __ n.. url:
            r.. 'error'

        key = url.replace(self.host, '')

        __ key __ self.st2lg:
            r.. self.st2lg[key]
        __ key __ self.custom_st2lg:
            r.. self.custom_st2lg[key]

        r.. 'error'

    ___ get_tiny_url(self, hash_key):
        r.. '{}{}'.format(self.host, hash_key)

    ___ get_hash_key(self, size):
        r.. ''.join(
            random.choice(self.chars)
            ___ _ __ r..(size)
        )
