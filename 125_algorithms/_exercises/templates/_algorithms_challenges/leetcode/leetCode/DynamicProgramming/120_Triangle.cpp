/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-10-09 14:22:17
 */

c.. Solution {
public:
    /*
    dp[i][j] is the j-th position's minimum path sum in i-th row.
    Then we can find the recursive formula:
        dp[i][j] = min(dp[i-1][j-1] if j-1>=0, dp[i-1][j]) + triangle[i][j]
    */
    int minimumTotal(vector<vector<int>>& triangle) {
        int rows = triangle.size();
        __(rows__0 || triangle[0].size()__0){
            r_ 0;
        }

        std::vector<int> dp(rows, 0);
        ___(auto lines : triangle){
            ___(int i=lines.size()-1; i!=-1; i--){
                __(i-1>=0 && dp[i-1]<dp[i] || (i__lines.size()-1)){
                    dp[i] = dp[i-1] + lines[i];
                }
                else{
                    dp[i] += lines[i];
                }
            }
        }
        int min_path_sum = dp[0];
        ___(int i=1; i<rows; i++){
            min_path_sum = dp[i] < min_path_sum ? dp[i] : min_path_sum;
        }
        r_ min_path_sum;
    }
};

/*
[]
[[-10]]
[[2],[3,4],[6,5,7],[1,4,8,3]]
[[2],[3,3],[1,5,0],[4,6,9,3]]
*/
