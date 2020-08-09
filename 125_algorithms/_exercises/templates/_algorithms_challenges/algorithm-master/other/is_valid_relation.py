"""
Question:

The rules look like this:
'A NE B' - means this means point A is located northeast of point B.
'A SW C' - means that point A is southwest of C.
'A N D' - means that point A is north of D but maybe true north, northeast, or northwest.

Given a list of rules, check if the sum of the rules validates. For example:
['A N B', 'B NE C', 'C N A'], returns False
['A N B', 'B NE C', 'C S A'], returns True


Testing:

>>> gotcha = []
>>> for _in, _out in (
...     ([], False),
...     ([''], False),
...     (['A N B', 'B NE C', 'C N A'], False),
...     (['A N B', 'B NW C', 'C N C'], False),
...     (['A N B', 'B N C', 'C N B'], False),
...     (['A N B', 'B NE C', 'C S A'], True),
...     (['A N B', 'B NW C', 'C S A'], True),
...     (['A E B', 'B E C', 'C S D', 'D S E'], True),
...     (['A N B', 'B S A', 'C E D', 'D W C'], True),
...
...     res = is_valid_relation(_in)
...     if res != _out: print(_in, res)
...     gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""
______ collections


___ is_valid_relation(strs
    """
    :type strs: list[str]
    :rtype: bool
    """
    __ not strs:
        r_ False

    # egraph => scan from east to west
    egraph = collections.defaultdict(set)
    wgraph = collections.defaultdict(set)
    ngraph = collections.defaultdict(set)
    sgraph = collections.defaultdict(set)

    ___ s in strs:
        __ not s:
            r_ False

        dst, d, src = s.split()

        __ 'E' in d:
            egraph[dst].add(src)
            wgraph[src].add(dst)
        ____ 'W' in d:
            wgraph[dst].add(src)
            egraph[src].add(dst)

        __ 'N' in d:
            ngraph[dst].add(src)
            sgraph[src].add(dst)
        ____ 'S' in d:
            sgraph[dst].add(src)
            ngraph[src].add(dst)

    ___ graph in (egraph, wgraph, ngraph, sgraph
        ___ node in graph.keys(
            __ dfs(graph, node, set()):
                r_ False

    r_ True


___ dfs(graph, node, visited
    """
    returns True if there is cycle in graph
    :type graph: dict{str: set}
    :type node: str
    :type visited: set
    :rtype: bool
    """
    __ node not in graph:
        r_ False
    __ node in visited:
        r_ True

    visited.add(node)

    ___ nxt in graph[node]:
        __ dfs(graph, nxt, visited
            r_ True

    r_ False
