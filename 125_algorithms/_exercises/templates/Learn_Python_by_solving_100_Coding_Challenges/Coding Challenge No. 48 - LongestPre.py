# Longest common prefix
# Question: Write a function to find the longest common prefix string amongst an array of strings.
# For Example:
# “Foo” and “Foobar” give “Foo” as longest prefix.
# Solutions:


class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])-1,-1,-1):
            prefix = strs[0][:i+1]
            validPrefix = True
            for j in range(1,len(strs)):
                if len(strs[j])<=i or strs[j][:i+1]!=prefix:
                    validPrefix = False
                    break
            if validPrefix:
                return prefix
        return ""


Solution().longestCommonPrefix(["Foo","FooBar","Food"])