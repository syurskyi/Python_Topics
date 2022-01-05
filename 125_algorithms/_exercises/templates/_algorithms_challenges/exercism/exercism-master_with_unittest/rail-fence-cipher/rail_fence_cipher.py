c_ Rails:

    ___ - , num_rails):
        num_rails = num_rails
        rails = [[] ___ _ __ r..(num_rails)]

    ___ populate_rails_linear  message, rail_lengths):
        message_list = l..(message)
        ___ rail __ linear_iterator(rail_lengths):
            rail.a..(message_list.pop(0))

    ___ populate_rails_zig_zag  message):
        message_list = l..(message)
        ___ rail __ zig_zag_iterator(message):
            rail.a..(message_list.pop(0))

    ___ to_string_linear
        r.. ''.j..([data ___ rail __ rails ___ data __ rail])

    ___ to_string_zig_zag  message):
        r.. ''.j..([rail.pop(0) ___ rail __
                        zig_zag_iterator(message)])

    ___ linear_iterator  rail_lengths):
        ___ index __ r..(l..(rails)):
            ___ rail_length __ r..(rail_lengths[index]):
                y.. rails[index]

    ___ zig_zag_iterator  message):
        index = 0
        increasing = T..
        ___ _ __ message:
            y.. rails[index]
            increasing = direction(index, increasing)
            index = increment_index(index, increasing)

    ___ increment_index  index, increasing):
        __ increasing:
            r.. index + 1
        ____:
            r.. index - 1

    ___ direction  index, increasing):
        __ index __ 0:
            r.. T..
        ____ index __ num_rails - 1:
            r.. F..
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
