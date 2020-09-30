# Longest common prefix
# Question: Write a function to find the longest common prefix string amongst an array of strings.
# For Example:
# “Foo” and “Foobar” give “Foo” as longest prefix.
# Solutions:


c_ Solution:
    # @return a string
    ___ longestCommonPrefix(self, strs):
        __ le.(strs) __ 0:
            r_ ""
        ___ i __ ra..(le.(strs[0])-1,-1,-1):
            prefix _ strs[0][:i+1]
            validPrefix _ T..
            ___ j __ ra..(1,le.(strs)):
                __ le.(strs[j])<_i or strs[j][:i+1]!_prefix:
                    validPrefix _ F..
                    break
            __ validPrefix:
                r_ prefix
        r_ ""


Solution().longestCommonPrefix(["Foo","FooBar","Food"])