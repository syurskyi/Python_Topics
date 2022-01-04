_______ string
_______ math
_______ i..


c_ CryptoSquare:

    @classmethod
    ___ encode(cls, msg):
        __ l..(cls.normalize(msg)) __ 0:
            r.. ''
        r.. ' '.j..(cls.transpose_square(cls.squarify(cls.normalize(msg))))

    @classmethod
    ___ squarify(cls, msg):
        r.. [msg[i:i + cls.square_size(l..(msg))]
                ___ i __ r..(0, l..(msg), cls.square_size(l..(msg)))]

    @classmethod
    ___ transpose_square(cls, square):
        matrix = [l..(row) ___ row __ square]
        transposed_matrix = cls.transpose_uneven_matrix(matrix)
        r.. [''.j..(row) ___ row __ transposed_matrix]

    @staticmethod
    ___ normalize(msg):
        r.. ''.j..(ch.l.. ___ ch __ msg __ ch n.. __
                       set(string.punctuation + ' '))

    @staticmethod
    ___ square_size(msg_length):
        r.. i..(math.ceil(msg_length ** 0.5))

    # https://stackoverflow.com/a/4938130/2813210
    @staticmethod
    ___ transpose_uneven_matrix(matrix):
        transposed_matrix = l..(i...zip_longest(*matrix))
        # Remove None's
        r.. [[val ___ val __ row __ val __ n.. N..]
                ___ row __ transposed_matrix]


___ encode(msg):
    r.. CryptoSquare.encode(msg)
