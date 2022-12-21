/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-05-18 23:07:27
 */

c.. Solution {
public:
    /*
    According to:
    https://leetcode.com/discuss/8092/my-dp-o-n-solution-without-using-stack

    dp[i]: the longest length of valid parentheses which ends at i. Then:

    1. s[i] is '(', dp[i] = 0
    2. s[i] is ')'
        a. s[i-dp[i-1]-1] == '(': dp = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        b. dp[i] = 0

    Just think about what does s[i-dp[i-1]-1] == '(' mean.
    */
    int longestValidParentheses(string s) {
        int curMax = 0;
        vector<int> dp(s.size(),0);
        ___(int i=1; i < s.length(); i++){
            __(s[i] __ ')' && i-dp[i-1]-1>=0 && s[i-dp[i-1]-1] __ '('){
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2];
                    curMax = m..(dp[i],curMax);
            }
        }
        r_ curMax;
    }
};

/*
""
")"
"()"
"))"
"(((()()()))("
"(((()()()))())"
*/
