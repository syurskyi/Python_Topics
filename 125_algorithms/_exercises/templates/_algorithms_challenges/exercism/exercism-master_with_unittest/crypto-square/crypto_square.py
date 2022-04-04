_______ s__
_______ m__
_______ i..


c_ CryptoSquare:

    @classmethod
    ___ encode(cls, msg
        __ l..(cls.normalize(msg __ 0:
            r.. ''
        r.. ' '.j..(cls.transpose_square(cls.squarify(cls.normalize(msg))))

    @classmethod
    ___ squarify(cls, msg
        r.. [msg[i:i + cls.square_size(l..(msg]
                ___ i __ r..(0, l..(msg), cls.square_size(l..(msg)))]

    @classmethod
    ___ transpose_square(cls, square
        matrix = [l..(row) ___ row __ square]
        transposed_matrix = cls.transpose_uneven_matrix(matrix)
        r.. [''.j..(row) ___ row __ transposed_matrix]

    $
    ___ normalize(msg
        r.. ''.j..(ch.l.. ___ ch __ msg __ ch n.. __
                       s..(s__.punctuation + ' '

    $
    ___ square_size(msg_length
        r.. i..(m__.c.. msg_length ** 0.5

    # https://stackoverflow.com/a/4938130/2813210
    $
    ___ transpose_uneven_matrix(matrix
        transposed_matrix = l..(i...z__(*matrix
        # Remove None's
        r.. [[val ___ val __ row __ val __ n.. N..]
                ___ row __ transposed_matrix]


___ encode(msg
    r.. CryptoSquare.encode(msg)
