# _______ j__
# ____ c.. _______ s__
# ____ d.. _______ d..
# ____ i.. _______ A.. I.. I..
# ____ p.. _______ P..
# ____ t___ _______ L..
#
#
# ?? frozen=T..
# c_ ServiceIPRange
#     """
#     Represents an IPv4 public network range, allocated by AWS for use with
#     a specific service and region.
#     """
#
#     service: s..
#     region: s..
#     cidr: I..
#
#     ___ -s
#         r.. _* c.. is allocated to the s..
#                 _*service in the r.. region
#
#
# ___ parse_ipv4_service_ranges source P.. __ L.. S..
#     """
#     Given a JSON file containing AWS public IP addresses, return a list of
#     ServiceIPRange objects representing all IPv4 network ranges. See also:
#
#     https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html
#     """
#     data j__.l.. ?.r..
#     w__ s.. A..
#         prefixes ? "prefixes"
#         ipv4_service_ranges
#             S..
#                 s.._p.. service
#                 r.._p.. region
#                 c.._I.. p.. ip_prefix
#
#             ___ prefix __ ?
#
#     r.. ?
#
#
# ___ get_aws_service_range address s..
#                           service_ranges l.. __ L.. S..
#     """
#     Return a list of ServiceIPRange objects representing all AWS public
#     IP ranges that contain `address`. Raise a ValueError if `address`
#     is not a valid IPv4 address.
#     """
#     ___
#         ipv4_address I.. ?
#     ______ A..
#         r.. V...("Address must be a valid IPv4 address")
#
#     r.. range_ ___ ? __ s..
#             __ i.. __ ?.c..