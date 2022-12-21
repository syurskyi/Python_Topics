"""
You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
 

Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20

判断是否与给定的字符串模式是一样的。

思路是把所有的字符串转换为同一种编码的格式之后与pattern对比即可。

用的 str 直接就过了，beat 95%。 换成 set 取交集应该更快一些。

测试地址：
https://leetcode.com/contest/weekly-contest-98/problems/find-and-replace-pattern/

beat:
95% 24ms.


"""

c.. Solution o..
    ___ findAndReplacePattern  words, pattern
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        
        ___ translate_pattern(word
            result = ['0']
            current = '0'
            patterns = {word[0]: '0'} 
            ___ i __ word[1:]:
                __ patterns.get(i) is n.. None:
                    result.append(patterns.get(i))
                ____
                    current = str(int(current)+1)
                    patterns[i] = current
                    result.append(current)

            r_ ''.join(result)
        
        x = translate_pattern(pattern)

        result   # list
        ___ i __ words:
            __ x __ translate_pattern(i
                result.append(i)
        
        r_ result
