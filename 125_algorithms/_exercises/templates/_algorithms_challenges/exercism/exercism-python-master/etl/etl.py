"""Transforms an old data structure into a new one"""

___ transform(old_structure
    """Swaps key and value in old data structure"""
    new_structure = {}
    ___ key, items in old_structure.items(
        ___ item in items:
            new_structure[item.lower()] = key
    r_ new_structure
