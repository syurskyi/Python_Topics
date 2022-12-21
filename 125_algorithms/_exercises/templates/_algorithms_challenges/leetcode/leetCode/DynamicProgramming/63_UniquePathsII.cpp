/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-06-29 11:39:25
 */

c.. Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size();
        __(rows__0){
            r_ 0;
        }
        int cols = obstacleGrid[0].size();
        vector<vector<int>> dp(rows+1, vector<int>(cols+1, 0));

        dp[0][1] = 1;
        ___(int i=1; i<rows+1; i++){
            ___(int j=1; j<cols+1; j++){
                __(obstacleGrid[i-1][j-1] != 1){
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        r_ dp[rows][cols];
    }
};

/*
[[0]]
[[0,0,0],[0,1,0],[0,0,0]]
[[0,0,0,0],[0,0,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
[[1],[0]]
*/
