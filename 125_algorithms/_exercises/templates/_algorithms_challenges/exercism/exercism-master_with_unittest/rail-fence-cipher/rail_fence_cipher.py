class Rails:

    ___ __init__(self, num_rails):
        self.num_rails = num_rails
        self.rails = [[] ___ _ __ r..(num_rails)]

    ___ populate_rails_linear(self, message, rail_lengths):
        message_list = l..(message)
        ___ rail __ self.linear_iterator(rail_lengths):
            rail.a..(message_list.pop(0))

    ___ populate_rails_zig_zag(self, message):
        message_list = l..(message)
        ___ rail __ self.zig_zag_iterator(message):
            rail.a..(message_list.pop(0))

    ___ to_string_linear(self):
        r.. ''.join([data ___ rail __ self.rails ___ data __ rail])

    ___ to_string_zig_zag(self, message):
        r.. ''.join([rail.pop(0) ___ rail __
                        self.zig_zag_iterator(message)])

    ___ linear_iterator(self, rail_lengths):
        ___ index __ r..(l..(self.rails)):
            ___ rail_length __ r..(rail_lengths[index]):
                y.. self.rails[index]

    ___ zig_zag_iterator(self, message):
        index = 0
        increasing = True
        ___ _ __ message:
            y.. self.rails[index]
            increasing = self.direction(index, increasing)
            index = self.increment_index(index, increasing)

    ___ increment_index(self, index, increasing):
        __ increasing:
            r.. index + 1
        ____:
            r.. index - 1

    ___ direction(self, index, increasing):
        __ index __ 0:
            r.. True
        ____ index __ self.num_rails - 1:
            r.. False
        ____:
            r.. increasing


___ encode(message, num_rails):
    rails = Rails(num_rails)
    rails.populate_rails_zig_zag(message)
    r.. rails.to_string_linear()


___ decode(message, num_rails):
    faulty_rails = Rails(num_rails)
    faulty_rails.populate_rails_zig_zag(message)
    rail_lengths = [l..(rail) ___ rail __ faulty_rails.rails]

    rails = Rails(num_rails)
    rails.populate_rails_linear(message, rail_lengths)
    r.. rails.to_string_zig_zag(message)
