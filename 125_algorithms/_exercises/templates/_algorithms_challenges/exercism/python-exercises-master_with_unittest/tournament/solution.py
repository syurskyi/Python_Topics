from collections import defaultdict

RESULTS = dict(win=0, draw=1, loss=2)


___ invert_result(result):
    __ result == 0:
        return 2
    elif result == 2:
        return 0
    return result


___ parse_game(game_line):
    game = game_line.split(';')
    __ len(game) == 3 and game[2] in RESULTS:
        result = RESULTS[game[2]]
        return (game[0], result), (game[1], invert_result(result))
    return []


___ calculate_points(stats):
    return stats[0] * 3 + stats[1]


___ format_table(results):
    table = ['Team                           | MP |  W |  D |  L |  P']

    for team, games in sorted(
            results.items(), key=lambda g: (-calculate_points(g[1]), g[0])):
        team_fmt = '{0:30} | {1:2} | {3:2} | {4:2} | {5:2} | {2:2}'
        table.append(
            team_fmt.format(team, sum(games), calculate_points(games), *games))

    return '\n'.join(table)


___ tally(data):
    table = defaultdict(lambda: [0, 0, 0])

    for line in data.split('\n'):
        for team, result in parse_game(line):
            table[team][result] += 1

    return format_table(table)
