'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object):
    ___ sequenceReconstruction(self, org, seqs):
        graph = {}
        degree = {}
        ___ seq __ seqs:
            length = l..(seq)
            ___ i __ r..(length):
                __ seq[i] n.. __ graph:
                    graph[seq[i]]    # list
                __ seq[i] n.. __ degree:
                    degree[seq[i]] = 0
                __ i > 0:
                    graph[seq[i-1]].a..(seq[i])
                    degree[seq[i]] += 1
        queue    # list
        ___ key, val __ degree.items():
            __ val __ 0:
                queue.a..(key)
        index = 0
        while queue:
            size = l..(queue)
            __ size > 1:
                r.. False
            curr = queue.pop(0)
            __ index >= l..(org) o. org[index] != curr:
                r.. False
            index += 1
            __ curr __ graph:
                ___ nextVal __ graph[curr]:
                    degree[nextVal] -= 1
                    __ degree[nextVal] __ 0:
                        queue.a..(nextVal)
        r.. index __ l..(org) and index __ l..(graph)
