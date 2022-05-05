# _______ __
# ____ p.. _______ P..
# ____ i.. _______ I..
# ____ u__.r.. _______ u..
#
# _______ p__
#
# ____ ? _______ ? ? ?
#
# URL "https://bites-data.s3.us-east-2.amazonaws.com/ip-ranges.json"
# TMP __.g.. ?  /tmp
# PATH P.. ? "ip-ranges.json"
# IP I.. '192.0.2.8/29'
#
#
# ?p__.f.. s.._='module'
# ___ json_file
#     """Import data into tmp folder"""
#     u.. ? ?
#     r.. ?
#
#
# ___ test_ServiceIPRange
#     serv ?
#         service_'Tester'
#         region_'Bolton'
#         cidr_I.. '158.152.1.0/24'
#
#     ... s.. ? __ '158.152.1.0/24 is allocated to the Tester service in the Bolton region'
#
#
# ___ test_parse_ipv4_service_ranges json_file
#     services ? ?
#     ... l.. ? __ 1886
#     ... ? 0 .r.. __ 'eu-west-1'
#     ... s.. 0 .s.. __ 'AMAZON'
#
#
# ___ test_get_aws_service_range json_file
#     services ? ?
#     service_range ? '13.248.118.1' ?
#     ... l.. ? __ 2
#     ... s.. s.r.. ___ ? __ ? __ eu-west-1
#     ... s.. s.s.. ___ ? __ ? __ AMAZON', 'GLOBALACCELERATOR
#     ... ? '158.152.1.65' ? __    # list
#     w__ p__.r.. V... __ exc
#         ? '0.0.0.256' ?
#     ... 'Address must be a valid IPv4 address' __ s.. ?.v..
