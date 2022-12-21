/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-19 15:29:06
 */

c.. Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        dfs(nums, 0, ans);
        r_ ans;
    }

    void dfs(vector<int> &num, int begin, vector<vector<int>> &ans){
        __(begin __ num.size()){
            ans.push_back(num);
            r_;
        }
        ___(int i=begin; i<num.size();i++){
            swap(num[begin], num[i]);
            dfs(num, begin+1, ans);
            // Backtrack
            swap(num[begin], num[i]);
        }
    }
};

/*
[]
[1]
[1,2,3]
*/
