from collections ______ defaultdict

WIN, LOSS, DRAW = 'WIN', 'LOSS', 'DRAW'

___ tally(tournament_results
    results = defaultdict(lambda: {WIN: 0, LOSS: 0, DRAW: 0})
    ___ line in tournament_results.splitlines(
        home, away, result = line.split(';')
        __ result __ 'win':
            results[home][WIN] += 1
            results[away][LOSS] += 1
        ____ result __ 'loss':
            results[home][LOSS] += 1
            results[away][WIN] += 1
        ____ result __ 'draw':
            results[home][DRAW] += 1
            results[away][DRAW] += 1
    lines = ['{:30s} | MP |  W |  D |  L |  P'.format('Team')]
    ___ team in sorted(results.keys(), key=
            lambda team: (-_score(**results[team]), team)):
        lines.append('{:30s} | {:2} | {:2} | {:2} | {:2} | {:2}'.format(
            team, su.(results[team].values()),
            results[team][WIN], results[team][DRAW], results[team][LOSS],
            _score(**results[team])))
    r_ '\n'.join(lines)

___ _score(*, WIN, LOSS, DRAW
    r_ 3 * WIN + DRAW
