'''
Created on Apr 18, 2017

@author: MT
'''

c_ Solution(o..
    ___ sequenceReconstruction  org, seqs
        graph    # dict
        degree    # dict
        ___ seq __ seqs:
            length = l..(seq)
            ___ i __ r..(length
                __ seq[i] n.. __ graph:
                    graph[seq[i]]    # list
                __ seq[i] n.. __ degree:
                    degree[seq[i]] = 0
                __ i > 0:
                    graph[seq[i-1]].a..(seq[i])
                    degree[seq[i]] += 1
        queue    # list
        ___ key, val __ degree.i..:
            __ val __ 0:
                queue.a..(key)
        index = 0
        w.... queue:
            size = l..(queue)
            __ size > 1:
                r.. F..
            curr = queue.p.. 0)
            __ index >= l..(org) o. org[index] != curr:
                r.. F..
            index += 1
            __ curr __ graph:
                ___ nextVal __ graph[curr]:
                    degree[nextVal] -= 1
                    __ degree[nextVal] __ 0:
                        queue.a..(nextVal)
        r.. index __ l..(org) a.. index __ l..(graph)
