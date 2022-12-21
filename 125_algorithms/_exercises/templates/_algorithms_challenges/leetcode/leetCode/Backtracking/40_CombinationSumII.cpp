/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-07-15 21:38:18
 */

c.. Solution {
    /*
    Classic backtracking problem.

    One key point: for one specified number,
    just scan the number larger than it to avoid duplicate combinations.
    Besides, the current path need to be reset after dfs call in general.
    That's saying, we need to do pop_back after push_back operator.
    */
private:
    void dfs_search(vector<int> &candidates, int start, int target, vector<int> &path, vector<vector<int>> &ans){
        __(target__0){
            ans.push_back(path);
        }
        ___(int i=start; i<candidates.size(); i++){
            int num = candidates[i];
            __(num > target){
                r_;
            }

            // Here skip the same `adjacent` element to avoid duplicated.
            __(i > start && candidates[i] __ candidates[i－1]){
                c_;
            }
            path.push_back(candidates[i]);
            dfs_search(candidates, i+1, target-num, path, ans);
            path.pop_back();
        }
    }
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        __(candidates.size() __ 0){
            r_ {};
        }
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        vector<vector<int>> ans;
        dfs_search(candidates, 0, target, path, ans);
        r_ ans;
    }
};

/*
[]
1
[2, 5, 1, 4, 9]
11
[10, 1, 2, 7, 6, 1, 5]
8
*/
