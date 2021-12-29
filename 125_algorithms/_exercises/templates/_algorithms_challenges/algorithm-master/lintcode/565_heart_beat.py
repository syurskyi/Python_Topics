class HeartBeat:

    ___ __init__(self):
        self.slaves_ip_list = {}

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    ___ initialize(self, slaves_ip_list, k):
        self.slaves_ip_list.update(d...f..(slaves_ip_list, 0))
        self.ttl = 2 * k

    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    ___ ping(self, timestamp, slave_ip):
        __ slave_ip __ self.slaves_ip_list:
            self.slaves_ip_list[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    ___ getDiedSlaves(self, timestamp):
        __ n.. timestamp:
            r.. []
        r.. [ ip
            ___ ip, t0 __ self.slaves_ip_list.items()
            __ timestamp - t0 >= self.ttl
        ]
