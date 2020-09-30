"""Transforms an old data structure into a new one"""

___ transform(old_structure
    """Swaps key and value in old data structure"""
    new_structure = {}
    ___ key, items __ old_structure.items(
        ___ item __ items:
            new_structure[item.lower()] = key
    r_ new_structure
