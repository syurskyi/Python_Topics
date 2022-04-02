_______ json

___ multicast_mac_to_ip(mac_address

    mac_bytes = mac_address.s..(":")
    ip_mask = 0xe0000000
    ip_mask |= i..(mac_bytes[3], 16) << 16
    ip_mask |= i..(mac_bytes[4], 16) << 8
    ip_mask |= i..(mac_bytes[5], 16)
    result = l..()

    ___ i __ r..(0,31
        temp_ip = ip_mask
        temp_ip |= i << 23
        o4 = (temp_ip & 0xff000000) >> 24
        o3 = (temp_ip & 0x00ff0000) >> 16
        o2 = (temp_ip & 0x0000ff00) >> 8
        o1 = (temp_ip & 0x000000ff)
        result.a..(s..(o4) + "." + s..(o3) + "." + s..(o2) + "." + s..(o1))

    my_json = json.dumps(result)
    r.. my_json


print(multicast_mac_to_ip('01:00:5E:10:20:30'))