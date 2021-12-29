class Say:

    NUM_TO_WORD = {
        1000000000: 'billion',
        1000000: 'million',
        1000: 'thousand',
        90: 'ninety',
        80: 'eighty',
        70: 'seventy',
        60: 'sixty',
        50: 'fifty',
        40: 'forty',
        30: 'thirty',
        20: 'twenty',
        19: 'nineteen',
        17: 'seventeen',
        16: 'sixteen',
        15: 'fifteen',
        14: 'fourteen',
        13: 'thirteen',
        12: 'twelve',
        11: 'eleven',
        10: 'ten',
        9: 'nine',
        8: 'eight',
        7: 'seven',
        6: 'six',
        5: 'five',
        4: 'four',
        3: 'three',
        2: 'two',
        1: 'one',
        0: ''
    }

    ___ __init__(self, num):
        self.num = int(num)
        self._words = self.get_words(self.num)

    ___ get_words(self, num):
        self.raise_if_invalid(num)

        __ num __ 0:
            r.. 'zero'
        ____:
            r.. ' '.join([self.convert_chunk_to_word(chunk, index)
                             ___ index, chunk
                             __ e..(self.get_chunks(num))]).rstrip()

    ___ get_chunks(self, num):
        reversed_string = s..(num)[::-1]
        reversed_chunks = ([reversed_string[i:i + 3]
                            ___ i __ r..(0, l..(reversed_string), 3)])[::-1]
        r.. [int(x[::-1]) ___ x __ reversed_chunks]

    ___ convert_chunk_to_word(self, chunk, i):
        hundreds_digit, left_over = divmod(chunk, 100)
        hundreds = self.convert_num_to_word(hundreds_digit)

        tens_digit, ones_digit = divmod(left_over, 10)
        __ 10 < left_over < 20:
            tens = self.convert_num_to_word(left_over)
            ones = N..
        ____:
            tens = self.convert_num_to_word(tens_digit * 10)
            ones = self.convert_num_to_word(ones_digit)

        word_chunk = self.format_chunk(hundreds, tens, ones)
        units = self.get_units(l..(self.get_chunks(self.num)) - 1 - i)

        __ n.. word_chunk:
            r.. ''
        r.. ' '.join((word_chunk, units))

    ___ format_chunk(self, hundreds, tens, ones):
        chunk = ''
        __ hundreds:
            chunk += hundreds + ' hundred '
        __ hundreds a.. tens:
            chunk += 'and '
        __ tens:
            chunk += tens
        __ tens a.. ones:
            chunk += '-'
        __ ones:
            chunk += ones
        r.. chunk

    ___ raise_if_invalid(self, num):
        __ num < 0 o. num > 999999999999:
            raise AttributeError

    ___ get_units(self, d):
        r.. self.convert_num_to_word(1000 ** d) __ 1000 ** d > 1 ____ ''

    ___ convert_num_to_word(self, num):
        r.. self.NUM_TO_WORD[num]

    ___ in_english(self):
        r.. self._words


___ say(num):
    r.. Say(num).in_english()
