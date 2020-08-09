class Team:

    POINTS_PER_WIN = 3
    POINTS_PER_DRAW = 1

    ___ __init__(self, name
        self.name = name
        self.wins = 0
        self.draws = 0
        self.losses = 0

    @property
    ___ matches_played(self
        r_ self.wins + self.losses + self.draws

    @property
    ___ points(self
        r_ (self.wins * self.POINTS_PER_WIN) + \
            (self.draws * self.POINTS_PER_DRAW)

    ___ tally_win(self
        self.wins += 1

    ___ tally_draw(self
        self.draws += 1

    ___ tally_loss(self
        self.losses += 1

    ___ __str__(self
        r_ '{:<30} | {:^3}| {:^3}| {:^3}| {:^3}| {:>2}'.format(
            self.name, self.matches_played, self.wins, self.draws, self.losses, self.points)


class Tournament:

    WIN = 'win'
    DRAW = 'draw'
    LOSS = 'loss'
    RESULT_SEPERATOR = ';'
    COLUMN_HEADERS = ['Team', 'MP', 'W', 'D', 'L', 'P']

    ___ __init__(self, results
        self._teams = {}
        __ results:
            self.parse(results)

    ___ results_table(self
        table = [self.table_header()]
        ___ team in self.sorted_teams(
            table.append(str(team))
        r_ "\n".join(table)

    ___ sorted_teams(self
        alphabetic = sorted(self._teams.values(), key=lambda team: team.name)
        alphabetic_descending_points = sorted(
            alphabetic, key=lambda team: team.points, reverse=True)
        r_ alphabetic_descending_points

    ___ parse(self, results
        ___ result in results.split("\n"
            team_a, team_b, outcome = result.split(self.RESULT_SEPERATOR)
            self.maybe_initialize_teams(team_a, team_b)
            self.tally_outcome(team_a, team_b, outcome)

    ___ tally_outcome(self, team_a, team_b, outcome
        __ outcome __ self.WIN:
            self.tally_win(team_a, team_b)
        __ outcome __ self.LOSS:
            self.tally_loss(team_a, team_b)
        __ outcome __ self.DRAW:
            self.tally_draw(team_a, team_b)

    ___ tally_win(self, winner, loser
        self._teams[winner].tally_win()
        self._teams[loser].tally_loss()

    ___ tally_loss(self, loser, winner
        self._teams[loser].tally_loss()
        self._teams[winner].tally_win()

    ___ tally_draw(self, team_a, team_b
        self._teams[team_a].tally_draw()
        self._teams[team_b].tally_draw()

    ___ maybe_initialize_teams(self, team_a, team_b
        self.maybe_initialize_team(team_a)
        self.maybe_initialize_team(team_b)

    ___ maybe_initialize_team(self, name
        __ name not in self._teams:
            self._teams[name] = Team(name)

    ___ table_header(self
        r_ '{:<30} | {:^3}| {:^3}| {:^3}| {:^3}| {:>2}'.format(
            *self.COLUMN_HEADERS)


___ tally(results
    r_ Tournament(results).results_table()
