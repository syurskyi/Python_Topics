#!/usr/bin/env python
# coding: utf-8
print(list)
print(tuple)
print(set)
print(dict)

print({a for a in dir(__builtins__) if isinstance(getattr(__builtins__, a), type)
                             and a.islower()} - {'__loader__'})

