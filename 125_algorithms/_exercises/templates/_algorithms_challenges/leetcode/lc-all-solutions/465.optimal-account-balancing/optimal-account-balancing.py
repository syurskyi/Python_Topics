class Solution(object):
  ___ minTransfers(self, transactions):
    balances = collections.defaultdict(int)
    people = set()
    for giver, receiver, amount in transactions:
      balances[giver] -= amount
      balances[receiver] += amount
      people |= {giver, receiver}
    for person, balance in balances.items():
      __ balance == 0:
        people.discard(person)
        del balances[person]
    people_list = list(people)

    ___ dfs(people_list):
      __ not people_list:
        return 0
      people = set(people_list)
      for i in range(2, len(people_list) + 1):
        for persons in itertools.combinations(people_list, i):
          __ sum(balances[p] for p in persons) == 0:
            people -= set(persons)
            return dfs(list(people)) + len(persons) - 1

    return dfs(people_list)
