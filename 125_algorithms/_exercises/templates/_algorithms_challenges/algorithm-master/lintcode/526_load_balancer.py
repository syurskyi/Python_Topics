_______ random


class LoadBalancer:
    ___ __init__(self):
        self.servers    # list
        self.svr2idx = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    ___ add(self, server_id):
        self.servers.a..(server_id)
        self.svr2idx[server_id] = l..(self.servers) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    ___ remove(self, server_id):
        svrs = self.servers

        i = self.svr2idx[server_id]
        key = svrs[-1]

        # swap `svrs[-1]` and `svrs[i]`
        self.svr2idx[key] = i
        svrs[i] = svrs[-1]

        svrs.pop()
        del self.svr2idx[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    ___ pick(self):
        i = random.randrange(l..(self.servers))
        r.. self.servers[i]
