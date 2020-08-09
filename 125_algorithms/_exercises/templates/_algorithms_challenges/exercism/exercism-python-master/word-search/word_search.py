from collections ______ defaultdict
from itertools ______ product

class Point(object
    ___ __init__(self, x, y
        self.x = x 
        self.y = y

    ___ __eq__(self, other
        r_ self.x __ other.x and self.y __ other.y


class WordSearch(object
    dirs = tuple(prod ___ prod in product((0, 1, -1), repeat=2) __ prod != (0,0))

    ___ __init__(self, puzzle
        hashes = defaultdict(list)
        ___ r, row in enumerate(puzzle
            ___ c, char in enumerate(row
                start = Point(c, r)
                ___ word, end in self._words_starting_from(puzzle, start
                    hashes[word].append((start, end))
        self._hashes = dict(hashes)

    ___ _words_starting_from(self, puzzle, start
        char = puzzle[start.y][start.x]
        yield (char, start) 
        queue = [(char, (start.x, start.y), diff) ___ diff in self.dirs]
        w___ queue:
            word, pos, diff = queue.pop()
            x, y = (p+d ___ p, d in zip(pos, diff))
            __ 0<= y < le.(puzzle) and 0 <= x < le.(puzzle[y]
                word += puzzle[y][x]
                yield(word, Point(x, y))
                queue.append((word, (x, y), diff))

    ___ search(self, word
        matches = self._hashes.get(word, [None])
        assert le.(matches) __ 1
        r_ matches[0]
