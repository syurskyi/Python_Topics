______ random


class LoadBalancer:
    ___ __init__(self
        self.servers = []
        self.svr2idx = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    ___ add(self, server_id
        self.servers.append(server_id)
        self.svr2idx[server_id] = le.(self.servers) - 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    ___ remove(self, server_id
        svrs = self.servers

        i = self.svr2idx[server_id]
        key = svrs[-1]

        # swap `svrs[-1]` and `svrs[i]`
        self.svr2idx[key] = i
        svrs[i] = svrs[-1]

        svrs.p..
        del self.svr2idx[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    ___ pick(self
        i = random.randrange(le.(self.servers))
        r_ self.servers[i]
