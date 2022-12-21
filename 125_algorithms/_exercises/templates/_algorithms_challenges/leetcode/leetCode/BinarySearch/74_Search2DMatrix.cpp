/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-13 11:17:48
 */

c.. Solution {
public:
    // Don't treat it as a 2D matrix, just treat it as a sorted list
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        __(matrix.empty()){
            r_ false;
        }
        int m_rows = matrix.size(), n_cols = matrix[0].size();
        int left=0, right = m_rows*n_cols-1;
        _____(left <= right){
            int mid = left + (right-left) / 2;
            int num = matrix[mid/n_cols][mid%n_cols];
            __(num < target){
                left = mid + 1;
            }
            else __(num > target){
                right = mid - 1;
            }
            else{
                r_ true;
            }
        }
        r_ false;
    }
};

/*
[[]]
0
[[1]]
0
[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
34
[[1, 3, 5], [10, 11, 16], [23, 30, 34]]
46
*/
