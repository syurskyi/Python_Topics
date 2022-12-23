/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-30 14:48:13
 */

c.. Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        __(grid.size()__0){
            r_ 0;
        }
        int rows = grid.size();
        int cols = grid[0].size();

        vector<vector<int>> dp(rows, vector<int>(cols, 0));
        ___(int i=0; i<rows; i++){
            ___(int j=0; j<cols; j++){
                dp[i][j] = grid[i][j];
                __(i__0 && j>0){
                    dp[i][j] += dp[i][j-1];
                }
                else __(j__0 && i>0){
                    dp[i][j] += dp[i-1][j];
                }
                else __(j > 0 && i>0){
                    dp[i][j] += m.. dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        r_ dp[rows-1][cols-1];
    }
};

/*
[]
[[0]]
[[1,2,4,3,2,1,5],[3,4,1,2,3,5,4],[3,2,4,5,1,2,5]]
*/
