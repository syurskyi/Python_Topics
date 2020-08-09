from itertools ______ permutations

___ solve(puzzle
    words, result = puzzle.split(' == ')
    words = words.split(' + ')
    letters = set(l ___ word in [result] + words ___ l in word)
    first_letters = set(w[0] ___ w in words + [result])

    ___ combination in combinations(letters, list(range(10))):
        __ any(v __ 0 and k in first_letters ___ k, v in combination.items()):
            continue
        __ translate(result, combination) __ su.(
                translate(word, combination) ___ word in words
            r_ combination

    r_ {}

___ combinations(keys, values
    ___ perm in permutations(values, le.(keys)):
        yield dict(zip(keys, list(values[p] ___ p in perm)))

___ translate(word, trans
    result = 0 
    ___ l in word:
        result = result * 10 + trans[l]
    r_ result
