_______ j__
____ ?.m.. _______ p.., M..

_______ r__

____ ? _______ ?


$p.. .o.. r__, 'g..
___ test_ipinfo_mexican_ip mockget
    # hardcoding a requests response
    content (b'{\n  "ip": "187.190.38.36",\n  "hostname": "domain.net",\n'
               b'  "city": "Mexico City",\n  "region": "Mexico City",\n  '
               b'"country": "MX",\n ' b'"loc": "11.0000,-00.1111",\n  '
               b'"postal": "12345",\n  "org": "some org"\n}')
    ?.r.. M.. ?_?
                                text_?.d.. utf-8
                                j__=l.... j__.l.. ?
                                s.._200
    ... ? '187.190.38.36' __ 'MX'


$p.. .o.. r__, 'g..
___ test_ipinfo_japan_ip mockget
    # and another IP in Japan
    content (b'{\n  "ip": "185.161.200.10",\n  "city": "Tokyo",\n  '
               b'"region": "Tokyo",\n ' b'"country": "JP",\n  "loc": '
               b'"00.1111,11.0000",\n  "postal": "123-4567",\n  '
               b'"org": "some other org"\n}')
    ?.r.. M.. ?_?
                                text_?.d.. utf-8
                                j__=l.... j__.l.. ?
                                s.._200
    ... ? '185.161.200.10' __ 'JP'