# -*- coding: utf-8 -*-

import re

s = "test text"
p = re.compile(r"([a-z]+((st)|(xt)))", re.S)
p.findall(s)
# [('test', 'st', 'st', ''), ('text', 'xt', '', 'xt')]
p = re.compile(r"([a-z]+(?:(?:st)|(?:xt)))", re.S)
p.findall(s)
# ['test', 'text']