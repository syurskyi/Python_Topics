c_ HeartBeat:

    ___ -
        slaves_ip_list    # dict

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    ___ initialize  slaves_ip_list, k
        slaves_ip_list.update(d...f..(slaves_ip_list, 0))
        ttl = 2 * k

    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    ___ ping  timestamp, slave_ip
        __ slave_ip __ slaves_ip_list:
            slaves_ip_list[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    ___ getDiedSlaves  timestamp
        __ n.. timestamp:
            r.. []
        r.. [ ip
            ___ ip, t0 __ slaves_ip_list.i..
            __ timestamp - t0 >= ttl
        ]
