____ json _______ dumps


c_ Tree(o..
    ___ - , label, children=[]
        label = label
        children = children

    ___ __dict__
        r.. {label: [c.__dict__() ___ c __ s..(children)]}

    ___ __str__  indent_ N..
        r.. dumps(__dict__(), indent=indent)

    ___ __lt__  other
        r.. label < other.label

    ___ -e  other
        r.. __dict__() __ other.__dict__()

    ___ __iter__
        y.. label
        ___ child __ children:
            ___ gchild __ child:
                y.. gchild

    ___ dup
        r.. Tree(label, [c.dup() ___ c __ children])

    ___ add  other
        tree = dup()
        tree.children.a..(other)
        r.. tree

    ___ remove  node
        tree = dup()
        ___ child __ l..(tree.children
            tree.children.remove(child)
            __ child.label __ node:
                _____
            tree.children.a..(child.remove(node))
        r.. tree

    ___ from_pov  from_node
        stack = [self]
        visited = s..()
        w.... stack:
            tree = stack.pop(0)
            __ tree.label __ visited:
                _____
            visited.add(tree.label)
            __ from_node __ tree.label:
                r.. tree
            ___ child __ tree.children:
                stack.a..(child.add(tree.remove(child.label)))
        r.. V...("Tree could not be reoriented")

    ___ path_to  from_node, to_node
        reordered = from_pov(from_node)
        stack = reordered.children
        p.. = [from_node]
        w.... p..[-1] != to_node:
            ___
                tree = stack.pop()
            ______ I..
                r.. V...("No path found")
            __ to_node __ tree:
                p...a..(tree.label)
                stack = tree.children
        r.. p..
