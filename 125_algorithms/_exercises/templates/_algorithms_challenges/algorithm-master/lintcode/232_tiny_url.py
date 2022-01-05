_______ r__


c_ TinyUrl:
    ___ - ):
        chars = [s..(i) ___ i __ r..(10)]
        chars.extend(chr(i) ___ i __ r..(o..('a'), o..('z') + 1))
        chars.extend(chr(i) ___ i __ r..(o..('A'), o..('Z') + 1))

        host = 'http://tiny.url/'
        size = 6
        lg2st    # dict
        st2lg    # dict

    ___ longToShort  url):
        """
        :type url: str
        :rtype: str
        """
        __ n.. url:
            r.. 'error'
        __ url __ lg2st:
            r.. get_tiny_url(lg2st[url])

        key = get_hash_key(size)
        w.... key __ st2lg:
            key = get_hash_key(size)

        lg2st[url] = key
        st2lg[key] = url
        r.. get_tiny_url(key)

    ___ shortToLong  url):
        """
        :type url: str
        :rtype: str
        """
        __ n.. url:
            r.. 'error'

        key = url.r..(host, '')

        __ key __ st2lg:
            r.. st2lg[key]

        r.. 'error'

    ___ get_tiny_url  hash_key):
        r.. '{}{}'.f..(host, hash_key)

    ___ get_hash_key  size):
        r.. ''.j..(
            r__.choice(chars)
            ___ _ __ r..(size)
        )
