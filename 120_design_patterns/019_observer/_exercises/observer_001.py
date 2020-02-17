#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
http://code.activestate.com/recipes/131499-observer-pattern/

*TL;DR80
Maintains a list of dependents and notifies them of any state changes.
"""

from __future__ import print_function


class Subject(object):

    def __init__(self):
        self._observers = []     # list

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except  ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


# Example usage
___c_ Data S..

    ___ -  name_''
        S__. -
        ?  ?
        _data = 0

    ??
    ___ data
        r_ _d..

    ??.?
    ___ data value
        _d.. ?
        .no..


___c_ HexViewer

    ___ update  subject
        print(u'HexViewer: Subject @ has data 0x%x'
              (?.n.. ?.d..


___c_ DecimalViewer

    ___ update  subject
        print(u'DecimalViewer: Subject @ has data @'
              (?.n.. ?.d..


# Example usage...
___ main
    data1 = D..('Data 1')
    data2 = D..('Data 2')
    view1 = DV..
    view2 = HV..
    d_1.at__ v1
    data1.at__ v2
    data2.at__ v2
    data2.at__ v1

    print(u"Setting Data 1 = 10")
    d1.d.. = 10
    print(u"Setting Data 2 = 15")
    d2.d.. = 15
    print(u"Setting Data 1 = 3")
    d1.d.. = 3
    print(u"Setting Data 2 = 5")
    d2.d.. = 5
    print(u"Detach HexViewer from data1 and data2.")
    d1.de.. v2
    d2.de.. v2
    print(u"Setting Data 1 = 10")
    d1.d.. = 10
    print(u"Setting Data 2 = 15")
    d2.d.. = 15


__ _______ __ ______
    ?

### OUTPUT ###
# Setting Data 1 = 10
# DecimalViewer: Subject Data 1 has data 10
# HexViewer: Subject Data 1 has data 0xa
# Setting Data 2 = 15
# HexViewer: Subject Data 2 has data 0xf
# DecimalViewer: Subject Data 2 has data 15
# Setting Data 1 = 3
# DecimalViewer: Subject Data 1 has data 3
# HexViewer: Subject Data 1 has data 0x3
# Setting Data 2 = 5
# HexViewer: Subject Data 2 has data 0x5
# DecimalViewer: Subject Data 2 has data 5
# Detach HexViewer from data1 and data2.
# Setting Data 1 = 10
# DecimalViewer: Subject Data 1 has data 10
# Setting Data 2 = 15
# DecimalViewer: Subject Data 2 has data 15
