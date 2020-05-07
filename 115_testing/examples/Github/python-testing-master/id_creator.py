class IdCreator:

    def faculty_id(self, value):
        if not isinstance(value, int):
            raise TypeError('Only integer values allowed')
        if value < 0:
            raise ValueError('Only positive values allowed')
        if value == 0:
            return 1
        else:
            return self.faculty_id(value-1) * value


# Testing without using a framework
if __name__ == '__main__':
    creator = IdCreator()
    assert creator.faculty_id(0) == 1
    assert creator.faculty_id(3) == 6

    try:
        creator.faculty_id(-1)
        assert 1 == 0
    except ValueError:
        pass

    try:
        creator.faculty_id('a')
        assert 1 == 0
    except TypeError:
        pass
