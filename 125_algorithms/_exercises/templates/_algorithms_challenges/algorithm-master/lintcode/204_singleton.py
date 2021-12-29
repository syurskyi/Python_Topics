class Solution:
    instance = None

    # @return: The same instance of this class every time
    @classmethod
    ___ getInstance(cls):
        __ not cls.instance:
            cls.instance = Solution()
        return cls.instance
