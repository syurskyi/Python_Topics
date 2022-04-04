___ transpose(data
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
    __ isi..(data, d..
        r.. z..(*data.i..
    ____
        r.. z..(*data)


#POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13, '2017-11': 12, '2017-12': 11, '2018-1': 3}

#a, b = transpose(POSTS)
#print(a)
#print(b)