_______ r__


c_ TinyUrl2:
    ___ - ):
        chars = [s..(i) ___ i __ r..(10)]
        chars.extend(chr(i) ___ i __ r..(ord('a'), ord('z') + 1))
        chars.extend(chr(i) ___ i __ r..(ord('A'), ord('Z') + 1))

        host = 'http://tiny.url/'
        size = 6
        lg2st    # dict
        st2lg    # dict

        custom_lg2st    # dict
        custom_st2lg    # dict

    ___ createCustom(self, url, key):
        """
        :type url: str
        :type key: str
        :rtype: str
        """
        __ n.. url o. n.. key:
            r.. 'error'

        __ (
            url __ custom_lg2st a..
            key __ custom_st2lg
        ):
            r.. get_tiny_url(key)

        __ (
            url n.. __ custom_lg2st a..
            key n.. __ custom_st2lg
        ):
            custom_lg2st[url] = key
            custom_st2lg[key] = url
            r.. get_tiny_url(key)

        r.. 'error'

    ___ longToShort(self, url):
        """
        :type url: str
        :rtype: str
        """
        __ n.. url:
            r.. 'error'
        __ url __ lg2st:
            r.. get_tiny_url(lg2st[url])
        __ url __ custom_lg2st:
            r.. get_tiny_url(custom_lg2st[url])

        key = get_hash_key(size)
        w.... key __ st2lg:
            key = get_hash_key(size)

        lg2st[url] = key
        st2lg[key] = url
        r.. get_tiny_url(key)

    ___ shortToLong(self, url):
        """
        :type url: str
        :rtype: str
        """
        __ n.. url:
            r.. 'error'

        key = url.r..(host, '')

        __ key __ st2lg:
            r.. st2lg[key]
        __ key __ custom_st2lg:
            r.. custom_st2lg[key]

        r.. 'error'

    ___ get_tiny_url(self, hash_key):
        r.. '{}{}'.f..(host, hash_key)

    ___ get_hash_key(self, size):
        r.. ''.j..(
            r__.choice(chars)
            ___ _ __ r..(size)
        )
