___ flatten_dictionary(dictionary
    ans = {}

    __ not dictionary:
        r_ ans

    dfs(dictionary, [], ans)
    r_ ans


___ dfs(dictionary, keys, ans
    __ not isinstance(dictionary, dict
        key = '.'.join(keys)
        ans[key] = dictionary
        r_

    ___ key in dictionary:
        __ key:
            keys.append(key)

        dfs(dictionary[key], keys, ans)

        __ key:
            keys.p..
