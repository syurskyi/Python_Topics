from collections ______ defaultdict

class Solution:
    ___ containsDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)

        for num in nums:
            __ m[num]:
                r_ True
            m[num]+=1
        r_ False