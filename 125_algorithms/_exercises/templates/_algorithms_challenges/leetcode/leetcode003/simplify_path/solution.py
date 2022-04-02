c_ Solution:
    # @param path, a string
    # @return a string
    ___ simplifyPath  p..
        ps = p...s..('/')[1:]
        res    # list
        ___ d __ ps:
            __ d __ '..':
                __ res:
                    res.pop()
            ____ d __ '.' o. d __ '':
                p..
            ____:
                res.a..(d)
        r.. '/' + '/'.j..(res)
