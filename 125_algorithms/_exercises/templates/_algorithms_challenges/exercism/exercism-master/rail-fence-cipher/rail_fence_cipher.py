class Rails:

    ___ __init__(self, num_rails
        self.num_rails = num_rails
        self.rails = [[] ___ _ in range(num_rails)]

    ___ populate_rails_linear(self, message, rail_lengths
        message_list = list(message)
        ___ rail in self.linear_iterator(rail_lengths
            rail.append(message_list.pop(0))

    ___ populate_rails_zig_zag(self, message
        message_list = list(message)
        ___ rail in self.zig_zag_iterator(message
            rail.append(message_list.pop(0))

    ___ to_string_linear(self
        r_ ''.join([data ___ rail in self.rails ___ data in rail])

    ___ to_string_zig_zag(self, message
        r_ ''.join([rail.pop(0) ___ rail in
                        self.zig_zag_iterator(message)])

    ___ linear_iterator(self, rail_lengths
        ___ index in range(le.(self.rails)):
            ___ rail_length in range(rail_lengths[index]
                yield self.rails[index]

    ___ zig_zag_iterator(self, message
        index = 0
        increasing = True
        ___ _ in message:
            yield self.rails[index]
            increasing = self.direction(index, increasing)
            index = self.increment_index(index, increasing)

    ___ increment_index(self, index, increasing
        __ increasing:
            r_ index + 1
        ____
            r_ index - 1

    ___ direction(self, index, increasing
        __ index __ 0:
            r_ True
        ____ index __ self.num_rails - 1:
            r_ False
        ____
            r_ increasing


___ encode(message, num_rails
    rails = Rails(num_rails)
    rails.populate_rails_zig_zag(message)
    r_ rails.to_string_linear()


___ decode(message, num_rails
    faulty_rails = Rails(num_rails)
    faulty_rails.populate_rails_zig_zag(message)
    rail_lengths = [le.(rail) ___ rail in faulty_rails.rails]

    rails = Rails(num_rails)
    rails.populate_rails_linear(message, rail_lengths)
    r_ rails.to_string_zig_zag(message)
