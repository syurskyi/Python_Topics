from collections import namedtuple
Member = namedtuple("Member",'name since_days karma_points bitecoin_earned')


___ transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """


    __ type(data) == dict:
        return [tuple(data.keys()),tuple(data.values())]
    elif type(data) == list:
        
        return [z for z in zip(*(tuple(d) for d in data))]







__ __name__ == "__main__":

    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]

    
    transpose(data)
