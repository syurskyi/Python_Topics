import re


def is_valid_ip(s):


    return re.search(r'^"\d+\.\d+\.\d+\.\d+"$',s) is not None


def is_valid_number(s):

    return re.search(r'^\d+$',s) is not None

def extract_ipv4(data):
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """

    
    result = []
    for l in data:
        if type(l) == list:
            result.extend(extract_ipv4(l))
        elif l == 'ip':
            print(data)
            try:
                result_1 = is_valid_ip(data[1][0])
                result_2 = is_valid_number(data[3][0])
                print(result_1,result_2)
            except:
                continue
            else:
                
                if result_1 and result_2:
                    print('here')
                    ip_address = data[1][0].strip('"')
                    mask = data[3][0].strip('"')

                    result.append((ip_address,mask))
                    break



    return result
