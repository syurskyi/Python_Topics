# -*- coding: utf-8 -*-
_____ ?
_____ ___

db_filename _ 'dhcp_snooping.db'

query_dict _ {
    'vlan': 'select mac, ip, interface from dhcp where vlan = ?',
    'mac': 'select vlan, ip, interface from dhcp where mac = ?',
    'ip': 'select vlan, mac, interface from dhcp where ip = ?',
    'interface': 'select vlan, mac, ip from dhcp where interface = ?'
}

key, value _ ___.ar..[1:]
keys _ query_dict.keys()

if not key __ keys:
    print('Enter key from {}'.f..(', '.join(keys)))
else:
    conn _ ?.c..(db_filename)
    conn.r_f.. _ ?.Row

    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)

    query _ query_dict[key]
    result _ conn.e..(query, (value, ))

    ___ row __ result:
        ___ row_name __ row.keys():
            print('{:12}: {}'.f..(row_name, row[row_name]))
        print('-' * 40)
