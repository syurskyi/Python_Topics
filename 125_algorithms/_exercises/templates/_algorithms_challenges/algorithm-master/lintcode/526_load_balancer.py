_______ r__


c_ LoadBalancer:
    ___ - ):
        servers    # list
        svr2idx    # dict

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    ___ add(self, server_id):
        servers.a..(server_id)
        svr2idx[server_id] = l..(servers) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    ___ remove(self, server_id):
        svrs = servers

        i = svr2idx[server_id]
        key = svrs[-1]

        # swap `svrs[-1]` and `svrs[i]`
        svr2idx[key] = i
        svrs[i] = svrs[-1]

        svrs.pop()
        del svr2idx[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    ___ pick
        i = r__.randrange(l..(servers))
        r.. servers[i]
