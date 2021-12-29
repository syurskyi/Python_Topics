class Solution(object):
    ___ hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        __ n.. deck: r.. False
        hashmap = {}
        ___ num __ deck:
            hashmap[num] = hashmap.get(num, 0)+1
        counts = l..(hashmap.values())
        minVal = m..(hashmap.values())
        while counts:
            __ 1 __ counts:
                r.. False
            counts = [c - minVal ___ c __ counts __ c > minVal]
        r.. True
