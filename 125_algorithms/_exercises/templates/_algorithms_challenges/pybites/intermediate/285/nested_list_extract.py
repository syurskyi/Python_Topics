_______ __


___ is_valid_ip(s):


    r.. __.s..(r'^"\d+\.\d+\.\d+\.\d+"$',s) __ n.. N..


___ is_valid_number(s):

    r.. __.s..(r'^\d+$',s) __ n.. N..

___ extract_ipv4(data):
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """

    
    result    # list
    ___ l __ data:
        __ t..(l) __ l..:
            result.extend(extract_ipv4(l))
        ____ l __ 'ip':
            print(data)
            try:
                result_1 = is_valid_ip(data[1][0])
                result_2 = is_valid_number(data[3][0])
                print(result_1,result_2)
            except:
                _____
            ____:
                
                __ result_1 a.. result_2:
                    print('here')
                    ip_address = data[1][0].strip('"')
                    mask = data[3][0].strip('"')

                    result.a..((ip_address,mask))
                    break



    r.. result
