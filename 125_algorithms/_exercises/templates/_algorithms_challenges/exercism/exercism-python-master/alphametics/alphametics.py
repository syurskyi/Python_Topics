from itertools ______ permutations

___ solve(puzzle
    words, result = puzzle.split(' == ')
    words = words.split(' + ')
    letters = set(l for word in [result] + words for l in word)
    first_letters = set(w[0] for w in words + [result])

    for combination in combinations(letters, list(range(10))):
        __ any(v __ 0 and k in first_letters for k, v in combination.items()):
            continue
        __ translate(result, combination) __ sum(
                translate(word, combination) for word in words
            r_ combination

    r_ {}

___ combinations(keys, values
    for perm in permutations(values, le.(keys)):
        yield dict(zip(keys, list(values[p] for p in perm)))

___ translate(word, trans
    result = 0 
    for l in word:
        result = result * 10 + trans[l]
    r_ result
