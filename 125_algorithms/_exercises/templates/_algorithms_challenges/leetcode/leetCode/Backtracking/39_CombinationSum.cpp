/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-14 20:32:51
 */

c.. Solution {
public:
    /*
    Classic backtracking problem.

    One key point: for one specified number,
    just scan itself and numbers larger than it to avoid duplicate combinations.
    Besides, the current path need to be reset after dfs call in general.
    Refer to:
    https://discuss.leetcode.com/topic/23142/python-dfs-solution
    */
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        __(candidates.size() __ 0){
            r_ {};
        }
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> ans;
        vector<int> path;
        dfs_search(candidates, 0, target, path, ans);
        r_ ans;
    }

    void dfs_search(vector<int>& candidates, int start, int target, vector<int> &path, vector<vector<int>> &ans){
        __(target__0){
            ans.push_back(path);
        }
        else{
            ___(int i=start; i<candidates.size(); i++){
                __(candidates[i] > target){
                    r_;
                }
                path.push_back(candidates[i]);
                dfs_search(candidates, i, target-candidates[i], path, ans);
                // Remember to do backtracking here.
                path.pop_back();
            }
        }
    }
};

/*
[]
2
[2, 3, 6, 7]
7
[1, 2, 3, 4]
10
*/
