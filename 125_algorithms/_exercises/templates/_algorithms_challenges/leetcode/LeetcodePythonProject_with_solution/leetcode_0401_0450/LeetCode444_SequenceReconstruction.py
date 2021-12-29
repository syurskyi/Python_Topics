'''
Created on Apr 18, 2017

@author: MT
'''

class Solution(object):
    ___ sequenceReconstruction(self, org, seqs):
        graph = {}
        degree = {}
        for seq in seqs:
            length = len(seq)
            for i in range(length):
                __ seq[i] not in graph:
                    graph[seq[i]] = []
                __ seq[i] not in degree:
                    degree[seq[i]] = 0
                __ i > 0:
                    graph[seq[i-1]].append(seq[i])
                    degree[seq[i]] += 1
        queue = []
        for key, val in degree.items():
            __ val == 0:
                queue.append(key)
        index = 0
        while queue:
            size = len(queue)
            __ size > 1:
                return False
            curr = queue.pop(0)
            __ index >= len(org) or org[index] != curr:
                return False
            index += 1
            __ curr in graph:
                for nextVal in graph[curr]:
                    degree[nextVal] -= 1
                    __ degree[nextVal] == 0:
                        queue.append(nextVal)
        return index == len(org) and index == len(graph)
