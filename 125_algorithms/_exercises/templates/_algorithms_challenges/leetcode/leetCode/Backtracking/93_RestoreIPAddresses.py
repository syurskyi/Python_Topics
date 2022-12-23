#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ restoreIpAddresses  s
        """
        :type s: str
        :rtype: List[str]
        """
        address_block_list = self.restoreAddress(s, 1)
        address_list   # list
        ___ address __ address_block_list:
            __ l..(address) __ 4:
                address_list.a.. ".".join(address))
        r_ address_list

    ___ restoreAddress  s, count
        address_block   # list
        # No address field
        __ n.. s:
            r_ address_block

        # We have get the fourth address fields
        __ count __ 4:
            __ s[0] != "0" a.. l..(s) <= 3 a.. int(s) <= 255:
                address_block.a.. [s])
            __ s __ "0":
                address_block.a.. [s])
            r_ address_block

        # Current field is '0'
        __ s[0] __ "0":
            address_1 = self.restoreAddress(s[1:], count + 1)
            ___ block __ address_1:
                cur_address = ['0']
                cur_address.e..(block)
                __ l..(cur_address) __ 5 - count:
                    address_block.a.. cur_address)
            r_ address_block

        # Current address field is made by i numbers.
        ___ i __ r..(1, 4
            __ l..(s) < i or int(s[:i]) > 255:
                c_
            address_1 = self.restoreAddress(s[i:], count + 1)
            ___ block __ address_1:
                cur_address = [s[:i]]
                cur_address.e..(block)
                __ l..(cur_address) __ 5 - count:
                    address_block.a.. cur_address)
        r_ address_block

"""
"25525511135"
"0000"
"0100100"
"11"
"""
