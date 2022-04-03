import csv
import os
from u__.r.. import u..
from collections import defaultdict

TMP = os.getenv("TMP", "/tmp")
DATA = 'battle-table.csv'
BATTLE_DATA = os.path.join(TMP, DATA)
if not os.path.isfile(BATTLE_DATA):
    u..(
        f'https://bites-data.s3.us-east-2.amazonaws.com/{DATA}',
        BATTLE_DATA
    )


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    defeat_map = defaultdict(list)
    with open(BATTLE_DATA) as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        defeat_map[row['Attacker']] = [k for k, v in row.items() if v == 'win']
    return defeat_map


def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()

    if player1 not in defeat_mapping or player2 not in defeat_mapping:
        raise ValueError('Invalid player string')

    if player1 == player2:
        return 'Tie'
    else:
        if player1 in defeat_mapping[player2]:
            return player2
        else:
            return player1
