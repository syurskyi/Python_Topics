# ch16/concurrent_network.py

____ copy ______ deepcopy
______ ti..
____ random ______ choice

c_ Network:
    ___  - (self, primary_key, primary_value):
        self.primary_key _ primary_key
        self.data _ {primary_key: primary_value}

    ___ -s(self):
        result _ '{\n'
        ___ key __ self.data:
            result +_ f'\t{key}: {self.data[key]};\n'

        r_ result + '}'

    ___ add_node(self, key, value):
        __ key not __ self.data:
            self.data[key] _ value
            r_ T..

        r_ F..

    # precondition: the object has more than one node left
    ___ refresh_primary(self):
        del self.data[self.primary_key]
        self.primary_key _ choice(li..(self.data))

    ___ get_primary_value(self):
        copy_network _ deepcopy(self)

        primary_key _ copy_network.primary_key
        t__.s..(1) # creating a delay
        r_ copy_network.data[primary_key]
