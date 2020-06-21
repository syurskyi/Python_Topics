from collections import defaultdict, OrderedDict, namedtuple, deque


def task1() -> defaultdict:
    dd = defaultdict(lambda: 'Unknown')
    dd['Alan'] = 'Manchester'
    return dd


def task2(arg_od: OrderedDict):
    arg_od.popitem()
    arg_od.popitem(False)
    # remember to remove start and end before moving Bob and Dan, otherwise they will be removed instead
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', False)


def task3(name: str, club: str) -> namedtuple:
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name, club)
    return player


def task4(arg_deque: deque):
    arg_deque.pop()  # remove last element
    arg_deque.append(arg_deque.popleft())  # remove first element and append it to last
    arg_deque.appendleft('Zack')  # add Zack to start