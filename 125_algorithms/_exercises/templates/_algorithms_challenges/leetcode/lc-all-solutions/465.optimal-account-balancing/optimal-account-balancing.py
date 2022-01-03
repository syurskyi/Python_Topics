c_ Solution(object):
  ___ minTransfers(self, transactions):
    balances = collections.defaultdict(int)
    people = set()
    ___ giver, receiver, amount __ transactions:
      balances[giver] -= amount
      balances[receiver] += amount
      people |= {giver, receiver}
    ___ person, balance __ balances.i..:
      __ balance __ 0:
        people.discard(person)
        del balances[person]
    people_list = l..(people)

    ___ dfs(people_list):
      __ n.. people_list:
        r.. 0
      people = set(people_list)
      ___ i __ r..(2, l..(people_list) + 1):
        ___ persons __ i...combinations(people_list, i):
          __ s..(balances[p] ___ p __ persons) __ 0:
            people -= set(persons)
            r.. dfs(l..(people)) + l..(persons) - 1

    r.. dfs(people_list)
