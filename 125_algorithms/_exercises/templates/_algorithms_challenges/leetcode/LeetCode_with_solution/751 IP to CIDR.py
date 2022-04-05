#!/usr/bin/python3
"""
Given a start IP address ip and a number of ips we need to cover n, return a
representation of the range as a list (of smallest possible length) of CIDR
blocks.

A CIDR block is a string consisting of an IP, followed by a slash, and then the
prefix length. For example: "123.45.67.89/20". That prefix length "20"
represents the number of common prefix bits in the specified range.

Example 1:
Input: ip = "255.0.0.7", n = 10
Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
Explanation:
The initial ip address, when converted to binary, looks like this (spaces added
for clarity):
255.0.0.7 -> 11111111 00000000 00000000 00000111
The address "255.0.0.7/32" specifies all addresses with a common prefix of 32
bits to the given address,
ie. just this one address.

The address "255.0.0.8/29" specifies all addresses with a common prefix of 29
bits to the given address:
255.0.0.8 -> 11111111 00000000 00000000 00001000
Addresses with common prefix of 29 bits are:
11111111 00000000 00000000 00001000
11111111 00000000 00000000 00001001
11111111 00000000 00000000 00001010
11111111 00000000 00000000 00001011
11111111 00000000 00000000 00001100
11111111 00000000 00000000 00001101
11111111 00000000 00000000 00001110
11111111 00000000 00000000 00001111

The address "255.0.0.16/32" specifies all addresses with a common prefix of 32
bits to the given address,
ie. just 11111111 00000000 00000000 00010000.

In total, the answer specifies the range of 10 ips starting with the address
255.0.0.7 .

There were other representations, such as:
["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
but our answer was the shortest possible.

Also note that a representation beginning with say, "255.0.0.7/30" would be
incorrect,
because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000
00000100
that are outside the specified range.
Note:
ip will be a valid IPv4 address.
Every implied address ip + x (for x < n) will be a valid IPv4 address.
n will be an integer in the range [1, 1000].
"""
____ t___ _______ L..


# the weights of ip when converting to binary
weights = [
    24,
    16,
    8,
    0,
]


c_ Solution:
    ___ ipToCIDR  ip: s.., n: i..) __ L..[s..]:
        """
        bit manipulation

        IP address, 8 bit, at each digit, total 32 bit, 8 byte
        Follow the example
        Input: ip = "255.0.0.7", n = 10
        Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
        255.0.0.7 -> 11111111 00000000 00000000 00000111 => cover 1
        255.0.0.8 -> 11111111 00000000 00000000 00001000 => cover 8
        255.0.0.16 -> 11111111 00000000 00000000 00010000 => cover 16 but only 32
        32 means all bits as fixed prefix 

        111, then 32 to cover only one, depends on LSB
        Greedy
        To cover n, can have representation covers > n

        need helper functions, write the main function first

        Iterate LSB to the next LSB skipping 1's
        num += lsb
        """
        num_ip = to_bin(ip)
        ret    # list
        w.... n > 0:
            lsb = get_lsb(num_ip)
            w.... (1 << lsb) > n:
                lsb -_ 1

            cur_cover = 1 << lsb
            n -_ cur_cover
            ret.a..(
                to_ip(num_ip) + f"/{32-lsb}"
            )
            num_ip += cur_cover

        r.. ret

    ___ to_bin  ip
        ret = 0
        ___ n, w __ z.. m..(i.., ip.s..(".", weights
            ret += n << w

        r.. ret

    ___ to_ip  bin
        ret    # list
        ___ w __ weights:
            ret.a..(
                (bin >> w) & 255
            )
        r.. ".".j.. m..(s.., ret

    ___ get_lsb  n
        lsb = 0
        w.... (n >> lsb) & 1 __ 0:
            lsb += 1
            #  n >>= lsb  # error
        r.. lsb


__ _______ __ _______
    ... Solution().ipToCIDR("60.166.253.147", 12) __ ["60.166.253.147/32","60.166.253.148/30","60.166.253.152/30","60.166.253.156/31","60.166.253.158/32"]
    ... Solution().ipToCIDR("255.0.0.7", 10) __ ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
