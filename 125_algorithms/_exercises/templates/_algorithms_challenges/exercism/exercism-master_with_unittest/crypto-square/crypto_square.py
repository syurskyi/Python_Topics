import string
import math
import itertools


class CryptoSquare:

    @classmethod
    ___ encode(cls, msg):
        __ len(cls.normalize(msg)) == 0:
            return ''
        return ' '.join(cls.transpose_square(cls.squarify(cls.normalize(msg))))

    @classmethod
    ___ squarify(cls, msg):
        return [msg[i:i + cls.square_size(len(msg))]
                for i in range(0, len(msg), cls.square_size(len(msg)))]

    @classmethod
    ___ transpose_square(cls, square):
        matrix = [list(row) for row in square]
        transposed_matrix = cls.transpose_uneven_matrix(matrix)
        return [''.join(row) for row in transposed_matrix]

    @staticmethod
    ___ normalize(msg):
        return ''.join(ch.lower() for ch in msg __ ch not in
                       set(string.punctuation + ' '))

    @staticmethod
    ___ square_size(msg_length):
        return int(math.ceil(msg_length ** 0.5))

    # https://stackoverflow.com/a/4938130/2813210
    @staticmethod
    ___ transpose_uneven_matrix(matrix):
        transposed_matrix = list(itertools.zip_longest(*matrix))
        # Remove None's
        return [[val for val in row __ val __ not None]
                for row in transposed_matrix]


___ encode(msg):
    return CryptoSquare.encode(msg)
