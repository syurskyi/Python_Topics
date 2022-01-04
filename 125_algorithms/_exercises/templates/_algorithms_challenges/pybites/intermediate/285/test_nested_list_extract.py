____ nested_list_extract _______ extract_ipv4


___ test_empty_list
    ... extract_ipv4([]) __ []


___ test_flat_list_no_match
    ... extract_ipv4(['ip']) __ []


___ test_nested_list_no_match
    ... extract_ipv4([['ip', 'mask']]) __ []


___ test_nested_list_no_ip
    ... extract_ipv4([['TEST', ['ip', [N..], 'mask', ['24'], 'type', ['ip_mask']], 'id']]) __ []


___ test_nested_list_not_an_ip
    ... extract_ipv4([['TEST', ['ip', ['"not.an.ip.address"'], 'mask', ['24'], 'type', ['ip_mask']], 'id']]) __ []


___ test_nested_list_no_mask
    ... extract_ipv4([['TEST', ['ip', ['"1.1.1.0"'], 'mask', [N..], 'type', ['ip_mask']], 'id']]) __ []


___ test_flat_list
    ... extract_ipv4(['ip', ['"172.16.0.0"'], 'mask', ['12'], 'type', ['ip_mask']]) __ [('172.16.0.0', '12')]


___ test_nested_list
    ... extract_ipv4(['TEST', 'parent', [], 'uuid', '"khk-yyas4h-323223-wewe-343er-3434-www"', 'display_name', '"services"', 'IPV4', [['ip', ['"192.168.1.0"'], 'mask', ['24'], 'type', ['ip_mask']], ['ip', ['"10.0.0.0"'], 'mask', ['8'], 'type', ['ip_mask']]]]) __ [('192.168.1.0', '24'), ('10.0.0.0', '8')]


___ test_deeply_nested_list
    ... extract_ipv4([['TEST', ['parent', [], 'uuid', ['"khk-yyas4h-323223-wewe-343er-3434-www"'], 'display_name', ['"services"'], 'IPV4', [[['ip', ['"1.1.1.0"'], 'mask', ['20'], 'type', ['ip_mask']], ['ip', ['"2.2.2.2"'], 'mask', ['32'], 'type', ['ip_mask']]]]]]]) __ [('1.1.1.0', '20'), ('2.2.2.2', '32')]
