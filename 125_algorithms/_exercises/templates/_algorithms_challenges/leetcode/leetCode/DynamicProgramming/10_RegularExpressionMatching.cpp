/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-07 22:22:45
 */


c.. Solution {
public:
    // Recursively
    bool isMatch(string s, string p) {
        __(p.empty())   r_ s.empty();
        __(p[1] __ '*'){
            // x* matches empty string or at least one character: x* -> xx*
            r_ (isMatch(s, p.substr(2)) || !s.empty() && (s[0] __ p[0] || '.' __ p[0]) && isMatch(s.substr(1), p));
        }
        else{
            r_ !s.empty() && (s[0] __ p[0] || '.' __ p[0]) && isMatch(s.substr(1), p.substr(1));
        }
    }
};


c.. Solution_2 {
public:
    /*
    According to:
    https://leetcode.com/discuss/43860/9-lines-16ms-c-dp-solutions-with-explanations
    Dynamic Programming
        P[i][j] to be true if s[0..i) matches p[0..j) and false otherwise;
    */
    bool isMatch(string s, string p) {
        int m = s.length(), n = p.length();
        vector<vector<bool>> dp(m + 1, vector<bool> (n + 1, false));
        dp[0][0] = true;
        ___ (int i = 0; i <= m; i++)
            ___ (int j = 1; j <= n; j++)
                __ (p[j - 1] __ '*')
                    dp[i][j] = dp[i][j - 2] || (i > 0 && (s[i - 1] __ p[j - 2] || p[j - 2] __ '.') && dp[i - 1][j]);
                else dp[i][j] = i > 0 && dp[i - 1][j - 1] && (s[i - 1] __ p[j - 1] || p[j - 1] __ '.');
        r_ dp[m][n];

    }
};
