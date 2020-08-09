class Solution(object
    ___ hasGroupsSizeX(self, deck
        """
        :type deck: List[int]
        :rtype: bool
        """
        __ not deck: r_ False
        hashmap = {}
        for num in deck:
            hashmap[num] = hashmap.get(num, 0)+1
        counts = list(hashmap.values())
        minVal = min(hashmap.values())
        w___ counts:
            __ 1 in counts:
                r_ False
            counts = [c - minVal for c in counts __ c > minVal]
        r_ True
