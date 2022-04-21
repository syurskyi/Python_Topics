_______ __
____ p.. _______ P..
____ ipaddress _______ IPv4Network
____ u__.r.. _______ u..

_______ p__

____ ips _______ (ServiceIPRange, parse_ipv4_service_ranges,
                 get_aws_service_range)

URL "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
TMP __.g.. TMP  /tmp
PATH P..(TMP, "ip-ranges.json")
IP IPv4Network('192.0.2.8/29')


?p__.f..(scope='module')
___ json_file
    """Import data into tmp folder"""
    u..(URL, PATH)
    r.. PATH


___ test_ServiceIPRange
    serv ServiceIPRange(
        service='Tester',
        region='Bolton',
        cidr=IPv4Network('158.152.1.0/24')
    )
    ... s..(serv) __ '158.152.1.0/24 is allocated to the Tester service in the Bolton region'


___ test_parse_ipv4_service_ranges(json_file
    services parse_ipv4_service_ranges(json_file)
    ... l..(services) __ 1886
    ... services[0].region __ 'eu-west-1'
    ... services[0].service __ 'AMAZON'


___ test_get_aws_service_range(json_file
    services parse_ipv4_service_ranges(json_file)
    service_range get_aws_service_range('13.248.118.1', services)
    ... l..(service_range) __ 2
    ... s..(s.region ___ s __ service_range) __ {'eu-west-1'}
    ... s..(s.service ___ s __ service_range) __ {'AMAZON', 'GLOBALACCELERATOR'}
    ... get_aws_service_range('158.152.1.65', services) __ []
    w__ p__.r..(V...) __ exc:
        get_aws_service_range('0.0.0.256', services)
    ... 'Address must be a valid IPv4 address' __ s..(exc.v..)
