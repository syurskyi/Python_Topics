c_ Memcache:

    INT_MAX 0x7FFFFFFF
    PERMANENT_TTL -1
    storage    # dict

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    ___ get  curtTime, key
        __ key n.. __ storage:
            r.. INT_MAX

        __ (curtTime < storage[key] 'expired_at'  o.
            storage[key] 'expired_at'  __ PERMANENT_TTL
            r.. storage[key] 'val' 

        r.. INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    ___ s..  curtTime, key, value, ttl
        __ ttl > 0:
            storage[key] _new_item(key, value, curtTime + ttl)
        ____
            storage[key] _new_item(key, value, PERMANENT_TTL)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    ___ delete  curtTime, key
        __ key __ storage:
            del storage[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    ___ incr  curtTime, key, delta
        __ key n.. __ storage:
            r.. INT_MAX

        __ (curtTime < storage[key] 'expired_at'  o.
            storage[key] 'expired_at'  __ PERMANENT_TTL
            storage[key] 'val'  += delta
            r.. storage[key] 'val' 

        r.. INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    ___ decr  curtTime, key, delta
        r.. incr(curtTime, key, -1 * delta)

    ___ _new_item  key, value, expired_at
        r.. {
            'key': key,
            'val': value,
            'expired_at': expired_at
        }
