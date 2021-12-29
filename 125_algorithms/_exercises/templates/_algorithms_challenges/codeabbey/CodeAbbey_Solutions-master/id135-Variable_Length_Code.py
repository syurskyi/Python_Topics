# Python 2.7

___ compress_string(string):
    answer    # list
    value_dict = {
        ' ': '11',             'e': '101',
        't': '1001',           'o': '10001',
        'n': '10000',          'a': '011',
        's': '0101',           'i': '01001',
        'r': '01000',          'h': '0011',
        'd': '00101',          'l': '001001',
        '!': '001000',         'u': '00011',
        'c': '000101',         'f': '000100',
        'm': '000011',         'p': '0000101',
        'g': '0000100',        'w': '0000011',
        'b': '0000010',        'y': '0000001',
        'v': '00000001',       'j': '000000001',
        'k': '0000000001',     'x': '00000000001',
        'q': '000000000001',   'z': '000000000000',
        }
    
    string = string[::].lower()

    # Convert to assigned values.
    eight_bit    # list
    ___ char __ string[::]:
        bits = ("%s") % (value_dict[char])
        eight_bit.a..(bits)
    eight_bit = (''.join(eight_bit))

    # Split into chunks of 8
    chunks    # list
    ___ byte __ r..(l..(eight_bit)):
        __ l..(eight_bit) > 0 and l..(eight_bit) < 8:
            while l..(eight_bit) < 8:
                eight_bit += '0'
        while l..(eight_bit) > 7:
            byte = eight_bit[:8]
            chunks.a..(byte)
            eight_bit = eight_bit[8:]
            #eight_bit = eight_bit[:-8]

    # Convert into hex and print answer.
    ___ chunk __ chunks:
        chunk = int(chunk, 2)
        encoded_value = hex(chunk)[2:].upper() #[2:] to remove the '0x'
        __ l..(encoded_value) __ 1:
            encoded_value = '0' + encoded_value
        answer.a..(encoded_value)
    print(' '.join(answer))
    
compress_string(raw_input())
