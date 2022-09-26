# value_dict.py

class ValueDict(dict):
    def key_of(self, value):
        for k, v in self.items():
            if v == value:
                return k
        raise ValueError(value)

    def keys_of(self, value):
        for k, v in self.items():
            if v == value:
                yield k

# from value_dict import ValueDict

inventory = ValueDict()
inventory["apple"] = 2
inventory["banana"] = 3
inventory.update({"orange": 2})

inventory
# {'apple': 2, 'banana': 3, 'orange': 2}

inventory.key_of(2)
# 'apple'
inventory.key_of(3)
# 'banana'

list(inventory.keys_of(2))
# ['apple', 'orange']
