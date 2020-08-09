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

    ___ __init__(self, num
        self.num = int(num)
        self._words = self.get_words(self.num)

    ___ get_words(self, num
        self.raise_if_invalid(num)

        __ num __ 0:
            r_ 'zero'
        ____
            r_ ' '.join([self.convert_chunk_to_word(chunk, index)
                             for index, chunk
                             in enumerate(self.get_chunks(num))]).rstrip()

    ___ get_chunks(self, num
        reversed_string = str(num)[::-1]
        reversed_chunks = ([reversed_string[i:i + 3]
                            for i in range(0, le.(reversed_string), 3)])[::-1]
        r_ [int(x[::-1]) for x in reversed_chunks]

    ___ convert_chunk_to_word(self, chunk, i
        hundreds_digit, left_over = divmod(chunk, 100)
        hundreds = self.convert_num_to_word(hundreds_digit)

        tens_digit, ones_digit = divmod(left_over, 10)
        __ 10 < left_over < 20:
            tens = self.convert_num_to_word(left_over)
            ones = None
        ____
            tens = self.convert_num_to_word(tens_digit * 10)
            ones = self.convert_num_to_word(ones_digit)

        word_chunk = self.format_chunk(hundreds, tens, ones)
        units = self.get_units(le.(self.get_chunks(self.num)) - 1 - i)

        __ not word_chunk:
            r_ ''
        r_ ' '.join((word_chunk, units))

    ___ format_chunk(self, hundreds, tens, ones
        chunk = ''
        __ hundreds:
            chunk += hundreds + ' hundred '
        __ hundreds and tens:
            chunk += 'and '
        __ tens:
            chunk += tens
        __ tens and ones:
            chunk += '-'
        __ ones:
            chunk += ones
        r_ chunk

    ___ raise_if_invalid(self, num
        __ num < 0 or num > 999999999999:
            raise AttributeError

    ___ get_units(self, d
        r_ self.convert_num_to_word(1000 ** d) __ 1000 ** d > 1 else ''

    ___ convert_num_to_word(self, num
        r_ self.NUM_TO_WORD[num]

    ___ in_english(self
        r_ self._words


___ say(num
    r_ Say(num).in_english()
