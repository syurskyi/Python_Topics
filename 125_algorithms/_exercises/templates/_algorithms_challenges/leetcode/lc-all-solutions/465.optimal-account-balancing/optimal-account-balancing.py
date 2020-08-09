class Solution(object
  ___ minTransfers(self, transactions
    balances = collections.defaultdict(int)
    people = set()
    ___ giver, receiver, amount in transactions:
      balances[giver] -= amount
      balances[receiver] += amount
      people |= {giver, receiver}
    ___ person, balance in balances.items(
      __ balance __ 0:
        people.discard(person)
        del balances[person]
    people_list = list(people)

    ___ dfs(people_list
      __ not people_list:
        r_ 0
      people = set(people_list)
      ___ i in range(2, le.(people_list) + 1
        ___ persons in itertools.combinations(people_list, i
          __ su.(balances[p] ___ p in persons) __ 0:
            people -= set(persons)
            r_ dfs(list(people)) + le.(persons) - 1

    r_ dfs(people_list)
