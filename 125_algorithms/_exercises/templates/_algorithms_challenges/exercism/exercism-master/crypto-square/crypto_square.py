______ string
______ ma__
______ itertools


class CryptoSquare:

    @classmethod
    ___ encode(cls, msg
        __ le.(cls.normalize(msg)) __ 0:
            r_ ''
        r_ ' '.join(cls.transpose_square(cls.squarify(cls.normalize(msg))))

    @classmethod
    ___ squarify(cls, msg
        r_ [msg[i:i + cls.square_size(le.(msg))]
                ___ i in range(0, le.(msg), cls.square_size(le.(msg)))]

    @classmethod
    ___ transpose_square(cls, square
        matrix = [list(row) ___ row in square]
        transposed_matrix = cls.transpose_uneven_matrix(matrix)
        r_ [''.join(row) ___ row in transposed_matrix]

    @staticmethod
    ___ normalize(msg
        r_ ''.join(ch.lower() ___ ch in msg __ ch not in
                       set(string.punctuation + ' '))

    @staticmethod
    ___ square_size(msg_length
        r_ int(ma__.ceil(msg_length ** 0.5))

    # https://stackoverflow.com/a/4938130/2813210
    @staticmethod
    ___ transpose_uneven_matrix(matrix
        transposed_matrix = list(itertools.zip_longest(*matrix))
        # Remove None's
        r_ [[val ___ val in row __ val is not None]
                ___ row in transposed_matrix]


___ encode(msg
    r_ CryptoSquare.encode(msg)
