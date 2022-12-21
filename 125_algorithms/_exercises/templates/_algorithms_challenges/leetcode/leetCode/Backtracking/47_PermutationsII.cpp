/*
 * @Author: xuezaigds@gmail.com
 * @Last Modified time: 2016-04-20 10:38:44
 */

c.. Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        helper(nums, 0, ans);
        r_ ans;
    }

    void helper(vector<int> num, int begin, vector<vector<int>> &ans){
        // num is passed by value
        __(begin__num.size()-1){
            ans.push_back(num);
            r_;
        }
        ___(int i=begin;i<num.size();i++){
            __(i!=begin && num[i]__num[begin])  c_;
            swap(num[i], num[begin]);
            helper(num, begin+1, ans);
            // No Backtracking here!!!
        }
    }
};


c.. Solution_2{
public:
    /*
     * 1. sort nums in ascending order, add it to res;
     * 2. generate the next permutation of nums, and add it to res;
     * 3. repeat 2 until the next permutation of nums returns to the sorted condition in 1.
     */
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        ans.push_back(nums);
        _____(nextPermutation(nums)){
            ans.push_back(nums);
        }
        r_ ans;
    }

    bool nextPermutation(vector<int>& nums) {
        __(nums.empty())    r_ false;
        int i;
        ___(i=nums.size()-1; i>=1; i--){
            __(nums[i] > nums[i-1]) break;
        }
        reverse(nums.begin()+i, nums.end());
        __(i__0)    r_ false;
        auto iter = upper_bound(nums.begin()+i, nums.end(), nums[i-1]);
        swap(nums[i-1], *iter);
        r_ true;
    }
};

/*
[]
[1]
[1,2,3]
[2,2,3,3]
*/
