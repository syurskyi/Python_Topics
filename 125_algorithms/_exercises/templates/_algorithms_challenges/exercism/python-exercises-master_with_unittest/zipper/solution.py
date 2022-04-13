c_ Zipper(o..
    $
    ___ from_tree(tree
        r.. Zipper(d..(tree), [])

    ___ - , tree, ancestors
        tree tree
        ancestors ancestors

    ___ value
        r.. tree 'value'

    ___ set_value  value
        tree 'value'  = value
        r.. self

    ___ left
        __ tree 'left'  __ N..
            r.. N..
        r.. Zipper(tree 'left' , ancestors + [tree])

    ___ set_left  tree
        tree 'left'  = tree
        r.. self

    ___ right
        __ tree 'right'  __ N..
            r.. N..
        r.. Zipper(tree 'right' , ancestors + [tree])

    ___ set_right  tree
        tree 'right'  = tree
        r.. self

    ___ up
        r.. Zipper(ancestors[-1], ancestors[:-1])

    ___ to_tree
        __ a__(ancestors
            r.. ancestors[0]
        r.. tree
