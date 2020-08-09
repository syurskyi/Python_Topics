______ random


class TinyUrl:
    ___ __init__(self
        self.chars = [str(i) for i in range(10)]
        self.chars.extend(chr(i) for i in range(ord('a'), ord('z') + 1))
        self.chars.extend(chr(i) for i in range(ord('A'), ord('Z') + 1))

        self.host = 'http://tiny.url/'
        self.size = 6
        self.lg2st = {}
        self.st2lg = {}

    ___ longToShort(self, url
        """
        :type url: str
        :rtype: str
        """
        __ not url:
            r_ 'error'
        __ url in self.lg2st:
            r_ self.get_tiny_url(self.lg2st[url])

        key = self.get_hash_key(self.size)
        w___ key in self.st2lg:
            key = self.get_hash_key(self.size)

        self.lg2st[url] = key
        self.st2lg[key] = url
        r_ self.get_tiny_url(key)

    ___ shortToLong(self, url
        """
        :type url: str
        :rtype: str
        """
        __ not url:
            r_ 'error'

        key = url.replace(self.host, '')

        __ key in self.st2lg:
            r_ self.st2lg[key]

        r_ 'error'

    ___ get_tiny_url(self, hash_key
        r_ '{}{}'.format(self.host, hash_key)

    ___ get_hash_key(self, size
        r_ ''.join(
            random.choice(self.chars)
            for _ in range(size)
        )
