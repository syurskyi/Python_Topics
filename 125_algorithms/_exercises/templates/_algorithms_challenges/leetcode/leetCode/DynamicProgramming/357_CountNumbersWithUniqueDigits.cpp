/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-08 10:45:15
 */


c.. Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        __(n__0){
            r_ 1;
        }
        __(n__1){
            r_ 10;
        }
        __(n__2){
            r_ 91;
        }
        vector<int> dp(n+1, 0);
        dp[1] = 10;
        dp[2] = 81;
        int result = 91;
        ___(int i=3; i<m.. 11, n+1); i++){
            dp[i] = dp[i-1] * (11-i);
            result += dp[i];
        }
        r_ result;
    }
};

/*
0
2
9
12
*/
