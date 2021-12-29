class Rails:

    ___ __init__(self, num_rails):
        self.num_rails = num_rails
        self.rails = [[] for _ in range(num_rails)]

    ___ populate_rails_linear(self, message, rail_lengths):
        message_list = list(message)
        for rail in self.linear_iterator(rail_lengths):
            rail.append(message_list.pop(0))

    ___ populate_rails_zig_zag(self, message):
        message_list = list(message)
        for rail in self.zig_zag_iterator(message):
            rail.append(message_list.pop(0))

    ___ to_string_linear(self):
        return ''.join([data for rail in self.rails for data in rail])

    ___ to_string_zig_zag(self, message):
        return ''.join([rail.pop(0) for rail in
                        self.zig_zag_iterator(message)])

    ___ linear_iterator(self, rail_lengths):
        for index in range(len(self.rails)):
            for rail_length in range(rail_lengths[index]):
                yield self.rails[index]

    ___ zig_zag_iterator(self, message):
        index = 0
        increasing = True
        for _ in message:
            yield self.rails[index]
            increasing = self.direction(index, increasing)
            index = self.increment_index(index, increasing)

    ___ increment_index(self, index, increasing):
        __ increasing:
            return index + 1
        else:
            return index - 1

    ___ direction(self, index, increasing):
        __ index == 0:
            return True
        elif index == self.num_rails - 1:
            return False
        else:
            return increasing


___ encode(message, num_rails):
    rails = Rails(num_rails)
    rails.populate_rails_zig_zag(message)
    return rails.to_string_linear()


___ decode(message, num_rails):
    faulty_rails = Rails(num_rails)
    faulty_rails.populate_rails_zig_zag(message)
    rail_lengths = [len(rail) for rail in faulty_rails.rails]

    rails = Rails(num_rails)
    rails.populate_rails_linear(message, rail_lengths)
    return rails.to_string_zig_zag(message)
