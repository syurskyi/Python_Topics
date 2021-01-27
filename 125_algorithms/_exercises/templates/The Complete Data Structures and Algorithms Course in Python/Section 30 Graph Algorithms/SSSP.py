#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.


c_ Graph:
    ___  -   gdict=N..
        __ gdict __ N..:
            gdict = {}
        gdict = gdict
    
    ___ bfs  start, end
        queue = []
        queue.ap..([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            __ node __ end:
                r_ path
            ___ adjacent __ gdict.get(node, []
                new_path = list(path)
                new_path.ap..(adjacent)
                queue.ap..(new_path)

customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g = Graph(customDict)
print(g.bfs("a", "e"))
