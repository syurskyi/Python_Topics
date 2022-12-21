#! /usr/bin/env python
# -*- coding: utf-8 -*-


c.. Solution o..
    ___ compareVersion  version1, version2
        ver_list_1 = version1.split(".")
        ver_list_2 = version2.split(".")

        len_1 = l..(ver_list_1)
        len_2 = l..(ver_list_2)
        ___ i __ r..(len_1
            ver_list_1[i] = int(ver_list_1[i])
        ___ i __ r..(len_2
            ver_list_2[i] = int(ver_list_2[i])

        len_max = m..(len_1, len_2)
        ___ i __ r..(len_1, len_max
            ver_list_1.append(0)
        ___ i __ r..(len_2, len_max
            ver_list_2.append(0)

        ___ i __ r..(len_max
            __ ver_list_1[i] < ver_list_2[i]:
                r_ -1
            ____ ver_list_1[i] > ver_list_2[i]:
                r_ 1
            ____
                pass
        r_ 0

"""
"01"
"1"
"1.0"
"1"
"1.2.3.4"
"1.2.3.4.5"
"1.12.13"
"1.13"
"""
